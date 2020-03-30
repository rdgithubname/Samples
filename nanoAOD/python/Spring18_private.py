import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        from Samples.Tools.config import redirector_clip_local as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Spring18_private.sql"

logger.info("Using db file: %s", dbFile)

## ttbar
TTLep_100X           = Sample.nanoAODfromDAS("TTLep_100X",          "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/dspitzba-crab_RunIISpring18MiniAOD-100X_upgrade2018_realistic_v10_ext1-v3_2018_v5-02dd2892506b658709fe71e2994c83cd/USER",           instance="phys03", genWeight="(1)", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.76*((3*0.108)**2) ) #3M
TTLep_100X_pilot     = Sample.nanoAODfromDAS("TTLep_100X_pilot",    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/dspitzba-crab_RunIISpring18MiniAOD-pilot_100X_upgrade2018_realistic_v10-v2_2018_v5-02dd2892506b658709fe71e2994c83cd/USER",          instance="phys03", genWeight="(1)", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.76*((3*0.108)**2) ) #1M
TTLep_100X_HEM_ext1  = Sample.nanoAODfromDAS("TTLep_100X_HEM_ext1", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/dspitzba-crab_RunIISpring18MiniAOD-HEMPremix_100X_upgrade2018_realistic_v10_ext1-v2_2018_v5-02dd2892506b658709fe71e2994c83cd/USER", instance="phys03", genWeight="(1)", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.76*((3*0.108)**2) ) #3M
TTLep_100X_HEM_ext2  = Sample.nanoAODfromDAS("TTLep_100X_HEM_ext2", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/dspitzba-crab_RunIISpring18MiniAOD-HEMPremix_100X_upgrade2018_realistic_v10_ext2-v1_2018_v5-02dd2892506b658709fe71e2994c83cd/USER", instance="phys03", genWeight="(1)", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.76*((3*0.108)**2) ) #3M


top = [
    TTLep_100X,
    TTLep_100X_pilot,
    TTLep_100X_HEM_ext1,
    TTLep_100X_HEM_ext2
    ]


allSamples = top


for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )

