import copy, os, sys
from RootTools.fwlite.FWLiteSample import FWLiteSample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite

else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"Run2018_26Sep2018.sql"

logger.info("Using db file: %s", dbFile)

## DoubleMuon
DoubleMuon_Run2018B_26Sep2018               = FWLiteSample.fromDAS("DoubleMuon_Run2018B_26Sep2018", "/DoubleMuon/Run2018B-26Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018B_26Sep2018_HEM           = FWLiteSample.fromDAS("DoubleMuon_Run2018B_26Sep2018_HEM", "/DoubleMuon/Run2018B-26Sep2018_HEM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018B_26Sep2018_HEMmitigation = FWLiteSample.fromDAS("DoubleMuon_Run2018B_26Sep2018_HEMmitigation", "/DoubleMuon/Run2018B-26Sep2018_HEMmitigation-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleMuon = [
    DoubleMuon_Run2018B_26Sep2018,
    DoubleMuon_Run2018B_26Sep2018_HEM,
    DoubleMuon_Run2018B_26Sep2018_HEMmitigation,
]

# MuonEG
MuonEG_Run2018B_26Sep2018               = FWLiteSample.fromDAS("MuonEG_Run2018B_26Sep2018", "/MuonEG/Run2018B-26Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018B_26Sep2018_HEM           = FWLiteSample.fromDAS("MuonEG_Run2018B_26Sep2018_HEM", "/MuonEG/Run2018B-26Sep2018_HEM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018B_26Sep2018_HEMmitigation = FWLiteSample.fromDAS("MuonEG_Run2018B_26Sep2018_HEMmitigation", "/MuonEG/Run2018B-26Sep2018_HEMmitigation-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MuonEG = [
    MuonEG_Run2018B_26Sep2018,
    MuonEG_Run2018B_26Sep2018_HEM,
    MuonEG_Run2018B_26Sep2018_HEMmitigation,
]

# EGamma
EGamma_Run2018B_26Sep2018               = FWLiteSample.fromDAS("EGamma_Run2018B_26Sep2018", "/EGamma/Run2018B-26Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018B_26Sep2018_HEM           = FWLiteSample.fromDAS("EGamma_Run2018B_26Sep2018_HEM", "/EGamma/Run2018B-26Sep2018_HEM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018B_26Sep2018_HEMmitigation = FWLiteSample.fromDAS("EGamma_Run2018B_26Sep2018_HEMmitigation", "/EGamma/Run2018B-26Sep2018_HEMmitigation-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

EGamma = [ 
    EGamma_Run2018B_26Sep2018,
    EGamma_Run2018B_26Sep2018_HEM,
    EGamma_Run2018B_26Sep2018_HEMmitigation,
]


## sum up
allSamples = DoubleMuon + MuonEG + EGamma

for sample in allSamples:
    sample.isData = True
