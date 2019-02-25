'''
miniAOD samples of Summer16 campaign, miniAODv2 (80X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*80X*/MINIAODSIM"
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
dbFile = dbDir+"Summer16_miniAODv2.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_MLM_FS_S16_80X       = FWLiteSample.fromDAS("DYJetsToLL_M50_MLM_FS_S16_80X", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_MLM_S16_80X          = FWLiteSample.fromDAS("DYJetsToLL_M50_MLM_S16_80X", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY = [
    DYJetsToLL_M50_MLM_FS_S16_80X,
    DYJetsToLL_M50_MLM_S16_80X,
]

## TTJets

TTJets_MLM_FS_S16_80X   = FWLiteSample.fromDAS("TTJets_MLM_FS_S16_80X", "/TTJets_13TeV-madgraphMLM/RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_MLM_S16_80X      = FWLiteSample.fromDAS("TTJets_MLM_S16_80X", "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTo2L2Nu_pow_S16_80X       = FWLiteSample.fromDAS("TTTo2L2Nu_pow_S16_80X", "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_pow_S16_80X   = FWLiteSample.fromDAS("ST_tW_antitop_pow_S16_80X", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_pow_S16_80X       = FWLiteSample.fromDAS("ST_tW_top_pow_S16_80X", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_schannel_amc_S16_80X     = FWLiteSample.fromDAS("ST_schannel_amc_S16_80X", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_amc_S16_80X     = FWLiteSample.fromDAS("ST_tchannel_amc_S16_80X", "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


top = [
    TTJets_MLM_FS_S16_80X,
    TTJets_MLM_S16_80X,
    TTTo2L2Nu_pow_S16_80X,
    ST_tW_antitop_pow_S16_80X,
    ST_tW_top_pow_S16_80X,
    ST_schannel_amc_S16_80X,
    ST_tchannel_amc_S16_80X,
]



WW_S16_80X      = FWLiteSample.fromDAS("WW_S16_80X", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WW_ext_S16_80X  = FWLiteSample.fromDAS("WW_ext_S16_80X", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_S16_80X      = FWLiteSample.fromDAS("WZ_S16_80X", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_ext_S16_80X  = FWLiteSample.fromDAS("WZ_ext_S16_80X", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ_S16_80X      = FWLiteSample.fromDAS("ZZ_S16_80X", "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ_ext_S16_80X  = FWLiteSample.fromDAS("ZZ_ext_S16_80X", "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WW_S16_80X,
    WW_ext_S16_80X,
    WZ_S16_80X,
    WZ_ext_S16_80X,
    ZZ_S16_80X,
    ZZ_ext_S16_80X,
]

allSamples = DY + top + multiboson

for sample in allSamples:
    sample.isData = False
