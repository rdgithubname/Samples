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
        from Samples.Tools.config import redirector_clip_local as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Run2016_05Feb2018.sql"

logger.info("Using db file: %s", dbFile)

# specify a local directory if you want to create (and afterwards automatically use) a local copy of the sample, otherwise use the grid.

## DoubleMuon
DoubleMuon_Run2016B_05Feb2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_05Feb2018_ver1",   "/DoubleMuon/Run2016B-05Feb2018_ver1-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016B_05Feb2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_05Feb2018_ver2",   "/DoubleMuon/Run2016B-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016C_05Feb2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_05Feb2018",        "/DoubleMuon/Run2016C-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016D_05Feb2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_05Feb2018",        "/DoubleMuon/Run2016D-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016E_05Feb2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_05Feb2018",        "/DoubleMuon/Run2016E-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016F_05Feb2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_05Feb2018",        "/DoubleMuon/Run2016F-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016G_05Feb2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016G_05Feb2018",        "/DoubleMuon/Run2016G-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016H_05Feb2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_05Feb2018_ver2",   "/DoubleMuon/Run2016H-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016H_05Feb2018_ver3  = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_05Feb2018_ver3",   "/DoubleMuon/Run2016H-05Feb2018_ver3-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

DoubleMuon_Run2016 = [\
    DoubleMuon_Run2016B_05Feb2018_ver1,
    DoubleMuon_Run2016B_05Feb2018_ver2,
    DoubleMuon_Run2016C_05Feb2018,
    DoubleMuon_Run2016D_05Feb2018,
    DoubleMuon_Run2016E_05Feb2018,
    DoubleMuon_Run2016F_05Feb2018,
    DoubleMuon_Run2016G_05Feb2018,
    DoubleMuon_Run2016H_05Feb2018_ver2,
    DoubleMuon_Run2016H_05Feb2018_ver3,
    ]

