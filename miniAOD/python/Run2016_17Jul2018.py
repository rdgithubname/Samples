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
dbFile = dbDir+"DB_Run2016_17Jul2018.sql"

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("DoubleMuon_Run2016B_17Jul2018_ver1", "/DoubleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("DoubleMuon_Run2016B_17Jul2018_ver2", "/DoubleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("DoubleMuon_Run2016C_17Jul2018", "/DoubleMuon/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("DoubleMuon_Run2016D_17Jul2018", "/DoubleMuon/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("DoubleMuon_Run2016E_17Jul2018", "/DoubleMuon/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("DoubleMuon_Run2016F_17Jul2018", "/DoubleMuon/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("DoubleMuon_Run2016G_17Jul2018", "/DoubleMuon/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("DoubleMuon_Run2016H_17Jul2018", "/DoubleMuon/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

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
MuonEG_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("MuonEG_Run2016B_17Jul2018_ver1", "/MuonEG/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("MuonEG_Run2016B_17Jul2018_ver2", "/MuonEG/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("MuonEG_Run2016C_17Jul2018", "/MuonEG/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("MuonEG_Run2016D_17Jul2018", "/MuonEG/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("MuonEG_Run2016E_17Jul2018", "/MuonEG/Run2016E-17Jul2018-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("MuonEG_Run2016F_17Jul2018", "/MuonEG/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("MuonEG_Run2016G_17Jul2018", "/MuonEG/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MuonEG_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("MuonEG_Run2016H_17Jul2018", "/MuonEG/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MuonEG = [\
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
DoubleEG_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("DoubleEG_Run2016B_17Jul2018_ver1", "/DoubleEG/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("DoubleEG_Run2016B_17Jul2018_ver2", "/DoubleEG/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("DoubleEG_Run2016C_17Jul2018", "/DoubleEG/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("DoubleEG_Run2016D_17Jul2018", "/DoubleEG/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("DoubleEG_Run2016E_17Jul2018", "/DoubleEG/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("DoubleEG_Run2016F_17Jul2018", "/DoubleEG/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("DoubleEG_Run2016G_17Jul2018", "/DoubleEG/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("DoubleEG_Run2016H_17Jul2018", "/DoubleEG/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleEG = [\
    DoubleEG_Run2016B_17Jul2018_ver1,
    DoubleEG_Run2016B_17Jul2018_ver2,
    DoubleEG_Run2016C_17Jul2018,
    DoubleEG_Run2016D_17Jul2018,
    DoubleEG_Run2016E_17Jul2018,
    DoubleEG_Run2016F_17Jul2018,
    DoubleEG_Run2016G_17Jul2018,
    DoubleEG_Run2016H_17Jul2018,
    ]

# SingleElectron
SingleElectron_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("SingleElectron_Run2016B_17Jul2018_ver1", "/SingleElectron/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("SingleElectron_Run2016B_17Jul2018_ver2", "/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("SingleElectron_Run2016C_17Jul2018", "/SingleElectron/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("SingleElectron_Run2016D_17Jul2018", "/SingleElectron/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("SingleElectron_Run2016E_17Jul2018", "/SingleElectron/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("SingleElectron_Run2016F_17Jul2018", "/SingleElectron/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("SingleElectron_Run2016G_17Jul2018", "/SingleElectron/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleElectron_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("SingleElectron_Run2016H_17Jul2018", "/SingleElectron/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleElectron = [\
    SingleElectron_Run2016B_17Jul2018_ver1,
    SingleElectron_Run2016B_17Jul2018_ver2,
    SingleElectron_Run2016C_17Jul2018,
    SingleElectron_Run2016D_17Jul2018,
    SingleElectron_Run2016E_17Jul2018,
    SingleElectron_Run2016F_17Jul2018,
    SingleElectron_Run2016G_17Jul2018,
    SingleElectron_Run2016H_17Jul2018,
    ]

# SingleMuon
SingleMuon_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("SingleMuon_Run2016B_17Jul2018_ver1", "/SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("SingleMuon_Run2016B_17Jul2018_ver2", "/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("SingleMuon_Run2016C_17Jul2018", "/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("SingleMuon_Run2016D_17Jul2018", "/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("SingleMuon_Run2016E_17Jul2018", "/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("SingleMuon_Run2016F_17Jul2018", "/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("SingleMuon_Run2016G_17Jul2018", "/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("SingleMuon_Run2016H_17Jul2018", "/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleMuon = [\
    SingleMuon_Run2016B_17Jul2018_ver1,
    SingleMuon_Run2016B_17Jul2018_ver2,
    SingleMuon_Run2016C_17Jul2018,
    SingleMuon_Run2016D_17Jul2018,
    SingleMuon_Run2016E_17Jul2018,
    SingleMuon_Run2016F_17Jul2018,
    SingleMuon_Run2016G_17Jul2018,
    SingleMuon_Run2016H_17Jul2018,
    ]

# MET
MET_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("MET_Run2016B_17Jul2018_ver1", "/MET/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("MET_Run2016B_17Jul2018_ver2", "/MET/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("MET_Run2016C_17Jul2018", "/MET/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("MET_Run2016D_17Jul2018", "/MET/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("MET_Run2016E_17Jul2018", "/MET/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("MET_Run2016F_17Jul2018", "/MET/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("MET_Run2016G_17Jul2018", "/MET/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("MET_Run2016H_17Jul2018", "/MET/Run2016H-17Jul2018-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2016B_17Jul2018_ver1,
    MET_Run2016B_17Jul2018_ver2,
    MET_Run2016C_17Jul2018,
    MET_Run2016D_17Jul2018,
    MET_Run2016E_17Jul2018,
    MET_Run2016F_17Jul2018,
    MET_Run2016G_17Jul2018,
    MET_Run2016H_17Jul2018,
]

# JetHT
JetHT_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("JetHT_Run2016B_17Jul2018_ver1", "/JetHT/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("JetHT_Run2016B_17Jul2018_ver2", "/JetHT/Run2016B-17Jul2018_ver2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("JetHT_Run2016C_17Jul2018", "/JetHT/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("JetHT_Run2016D_17Jul2018", "/JetHT/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("JetHT_Run2016E_17Jul2018", "/JetHT/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("JetHT_Run2016F_17Jul2018", "/JetHT/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("JetHT_Run2016G_17Jul2018", "/JetHT/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("JetHT_Run2016H_17Jul2018", "/JetHT/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

JetHT = [\
    JetHT_Run2016B_17Jul2018_ver1,
    JetHT_Run2016B_17Jul2018_ver2,
    JetHT_Run2016C_17Jul2018,
    JetHT_Run2016D_17Jul2018,
    JetHT_Run2016E_17Jul2018,
    JetHT_Run2016F_17Jul2018,
    JetHT_Run2016G_17Jul2018,
    JetHT_Run2016H_17Jul2018,
]

# HTMHT
HTMHT_Run2016B_17Jul2018_ver1  =   FWLiteSample.fromDAS("HTMHT_Run2016B_17Jul2018_ver1", "/HTMHT/Run2016B-17Jul2018_ver1-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016B_17Jul2018_ver2  =   FWLiteSample.fromDAS("HTMHT_Run2016B_17Jul2018_ver2", "/HTMHT/Run2016B-17Jul2018_ver2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016C_17Jul2018       =   FWLiteSample.fromDAS("HTMHT_Run2016C_17Jul2018", "/HTMHT/Run2016C-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016D_17Jul2018       =   FWLiteSample.fromDAS("HTMHT_Run2016D_17Jul2018", "/HTMHT/Run2016D-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016E_17Jul2018       =   FWLiteSample.fromDAS("HTMHT_Run2016E_17Jul2018", "/HTMHT/Run2016E-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016F_17Jul2018       =   FWLiteSample.fromDAS("HTMHT_Run2016F_17Jul2018", "/HTMHT/Run2016F-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016G_17Jul2018       =   FWLiteSample.fromDAS("HTMHT_Run2016G_17Jul2018", "/HTMHT/Run2016G-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
HTMHT_Run2016H_17Jul2018       =   FWLiteSample.fromDAS("HTMHT_Run2016H_17Jul2018", "/HTMHT/Run2016H-17Jul2018-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

HTMHT = [\
    HTMHT_Run2016B_17Jul2018_ver1,
    HTMHT_Run2016B_17Jul2018_ver2,
    HTMHT_Run2016C_17Jul2018,
    HTMHT_Run2016D_17Jul2018,
    HTMHT_Run2016E_17Jul2018,
    HTMHT_Run2016F_17Jul2018,
    HTMHT_Run2016G_17Jul2018,
    HTMHT_Run2016H_17Jul2018,
]

## add up all samples
allSamples = DoubleMuon + MuonEG + DoubleEG + SingleElectron + SingleMuon + MET + JetHT + HTMHT

for sample in allSamples:
    sample.isData = True
