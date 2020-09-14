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
            from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2017_nanoAODv6.sql'

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017B_25Oct2019", "/DoubleMuon/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017C_25Oct2019", "/DoubleMuon/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017D_25Oct2019", "/DoubleMuon/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017E_25Oct2019", "/DoubleMuon/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017F_25Oct2019", "/DoubleMuon/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2017B_25Oct2019,
    DoubleMuon_Run2017C_25Oct2019,
    DoubleMuon_Run2017D_25Oct2019,
    DoubleMuon_Run2017E_25Oct2019,
    DoubleMuon_Run2017F_25Oct2019,
]

# MuonEG
MuonEG_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017B_25Oct2019", "/MuonEG/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017C_25Oct2019", "/MuonEG/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017D_25Oct2019", "/MuonEG/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017E_25Oct2019", "/MuonEG/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017F_25Oct2019", "/MuonEG/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MuonEG = [
    MuonEG_Run2017B_25Oct2019,
    MuonEG_Run2017C_25Oct2019,
    MuonEG_Run2017D_25Oct2019,
    MuonEG_Run2017E_25Oct2019,
    MuonEG_Run2017F_25Oct2019,
]

# DoubleEG
DoubleEG_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017B_25Oct2019", "/DoubleEG/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017C_25Oct2019", "/DoubleEG/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017D_25Oct2019", "/DoubleEG/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017E_25Oct2019", "/DoubleEG/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017F_25Oct2019", "/DoubleEG/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleEG = [
    DoubleEG_Run2017B_25Oct2019,
    DoubleEG_Run2017C_25Oct2019,
    DoubleEG_Run2017D_25Oct2019,
    DoubleEG_Run2017E_25Oct2019,
    DoubleEG_Run2017F_25Oct2019,
]

# SingleMuon
SingleMuon_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017B_25Oct2019", "/SingleMuon/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017C_25Oct2019", "/SingleMuon/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017D_25Oct2019", "/SingleMuon/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017E_25Oct2019", "/SingleMuon/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017F_25Oct2019", "/SingleMuon/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleMuon = [
    SingleMuon_Run2017B_25Oct2019,
    SingleMuon_Run2017C_25Oct2019,
    SingleMuon_Run2017D_25Oct2019,
    SingleMuon_Run2017E_25Oct2019,
    SingleMuon_Run2017F_25Oct2019,
]

# SingleElectron
SingleElectron_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017B_25Oct2019", "/SingleElectron/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017C_25Oct2019", "/SingleElectron/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017D_25Oct2019", "/SingleElectron/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017E_25Oct2019", "/SingleElectron/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017F_25Oct2019", "/SingleElectron/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleElectron = [
    SingleElectron_Run2017B_25Oct2019,
    SingleElectron_Run2017C_25Oct2019,
    SingleElectron_Run2017D_25Oct2019,
    SingleElectron_Run2017E_25Oct2019,
    SingleElectron_Run2017F_25Oct2019,
]

# JetHT
JetHT_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017B_25Oct2019", "/JetHT/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017C_25Oct2019", "/JetHT/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017D_25Oct2019", "/JetHT/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017E_25Oct2019", "/JetHT/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017F_25Oct2019", "/JetHT/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

JetHT = [
    JetHT_Run2017B_25Oct2019,
    JetHT_Run2017C_25Oct2019,
    JetHT_Run2017D_25Oct2019,
    JetHT_Run2017E_25Oct2019,
    JetHT_Run2017F_25Oct2019,
]

# MET
MET_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017B_25Oct2019", "/MET/Run2017B-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017C_25Oct2019", "/MET/Run2017C-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017D_25Oct2019", "/MET/Run2017D-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017E_25Oct2019", "/MET/Run2017E-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017F_25Oct2019", "/MET/Run2017F-Nano25Oct2019-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MET = [
    MET_Run2017B_25Oct2019,
    MET_Run2017C_25Oct2019,
    MET_Run2017D_25Oct2019,
    MET_Run2017E_25Oct2019,
    MET_Run2017F_25Oct2019,
]

allSamples = DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron + JetHT + MET

for s in allSamples:
    s.json   = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt")
    s.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )

