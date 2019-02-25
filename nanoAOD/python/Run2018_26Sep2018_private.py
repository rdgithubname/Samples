import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
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
    from Samples.Tools.config import  redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"DB_Run2018_26Sep2018_private.sql"

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2018B_26Sep2018               = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_26Sep2018",                "/DoubleMuon/dspitzba-crab_Run2018B-26Sep2018-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")
DoubleMuon_Run2018B_26Sep2018_HEM           = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_26Sep2018_HEM",            "/DoubleMuon/dspitzba-crab_Run2018B-26Sep2018_HEM-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")
DoubleMuon_Run2018B_26Sep2018_HEMmitigation = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_26Sep2018_HEMmitigation",  "/DoubleMuon/dspitzba-crab_Run2018B-26Sep2018_HEMmitigation-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")

DoubleMuon = [
    DoubleMuon_Run2018B_26Sep2018,
    DoubleMuon_Run2018B_26Sep2018_HEM,
    DoubleMuon_Run2018B_26Sep2018_HEMmitigation,
    ]

# MuonEG
MuonEG_Run2018B_26Sep2018               = Sample.nanoAODfromDAS("MuonEG_Run2018B_26Sep2018",                "/MuonEG/dspitzba-crab_Run2018B-26Sep2018-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")
MuonEG_Run2018B_26Sep2018_HEM           = Sample.nanoAODfromDAS("MuonEG_Run2018B_26Sep2018_HEM",            "/MuonEG/dspitzba-crab_Run2018B-26Sep2018_HEM-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")
MuonEG_Run2018B_26Sep2018_HEMmitigation = Sample.nanoAODfromDAS("MuonEG_Run2018B_26Sep2018_HEMmitigation",  "/MuonEG/dspitzba-crab_Run2018B-26Sep2018_HEMmitigation-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")

MuonEG = [
    MuonEG_Run2018B_26Sep2018,
    MuonEG_Run2018B_26Sep2018_HEM,
    MuonEG_Run2018B_26Sep2018_HEMmitigation,
    ]

# EGamma
EGamma_Run2018B_26Sep2018               = Sample.nanoAODfromDAS("EGamma_Run2018B_26Sep2018",                "/EGamma/dspitzba-crab_Run2018B-26Sep2018-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")
EGamma_Run2018B_26Sep2018_HEM           = Sample.nanoAODfromDAS("EGamma_Run2018B_26Sep2018_HEM",            "/EGamma/dspitzba-crab_Run2018B-26Sep2018_HEM-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")
EGamma_Run2018B_26Sep2018_HEMmitigation = Sample.nanoAODfromDAS("EGamma_Run2018B_26Sep2018_HEMmitigation",  "/EGamma/dspitzba-crab_Run2018B-26Sep2018_HEMmitigation-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03")

EGamma = [
    EGamma_Run2018B_26Sep2018,
    EGamma_Run2018B_26Sep2018_HEM,
    EGamma_Run2018B_26Sep2018_HEMmitigation,
    ]

allSamples = DoubleMuon + MuonEG + EGamma

for s in allSamples:
    s.json = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt")
    s.isData  = True

