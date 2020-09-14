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
        from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Run2018_17Sep2018_private.sql"

logger.info("Using db file: %s", dbFile)

'''
Single and double lepton PDs are generated with GTs using 2018 V8 JECs.
'''

# DoubleMuon
DoubleMuon_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018A-17Sep2018-v2_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018B-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018C-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_17Sep2018", "/DoubleMuon/dspitzba-crab_Run2018D-PromptReco-v2_legacy_nano_v4-67e33113cecc3df848e7adac0079af3d/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2018A_17Sep2018,
    DoubleMuon_Run2018B_17Sep2018,
    DoubleMuon_Run2018C_17Sep2018,
    DoubleMuon_Run2018D_17Sep2018,
]

# MuonEG
MuonEG_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018A_17Sep2018", "/MuonEG/dspitzba-crab_Run2018A-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018B_17Sep2018", "/MuonEG/dspitzba-crab_Run2018B-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018C_17Sep2018", "/MuonEG/dspitzba-crab_Run2018C-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("MuonEG_Run2018D_17Sep2018", "/MuonEG/dspitzba-crab_Run2018D-PromptReco-v2_legacy_nano_v4-67e33113cecc3df848e7adac0079af3d/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MuonEG = [
    MuonEG_Run2018A_17Sep2018,
    MuonEG_Run2018B_17Sep2018,
    MuonEG_Run2018C_17Sep2018,
    MuonEG_Run2018D_17Sep2018,
]

# EGamma
EGamma_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018A_17Sep2018", "/EGamma/dspitzba-crab_Run2018A-17Sep2018-v2_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
EGamma_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018B_17Sep2018", "/EGamma/dspitzba-crab_Run2018B-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
EGamma_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018C_17Sep2018", "/EGamma/dspitzba-crab_Run2018C-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
EGamma_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018D_17Sep2018", "/EGamma/dspitzba-crab_Run2018D-PromptReco-v2_legacy_nano_v4-67e33113cecc3df848e7adac0079af3d/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#EGamma_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("EGamma_Run2018D_17Sep2018", "/EGamma/schoef-crab_Run2018D-22Jan2019-v2_legacy_nano_v5-fd74ba782b114ba9806803805a362d43/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

EGamma = [
    EGamma_Run2018A_17Sep2018,
    EGamma_Run2018B_17Sep2018,
    EGamma_Run2018C_17Sep2018,
    EGamma_Run2018D_17Sep2018,
]

# SingleMuon
SingleMuon_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018A_17Sep2018", "/SingleMuon/dspitzba-crab_Run2018A-17Sep2018-v2_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018B_17Sep2018", "/SingleMuon/dspitzba-crab_Run2018B-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018C_17Sep2018", "/SingleMuon/dspitzba-crab_Run2018C-17Sep2018-v1_legacy_nano_v4-54bc8181fe074b255f8b5cd51be6ae49/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018D_17Sep2018", "/SingleMuon/dspitzba-crab_Run2018D-PromptReco-v2_legacy_nano_v4-67e33113cecc3df848e7adac0079af3d/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#SingleMuon_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("SingleMuon_Run2018D_17Sep2018", "/SingleMuon/schoef-crab_Run2018D-22Jan2019-v2_legacy_nano_v5-fd74ba782b114ba9806803805a362d43/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleMuon = [
    SingleMuon_Run2018A_17Sep2018,
    SingleMuon_Run2018B_17Sep2018,
    SingleMuon_Run2018C_17Sep2018,
    SingleMuon_Run2018D_17Sep2018,
]

# JetHT
JetHT_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018A_17Sep2018", "/JetHT/llechner-crab_Run2018A-17Sep2018-v1_legacy_nano_v3-64dd1b7ffa8685539eecf5892de8b932/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018B_17Sep2018", "/JetHT/llechner-crab_Run2018B-17Sep2018-v1_legacy_nano_v3-64dd1b7ffa8685539eecf5892de8b932/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018C_17Sep2018", "/JetHT/llechner-crab_Run2018C-17Sep2018-v1_legacy_nano_v3-64dd1b7ffa8685539eecf5892de8b932/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("JetHT_Run2018D_17Sep2018", "/JetHT/llechner-crab_Run2018D-PromptReco-v2_legacy_nano_v4-9584527b655981757f752982f8020420/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

JetHT = [
    JetHT_Run2018A_17Sep2018,
    JetHT_Run2018B_17Sep2018,
    JetHT_Run2018C_17Sep2018,
    JetHT_Run2018D_17Sep2018,
]

# MET
MET_Run2018A_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018A_17Sep2018", "/MET/llechner-crab_Run2018A-17Sep2018-v1_legacy_nano_v3-64dd1b7ffa8685539eecf5892de8b932/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2018B_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018B_17Sep2018", "/MET/llechner-crab_Run2018B-17Sep2018-v1_legacy_nano_v3-64dd1b7ffa8685539eecf5892de8b932/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2018C_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018C_17Sep2018", "/MET/llechner-crab_Run2018C-17Sep2018-v1_legacy_nano_v3-64dd1b7ffa8685539eecf5892de8b932/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2018D_17Sep2018 = Sample.nanoAODfromDAS("MET_Run2018D_17Sep2018", "/MET/llechner-crab_Run2018D-PromptReco-v2_legacy_nano_v4-9584527b655981757f752982f8020420/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

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
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )

