import imp, os, sys
from optparse import OptionParser
import re, subprocess
from math import ceil
from Samples.Tools.config import  redirector

# 2016 FastSim
from Samples.miniAOD.Spring16_miniAODv2         import allSamples as Spring16_miniAODv2
from Samples.miniAOD.Summer16_Fast_miniAODv3    import allSamples as Summer16_Fast_miniAODv3
print "s16 ran"
# 2017 FastSim
from Samples.miniAOD.Fall17_Fast_miniAODv2      import allSamples as Fall17_Fast_miniAODv2
print "fall17 ran"
# 2018 FastSim
from Samples.miniAOD.Autumn18_Fast_miniAODv1    import allSamples as Autumn18_Fast_miniAODv1
print "autumn 18 fast ran"
# 2016 private
from Samples.miniAOD.Summer16_private           import allSamples as Summer16_private
# 2016 FullSim
from Samples.miniAOD.Summer16_miniAODv2         import allSamples as Summer16_miniAODv2
from Samples.miniAOD.Summer16_miniAODv3         import allSamples as Summer16_miniAODv3
print "Summer16 ran"
# 2017 private
from Samples.miniAOD.Fall17_private             import allSamples as Fall17_private
print "fall17 private ran"
# 2017 FullSim
from Samples.miniAOD.Fall17_miniAODv2           import allSamples as Fall17_miniAODv2
print "fall17 v2 ran"
# 2018 FullSim
#from Samples.miniAOD.Autumn18_miniAODv1         import allSamples as Autumn18_miniAODv1
#print "autumn18_v1 ran"
# 2018 private
from Samples.miniAOD.Autumn18_private           import allSamples as Autumn18_private
print "autumn18_priv ran"
# 2016 Data
from Samples.miniAOD.Run2016_17Jul2018          import allSamples as Run2016_17Jul2018
print "data16 ran"
# 2017 Data
from Samples.miniAOD.Run2017_31Mar2018          import allSamples as Run2017_31Mar2018
print "data17 ran"
# 2018 special HEM Data
from Samples.miniAOD.Run2018_26Sep2018          import allSamples as Run2018_26Sep2018
print "data18  ran"
# 2018 prompt Data (in the end only for D!)
from Samples.miniAOD.Run2018_promptReco         import allSamples as Run2018_promptReco
print "data18_pr  ran"
# 2018 rereco Data (for A->C)
from Samples.miniAOD.Run2018_17Sep2018          import allSamples as Run2018_17Sep2018
print "data18 sep ran"

all_modules  = [ "Spring16_miniAODv2", "Summer16_Fast_miniAODv3", "Fall17_Fast_miniAODv2", "Autumn18_Fast_miniAODv1", "Summer16_miniAODv2", "Summer16_miniAODv3", "Fall17_miniAODv2"]#, "Autumn18_miniAODv1" ]
all_modules += [ "Run2016_17Jul2018", "Run2017_31Mar2018", "Run2018_26Sep2018", "Run2018_promptReco", "Run2018_17Sep2018", "Run2017_17Nov2017" ]
all_modules += [ "Summer16_private", "Fall17_private", "Autumn18_private" ]

allSamples  = Spring16_miniAODv2 + Summer16_Fast_miniAODv3 + Fall17_Fast_miniAODv2 + Summer16_miniAODv2 + Summer16_miniAODv3 + Fall17_miniAODv2 +  Autumn18_Fast_miniAODv1 #Autumn18_miniAODv1 +
allSamples += Summer16_private + Fall17_private + Autumn18_private
allSamples += Run2016_17Jul2018 + Run2017_31Mar2018 + Run2018_26Sep2018 + Run2018_promptReco + Run2018_17Sep2018

cfgPath    = os.path.expandvars( "$CMSSW_BASE/src/Samples/cfg/" )
allConfigs = [ x.strip( ".py" ) for x in os.listdir( cfgPath ) if x.endswith(".py") ]

parser = OptionParser(usage="python launch.py [options] component1 [ component2 ...]", \
                          description="Launch heppy jobs with CRAB3. Components correspond to the variables defined in heppy_samples.py (their name attributes)")
parser.add_option("--production_label", dest="production_label",                                  default="heppy", help="production label")
parser.add_option("--remoteDir",        dest="remoteDir",                                         default="",      help="remote subdirectory")
parser.add_option("--unitsPerJob",      dest="unitsPerJob",      type=int,                        default=1,       help="Nr. of units (files) / crab job")
parser.add_option("--totalUnits",       dest="totalUnits",       type=int,                        default=None,    help="Total nr. of units (files)")
parser.add_option("--config",           dest="config",                     choices = allConfigs,                   help="Which config?")
parser.add_option("--module",           dest="module",                     choices = all_modules,                  help="Which module X in Samples.miniAOD.X?")
parser.add_option("--sample",           dest="sample",                                                             help="Which sample?")
parser.add_option("--inputDBS",         dest="inputDBS",          choices = ['phys03','global'],  default="global",help="Private or global production?")
parser.add_option("--publish",          action='store_true',                                      default=False,   help="Publish on dbs?")
parser.add_option("--runOnNonValid",    action='store_true',                                      default=False,   help="Allow running on invalid samples/samples still in production?")
parser.add_option("--runOnLocal",       action='store_true',                                      default=False,   help="Run on local DPM files")
parser.add_option("--dryrun",           action='store_true',                                      default=False,   help="Test script?")
parser.add_option("--sorted",           action='store_true',                                      default=False,   help="sort filelist by ending integer (only for local processing)")
parser.add_option('--nJobs',            action='store',          type=int,                        default=1,       help="Maximum number of simultaneous jobs.")
parser.add_option('--job',              action='store',          type=int,                        default=0,       help="Run only job i")
( options, args ) = parser.parse_args()

