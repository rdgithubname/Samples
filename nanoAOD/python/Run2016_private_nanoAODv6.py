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
        from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2016_private_nanoAODv6.sql'
logger.info("Using db file: %s", dbFile)

# DoubleMuon
#DoubleMuon_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_25Oct2019_ver2",   "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_25Oct2019",        "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_25Oct2019",        "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_25Oct2019",        "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_25Oct2019",        "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("DoubleMuon_Run2016G_25Oct2019",        "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_25Oct2019",        "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleMuon = [
    #DoubleMuon_Run2016B_25Oct2019_ver1,
    DoubleMuon_Run2016B_25Oct2019_ver2,
    DoubleMuon_Run2016C_25Oct2019,
    DoubleMuon_Run2016D_25Oct2019,
    DoubleMuon_Run2016E_25Oct2019,
    DoubleMuon_Run2016F_25Oct2019,
    DoubleMuon_Run2016G_25Oct2019,
    DoubleMuon_Run2016H_25Oct2019,
]

# MuonEG
#MuonEG_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2016B_25Oct2019_ver2",   "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("MuonEG_Run2016C_25Oct2019",        "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("MuonEG_Run2016D_25Oct2019",        "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("MuonEG_Run2016E_25Oct2019",        "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("MuonEG_Run2016F_25Oct2019",        "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("MuonEG_Run2016G_25Oct2019",        "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("MuonEG_Run2016H_25Oct2019",        "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MuonEG = [
    #MuonEG_Run2016B_25Oct2019_ver1,
    MuonEG_Run2016B_25Oct2019_ver2,
    MuonEG_Run2016C_25Oct2019,
    MuonEG_Run2016D_25Oct2019,
    MuonEG_Run2016E_25Oct2019,
    MuonEG_Run2016F_25Oct2019,
    MuonEG_Run2016G_25Oct2019,
    MuonEG_Run2016H_25Oct2019,
]

# DoubleEG
#DoubleEG_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_25Oct2019_ver2",   "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("DoubleEG_Run2016C_25Oct2019",        "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("DoubleEG_Run2016D_25Oct2019",        "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("DoubleEG_Run2016E_25Oct2019",        "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("DoubleEG_Run2016F_25Oct2019",        "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("DoubleEG_Run2016G_25Oct2019",        "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("DoubleEG_Run2016H_25Oct2019",        "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleEG = [
    #DoubleEG_Run2016B_25Oct2019_ver1,
    DoubleEG_Run2016B_25Oct2019_ver2,
    DoubleEG_Run2016C_25Oct2019,
    DoubleEG_Run2016D_25Oct2019,
    DoubleEG_Run2016E_25Oct2019,
    DoubleEG_Run2016F_25Oct2019,
    DoubleEG_Run2016G_25Oct2019,
    DoubleEG_Run2016H_25Oct2019,
]

# SingleMuon
#SingleMuon_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("SingleMuon_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("SingleMuon_Run2016B_25Oct2019_ver2",   "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("SingleMuon_Run2016C_25Oct2019",        "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("SingleMuon_Run2016D_25Oct2019",        "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("SingleMuon_Run2016E_25Oct2019",        "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("SingleMuon_Run2016F_25Oct2019",        "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("SingleMuon_Run2016G_25Oct2019",        "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("SingleMuon_Run2016H_25Oct2019",        "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleMuon = [
    #SingleMuon_Run2016B_25Oct2019_ver1,
    SingleMuon_Run2016B_25Oct2019_ver2,
    SingleMuon_Run2016C_25Oct2019,
    SingleMuon_Run2016D_25Oct2019,
    SingleMuon_Run2016E_25Oct2019,
    SingleMuon_Run2016F_25Oct2019,
    SingleMuon_Run2016G_25Oct2019,
    SingleMuon_Run2016H_25Oct2019,
]

# SingleElectron
#SingleElectron_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_25Oct2019_ver2",   "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("SingleElectron_Run2016C_25Oct2019",        "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("SingleElectron_Run2016D_25Oct2019",        "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("SingleElectron_Run2016E_25Oct2019",        "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("SingleElectron_Run2016F_25Oct2019",        "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("SingleElectron_Run2016G_25Oct2019",        "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("SingleElectron_Run2016H_25Oct2019",        "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleElectron = [
    #SingleElectron_Run2016B_25Oct2019_ver1,
    SingleElectron_Run2016B_25Oct2019_ver2,
    SingleElectron_Run2016C_25Oct2019,
    SingleElectron_Run2016D_25Oct2019,
    SingleElectron_Run2016E_25Oct2019,
    SingleElectron_Run2016F_25Oct2019,
    SingleElectron_Run2016G_25Oct2019,
    SingleElectron_Run2016H_25Oct2019,
]

# JetHT
#JetHT_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("JetHT_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("JetHT_Run2016B_25Oct2019_ver2","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("JetHT_Run2016C_25Oct2019","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("JetHT_Run2016D_25Oct2019","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("JetHT_Run2016E_25Oct2019","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("JetHT_Run2016F_25Oct2019","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("JetHT_Run2016G_25Oct2019","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("JetHT_Run2016H_25Oct2019","/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

JetHT = [
    #JetHT_Run2016B_25Oct2019_ver1,
    JetHT_Run2016B_25Oct2019_ver2,
    JetHT_Run2016C_25Oct2019,
    JetHT_Run2016D_25Oct2019,
    JetHT_Run2016E_25Oct2019,
    JetHT_Run2016F_25Oct2019,
    JetHT_Run2016G_25Oct2019,
    JetHT_Run2016H_25Oct2019,
]

# MET
#MET_Run2016B_25Oct2019_ver1  = Sample.nanoAODfromDAS("MET_Run2016B_25Oct2019_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016B_25Oct2019_ver2  = Sample.nanoAODfromDAS("MET_Run2016B_25Oct2019_ver2",   "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016B_ver2-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016C_25Oct2019       = Sample.nanoAODfromDAS("MET_Run2016C_25Oct2019",        "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016C-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016D_25Oct2019       = Sample.nanoAODfromDAS("MET_Run2016D_25Oct2019",        "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016D-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016E_25Oct2019       = Sample.nanoAODfromDAS("MET_Run2016E_25Oct2019",        "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016E-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016F_25Oct2019       = Sample.nanoAODfromDAS("MET_Run2016F_25Oct2019",        "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016F-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016G_25Oct2019       = Sample.nanoAODfromDAS("MET_Run2016G_25Oct2019",        "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016G-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016H_25Oct2019       = Sample.nanoAODfromDAS("MET_Run2016H_25Oct2019",        "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2016H-ba7e3129b1ff910ad1abce6981b33804/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MET = [
    #MET_Run2016B_25Oct2019_ver1,
   MET_Run2016B_25Oct2019_ver2,
   MET_Run2016C_25Oct2019,
   MET_Run2016D_25Oct2019,
   MET_Run2016E_25Oct2019,
   MET_Run2016F_25Oct2019,
   MET_Run2016G_25Oct2019,
   MET_Run2016H_25Oct2019,
]

allSamples = DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron + JetHT + MET

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 ) 
