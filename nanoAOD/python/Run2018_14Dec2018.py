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
dbFile = dbDir+"/DB_Run2018_14Dec2018.sql"

logger.info("Using db file: %s", dbFile)

## DoubleMuon
DoubleMuon_Run2018A_14Dec2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_14Dec2018",   "/DoubleMuon/Run2018A-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018B_14Dec2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_14Dec2018",   "/DoubleMuon/Run2018B-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018C_14Dec2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_14Dec2018",   "/DoubleMuon/Run2018C-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2018D_14Dec2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_14Dec2018",   "/DoubleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

DoubleMuon_Run2018 = [\
    DoubleMuon_Run2018A_14Dec2018,
    DoubleMuon_Run2018B_14Dec2018,
    DoubleMuon_Run2018C_14Dec2018,
    DoubleMuon_Run2018D_14Dec2018,
    ]

## MuonEG
MuonEG_Run2018A_14Dec2018  = Sample.nanoAODfromDAS("MuonEG_Run2018A_14Dec2018",   "/MuonEG/Run2018A-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018B_14Dec2018  = Sample.nanoAODfromDAS("MuonEG_Run2018B_14Dec2018",   "/MuonEG/Run2018B-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018C_14Dec2018  = Sample.nanoAODfromDAS("MuonEG_Run2018C_14Dec2018",   "/MuonEG/Run2018C-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2018D_14Dec2018  = Sample.nanoAODfromDAS("MuonEG_Run2018D_14Dec2018",   "/MuonEG/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

MuonEG_Run2018 = [\
    MuonEG_Run2018A_14Dec2018,
    MuonEG_Run2018B_14Dec2018,
    MuonEG_Run2018C_14Dec2018,
    MuonEG_Run2018D_14Dec2018,
    ]

## DoubleEG
EGamma_Run2018A_14Dec2018  = Sample.nanoAODfromDAS("EGamma_Run2018A_14Dec2018",   "/EGamma/Run2018A-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018B_14Dec2018  = Sample.nanoAODfromDAS("EGamma_Run2018B_14Dec2018",   "/EGamma/Run2018B-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018C_14Dec2018  = Sample.nanoAODfromDAS("EGamma_Run2018C_14Dec2018",   "/EGamma/Run2018C-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
EGamma_Run2018D_14Dec2018  = Sample.nanoAODfromDAS("EGamma_Run2018D_14Dec2018",   "/EGamma/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

EGamma_Run2018 = [\
    EGamma_Run2018A_14Dec2018,
    EGamma_Run2018B_14Dec2018,
    EGamma_Run2018C_14Dec2018,
    EGamma_Run2018D_14Dec2018,
    ]


## SingleMuon
SingleMuon_Run2018A_14Dec2018  = Sample.nanoAODfromDAS("SingleMuon_Run2018A_14Dec2018",   "/SingleMuon/Run2018A-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018B_14Dec2018  = Sample.nanoAODfromDAS("SingleMuon_Run2018B_14Dec2018",   "/SingleMuon/Run2018B-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018C_14Dec2018  = Sample.nanoAODfromDAS("SingleMuon_Run2018C_14Dec2018",   "/SingleMuon/Run2018C-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2018D_14Dec2018  = Sample.nanoAODfromDAS("SingleMuon_Run2018D_14Dec2018",   "/SingleMuon/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

SingleMuon_Run2018 = [\
    SingleMuon_Run2018A_14Dec2018,
    SingleMuon_Run2018B_14Dec2018,
    SingleMuon_Run2018C_14Dec2018,
    SingleMuon_Run2018D_14Dec2018,
    ]

## MET
MET_Run2018A_14Dec2018  = Sample.nanoAODfromDAS("MET_Run2018A_14Dec2018",   "/MET/Run2018A-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
#MET_Run2018B_14Dec2018  = Sample.nanoAODfromDAS("MET_Run2018B_14Dec2018",   "/MET/Run2018B-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2018C_14Dec2018  = Sample.nanoAODfromDAS("MET_Run2018C_14Dec2018",   "/MET/Run2018C-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2018D_14Dec2018  = Sample.nanoAODfromDAS("MET_Run2018D_14Dec2018",   "/MET/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

MET_Run2018 = [\
    MET_Run2018A_14Dec2018,
#    MET_Run2018B_14Dec2018,
    MET_Run2018C_14Dec2018,
    MET_Run2018D_14Dec2018,
    ]

## JetHT
JetHT_Run2018A_14Dec2018  = Sample.nanoAODfromDAS("JetHT_Run2018A_14Dec2018",   "/JetHT/Run2018A-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
JetHT_Run2018B_14Dec2018  = Sample.nanoAODfromDAS("JetHT_Run2018B_14Dec2018",   "/JetHT/Run2018B-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
JetHT_Run2018C_14Dec2018  = Sample.nanoAODfromDAS("JetHT_Run2018C_14Dec2018",   "/JetHT/Run2018C-Nano14Dec2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
JetHT_Run2018D_14Dec2018  = Sample.nanoAODfromDAS("JetHT_Run2018D_14Dec2018",   "/JetHT/Run2018D-Nano14Dec2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

JetHT_Run2018 = [\
    JetHT_Run2018A_14Dec2018,
    JetHT_Run2018B_14Dec2018,
    JetHT_Run2018C_14Dec2018,
    JetHT_Run2018D_14Dec2018,
    ]

allSamples = DoubleMuon_Run2018 + MuonEG_Run2018 + EGamma_Run2018 + SingleMuon_Run2018 + MET_Run2018 + JetHT_Run2018

for s in allSamples:
    s.json = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt")
    s.isData  = True

