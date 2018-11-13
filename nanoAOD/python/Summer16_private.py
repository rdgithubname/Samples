import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
if __name__=='__main__':
    import Samples.Tools.logger as logger
    logger = logger.get_logger('DEBUG', logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger('DEBUG', logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+'DB_Summer16_private.sql'

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_MLM_FS_S16_80X_priv  = Sample.nanoAODfromDAS('DYJetsToLL_M50_MLM_FS_S16_80X_priv', '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER', dbFile=dbFile, redirector=redirector, instance='phys03', xSection=2008.*3)
DYJetsToLL_M50_MLM_S16_80X_priv     = Sample.nanoAODfromDAS('DYJetsToLL_M50_MLM_S16_80X_priv', '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2_METSig_v1-95163dc1655e9579f2e671fa6cceb399/USER', dbFile=dbFile, redirector=redirector, instance='phys03', xSection=2008.*3)

DY = [
    DYJetsToLL_M50_MLM_FS_S16_80X_priv,
    DYJetsToLL_M50_MLM_S16_80X_priv,
    ]

TTJets_MLM_FS_S16_80X_priv  = Sample.nanoAODfromDAS('TTJets_MLM_FS_S16_80X_priv', '/TTJets_13TeV-madgraphMLM/dspitzba-crab_RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER', dbFile=dbFile, redirector=redirector, instance='phys03', xSection=831.76)
TTJets_MLM_S16_80X_priv     = Sample.nanoAODfromDAS('TTJets_MLM_S16_80X_priv', '/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER', dbFile=dbFile, redirector=redirector, instance='phys03', xSection=831.76)

top = [
    TTJets_MLM_FS_S16_80X_priv,
    TTJets_MLM_S16_80X_priv,
    ]

## Signals
#T2tt_mStop_850_mLSP_100 = Sample.nanoAODfromDAS("T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1)
#T2tt_mStop_650_mLSP_350 = Sample.nanoAODfromDAS("T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1)
#T2tt_mStop_500_mLSP_325 = Sample.nanoAODfromDAS("T2tt_mStop_500_mLSP_325", "/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1)
#T2tt_mStop_325_mLSP_150 = Sample.nanoAODfromDAS("T2tt_mStop_325_mLSP_150", "/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1)

signals = [
#    T2tt_mStop_850_mLSP_100,
#    T2tt_mStop_650_mLSP_350,
#    T2tt_mStop_500_mLSP_325,
#    T2tt_mStop_325_mLSP_150,
    ]

other = [
    ]

allSamples = DY + other + signals + top

for s in allSamples:
    s.isData = False

