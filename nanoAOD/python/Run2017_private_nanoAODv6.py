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
dbFile = dbDir+'/DB_Run2017_private_nanoAODv6.sql'

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017B_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017C_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017D_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017E_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleMuon_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("DoubleMuon_Run2017F_25Oct2019", "/DoubleMuon/schoef-TopNanoAODv6-1-2-4_DoubleMuon_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2017B_25Oct2019,
    DoubleMuon_Run2017C_25Oct2019,
    DoubleMuon_Run2017D_25Oct2019,
    DoubleMuon_Run2017E_25Oct2019,
    DoubleMuon_Run2017F_25Oct2019,
]

# MuonEG
MuonEG_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017B_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017C_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017D_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017E_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MuonEG_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("MuonEG_Run2017F_25Oct2019", "/MuonEG/schoef-TopNanoAODv6-1-2-4_MuonEG_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

MuonEG = [
    MuonEG_Run2017B_25Oct2019,
    MuonEG_Run2017C_25Oct2019,
    MuonEG_Run2017D_25Oct2019,
    MuonEG_Run2017E_25Oct2019,
    MuonEG_Run2017F_25Oct2019,
]

# DoubleEG
DoubleEG_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017B_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017C_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017D_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017E_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
DoubleEG_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("DoubleEG_Run2017F_25Oct2019", "/DoubleEG/schoef-TopNanoAODv6-1-2-4_DoubleEG_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

DoubleEG = [
    DoubleEG_Run2017B_25Oct2019,
    DoubleEG_Run2017C_25Oct2019,
    DoubleEG_Run2017D_25Oct2019,
    DoubleEG_Run2017E_25Oct2019,
    DoubleEG_Run2017F_25Oct2019,
]

# SingleMuon
SingleMuon_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017B_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017C_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017D_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017E_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleMuon_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("SingleMuon_Run2017F_25Oct2019", "/SingleMuon/schoef-TopNanoAODv6-1-2-4_SingleMuon_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleMuon = [
    SingleMuon_Run2017B_25Oct2019,
    SingleMuon_Run2017C_25Oct2019,
    SingleMuon_Run2017D_25Oct2019,
    SingleMuon_Run2017E_25Oct2019,
    SingleMuon_Run2017F_25Oct2019,
]

# SingleElectron
SingleElectron_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017B_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017C_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017D_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017E_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
SingleElectron_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("SingleElectron_Run2017F_25Oct2019", "/SingleElectron/schoef-TopNanoAODv6-1-2-4_SingleElectron_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

SingleElectron = [
    SingleElectron_Run2017B_25Oct2019,
    SingleElectron_Run2017C_25Oct2019,
    SingleElectron_Run2017D_25Oct2019,
    SingleElectron_Run2017E_25Oct2019,
    SingleElectron_Run2017F_25Oct2019,
]

# JetHT
JetHT_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017B_25Oct2019", "/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017C_25Oct2019", "/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017D_25Oct2019", "/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017E_25Oct2019", "/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
JetHT_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("JetHT_Run2017F_25Oct2019", "/JetHT/schoef-TopNanoAODv6-1-2-6_JetHT_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

JetHT = [
   JetHT_Run2017B_25Oct2019,
   JetHT_Run2017C_25Oct2019,
   JetHT_Run2017D_25Oct2019,
   JetHT_Run2017E_25Oct2019,
   JetHT_Run2017F_25Oct2019,
]

# MET
MET_Run2017B_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017B_25Oct2019", "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2017B-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2017C_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017C_25Oct2019", "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2017C-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2017D_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017D_25Oct2019", "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2017D-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2017E_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017E_25Oct2019", "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2017E-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)
MET_Run2017F_25Oct2019 = Sample.nanoAODfromDAS("MET_Run2017F_25Oct2019", "/MET/schoef-TopNanoAODv6-1-2-6_MET_Run2017F-9721c24ccc7f925c513e24ff74941177/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov)

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

