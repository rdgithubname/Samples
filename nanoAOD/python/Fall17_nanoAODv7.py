import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
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
        if __name__ == "__main__" and not options.check_completeness:
            from Samples.Tools.config import redirector_global as redirector
        else:
            from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

print redirector
# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Fall17_nanoAODv7.sql'

logger.info("Using db file: %s", dbFile)

tWll_thad_Wlept_DR  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DR",  "/TWZToLL_thad_Wlept_5f_DR_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_thad_Wlept_DS  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DS",  "/TWZToLL_thad_Wlept_5f_DS_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Whad_DR  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DR",  "/TWZToLL_tlept_Whad_5f_DR_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Whad_DS  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DS",  "/TWZToLL_tlept_Whad_5f_DS_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
tWll_tlept_Wlept_DR = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DR", "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )
tWll_tlept_Wlept_DS = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DS", "/TWZToLL_tlept_Wlept_5f_DS_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )

top = [
    tWll_thad_Wlept_DR,
    tWll_thad_Wlept_DS,
    tWll_tlept_Whad_DR,
    tWll_tlept_Whad_DS,
    tWll_tlept_Wlept_DR,
    tWll_tlept_Wlept_DS,
]

allSamples = top

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=10 )
