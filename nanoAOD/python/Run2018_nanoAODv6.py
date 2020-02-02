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
    if "clip" in os.getenv("HOSTNAME").lower():
        if __name__ == "__main__":
            from Samples.Tools.config import redirector_global_clip as redirector
        else:
            from Samples.Tools.config import redirector_clip_scratch as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2018_nanoAODv6.sql'

logger.info("Using db file: %s", dbFile)

'''
Single and double lepton PDs are generated with GTs using 2018 V8 JECs.
'''

# DoubleMuon
DoubleMuon_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_17Sep2018", "/DoubleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_17Sep2018", "/DoubleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_17Sep2018", "/DoubleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_17Sep2018", "/DoubleMuon/Run2018D-Nano25Oct2019_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2018A_17Sep2018,
    DoubleMuon_Run2018B_17Sep2018,
    DoubleMuon_Run2018C_17Sep2018,
    DoubleMuon_Run2018D_17Sep2018,
]

# MuonEG
MuonEG_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018A_17Sep2018", "/MuonEG/Run2018A-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018B_17Sep2018", "/MuonEG/Run2018B-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018C_17Sep2018", "/MuonEG/Run2018C-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018D_17Sep2018", "/MuonEG/Run2018D-Nano25Oct2019_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MuonEG = [
    MuonEG_Run2018A_17Sep2018,
    MuonEG_Run2018B_17Sep2018,
    MuonEG_Run2018C_17Sep2018,
    MuonEG_Run2018D_17Sep2018,
]

# EGamma
EGamma_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018A_17Sep2018", "/EGamma/Run2018A-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
EGamma_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018B_17Sep2018", "/EGamma/Run2018B-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
EGamma_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018C_17Sep2018", "/EGamma/Run2018C-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
EGamma_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018D_17Sep2018", "/EGamma/Run2018D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

EGamma = [
    EGamma_Run2018A_17Sep2018,
    EGamma_Run2018B_17Sep2018,
    EGamma_Run2018C_17Sep2018,
    EGamma_Run2018D_17Sep2018,
]

# SingleMuon
SingleMuon_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018A_17Sep2018", "/SingleMuon/Run2018A-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018B_17Sep2018", "/SingleMuon/Run2018B-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018C_17Sep2018", "/SingleMuon/Run2018C-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018D_17Sep2018", "/SingleMuon/Run2018D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleMuon = [
    SingleMuon_Run2018A_17Sep2018,
    SingleMuon_Run2018B_17Sep2018,
    SingleMuon_Run2018C_17Sep2018,
    SingleMuon_Run2018D_17Sep2018,
]

# JetHT
JetHT_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018A_17Sep2018", "/JetHT/Run2018A-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018B_17Sep2018", "/JetHT/Run2018B-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018C_17Sep2018", "/JetHT/Run2018C-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018D_17Sep2018", "/JetHT/Run2018D-Nano25Oct2019_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

JetHT = [
    JetHT_Run2018A_17Sep2018,
    JetHT_Run2018B_17Sep2018,
    JetHT_Run2018C_17Sep2018,
    JetHT_Run2018D_17Sep2018,
]

# MET
MET_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018A_17Sep2018", "/MET/Run2018A-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018B_17Sep2018", "/MET/Run2018B-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018C_17Sep2018", "/MET/Run2018C-Nano25Oct2019-v1/NANOAOD",  dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018D_17Sep2018", "/MET/Run2018D-Nano25Oct2019_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MET = [
    MET_Run2018A_17Sep2018,
    MET_Run2018B_17Sep2018,
    MET_Run2018C_17Sep2018,
    MET_Run2018D_17Sep2018,
]

allSamples = DoubleMuon + MuonEG + EGamma + SingleMuon + JetHT + MET

for s in allSamples:
    s.json = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt")
    s.isData  = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
