'''
dasgoclient -query="dataset=/SingleMuon/Run2017*31Mar2018*/MINIAOD"
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
dbFile = dbDir+"Run2017_31Mar2018.sql"
    
logger.info("Using db file: %s", dbFile)

## DoubleMuon
DoubleMuon_Run2017B_31Mar2018   = FWLiteSample.fromDAS("DoubleMuon_Run2017B_31Mar2018", "/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017C_31Mar2018   = FWLiteSample.fromDAS("DoubleMuon_Run2017C_31Mar2018", "/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017D_31Mar2018   = FWLiteSample.fromDAS("DoubleMuon_Run2017D_31Mar2018", "/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017E_31Mar2018   = FWLiteSample.fromDAS("DoubleMuon_Run2017E_31Mar2018", "/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017F_31Mar2018   = FWLiteSample.fromDAS("DoubleMuon_Run2017F_31Mar2018", "/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleMuon = [
    DoubleMuon_Run2017B_31Mar2018,
    DoubleMuon_Run2017C_31Mar2018,
    DoubleMuon_Run2017D_31Mar2018,
    DoubleMuon_Run2017E_31Mar2018,
    DoubleMuon_Run2017F_31Mar2018,
]

DoubleEG_Run2017B_31Mar2018   = FWLiteSample.fromDAS("DoubleEG_Run2017B_31Mar2018", "/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017C_31Mar2018   = FWLiteSample.fromDAS("DoubleEG_Run2017C_31Mar2018", "/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017D_31Mar2018   = FWLiteSample.fromDAS("DoubleEG_Run2017D_31Mar2018", "/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017E_31Mar2018   = FWLiteSample.fromDAS("DoubleEG_Run2017E_31Mar2018", "/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017F_31Mar2018   = FWLiteSample.fromDAS("DoubleEG_Run2017F_31Mar2018", "/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleEG = [
    DoubleEG_Run2017B_31Mar2018,
    DoubleEG_Run2017C_31Mar2018,
    DoubleEG_Run2017D_31Mar2018,
    DoubleEG_Run2017E_31Mar2018,
    DoubleEG_Run2017F_31Mar2018,
]

MuonEG_Run2017B_31Mar2018   = FWLiteSample.fromDAS("MuonEG_Run2017B_31Mar2018", "/MuonEG/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2017C_31Mar2018   = FWLiteSample.fromDAS("MuonEG_Run2017C_31Mar2018", "/MuonEG/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2017D_31Mar2018   = FWLiteSample.fromDAS("MuonEG_Run2017D_31Mar2018", "/MuonEG/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2017E_31Mar2018   = FWLiteSample.fromDAS("MuonEG_Run2017E_31Mar2018", "/MuonEG/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2017F_31Mar2018   = FWLiteSample.fromDAS("MuonEG_Run2017F_31Mar2018", "/MuonEG/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MuonEG = [
    MuonEG_Run2017B_31Mar2018,
    MuonEG_Run2017C_31Mar2018,
    MuonEG_Run2017D_31Mar2018,
    MuonEG_Run2017E_31Mar2018,
    MuonEG_Run2017F_31Mar2018,
]

SingleMuon_Run2017B_31Mar2018   = FWLiteSample.fromDAS("SingleMuon_Run2017B_31Mar2018", "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017C_31Mar2018   = FWLiteSample.fromDAS("SingleMuon_Run2017C_31Mar2018", "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017D_31Mar2018   = FWLiteSample.fromDAS("SingleMuon_Run2017D_31Mar2018", "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017E_31Mar2018   = FWLiteSample.fromDAS("SingleMuon_Run2017E_31Mar2018", "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017F_31Mar2018   = FWLiteSample.fromDAS("SingleMuon_Run2017F_31Mar2018", "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleMuon = [
    SingleMuon_Run2017B_31Mar2018,
    SingleMuon_Run2017C_31Mar2018,
    SingleMuon_Run2017D_31Mar2018,
    SingleMuon_Run2017E_31Mar2018,
    SingleMuon_Run2017F_31Mar2018,
]

SingleElectron_Run2017B_31Mar2018   = FWLiteSample.fromDAS("SingleElectron_Run2017B_31Mar2018", "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2017C_31Mar2018   = FWLiteSample.fromDAS("SingleElectron_Run2017C_31Mar2018", "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2017D_31Mar2018   = FWLiteSample.fromDAS("SingleElectron_Run2017D_31Mar2018", "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2017E_31Mar2018   = FWLiteSample.fromDAS("SingleElectron_Run2017E_31Mar2018", "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2017F_31Mar2018   = FWLiteSample.fromDAS("SingleElectron_Run2017F_31Mar2018", "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleElectron = [
    SingleElectron_Run2017B_31Mar2018,
    SingleElectron_Run2017C_31Mar2018,
    SingleElectron_Run2017D_31Mar2018,
    SingleElectron_Run2017E_31Mar2018,
    SingleElectron_Run2017F_31Mar2018,
]

MET_Run2017B_31Mar2018   = FWLiteSample.fromDAS("MET_Run2017B_31Mar2018", "/MET/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017C_31Mar2018   = FWLiteSample.fromDAS("MET_Run2017C_31Mar2018", "/MET/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017D_31Mar2018   = FWLiteSample.fromDAS("MET_Run2017D_31Mar2018", "/MET/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017E_31Mar2018   = FWLiteSample.fromDAS("MET_Run2017E_31Mar2018", "/MET/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017F_31Mar2018   = FWLiteSample.fromDAS("MET_Run2017F_31Mar2018", "/MET/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [
    MET_Run2017B_31Mar2018,
    MET_Run2017C_31Mar2018,
    MET_Run2017D_31Mar2018,
    MET_Run2017E_31Mar2018,
    MET_Run2017F_31Mar2018,
]

JetHT_Run2017B_31Mar2018   = FWLiteSample.fromDAS("JetHT_Run2017B_31Mar2018", "/JetHT/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017C_31Mar2018   = FWLiteSample.fromDAS("JetHT_Run2017C_31Mar2018", "/JetHT/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017D_31Mar2018   = FWLiteSample.fromDAS("JetHT_Run2017D_31Mar2018", "/JetHT/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017E_31Mar2018   = FWLiteSample.fromDAS("JetHT_Run2017E_31Mar2018", "/JetHT/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017F_31Mar2018   = FWLiteSample.fromDAS("JetHT_Run2017F_31Mar2018", "/JetHT/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

JetHT = [
    JetHT_Run2017B_31Mar2018,
    JetHT_Run2017C_31Mar2018,
    JetHT_Run2017D_31Mar2018,
    JetHT_Run2017E_31Mar2018,
    JetHT_Run2017F_31Mar2018,
]

HTMHT_Run2017B_31Mar2018   = FWLiteSample.fromDAS("HTMHT_Run2017B_31Mar2018", "/HTMHT/Run2017B-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2017C_31Mar2018   = FWLiteSample.fromDAS("HTMHT_Run2017C_31Mar2018", "/HTMHT/Run2017C-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2017D_31Mar2018   = FWLiteSample.fromDAS("HTMHT_Run2017D_31Mar2018", "/HTMHT/Run2017D-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2017E_31Mar2018   = FWLiteSample.fromDAS("HTMHT_Run2017E_31Mar2018", "/HTMHT/Run2017E-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2017F_31Mar2018   = FWLiteSample.fromDAS("HTMHT_Run2017F_31Mar2018", "/HTMHT/Run2017F-31Mar2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

HTMHT = [
    HTMHT_Run2017B_31Mar2018,
    HTMHT_Run2017C_31Mar2018,
    HTMHT_Run2017D_31Mar2018,
    HTMHT_Run2017E_31Mar2018,
    HTMHT_Run2017F_31Mar2018,
]


## sum up
allSamples = DoubleMuon + DoubleEG + MuonEG + SingleMuon + SingleElectron + MET + HTMHT + JetHT

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
