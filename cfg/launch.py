import imp, os, sys
from optparse import OptionParser
import re

from Samples.miniAOD.Summer16_miniAODv3 import allSamples as Summer16_miniAODv3
from Samples.miniAOD.Summer16_miniAODv2 import allSamples as Summer16_miniAODv2
from Samples.miniAOD.Run2016_17Jul2018 import allSamples as Run2016_17Jul2018
from Samples.miniAOD.Run2018_26Sep2018 import allSamples as Run2018_26Sep2018


allSamples = Summer16_miniAODv3 + Summer16_miniAODv2 + Run2016_17Jul2018 + Run2018_26Sep2018

parser = OptionParser(usage="python launch.py [options] component1 [ component2 ...]", \
                          description="Launch heppy jobs with CRAB3. Components correspond to the variables defined in heppy_samples.py (their name attributes)")
parser.add_option("--production_label", dest="production_label",        help="production label", default="heppy")
parser.add_option("--remoteDir",        dest="remoteDir",               help="remote subdirectory", default="")
parser.add_option("--unitsPerJob",      dest="unitsPerJob",             help="Nr. of units (files) / crab job", type="int", default=1)
parser.add_option("--totalUnits",       dest="totalUnits",              help="Total nr. of units (files)", type="int", default=None)
parser.add_option("--era",              dest="era",                     help="Which era?")
parser.add_option("--sample",           dest="sample",                  help="Which sample?")
parser.add_option("--publish",          action='store_true',            help="Publish on dbs?", default=False)
( options, args ) = parser.parse_args()

dataset = None
for sample in allSamples:
    if sample.name == options.sample:
        dataset = sample.DASname

if dataset is None:
    raise NotImplementedError

os.system("scram runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

#os.environ["CMG_REMOTE_DIR"]  = options.remoteDir
os.environ["CRAB_UNITS_PER_JOB"] = str(options.unitsPerJob)
if options.totalUnits:
    os.environ["CRAB_TOTAL_UNITS"] = str(options.totalUnits)

m=re.match("\/(.*)\/(.*)\/(.*)",dataset)

os.environ["CRAB_PROD_LABEL"]  = m.group(2) + "_" + options.production_label

os.environ["MAOD_SAMPLE_M1"]    = m.group(1)
os.environ["MAOD_SAMPLE_M2"]    = m.group(2)
os.environ["ORIG_PROD_LABEL"]   = options.production_label
os.environ["MAOD_SAMPLE_NAME"]  = m.group(1)+"_"+m.group(2)

os.environ["CRAB_PUBLISH"]      = 'True' if options.publish else 'False'
os.environ["CRAB_DATASET"]      = dataset

print "### Publication is set to", os.environ["CRAB_PUBLISH"]

if options.era == '94X_mc':
    os.environ["CMSRUN_CFG"] = "test94X_NANO.py"
elif options.era == '80X_mc':
    os.environ["CMSRUN_CFG"] = "test80X_NANO.py"
elif options.era == '80X_mc_fast':
    os.environ["CMSRUN_CFG"] = "test80X_fast_NANO.py"
elif options.era == '94X_data':
    os.environ["CMSRUN_CFG"] = "test_data_94X_NANO.py"
elif options.era == '102X_data':
    os.environ["CMSRUN_CFG"] = "test_data_102X_NANO.py"
else:
    raise NotImplementedError

os.system("which crab")
os.system("crab submit -c crabConfig.py")

