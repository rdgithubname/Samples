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

# MuonEG
MuonEG_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2016B_17Jul2018_ver1",   "/MuonEG/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2016B_17Jul2018_ver2",   "/MuonEG/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("MuonEG_Run2016C_17Jul2018",        "/MuonEG/dspitzba-crab_Run2016C-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("MuonEG_Run2016D_17Jul2018",        "/MuonEG/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("MuonEG_Run2016E_17Jul2018",        "/MuonEG/dspitzba-crab_Run2016E-17Jul2018-v2_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("MuonEG_Run2016F_17Jul2018",        "/MuonEG/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("MuonEG_Run2016G_17Jul2018",        "/MuonEG/dspitzba-crab_Run2016G-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("MuonEG_Run2016H_17Jul2018",        "/MuonEG/dspitzba-crab_Run2016H-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MuonEG = [
    MuonEG_Run2016B_17Jul2018_ver1,
    MuonEG_Run2016B_17Jul2018_ver2,
    MuonEG_Run2016C_17Jul2018,
    MuonEG_Run2016D_17Jul2018,
    MuonEG_Run2016E_17Jul2018,
    MuonEG_Run2016F_17Jul2018,
    MuonEG_Run2016G_17Jul2018,
    MuonEG_Run2016H_17Jul2018,
]

# DoubleEG
DoubleEG_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_17Jul2018_ver1",   "/DoubleEG/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_17Jul2018_ver2",   "/DoubleEG/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("DoubleEG_Run2016C_17Jul2018",        "/DoubleEG/dspitzba-crab_Run2016C-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("DoubleEG_Run2016D_17Jul2018",        "/DoubleEG/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("DoubleEG_Run2016E_17Jul2018",        "/DoubleEG/dspitzba-crab_Run2016E-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("DoubleEG_Run2016F_17Jul2018",        "/DoubleEG/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("DoubleEG_Run2016G_17Jul2018",        "/DoubleEG/dspitzba-crab_Run2016G-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("DoubleEG_Run2016H_17Jul2018",        "/DoubleEG/dspitzba-crab_Run2016H-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleEG = [
    DoubleEG_Run2016B_17Jul2018_ver1,
    DoubleEG_Run2016B_17Jul2018_ver2,
    DoubleEG_Run2016C_17Jul2018,
    DoubleEG_Run2016D_17Jul2018,
    DoubleEG_Run2016E_17Jul2018,
    DoubleEG_Run2016F_17Jul2018,
    DoubleEG_Run2016G_17Jul2018,
    DoubleEG_Run2016H_17Jul2018,
]

# SingleMuon
SingleMuon_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("SingleMuon_Run2016B_17Jul2018_ver1",   "/SingleMuon/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("SingleMuon_Run2016B_17Jul2018_ver2",   "/SingleMuon/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("SingleMuon_Run2016C_17Jul2018",        "/SingleMuon/dspitzba-crab_Run2016C-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("SingleMuon_Run2016D_17Jul2018",        "/SingleMuon/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("SingleMuon_Run2016E_17Jul2018",        "/SingleMuon/dspitzba-crab_Run2016E-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("SingleMuon_Run2016F_17Jul2018",        "/SingleMuon/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("SingleMuon_Run2016G_17Jul2018",        "/SingleMuon/dspitzba-crab_Run2016G-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("SingleMuon_Run2016H_17Jul2018",        "/SingleMuon/dspitzba-crab_Run2016H-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleMuon = [
    SingleMuon_Run2016B_17Jul2018_ver1,
    SingleMuon_Run2016B_17Jul2018_ver2,
    SingleMuon_Run2016C_17Jul2018,
    SingleMuon_Run2016D_17Jul2018,
    SingleMuon_Run2016E_17Jul2018,
    SingleMuon_Run2016F_17Jul2018,
    SingleMuon_Run2016G_17Jul2018,
    SingleMuon_Run2016H_17Jul2018,
]

# SingleElectron
SingleElectron_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_17Jul2018_ver1",   "/SingleElectron/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_17Jul2018_ver2",   "/SingleElectron/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("SingleElectron_Run2016C_17Jul2018",        "/SingleElectron/dspitzba-crab_Run2016C-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("SingleElectron_Run2016D_17Jul2018",        "/SingleElectron/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("SingleElectron_Run2016E_17Jul2018",        "/SingleElectron/dspitzba-crab_Run2016E-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("SingleElectron_Run2016F_17Jul2018",        "/SingleElectron/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("SingleElectron_Run2016G_17Jul2018",        "/SingleElectron/dspitzba-crab_Run2016G-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("SingleElectron_Run2016H_17Jul2018",        "/SingleElectron/dspitzba-crab_Run2016H-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleElectron = [
    SingleElectron_Run2016B_17Jul2018_ver1,
    SingleElectron_Run2016B_17Jul2018_ver2,
    SingleElectron_Run2016C_17Jul2018,
    SingleElectron_Run2016D_17Jul2018,
    SingleElectron_Run2016E_17Jul2018,
    SingleElectron_Run2016F_17Jul2018,
    SingleElectron_Run2016G_17Jul2018,
    SingleElectron_Run2016H_17Jul2018,
]

# JetHT
JetHT_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("JetHT_Run2016B_17Jul2018_ver1",   "/JetHT/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("JetHT_Run2016B_17Jul2018_ver2",   "/JetHT/dspitzba-crab_Run2016B-17Jul2018_ver2-v2_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("JetHT_Run2016C_17Jul2018",        "/JetHT/dspitzba-crab_Run2016C-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("JetHT_Run2016D_17Jul2018",        "/JetHT/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("JetHT_Run2016E_17Jul2018",        "/JetHT/dspitzba-crab_Run2016E-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("JetHT_Run2016F_17Jul2018",        "/JetHT/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("JetHT_Run2016G_17Jul2018",        "/JetHT/dspitzba-crab_Run2016G-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#JetHT_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("JetHT_Run2016H_17Jul2018",        "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

JetHT = [
    JetHT_Run2016B_17Jul2018_ver1,
    JetHT_Run2016B_17Jul2018_ver2,
    JetHT_Run2016C_17Jul2018,
    JetHT_Run2016D_17Jul2018,
    JetHT_Run2016E_17Jul2018,
    JetHT_Run2016F_17Jul2018,
    JetHT_Run2016G_17Jul2018,
#    JetHT_Run2016H_17Jul2018,
]

# MET
#MET_Run2016B_17Jul2018_ver1  = Sample.nanoAODfromDAS("MET_Run2016B_17Jul2018_ver1",   "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016B_17Jul2018_ver2  = Sample.nanoAODfromDAS("MET_Run2016B_17Jul2018_ver2",   "/MET/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#MET_Run2016C_17Jul2018       = Sample.nanoAODfromDAS("MET_Run2016C_17Jul2018",        "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016D_17Jul2018       = Sample.nanoAODfromDAS("MET_Run2016D_17Jul2018",        "/MET/dspitzba-crab_Run2016D-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016E_17Jul2018       = Sample.nanoAODfromDAS("MET_Run2016E_17Jul2018",        "/MET/dspitzba-crab_Run2016E-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016F_17Jul2018       = Sample.nanoAODfromDAS("MET_Run2016F_17Jul2018",        "/MET/dspitzba-crab_Run2016F-17Jul2018-v1_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
#MET_Run2016G_17Jul2018       = Sample.nanoAODfromDAS("MET_Run2016G_17Jul2018",        "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2016H_17Jul2018       = Sample.nanoAODfromDAS("MET_Run2016H_17Jul2018",        "/MET/dspitzba-crab_Run2016H-17Jul2018-v2_legacy_nano_v3-03ee60067ceb0bfa7485a17c69df2670/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MET = [
#    MET_Run2016B_17Jul2018_ver1,
    MET_Run2016B_17Jul2018_ver2,
#    MET_Run2016C_17Jul2018,
    MET_Run2016D_17Jul2018,
    MET_Run2016E_17Jul2018,
    MET_Run2016F_17Jul2018,
#    MET_Run2016G_17Jul2018,
    MET_Run2016H_17Jul2018,
]

allSamples = DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron + JetHT + MET

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt")
    s.isData    = True
