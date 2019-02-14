'''
dasgoclient -query="dataset=/*/Run2018*17Sep*/MINIAOD"
For A-C
'''
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
dbFile = dbDir+"Run2018_17Sep2018.sql"

logger.info("Using db file: %s", dbFile)


DoubleMuon_Run2018A_17Sep2018_v2 = FWLiteSample.fromDAS("DoubleMuon_Run2018A_17Sep2018_v2", "/DoubleMuon/Run2018A-17Sep2018-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
DoubleMuon_Run2018B_17Sep2018_v1 = FWLiteSample.fromDAS("DoubleMuon_Run2018B_17Sep2018_v1", "/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
DoubleMuon_Run2018C_17Sep2018_v1 = FWLiteSample.fromDAS("DoubleMuon_Run2018C_17Sep2018_v1", "/DoubleMuon/Run2018C-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

DoubleMuon = [
    DoubleMuon_Run2018A_17Sep2018_v2,
    DoubleMuon_Run2018B_17Sep2018_v1,
    DoubleMuon_Run2018C_17Sep2018_v1,
]

MuonEG_Run2018A_17Sep2018_v1 = FWLiteSample.fromDAS("MuonEG_Run2018A_17Sep2018_v1", "/MuonEG/Run2018A-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
MuonEG_Run2018B_17Sep2018_v1 = FWLiteSample.fromDAS("MuonEG_Run2018B_17Sep2018_v1", "/MuonEG/Run2018B-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
MuonEG_Run2018C_17Sep2018_v1 = FWLiteSample.fromDAS("MuonEG_Run2018C_17Sep2018_v1", "/MuonEG/Run2018C-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

MuonEG = [
    MuonEG_Run2018A_17Sep2018_v1,
    MuonEG_Run2018B_17Sep2018_v1,
    MuonEG_Run2018C_17Sep2018_v1,
]

EGamma_Run2018A_17Sep2018_v2 = FWLiteSample.fromDAS("EGamma_Run2018A_17Sep2018_v2", "/EGamma/Run2018A-17Sep2018-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
EGamma_Run2018B_17Sep2018_v1 = FWLiteSample.fromDAS("EGamma_Run2018B_17Sep2018_v1", "/EGamma/Run2018B-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
EGamma_Run2018C_17Sep2018_v1 = FWLiteSample.fromDAS("EGamma_Run2018C_17Sep2018_v1", "/EGamma/Run2018C-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

EGamma = [
    EGamma_Run2018A_17Sep2018_v2,
    EGamma_Run2018B_17Sep2018_v1,
    EGamma_Run2018C_17Sep2018_v1,
]

SingleMuon_Run2018A_17Sep2018_v2 = FWLiteSample.fromDAS("SingleMuon_Run2018A_17Sep2018_v2", "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
SingleMuon_Run2018B_17Sep2018_v1 = FWLiteSample.fromDAS("SingleMuon_Run2018B_17Sep2018_v1", "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
SingleMuon_Run2018C_17Sep2018_v1 = FWLiteSample.fromDAS("SingleMuon_Run2018C_17Sep2018_v1", "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

SingleMuon = [
    SingleMuon_Run2018A_17Sep2018_v2,
    SingleMuon_Run2018B_17Sep2018_v1,
    SingleMuon_Run2018C_17Sep2018_v1,
]

MET_Run2018A_17Sep2018_v1 = FWLiteSample.fromDAS("MET_Run2018A_17Sep2018_v1", "/MET/Run2018A-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
MET_Run2018B_17Sep2018_v1 = FWLiteSample.fromDAS("MET_Run2018B_17Sep2018_v1", "/MET/Run2018B-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
MET_Run2018C_17Sep2018_v1 = FWLiteSample.fromDAS("MET_Run2018C_17Sep2018_v1", "/MET/Run2018C-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

MET = [
    MET_Run2018A_17Sep2018_v1,
    MET_Run2018B_17Sep2018_v1,
    MET_Run2018C_17Sep2018_v1,
]

JetHT_Run2018A_17Sep2018_v1 = FWLiteSample.fromDAS("JetHT_Run2018A_17Sep2018_v1", "/JetHT/Run2018A-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
JetHT_Run2018B_17Sep2018_v1 = FWLiteSample.fromDAS("JetHT_Run2018B_17Sep2018_v1", "/JetHT/Run2018B-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
JetHT_Run2018C_17Sep2018_v1 = FWLiteSample.fromDAS("JetHT_Run2018C_17Sep2018_v1", "/JetHT/Run2018C-17Sep2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

JetHT = [
    JetHT_Run2018A_17Sep2018_v1,
    JetHT_Run2018B_17Sep2018_v1,
    JetHT_Run2018C_17Sep2018_v1,
]


## sum up
allSamples = DoubleMuon + MuonEG + EGamma + SingleMuon + MET + JetHT

for sample in allSamples:
    sample.isData = True

