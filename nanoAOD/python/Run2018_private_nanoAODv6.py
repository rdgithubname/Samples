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
            from Samples.Tools.config import redirector_clip_local as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2018_private_nanoAODv6.sql'

logger.info("Using db file: %s", dbFile)

'''
Single and double lepton PDs are generated with GTs using 2018 V8 JECs.
'''

# DoubleMuon
DoubleMuon_Run2018A_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2018A-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018B_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2018B-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018C_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2018C-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2018D_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2018D-831765d0aa9cd559fee11ff659127d4e/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2018A_25Oct2019,
    DoubleMuon_Run2018B_25Oct2019,
    DoubleMuon_Run2018C_25Oct2019,
    DoubleMuon_Run2018D_25Oct2019,
]

# MuonEG
MuonEG_Run2018A_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2018A_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2018A-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2018B_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2018B_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2018B-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2018C_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2018C_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2018C-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2018D_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2018D_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2018D-831765d0aa9cd559fee11ff659127d4e/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MuonEG = [
    MuonEG_Run2018A_25Oct2019,
    MuonEG_Run2018B_25Oct2019,
    MuonEG_Run2018C_25Oct2019,
    MuonEG_Run2018D_25Oct2019,
]

# EGamma
EGamma_Run2018A_25Oct2019 = Sample.nanoAODfromDAS("EGamma_Run2018A_25Oct2019", "/EGamma/schoef-TopNanoAODv6-1-2-4_EGamma_Run2018A-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
EGamma_Run2018B_25Oct2019 = Sample.nanoAODfromDAS("EGamma_Run2018B_25Oct2019", "/EGamma/schoef-TopNanoAODv6-1-2-4_EGamma_Run2018B-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
EGamma_Run2018C_25Oct2019 = Sample.nanoAODfromDAS("EGamma_Run2018C_25Oct2019", "/EGamma/schoef-TopNanoAODv6-1-2-4_EGamma_Run2018C-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
EGamma_Run2018D_25Oct2019 = Sample.nanoAODfromDAS("EGamma_Run2018D_25Oct2019", "/EGamma/schoef-TopNanoAODv6-1-2-4_EGamma_Run2018D-831765d0aa9cd559fee11ff659127d4e/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

EGamma = [
    EGamma_Run2018A_25Oct2019,
    EGamma_Run2018B_25Oct2019,
    EGamma_Run2018C_25Oct2019,
    EGamma_Run2018D_25Oct2019,
]

# SingleMuon
SingleMuon_Run2018A_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2018A_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2018A-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2018B_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2018B_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2018B-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2018C_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2018C_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2018C-2667fe41f354e79b08df8a25806ccf17/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2018D_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2018D_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2018D-831765d0aa9cd559fee11ff659127d4e/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleMuon = [
    SingleMuon_Run2018A_25Oct2019,
    SingleMuon_Run2018B_25Oct2019,
    SingleMuon_Run2018C_25Oct2019,
    SingleMuon_Run2018D_25Oct2019,
]

# JetHT
#JetHT_Run2018A_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2018A_25Oct2019", "",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#JetHT_Run2018B_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2018B_25Oct2019", "",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#JetHT_Run2018C_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2018C_25Oct2019", "",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#JetHT_Run2018D_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2018D_25Oct2019", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

JetHT = [
#    JetHT_Run2018A_25Oct2019,
#    JetHT_Run2018B_25Oct2019,
#    JetHT_Run2018C_25Oct2019,
#    JetHT_Run2018D_25Oct2019,
]

# MET
#MET_Run2018A_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2018A_25Oct2019", "",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#MET_Run2018B_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2018B_25Oct2019", "",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#MET_Run2018C_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2018C_25Oct2019", "",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#MET_Run2018D_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2018D_25Oct2019", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MET = [
#    MET_Run2018A_25Oct2019,
#    MET_Run2018B_25Oct2019,
#    MET_Run2018C_25Oct2019,
#    MET_Run2018D_25Oct2019,
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