print "## Starting submission to crab for sample(s) %s from module %s"%( options.sample, options.module )

module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/miniAOD/%s.py" % options.module )
try:
    tmp_module = imp.load_source( options.sample, os.path.expandvars( module_file ) ) 
    datasets   = getattr(tmp_module, options.sample)
except:
    raise RuntimeError( "Not found: Sample: %s, Module: %s, module_file: %s" % (options.sample, options.module, module_file) ) 

if not isinstance( datasets, list ): datasets = [ datasets ]

print "## Will process from module %s the following samples: %s"%(options.module,  ",".join( d.name for d in datasets ) )

os.system("scram runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

os.environ['CRAB_RUNONNONVALID'] = 'True' if options.runOnNonValid else 'False'
print "## Running on non-valid input dataset is set to: %s"%os.environ['CRAB_RUNONNONVALID']

os.environ["CRAB_PUBLISH"] = 'True' if options.publish else 'False'
print "## Publication is set to", os.environ["CRAB_PUBLISH"]

## Config selection
os.environ["CMSRUN_CFG"] = os.path.join( cfgPath, "%s.py" % options.config )
print "## Will use the following config: %s"%os.environ["CMSRUN_CFG"]

os.system("which crab")

#os.environ["CMG_REMOTE_DIR"]  = options.remoteDir
os.environ["CRAB_UNITS_PER_JOB"] = str(options.unitsPerJob)
if options.totalUnits:
    os.environ["CRAB_TOTAL_UNITS"] = str(options.totalUnits)

for dataset in datasets:

    if options.runOnLocal:

        def splitList( l, n ):
            # split list l in chunks of n entries
            partList = []
            newList = []
            for i, entry in enumerate(l):
                if i!=0 and not i%int(n):
                    newList.append(partList)
                    partList = []
                partList.append(entry)
            newList.append(partList)
            return newList

        dir     = "%s/%s_%s"%(options.production_label,options.module,dataset.name)
        dpmPath = "/dpm/oeaw.ac.at/home/cms/store/user/%s/nanoAOD/%s/"%(os.environ["USER"],dir)
        tmpPath = "/tmp/%s/"%dir
        if not os.path.isdir(tmpPath):
            try: os.makedirs(tmpPath)
            except: pass

        # split list of files in chunks, so that every subset contains options.unitsPerJob number of files
        if options.sorted: dataset.files.sort(key=lambda x: int(x.split("_")[-1].rstrip(".root")))
        splittedFileList = splitList( dataset.files, options.unitsPerJob )
        fileIndex        = 0

        if options.nJobs > 1:
            
            def jobList( l, n ):
                # split list l in n equal chunks
                k, m = divmod(len(l), n)
                return list(l[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n))

            options.nJobs = min( options.nJobs, len(splittedFileList) )
            if options.job >= options.nJobs:
                print "## Total number of jobs is %i. No Jobs left to run on. Exiting ..."%options.nJobs
                sys.exit(0)

            # every job should process an equal amount of files
            fileList         = jobList( splittedFileList, options.nJobs )
            fileIndex        = sum([len(l) for l in fileList[:options.job]])
            splittedFileList = fileList[options.job]

        for i, fileList in enumerate(splittedFileList):

            if options.sorted: fileList.sort(key=lambda x: int(x.split("_")[-1].rstrip(".root")))

            index = i + fileIndex
            outFile     = "%s_%i.root"%(dataset.name,index)
            dpmFilePath = os.path.join( dpmPath, outFile )
            tmpFilePath = os.path.join( tmpPath, outFile )

            cmd = [ 'cmsRun', os.environ["CMSRUN_CFG"], "outputFile=%s"%tmpFilePath, "inputFiles=%s"%",".join(fileList), "maxEvents=%i"%(int(options.totalUnits/options.unitsPerJob) if options.totalUnits else -1)]
            print "## Issue command: %s"%" ".join( cmd )
            if not options.dryrun:
                subprocess.call( cmd )

            print "## Files in TMP directory: %s"%", ".join(os.listdir(tmpPath))
            cmd = [ 'xrdcp', '-f',  tmpFilePath, redirector + dpmFilePath ]
            print "## Issue copy command: %s"%" ".join( cmd )
            if not options.dryrun:
                try: subprocess.call( cmd )
                except: subprocess.call( cmd )

    else:
        DASname, DAScampaign, DAStier = dataset.DASname.split('/')[1:]

        os.environ["CRAB_PROD_LABEL"]  = DAScampaign + "_" + options.production_label

        os.environ["ORIG_PROD_LABEL"]   = options.production_label
        os.environ["MAOD_SAMPLE_NAME"]  = DASname+"_"+DAScampaign

        os.environ["CRAB_DATASET"]      = dataset.DASname
        os.environ["CRAB_input_DBS"]    = options.inputDBS
        if options.dryrun:
            print "Processing %s %s" %( dataset.name, dataset.DASname )
            print "## Dryrun, continue..."
            continue

        os.system("crab submit -c crabConfig.py")

