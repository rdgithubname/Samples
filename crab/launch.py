import imp, os, sys
from optparse import OptionParser
import re

# 2016 FastSim
from Samples.miniAOD.Spring16_miniAODv2 import allSamples as Spring16_miniAODv2
# 2016 FullSim
from Samples.miniAOD.Summer16_miniAODv2 import allSamples as Summer16_miniAODv2
from Samples.miniAOD.Summer16_miniAODv3 import allSamples as Summer16_miniAODv3
# 2017 FullSim
from Samples.miniAOD.Fall17_miniAODv2   import allSamples as Fall17_miniAODv2
# 2018 FullSim
from Samples.miniAOD.Autumn18_miniAODv1 import allSamples as Autumn18_miniAODv1
# 2016 Data
from Samples.miniAOD.Run2016_17Jul2018  import allSamples as Run2016_17Jul2018
# 2017 Data
from Samples.miniAOD.Run2017_31Mar2018  import allSamples as Run2017_31Mar2018
# 2018 special HEM Data
from Samples.miniAOD.Run2018_26Sep2018  import allSamples as Run2018_26Sep2018
# 2018 prompt Data (in the end only for D!)
from Samples.miniAOD.Run2018_promptReco import allSamples as Run2018_promptReco
# 2018 rereco Data (for A->C)
from Samples.miniAOD.Run2018_17Sep2018  import allSamples as Run2018_17Sep2018

all_modules = [ "Spring16_miniAODv2", "Summer16_miniAODv2", "Summer16_miniAODv3", "Fall17_miniAODv2", "Autumn18_miniAODv1"]
all_modules +=[ "Run2016_17Jul2018", "Run2017_31Mar2018", "Run2018_26Sep2018", "Run2018_promptReco", "Run2018_17Sep2018"]

allSamples  = Spring16_miniAODv2 + Summer16_miniAODv2 + Summer16_miniAODv3 + Fall17_miniAODv2 + Autumn18_miniAODv1
allSamples += Run2016_17Jul2018 + Run2017_31Mar2018 + Run2018_26Sep2018 + Run2018_promptReco + Run2018_17Sep2018

parser = OptionParser(usage="python launch.py [options] component1 [ component2 ...]", \
                          description="Launch heppy jobs with CRAB3. Components correspond to the variables defined in heppy_samples.py (their name attributes)")
parser.add_option("--production_label", dest="production_label",        help="production label", default="heppy")
parser.add_option("--remoteDir",        dest="remoteDir",               help="remote subdirectory", default="")
parser.add_option("--unitsPerJob",      dest="unitsPerJob",             help="Nr. of units (files) / crab job", type="int", default=1)
parser.add_option("--totalUnits",       dest="totalUnits",              help="Total nr. of units (files)", type="int", default=None)
parser.add_option("--config",           dest="config",                     help="Which config?")
parser.add_option("--module",           dest="module",                  choices = all_modules, help="Which module X in Samples.miniAOD.X?")
parser.add_option("--sample",           dest="sample",                  help="Which sample?")
parser.add_option("--publish",          action='store_true',            help="Publish on dbs?", default=False)
parser.add_option("--dryrun",           action='store_true',            help="Test script?", default=False)
( options, args ) = parser.parse_args()

print "## Starting submission to crab for sample(s) %s from module %s"%( options.sample, options.module )

module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/miniAOD/%s.py" % options.module )
try:
    tmp_module = imp.load_source( options.sample, os.path.expandvars( module_file ) ) 
    datasets   = getattr(tmp_module, options.sample)
except:
    raise RuntimeError( "Not found: Sample: %s, Module: %s, module_file: %s" % (options.sample, options.module, module_file) ) 

if type(datasets)!=type([]):
    datasets = [datasets]

print "## Will process from module %s the following samples: %s"%(options.module,  ",".join( d.name for d in datasets ) )

os.system("scram runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

## Config selection

# fullsim configs
if options.config == 'mc_80X_Summer16':
    CMSRUN_CFG = "nano_mc_80X_Summer16"
elif options.config == 'mc_94X_Summer16_miniAODv3':
    CMSRUN_CFG = "nano_mc_94X_Summer16_miniAODv3"
elif options.config == 'mc_94X_Fall17_miniAODv2':
    CMSRUN_CFG = "nano_mc_94X_Fall17_miniAODv2"
elif options.config == 'mc_102X_Autumn18_miniAODv1':
    CMSRUN_CFG = "nano_mc_102X_Autumn18_miniAODv1"
# fastsim configs
elif options.config == 'mc_80X_fast':
    CMSRUN_CFG = "nano_mc_fast_80X_Summer16"
# data configs
elif options.config == 'data_94X_Run2016':
    CMSRUN_CFG = "nano_data_94X_Run2016"
elif options.config == 'data_94X_Run2017':
    CMSRUN_CFG = "nano_data_94X_Run2017"
elif options.config == 'data_102X_Run2018_promptReco':
    CMSRUN_CFG = "nano_data_102X_Run2018_promptReco"
elif options.config == 'data_102X_Run2018_17Sep2018':
    CMSRUN_CFG = "nano_data_102X_Run2018_17Sep2018"

else:
    raise NotImplementedError

os.environ["CRAB_PUBLISH"]      = 'True' if options.publish else 'False'
print "## Publication is set to", os.environ["CRAB_PUBLISH"]

os.environ["CMSRUN_CFG"] = os.path.expandvars( "$CMSSW_BASE/src/Samples/cfg/%s.py" % CMSRUN_CFG )
print "## Will use the following config: %s"%os.environ["CMSRUN_CFG"]

os.system("which crab")

#os.environ["CMG_REMOTE_DIR"]  = options.remoteDir
os.environ["CRAB_UNITS_PER_JOB"] = str(options.unitsPerJob)
if options.totalUnits:
    os.environ["CRAB_TOTAL_UNITS"] = str(options.totalUnits)

for dataset in datasets:
    DASname, DAScampaign, DAStier = dataset.DASname.split('/')[1:]

    os.environ["CRAB_PROD_LABEL"]  = DAScampaign + "_" + options.production_label

    os.environ["ORIG_PROD_LABEL"]   = options.production_label
    os.environ["MAOD_SAMPLE_NAME"]  = DASname+"_"+DAScampaign

    os.environ["CRAB_DATASET"]      = dataset.DASname

    if options.dryrun:
        print "Processing %s %s" %( dataset.name, dataset.DASname )
        print "## Dryrun, continue..."
        continue

    os.system("crab submit -c crabConfig.py")