## MuonEG
MuonEG_Run2016B_05Feb2018_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2016B_05Feb2018_ver1",   "/MuonEG/Run2016B-05Feb2018_ver1-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016B_05Feb2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2016B_05Feb2018_ver2",   "/MuonEG/Run2016B-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016C_05Feb2018       = Sample.nanoAODfromDAS("MuonEG_Run2016C_05Feb2018",        "/MuonEG/Run2016C-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016D_05Feb2018       = Sample.nanoAODfromDAS("MuonEG_Run2016D_05Feb2018",        "/MuonEG/Run2016D-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016E_05Feb2018       = Sample.nanoAODfromDAS("MuonEG_Run2016E_05Feb2018",        "/MuonEG/Run2016E-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016F_05Feb2018       = Sample.nanoAODfromDAS("MuonEG_Run2016F_05Feb2018",        "/MuonEG/Run2016F-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016G_05Feb2018       = Sample.nanoAODfromDAS("MuonEG_Run2016G_05Feb2018",        "/MuonEG/Run2016G-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016H_05Feb2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2016H_05Feb2018_ver2",   "/MuonEG/Run2016H-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016H_05Feb2018_ver3  = Sample.nanoAODfromDAS("MuonEG_Run2016H_05Feb2018_ver3",   "/MuonEG/Run2016H-05Feb2018_ver3-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

MuonEG_Run2016 = [\
    MuonEG_Run2016B_05Feb2018_ver1,
    MuonEG_Run2016B_05Feb2018_ver2,
    MuonEG_Run2016C_05Feb2018,
    MuonEG_Run2016D_05Feb2018,
    MuonEG_Run2016E_05Feb2018,
    MuonEG_Run2016F_05Feb2018,
    MuonEG_Run2016G_05Feb2018,
    MuonEG_Run2016H_05Feb2018_ver2,
    MuonEG_Run2016H_05Feb2018_ver3,
    ]

## DoubleEG
DoubleEG_Run2016B_05Feb2018_ver1    = Sample.nanoAODfromDAS("DoubleEG_Run2016B_05Feb2018_ver1", "/DoubleEG/Run2016B-05Feb2018_ver1-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016B_05Feb2018_ver2    = Sample.nanoAODfromDAS("DoubleEG_Run2016B_05Feb2018_ver2", "/DoubleEG/Run2016B-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016C_05Feb2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016C_05Feb2018",      "/DoubleEG/Run2016C-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016D_05Feb2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016D_05Feb2018",      "/DoubleEG/Run2016D-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016E_05Feb2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016E_05Feb2018",      "/DoubleEG/Run2016E-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016F_05Feb2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016F_05Feb2018",      "/DoubleEG/Run2016F-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016G_05Feb2018         = Sample.nanoAODfromDAS("DoubleEG_Run2016G_05Feb2018",      "/DoubleEG/Run2016G-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016H_05Feb2018_ver2    = Sample.nanoAODfromDAS("DoubleEG_Run2016H_05Feb2018_ver2", "/DoubleEG/Run2016H-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016H_05Feb2018_ver3    = Sample.nanoAODfromDAS("DoubleEG_Run2016H_05Feb2018_ver3", "/DoubleEG/Run2016H-05Feb2018_ver3-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

DoubleEG_Run2016 = [\
    DoubleEG_Run2016B_05Feb2018_ver1,
    DoubleEG_Run2016B_05Feb2018_ver2,
    DoubleEG_Run2016C_05Feb2018,
    DoubleEG_Run2016D_05Feb2018,
    DoubleEG_Run2016E_05Feb2018,
    DoubleEG_Run2016F_05Feb2018,
    DoubleEG_Run2016G_05Feb2018,
    DoubleEG_Run2016H_05Feb2018_ver2,
    DoubleEG_Run2016H_05Feb2018_ver3,
    ]
    
## SingleElectron
SingleElectron_Run2016B_05Feb2018_ver1    = Sample.nanoAODfromDAS("SingleElectron_Run2016B_05Feb2018_ver1", "/SingleElectron/Run2016B-05Feb2018_ver1-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016B_05Feb2018_ver2    = Sample.nanoAODfromDAS("SingleElectron_Run2016B_05Feb2018_ver2", "/SingleElectron/Run2016B-05Feb2018_ver2-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016C_05Feb2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016C_05Feb2018",      "/SingleElectron/Run2016C-05Feb2018-v2/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016D_05Feb2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016D_05Feb2018",      "/SingleElectron/Run2016D-05Feb2018-v2/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016E_05Feb2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016E_05Feb2018",      "/SingleElectron/Run2016E-05Feb2018-v2/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016F_05Feb2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016F_05Feb2018",      "/SingleElectron/Run2016F-05Feb2018-v2/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016G_05Feb2018         = Sample.nanoAODfromDAS("SingleElectron_Run2016G_05Feb2018",      "/SingleElectron/Run2016G-05Feb2018-v2/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016H_05Feb2018_ver2    = Sample.nanoAODfromDAS("SingleElectron_Run2016H_05Feb2018_ver2", "/SingleElectron/Run2016H-05Feb2018_ver2-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016H_05Feb2018_ver3    = Sample.nanoAODfromDAS("SingleElectron_Run2016H_05Feb2018_ver3", "/SingleElectron/Run2016H-05Feb2018_ver3-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

SingleElectron_Run2016 = [\
    SingleElectron_Run2016B_05Feb2018_ver1,
    SingleElectron_Run2016B_05Feb2018_ver2,
    SingleElectron_Run2016C_05Feb2018,
    SingleElectron_Run2016D_05Feb2018,
    SingleElectron_Run2016E_05Feb2018,
    SingleElectron_Run2016F_05Feb2018,
    SingleElectron_Run2016G_05Feb2018,
    SingleElectron_Run2016H_05Feb2018_ver2,
    SingleElectron_Run2016H_05Feb2018_ver3,
    ]
    
## SingleMuon
SingleMuon_Run2016B_05Feb2018_ver1    = Sample.nanoAODfromDAS("SingleMuon_Run2016B_05Feb2018_ver1", "/SingleMuon/Run2016B-05Feb2018_ver1-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016B_05Feb2018_ver2    = Sample.nanoAODfromDAS("SingleMuon_Run2016B_05Feb2018_ver2", "/SingleMuon/Run2016B-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016C_05Feb2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016C_05Feb2018",      "/SingleMuon/Run2016C-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016D_05Feb2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016D_05Feb2018",      "/SingleMuon/Run2016D-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016E_05Feb2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016E_05Feb2018",      "/SingleMuon/Run2016E-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016F_05Feb2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016F_05Feb2018",      "/SingleMuon/Run2016F-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016G_05Feb2018         = Sample.nanoAODfromDAS("SingleMuon_Run2016G_05Feb2018",      "/SingleMuon/Run2016G-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016H_05Feb2018_ver2    = Sample.nanoAODfromDAS("SingleMuon_Run2016H_05Feb2018_ver2", "/SingleMuon/Run2016H-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016H_05Feb2018_ver3    = Sample.nanoAODfromDAS("SingleMuon_Run2016H_05Feb2018_ver3", "/SingleMuon/Run2016H-05Feb2018_ver3-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

SingleMuon_Run2016 = [\
    SingleMuon_Run2016B_05Feb2018_ver1,
    SingleMuon_Run2016B_05Feb2018_ver2,
    SingleMuon_Run2016C_05Feb2018,
    SingleMuon_Run2016D_05Feb2018,
    SingleMuon_Run2016E_05Feb2018,
    SingleMuon_Run2016F_05Feb2018,
    SingleMuon_Run2016G_05Feb2018,
    SingleMuon_Run2016H_05Feb2018_ver2,
    SingleMuon_Run2016H_05Feb2018_ver3,
    ]

## MET
MET_Run2016B_05Feb2018_ver1    = Sample.nanoAODfromDAS("MET_Run2016B_05Feb2018_ver1", "/MET/Run2016B-05Feb2018_ver1-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016B_05Feb2018_ver2    = Sample.nanoAODfromDAS("MET_Run2016B_05Feb2018_ver2", "/MET/Run2016B-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016C_05Feb2018         = Sample.nanoAODfromDAS("MET_Run2016C_05Feb2018",      "/MET/Run2016C-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016D_05Feb2018         = Sample.nanoAODfromDAS("MET_Run2016D_05Feb2018",      "/MET/Run2016D-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016E_05Feb2018         = Sample.nanoAODfromDAS("MET_Run2016E_05Feb2018",      "/MET/Run2016E-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016F_05Feb2018         = Sample.nanoAODfromDAS("MET_Run2016F_05Feb2018",      "/MET/Run2016F-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016G_05Feb2018         = Sample.nanoAODfromDAS("MET_Run2016G_05Feb2018",      "/MET/Run2016G-05Feb2018-v1/NANOAOD",      dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016H_05Feb2018_ver2    = Sample.nanoAODfromDAS("MET_Run2016H_05Feb2018_ver2", "/MET/Run2016H-05Feb2018_ver2-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MET_Run2016H_05Feb2018_ver3    = Sample.nanoAODfromDAS("MET_Run2016H_05Feb2018_ver3", "/MET/Run2016H-05Feb2018_ver3-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

MET_Run2016 = [\
    MET_Run2016B_05Feb2018_ver1,
    MET_Run2016B_05Feb2018_ver2,
    MET_Run2016C_05Feb2018,
    MET_Run2016D_05Feb2018,
    MET_Run2016E_05Feb2018,
    MET_Run2016F_05Feb2018,
    MET_Run2016G_05Feb2018,
    MET_Run2016H_05Feb2018_ver2,
    MET_Run2016H_05Feb2018_ver3,
    ]
    
allSamples = DoubleMuon_Run2016 + MuonEG_Run2016 + DoubleEG_Run2016 + SingleElectron_Run2016 + SingleMuon_Run2016 + MET_Run2016

for s in allSamples:
    s.json   = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt")
    s.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )

