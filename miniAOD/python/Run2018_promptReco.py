'''
dasgoclient -query="dataset=/*/Run2018*PromptReco*/MINIAOD"
Only for Run2018D!
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
dbFile = dbDir+"Run2018_promptReco.sql"

logger.info("Using db file: %s", dbFile)


DoubleMuon_Run2018A_promptReco_v1 = FWLiteSample.fromDAS("DoubleMuon_Run2018A_promptReco_v1", "/DoubleMuon/Run2018A-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018A_promptReco_v2 = FWLiteSample.fromDAS("DoubleMuon_Run2018A_promptReco_v2", "/DoubleMuon/Run2018A-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018A_promptReco_v3 = FWLiteSample.fromDAS("DoubleMuon_Run2018A_promptReco_v3", "/DoubleMuon/Run2018A-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018B_promptReco_v1 = FWLiteSample.fromDAS("DoubleMuon_Run2018B_promptReco_v1", "/DoubleMuon/Run2018B-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018B_promptReco_v2 = FWLiteSample.fromDAS("DoubleMuon_Run2018B_promptReco_v2", "/DoubleMuon/Run2018B-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018C_promptReco_v1 = FWLiteSample.fromDAS("DoubleMuon_Run2018C_promptReco_v1", "/DoubleMuon/Run2018C-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018C_promptReco_v2 = FWLiteSample.fromDAS("DoubleMuon_Run2018C_promptReco_v2", "/DoubleMuon/Run2018C-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018C_promptReco_v3 = FWLiteSample.fromDAS("DoubleMuon_Run2018C_promptReco_v3", "/DoubleMuon/Run2018C-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018D_promptReco_v2 = FWLiteSample.fromDAS("DoubleMuon_Run2018D_promptReco_v2", "/DoubleMuon/Run2018D-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleMuon = [
    DoubleMuon_Run2018A_promptReco_v1,
    DoubleMuon_Run2018A_promptReco_v2,
    DoubleMuon_Run2018A_promptReco_v3,
    DoubleMuon_Run2018B_promptReco_v1,
    DoubleMuon_Run2018B_promptReco_v2,
    DoubleMuon_Run2018C_promptReco_v1,
    DoubleMuon_Run2018C_promptReco_v2,
    DoubleMuon_Run2018C_promptReco_v3,
    DoubleMuon_Run2018D_promptReco_v2,
]

EGamma_Run2018A_promptReco_v1 = FWLiteSample.fromDAS("EGamma_Run2018A_promptReco_v1", "/EGamma/Run2018A-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018A_promptReco_v2 = FWLiteSample.fromDAS("EGamma_Run2018A_promptReco_v2", "/EGamma/Run2018A-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018A_promptReco_v3 = FWLiteSample.fromDAS("EGamma_Run2018A_promptReco_v3", "/EGamma/Run2018A-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018B_promptReco_v1 = FWLiteSample.fromDAS("EGamma_Run2018B_promptReco_v1", "/EGamma/Run2018B-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018B_promptReco_v2 = FWLiteSample.fromDAS("EGamma_Run2018B_promptReco_v2", "/EGamma/Run2018B-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018C_promptReco_v1 = FWLiteSample.fromDAS("EGamma_Run2018C_promptReco_v1", "/EGamma/Run2018C-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018C_promptReco_v2 = FWLiteSample.fromDAS("EGamma_Run2018C_promptReco_v2", "/EGamma/Run2018C-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018C_promptReco_v3 = FWLiteSample.fromDAS("EGamma_Run2018C_promptReco_v3", "/EGamma/Run2018C-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018D_promptReco_v1 = FWLiteSample.fromDAS("EGamma_Run2018D_promptReco_v1", "/EGamma/Run2018D-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018D_promptReco_v2 = FWLiteSample.fromDAS("EGamma_Run2018D_promptReco_v2", "/EGamma/Run2018D-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

EGamma = [
    EGamma_Run2018A_promptReco_v1,
    EGamma_Run2018A_promptReco_v2,
    EGamma_Run2018A_promptReco_v3,
    EGamma_Run2018B_promptReco_v1,
    EGamma_Run2018B_promptReco_v2,
    EGamma_Run2018C_promptReco_v1,
    EGamma_Run2018C_promptReco_v2,
    EGamma_Run2018C_promptReco_v3,
    EGamma_Run2018D_promptReco_v1,
    EGamma_Run2018D_promptReco_v2,
]


MuonEG_Run2018A_promptReco_v1 = FWLiteSample.fromDAS("MuonEG_Run2018A_promptReco_v1", "/MuonEG/Run2018A-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018A_promptReco_v2 = FWLiteSample.fromDAS("MuonEG_Run2018A_promptReco_v2", "/MuonEG/Run2018A-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018A_promptReco_v3 = FWLiteSample.fromDAS("MuonEG_Run2018A_promptReco_v3", "/MuonEG/Run2018A-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018B_promptReco_v1 = FWLiteSample.fromDAS("MuonEG_Run2018B_promptReco_v1", "/MuonEG/Run2018B-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018B_promptReco_v2 = FWLiteSample.fromDAS("MuonEG_Run2018B_promptReco_v2", "/MuonEG/Run2018B-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018C_promptReco_v1 = FWLiteSample.fromDAS("MuonEG_Run2018C_promptReco_v1", "/MuonEG/Run2018C-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018C_promptReco_v2 = FWLiteSample.fromDAS("MuonEG_Run2018C_promptReco_v2", "/MuonEG/Run2018C-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018C_promptReco_v3 = FWLiteSample.fromDAS("MuonEG_Run2018C_promptReco_v3", "/MuonEG/Run2018C-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2018D_promptReco_v2 = FWLiteSample.fromDAS("MuonEG_Run2018D_promptReco_v2", "/MuonEG/Run2018D-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MuonEG = [
    MuonEG_Run2018A_promptReco_v1,
    MuonEG_Run2018A_promptReco_v2,
    MuonEG_Run2018A_promptReco_v3,
    MuonEG_Run2018B_promptReco_v1,
    MuonEG_Run2018B_promptReco_v2,
    MuonEG_Run2018C_promptReco_v1,
    MuonEG_Run2018C_promptReco_v2,
    MuonEG_Run2018C_promptReco_v3,
    MuonEG_Run2018D_promptReco_v2,
]

SingleMuon_Run2018A_promptReco_v1 = FWLiteSample.fromDAS("SingleMuon_Run2018A_promptReco_v1", "/SingleMuon/Run2018A-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018A_promptReco_v2 = FWLiteSample.fromDAS("SingleMuon_Run2018A_promptReco_v2", "/SingleMuon/Run2018A-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018A_promptReco_v3 = FWLiteSample.fromDAS("SingleMuon_Run2018A_promptReco_v3", "/SingleMuon/Run2018A-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018B_promptReco_v1 = FWLiteSample.fromDAS("SingleMuon_Run2018B_promptReco_v1", "/SingleMuon/Run2018B-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018B_promptReco_v2 = FWLiteSample.fromDAS("SingleMuon_Run2018B_promptReco_v2", "/SingleMuon/Run2018B-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018C_promptReco_v1 = FWLiteSample.fromDAS("SingleMuon_Run2018C_promptReco_v1", "/SingleMuon/Run2018C-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018C_promptReco_v2 = FWLiteSample.fromDAS("SingleMuon_Run2018C_promptReco_v2", "/SingleMuon/Run2018C-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018C_promptReco_v3 = FWLiteSample.fromDAS("SingleMuon_Run2018C_promptReco_v3", "/SingleMuon/Run2018C-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018D_promptReco_v2 = FWLiteSample.fromDAS("SingleMuon_Run2018D_promptReco_v2", "/SingleMuon/Run2018D-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleMuon = [
    SingleMuon_Run2018A_promptReco_v1,
    SingleMuon_Run2018A_promptReco_v2,
    SingleMuon_Run2018A_promptReco_v3,
    SingleMuon_Run2018B_promptReco_v1,
    SingleMuon_Run2018B_promptReco_v2,
    SingleMuon_Run2018C_promptReco_v1,
    SingleMuon_Run2018C_promptReco_v2,
    SingleMuon_Run2018C_promptReco_v3,
    SingleMuon_Run2018D_promptReco_v2,
]

JetHT_Run2018A_promptReco_v1 = FWLiteSample.fromDAS("JetHT_Run2018A_promptReco_v1", "/JetHT/Run2018A-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018A_promptReco_v2 = FWLiteSample.fromDAS("JetHT_Run2018A_promptReco_v2", "/JetHT/Run2018A-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018A_promptReco_v3 = FWLiteSample.fromDAS("JetHT_Run2018A_promptReco_v3", "/JetHT/Run2018A-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018B_promptReco_v1 = FWLiteSample.fromDAS("JetHT_Run2018B_promptReco_v1", "/JetHT/Run2018B-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018B_promptReco_v2 = FWLiteSample.fromDAS("JetHT_Run2018B_promptReco_v2", "/JetHT/Run2018B-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018C_promptReco_v1 = FWLiteSample.fromDAS("JetHT_Run2018C_promptReco_v1", "/JetHT/Run2018C-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018C_promptReco_v2 = FWLiteSample.fromDAS("JetHT_Run2018C_promptReco_v2", "/JetHT/Run2018C-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018C_promptReco_v3 = FWLiteSample.fromDAS("JetHT_Run2018C_promptReco_v3", "/JetHT/Run2018C-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018D_promptReco_v1 = FWLiteSample.fromDAS("JetHT_Run2018D_promptReco_v1", "/JetHT/Run2018D-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018D_promptReco_v2 = FWLiteSample.fromDAS("JetHT_Run2018D_promptReco_v2", "/JetHT/Run2018D-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

JetHT = [
    JetHT_Run2018A_promptReco_v1,
    JetHT_Run2018A_promptReco_v2,
    JetHT_Run2018A_promptReco_v3,
    JetHT_Run2018B_promptReco_v1,
    JetHT_Run2018B_promptReco_v2,
    JetHT_Run2018C_promptReco_v1,
    JetHT_Run2018C_promptReco_v2,
    JetHT_Run2018C_promptReco_v3,
    JetHT_Run2018D_promptReco_v1,
    JetHT_Run2018D_promptReco_v2,
]

MET_Run2018A_promptReco_v1 = FWLiteSample.fromDAS("MET_Run2018A_promptReco_v1", "/MET/Run2018A-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018A_promptReco_v2 = FWLiteSample.fromDAS("MET_Run2018A_promptReco_v2", "/MET/Run2018A-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018A_promptReco_v3 = FWLiteSample.fromDAS("MET_Run2018A_promptReco_v3", "/MET/Run2018A-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018B_promptReco_v1 = FWLiteSample.fromDAS("MET_Run2018B_promptReco_v1", "/MET/Run2018B-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018B_promptReco_v2 = FWLiteSample.fromDAS("MET_Run2018B_promptReco_v2", "/MET/Run2018B-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018C_promptReco_v1 = FWLiteSample.fromDAS("MET_Run2018C_promptReco_v1", "/MET/Run2018C-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018C_promptReco_v2 = FWLiteSample.fromDAS("MET_Run2018C_promptReco_v2", "/MET/Run2018C-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018C_promptReco_v3 = FWLiteSample.fromDAS("MET_Run2018C_promptReco_v3", "/MET/Run2018C-PromptReco-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018D_promptReco_v1 = FWLiteSample.fromDAS("MET_Run2018D_promptReco_v1", "/MET/Run2018D-PromptReco-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018D_promptReco_v2 = FWLiteSample.fromDAS("MET_Run2018D_promptReco_v2", "/MET/Run2018D-PromptReco-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [
    MET_Run2018A_promptReco_v1,
    MET_Run2018A_promptReco_v2,
    MET_Run2018A_promptReco_v3,
    MET_Run2018B_promptReco_v1,
    MET_Run2018B_promptReco_v2,
    MET_Run2018C_promptReco_v1,
    MET_Run2018C_promptReco_v2,
    MET_Run2018C_promptReco_v3,
    MET_Run2018D_promptReco_v1,
    MET_Run2018D_promptReco_v2,
]




## sum up
allSamples = DoubleMuon + MuonEG + EGamma + SingleMuon + JetHT + MET

for sample in allSamples:
    sample.isData = True
