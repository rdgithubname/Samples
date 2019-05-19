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
dbFile = dbDir+"/DB_Run2017_31Mar2018.sql"

logger.info("Using db file: %s", dbFile)

# specify a local directory if you want to create (and afterwards automatically use) a local copy of the sample, otherwise use the grid.

## DoubleMuon
DoubleMuon_Run2017B_31Mar2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2017B_31Mar2018",   "/DoubleMuon/Run2017B-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017C_31Mar2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2017C_31Mar2018",   "/DoubleMuon/Run2017C-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017D_31Mar2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2017D_31Mar2018",   "/DoubleMuon/Run2017D-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017E_31Mar2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2017E_31Mar2018",   "/DoubleMuon/Run2017E-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2017F_31Mar2018  = Sample.nanoAODfromDAS("DoubleMuon_Run2017F_31Mar2018",   "/DoubleMuon/Run2017F-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

DoubleMuon_Run2017 = [\
    DoubleMuon_Run2017B_31Mar2018,
    DoubleMuon_Run2017C_31Mar2018,
    DoubleMuon_Run2017D_31Mar2018,
    DoubleMuon_Run2017E_31Mar2018,
    DoubleMuon_Run2017F_31Mar2018,
    ]

## MuonEG
MuonEG_Run2017B_31Mar2018  = Sample.nanoAODfromDAS("MuonEG_Run2017B_31Mar2018",   "/MuonEG/Run2017B-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2017C_31Mar2018  = Sample.nanoAODfromDAS("MuonEG_Run2017C_31Mar2018",   "/MuonEG/Run2017C-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2017D_31Mar2018  = Sample.nanoAODfromDAS("MuonEG_Run2017D_31Mar2018",   "/MuonEG/Run2017D-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2017E_31Mar2018  = Sample.nanoAODfromDAS("MuonEG_Run2017E_31Mar2018",   "/MuonEG/Run2017E-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2017F_31Mar2018  = Sample.nanoAODfromDAS("MuonEG_Run2017F_31Mar2018",   "/MuonEG/Run2017F-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

MuonEG_Run2017 = [\
    MuonEG_Run2017B_31Mar2018,
    MuonEG_Run2017C_31Mar2018,
    MuonEG_Run2017D_31Mar2018,
    MuonEG_Run2017E_31Mar2018,
    MuonEG_Run2017F_31Mar2018,
    ]

## DoubleEG
DoubleEG_Run2017B_31Mar2018  = Sample.nanoAODfromDAS("DoubleEG_Run2017B_31Mar2018",   "/DoubleEG/Run2017B-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2017C_31Mar2018  = Sample.nanoAODfromDAS("DoubleEG_Run2017C_31Mar2018",   "/DoubleEG/Run2017C-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2017D_31Mar2018  = Sample.nanoAODfromDAS("DoubleEG_Run2017D_31Mar2018",   "/DoubleEG/Run2017D-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2017E_31Mar2018  = Sample.nanoAODfromDAS("DoubleEG_Run2017E_31Mar2018",   "/DoubleEG/Run2017E-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2017F_31Mar2018  = Sample.nanoAODfromDAS("DoubleEG_Run2017F_31Mar2018",   "/DoubleEG/Run2017F-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

DoubleEG_Run2017 = [\
    DoubleEG_Run2017B_31Mar2018,
    DoubleEG_Run2017C_31Mar2018,
    DoubleEG_Run2017D_31Mar2018,
    DoubleEG_Run2017E_31Mar2018,
    DoubleEG_Run2017F_31Mar2018,
    ]
    
## SingleMuon
SingleMuon_Run2017B_31Mar2018  = Sample.nanoAODfromDAS("SingleMuon_Run2017B_31Mar2018",   "/SingleMuon/Run2017B-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2017C_31Mar2018  = Sample.nanoAODfromDAS("SingleMuon_Run2017C_31Mar2018",   "/SingleMuon/Run2017C-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2017D_31Mar2018  = Sample.nanoAODfromDAS("SingleMuon_Run2017D_31Mar2018",   "/SingleMuon/Run2017D-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2017E_31Mar2018  = Sample.nanoAODfromDAS("SingleMuon_Run2017E_31Mar2018",   "/SingleMuon/Run2017E-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2017F_31Mar2018  = Sample.nanoAODfromDAS("SingleMuon_Run2017F_31Mar2018",   "/SingleMuon/Run2017F-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

SingleMuon_Run2017 = [\
    SingleMuon_Run2017B_31Mar2018,
    SingleMuon_Run2017C_31Mar2018,
    SingleMuon_Run2017D_31Mar2018,
    SingleMuon_Run2017E_31Mar2018,
    SingleMuon_Run2017F_31Mar2018,
    ]
    
## SingleElectron
SingleElectron_Run2017B_31Mar2018  = Sample.nanoAODfromDAS("SingleElectron_Run2017B_31Mar2018",   "/SingleElectron/Run2017B-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2017C_31Mar2018  = Sample.nanoAODfromDAS("SingleElectron_Run2017C_31Mar2018",   "/SingleElectron/Run2017C-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2017D_31Mar2018  = Sample.nanoAODfromDAS("SingleElectron_Run2017D_31Mar2018",   "/SingleElectron/Run2017D-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2017E_31Mar2018  = Sample.nanoAODfromDAS("SingleElectron_Run2017E_31Mar2018",   "/SingleElectron/Run2017E-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2017F_31Mar2018  = Sample.nanoAODfromDAS("SingleElectron_Run2017F_31Mar2018",   "/SingleElectron/Run2017F-31Mar2018-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)

SingleElectron_Run2017 = [\
    SingleElectron_Run2017B_31Mar2018,
    SingleElectron_Run2017C_31Mar2018,
    SingleElectron_Run2017D_31Mar2018,
    SingleElectron_Run2017E_31Mar2018,
    SingleElectron_Run2017F_31Mar2018,
    ]
    

allSamples = DoubleMuon_Run2017 + MuonEG_Run2017 + DoubleEG_Run2017 + SingleMuon_Run2017 + SingleElectron_Run2017

for s in allSamples:
    s.json   = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt")
    s.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
