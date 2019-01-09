import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )

    def get_parser():
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
        argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
        return argParser
    
    options = get_parser().parse_args()
    ov = options.overwrite

else:
    import logging
    logger = logging.getLogger(__name__)

    ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"DB_Run2016_17Jul2018_private.sql"

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_17Jul2018_ver1",   "/DoubleMuon/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_17Jul2018_ver2",   "/DoubleMuon/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_17Jul2018",        "/DoubleMuon/dspitzba-crab_Run2016C-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_17Jul2018",        "/DoubleMuon/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_17Jul2018",        "/DoubleMuon/dspitzba-crab_Run2016E-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_17Jul2018",        "/DoubleMuon/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016G_17Jul2018",        "/DoubleMuon/dspitzba-crab_Run2016G-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_17Jul2018",        "/DoubleMuon/dspitzba-crab_Run2016H-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)








DoubleMuon = [
    DoubleMuon_Run2016B_17Jul2018_ver1,
    DoubleMuon_Run2016B_17Jul2018_ver2,
    DoubleMuon_Run2016C_17Jul2018,
    DoubleMuon_Run2016D_17Jul2018,
    DoubleMuon_Run2016E_17Jul2018,
    DoubleMuon_Run2016F_17Jul2018,
    DoubleMuon_Run2016G_17Jul2018,
    DoubleMuon_Run2016H_17Jul2018,
]

MuonEG = [
]

DoubleEG = [
]

allSamples = DoubleMuon + MuonEG + DoubleEG

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt")
    s.isData    = True
