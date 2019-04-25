'''
miniAOD samples of Summer16 campaign, miniAODv3 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*94X*/MINIAODSIM"
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
dbFile = dbDir+"Summer16_miniAODv3.sql"

logger.info("Using db file: %s", dbFile) 

## DY
DYJetsToLL_M10to50_NLO_S16_94X         = FWLiteSample.fromDAS("DYJetsToLL_M10to50_NLO_S16_94X", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_NLO_S16_94X_ext1    = FWLiteSample.fromDAS("DYJetsToLL_M10to50_NLO_S16_94X_ext1", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M5to50_HT70to100_LO_S16_94X         = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT70to100_LO_S16_94X", "/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT100to200_LO_S16_94X        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT100to200_LO_S16_94X", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT100to200_LO_S16_94X_ext1   = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT100to200_LO_S16_94X_ext1", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT200to400_LO_S16_94X        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT200to400_LO_S16_94X", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT200to400_LO_S16_94X_ext1   = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT200to400_LO_S16_94X_ext1", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT400to600_LO_S16_94X        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT400to600_LO_S16_94X", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT400to600_LO_S16_94X_ext1   = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT400to600_LO_S16_94X_ext1", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT600toInf_LO_S16_94X        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT600toInf_LO_S16_94X", "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_NLO_S16_94X_ext2        = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO_S16_94X_ext2", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M50_LO_FS_S16_94X       = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_FS_S16_94X", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_S16_94X_ext1         = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_S16_94X_ext1", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_S16_94X_ext2         = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_S16_94X_ext2", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_HT70to100_LO_S16_94X        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100_LO_S16_94X", "/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO_S16_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO_S16_94X_ext1", "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_S16_94X       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_S16_94X", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_S16_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_S16_94X_ext1", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_S16_94X       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_S16_94X", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_S16_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_S16_94X_ext1", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800_LO_S16_94X       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800_LO_S16_94X", "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200_LO_S16_94X      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200_LO_S16_94X", "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500_LO_S16_94X     = FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500_LO_S16_94X", "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT2500toInf_LO_S16_94X      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf_LO_S16_94X", "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY = [
    #DYJetsToLL_M50_LO_FS_S16_94X,
    DYJetsToLL_M50_LO_S16_94X_ext1,
    DYJetsToLL_M50_LO_S16_94X_ext2,
    DYJetsToLL_M50_NLO_S16_94X_ext2,
    DYJetsToLL_M10to50_NLO_S16_94X,
    DYJetsToLL_M10to50_NLO_S16_94X_ext1,
]

DY_HT = [
    DYJetsToLL_M50_HT70to100_LO_S16_94X,
    DYJetsToLL_M50_HT100to200_LO_S16_94X_ext1,
    DYJetsToLL_M50_HT200to400_LO_S16_94X,
    DYJetsToLL_M50_HT200to400_LO_S16_94X_ext1,
    DYJetsToLL_M50_HT400to600_LO_S16_94X,
    DYJetsToLL_M50_HT400to600_LO_S16_94X_ext1,
    DYJetsToLL_M50_HT600to800_LO_S16_94X,
    DYJetsToLL_M50_HT800to1200_LO_S16_94X,
    DYJetsToLL_M50_HT1200to2500_LO_S16_94X,
    DYJetsToLL_M50_HT2500toInf_LO_S16_94X,

    DYJetsToLL_M5to50_HT70to100_LO_S16_94X,
    DYJetsToLL_M5to50_HT100to200_LO_S16_94X,
    DYJetsToLL_M5to50_HT100to200_LO_S16_94X_ext1,
    DYJetsToLL_M5to50_HT200to400_LO_S16_94X,
    DYJetsToLL_M5to50_HT200to400_LO_S16_94X_ext1,
    DYJetsToLL_M5to50_HT400to600_LO_S16_94X,
    DYJetsToLL_M5to50_HT400to600_LO_S16_94X_ext1,
    DYJetsToLL_M5to50_HT600toInf_LO_S16_94X,
]

# single top
ST_schannel_4f_NLO_S16_94X                 = FWLiteSample.fromDAS("ST_schannel_4f_NLO_S16_94X", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_4f_pow_S16_94X         = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow_S16_94X", "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_pow_S16_94X             = FWLiteSample.fromDAS("ST_tchannel_top_4f_pow_S16_94X", "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_4f = [
    ST_schannel_4f_NLO_S16_94X,
    ST_tchannel_antitop_4f_pow_S16_94X,
    ST_tchannel_top_4f_pow_S16_94X,
]

ST_tW_antitop_NoFullyHad_5f_pow_S16_94X    = FWLiteSample.fromDAS("ST_tW_antitop_NoFullyHad_5f_pow_S16_94X", "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_5f_pow_S16_94X_ext1          = FWLiteSample.fromDAS("ST_tW_antitop_5f_pow_S16_94X_ext1", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_5f_pow_S16_94X               = FWLiteSample.fromDAS("ST_tW_antitop_5f_pow_S16_94X", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow_S16_94X        = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow_S16_94X", "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_5f_pow_S16_94X_ext1              = FWLiteSample.fromDAS("ST_tW_top_5f_pow_S16_94X_ext1", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_5f_pow_S16_94X                   = FWLiteSample.fromDAS("ST_tW_top_5f_pow_S16_94X", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tWll_5f_LO_S16_94X                      = FWLiteSample.fromDAS("ST_tWll_5f_LO_S16_94X", "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tWnunu_5f_LO_S16_94X                    = FWLiteSample.fromDAS("ST_tWnunu_5f_LO_S16_94X", "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_5f = [
    ST_tW_antitop_NoFullyHad_5f_pow_S16_94X,
    #ST_tW_antitop_5f_pow_S16_94X_ext1,
    #ST_tW_antitop_5f_pow_S16_94X,
    ST_tW_top_NoFullyHad_5f_pow_S16_94X,
    #ST_tW_top_5f_pow_S16_94X_ext1,
    #ST_tW_top_5f_pow_S16_94X,
    ST_tWll_5f_LO_S16_94X,
    ST_tWnunu_5f_LO_S16_94X,
]

# TTJets
#TTJets_LO_FS_S16_94X   = FWLiteSample.fromDAS("TTJets_LO_FS_S16_94X", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#TTJets_LO_S16_94X      = FWLiteSample.fromDAS("TTJets_LO_S16_94X", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTo2L2Nu_noSC_pow_S16_94X  = FWLiteSample.fromDAS("TTTo2L2Nu_noSC_pow_S16_94X", "/TTTo2L2Nu_noSC_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow_S16_94X       = FWLiteSample.fromDAS("TTTo2L2Nu_pow_S16_94X", "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemilepton_pow_S16_94X  = FWLiteSample.fromDAS("TTToSemilepton_pow_S16_94X", "/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TT_pow_S16_94X              = FWLiteSample.fromDAS("TT_pow_S16_94X", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets = [
    TTTo2L2Nu_noSC_pow_S16_94X,
    TTTo2L2Nu_pow_S16_94X,
    TTToSemilepton_pow_S16_94X,
    #TT_pow_S16_94X,
]

# t(t)g(g)
THQ_LO_S16_94X                  = FWLiteSample.fromDAS("THQ_LO_S16_94X", "/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THW_LO_S16_94X                  = FWLiteSample.fromDAS("THW_LO_S16_94X", "/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
tZq_ll_NLO_S16_94X              = FWLiteSample.fromDAS("tZq_ll_NLO_S16_94X", "/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTT_NLO_S16_94X                = FWLiteSample.fromDAS("TTTT_NLO_S16_94X", "/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWW_NLO_S16_94X                = FWLiteSample.fromDAS("TTWW_NLO_S16_94X", "/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWZ_NLO_S16_94X                = FWLiteSample.fromDAS("TTWZ_NLO_S16_94X", "/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZZ_NLO_S16_94X                = FWLiteSample.fromDAS("TTZZ_NLO_S16_94X", "/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTWJetsToLNu_NLO_S16_94X        = FWLiteSample.fromDAS("TTWJetsToLNu_NLO_S16_94X", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToQQ_NLO_S16_94X         = FWLiteSample.fromDAS("TTWJetsToQQ_NLO_S16_94X", "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLLNuNu_NLO_S16_94X_ext2    = FWLiteSample.fromDAS("TTZToLLNuNu_NLO_S16_94X_ext2", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLLNuNu_NLO_S16_94X_ext3    = FWLiteSample.fromDAS("TTZToLLNuNu_NLO_S16_94X_ext3", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLL_M1to10_LO_S16_94X       = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO_S16_94X", "/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToQQ_NLO_S16_94X             = FWLiteSample.fromDAS("TTZToQQ_NLO_S16_94X", "/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttZJets_LO_S16_94X              = FWLiteSample.fromDAS("ttZJets_LO_S16_94X", "/ttZJets_13TeV_madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHToNonbb_pow_S16_94X          = FWLiteSample.fromDAS("ttHToNonbb_pow_S16_94X", "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_pow_S16_94X             = FWLiteSample.fromDAS("ttHTobb_pow_S16_94X", "/ttHTobb_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TGG_S16_94X                     = FWLiteSample.fromDAS("TGG_S16_94X", "/TGGJets_leptonDecays_13TeV_MadGraph_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TGJets_lep_NLO_S16_94X          = FWLiteSample.fromDAS("TGJets_lep_NLO_PS_S16_94X", "/TGJets_leptonDecays_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGJets_NLO_S16_94X             = FWLiteSample.fromDAS("TTGJets_NLO_S16_94X", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGJets_NLO_S16_94X_ext1        = FWLiteSample.fromDAS("TTGJets_NLO_S16_94X_ext1", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_S16_94X           = FWLiteSample.fromDAS("TTGamma_dilep_LO_S16_94X", "/TTGamma_Dilept_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilepFromT_LO_S16_94X    = FWLiteSample.fromDAS("TTGamma_semilepFromT_LO_S16_94X", "/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilepFromTbar_LO_S16_94X = FWLiteSample.fromDAS("TTGamma_semilepFromTbar_LO_S16_94X", "/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_had_LO_S16_94X             = FWLiteSample.fromDAS("TTGamma_had_LO_S16_94X", "/TTGamma_Hadronic_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTX = [
    THQ_LO_S16_94X,
    THW_LO_S16_94X,
    tZq_ll_NLO_S16_94X,
    TTTT_NLO_S16_94X,
    TTWZ_NLO_S16_94X,
    TTWW_NLO_S16_94X,
    TTZZ_NLO_S16_94X,
    TTWJetsToLNu_NLO_S16_94X,
    TTWJetsToQQ_NLO_S16_94X,
    TTZToLL_M1to10_LO_S16_94X,
    TTZToLLNuNu_NLO_S16_94X_ext2,
    TTZToLLNuNu_NLO_S16_94X_ext3,
    TTZToQQ_NLO_S16_94X,
    ttZJets_LO_S16_94X,
    ttHToNonbb_pow_S16_94X,
    ttHTobb_pow_S16_94X,
    TGG_S16_94X,
    TGJets_lep_NLO_S16_94X,
    TTGJets_NLO_S16_94X,
    TTGJets_NLO_S16_94X_ext1,
    TTGamma_dilep_LO_S16_94X,
    TTGamma_semilepFromT_LO_S16_94X,
    TTGamma_semilepFromTbar_LO_S16_94X,
    TTGamma_had_LO_S16_94X,
]



## W+jets
WJetsToLNu_LO_S16_94X                  = FWLiteSample.fromDAS("WJetsToLNu_LO_S16_94X", "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_LO_S16_94X_ext2             = FWLiteSample.fromDAS("WJetsToLNu_LO_S16_94X_ext2", "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJets = [
    WJetsToLNu_LO_S16_94X,
    WJetsToLNu_LO_S16_94X_ext2,
]

WJetsToLNu_HT70To100_LO_S16_94X            = FWLiteSample.fromDAS("WJetsToLNu_HT70To100_LO_S16_94X", "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT100To200_LO_S16_94X           = FWLiteSample.fromDAS("WJetsToLNu_HT100To200_LO_S16_94X", "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400_LO_S16_94X           = FWLiteSample.fromDAS("WJetsToLNu_HT200To400_LO_S16_94X", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400_LO_S16_94X_ext1      = FWLiteSample.fromDAS("WJetsToLNu_HT200To400_LO_S16_94X_ext1", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400_LO_S16_94X_ext2      = FWLiteSample.fromDAS("WJetsToLNu_HT200To400_LO_S16_94X_ext2", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400To600_LO_S16_94X           = FWLiteSample.fromDAS("WJetsToLNu_HT400To600_LO_S16_94X", "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400To600_LO_S16_94X_ext1      = FWLiteSample.fromDAS("WJetsToLNu_HT400To600_LO_S16_94X_ext1", "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600To800_LO_S16_94X           = FWLiteSample.fromDAS("WJetsToLNu_HT600To800_LO_S16_94X", "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600To800_LO_S16_94X_ext1      = FWLiteSample.fromDAS("WJetsToLNu_HT600To800_LO_S16_94X_ext1", "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800To1200_LO_S16_94X          = FWLiteSample.fromDAS("WJetsToLNu_HT800To1200_LO_S16_94X", "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800To1200_LO_S16_94X_ext1     = FWLiteSample.fromDAS("WJetsToLNu_HT800To1200_LO_S16_94X_ext1", "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200To2500_LO_S16_94X         = FWLiteSample.fromDAS("WJetsToLNu_HT1200To2500_LO_S16_94X", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200To2500_LO_S16_94X_ext1    = FWLiteSample.fromDAS("WJetsToLNu_HT1200To2500_LO_S16_94X_ext1", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500ToInf_LO_S16_94X          = FWLiteSample.fromDAS("WJetsToLNu_HT2500ToInf_LO_S16_94X", "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500ToInf_LO_S16_94X_ext1     = FWLiteSample.fromDAS("WJetsToLNu_HT2500ToInf_LO_S16_94X_ext1", "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_HT = [
    WJetsToLNu_HT70To100_LO_S16_94X,
    WJetsToLNu_HT100To200_LO_S16_94X,
    WJetsToLNu_HT200To400_LO_S16_94X,
    WJetsToLNu_HT200To400_LO_S16_94X_ext1,
    WJetsToLNu_HT200To400_LO_S16_94X_ext2,
    WJetsToLNu_HT400To600_LO_S16_94X,
    WJetsToLNu_HT400To600_LO_S16_94X_ext1,
    WJetsToLNu_HT600To800_LO_S16_94X,
    WJetsToLNu_HT600To800_LO_S16_94X_ext1,
    WJetsToLNu_HT800To1200_LO_S16_94X,
    WJetsToLNu_HT800To1200_LO_S16_94X_ext1,
    WJetsToLNu_HT1200To2500_LO_S16_94X,
    WJetsToLNu_HT1200To2500_LO_S16_94X_ext1,
    WJetsToLNu_HT2500ToInf_LO_S16_94X,
    WJetsToLNu_HT2500ToInf_LO_S16_94X_ext1,
]

## diboson samples

VVTo2L2Nu_NLO_S16_94X       = FWLiteSample.fromDAS("VVTo2L2Nu_NLO_S16_94X", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
VVTo2L2Nu_NLO_S16_94X_ext1  = FWLiteSample.fromDAS("VVTo2L2Nu_NLO_S16_94X_ext1", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo1L1Nu2Q_NLO_S16_94X     = FWLiteSample.fromDAS("WWTo1L1Nu2Q_NLO_S16_94X", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWToLNuQQ_S16_94X           = FWLiteSample.fromDAS("WWToLNuQQ_S16_94X", "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu_S16_94X           = FWLiteSample.fromDAS("WWTo2L2Nu_S16_94X", "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L1Nu2Q_NLO_S16_94X     = FWLiteSample.fromDAS("WZTo1L1Nu2Q_NLO_S16_94X", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L3Nu_NLO_S16_94X       = FWLiteSample.fromDAS("WZTo1L3Nu_NLO_S16_94X", "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2L2Q_NLO_S16_94X        = FWLiteSample.fromDAS("WZTo2L2Q_NLO_S16_94X", "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_NLO_S16_94X        = FWLiteSample.fromDAS("WZTo3LNu_NLO_S16_94X", "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_pow_S16_94X_ext1   = FWLiteSample.fromDAS("WZTo3LNu_pow_S16_94X_ext1", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Nu_pow_S16_94X       = FWLiteSample.fromDAS("ZZTo2L2Nu_pow_S16_94X", "/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Q_pow_S16_94X        = FWLiteSample.fromDAS("ZZTo2L2Q_pow_S16_94X", "/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2Q2Nu_NLO_S16_94X       = FWLiteSample.fromDAS("ZZTo2Q2Nu_NLO_S16_94X", "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4L_pow_S16_94X          = FWLiteSample.fromDAS("ZZTo4L_pow_S16_94X", "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WW_S16_94X                  = FWLiteSample.fromDAS("WW_S16_94X", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WW_S16_94X_ext1             = FWLiteSample.fromDAS("WW_S16_94X_ext1", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_S16_94X                  = FWLiteSample.fromDAS("WZ_S16_94X", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_S16_94X_ext1             = FWLiteSample.fromDAS("WZ_S16_94X_ext1", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ_S16_94X                  = FWLiteSample.fromDAS("ZZ_S16_94X", "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZGTo2LG_NLO_S16_94X_ext1    = FWLiteSample.fromDAS("ZGTo2LG_NLO_S16_94X_ext1", "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO_S16_94X         = FWLiteSample.fromDAS("WGToLNuG_LO_S16_94X", "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_NLO_S16_94X        = FWLiteSample.fromDAS("WGToLNuG_NLO_S16_94X", "/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diboson = [
    VVTo2L2Nu_NLO_S16_94X,
    VVTo2L2Nu_NLO_S16_94X_ext1,
    WWTo1L1Nu2Q_NLO_S16_94X,
    WWToLNuQQ_S16_94X,
    WWTo2L2Nu_S16_94X,
    WZTo1L1Nu2Q_NLO_S16_94X,
    WZTo1L3Nu_NLO_S16_94X,
    WZTo2L2Q_NLO_S16_94X,
    WZTo3LNu_NLO_S16_94X,
    WZTo3LNu_pow_S16_94X_ext1,
    ZZTo2L2Nu_pow_S16_94X,
    ZZTo2L2Q_pow_S16_94X,
    ZZTo2Q2Nu_NLO_S16_94X,
    ZZTo4L_pow_S16_94X,
    WW_S16_94X,
    WW_S16_94X_ext1,
    WZ_S16_94X,
    WZ_S16_94X_ext1,
    ZZ_S16_94X,
    ZGTo2LG_NLO_S16_94X_ext1,
    WGToLNuG_LO_S16_94X,
    WGToLNuG_NLO_S16_94X,
]

## triboson samples and beyond

WWW_NLO_S16_94X = FWLiteSample.fromDAS("WWW_NLO_S16_94X", "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWZ_NLO_S16_94X = FWLiteSample.fromDAS("WWZ_NLO_S16_94X", "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZZ_NLO_S16_94X = FWLiteSample.fromDAS("WZZ_NLO_S16_94X", "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZZ_NLO_S16_94X = FWLiteSample.fromDAS("ZZZ_NLO_S16_94X", "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WWW_NLO_S16_94X,
    WWZ_NLO_S16_94X,
    WZZ_NLO_S16_94X,
    ZZZ_NLO_S16_94X,
]

## gluglu

GluGluHToZZTo4L_S16_94X             = FWLiteSample.fromDAS("GluGluHToZZTo4L_S16_94X", "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2mu_S16_94X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu_S16_94X", "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2tau_S16_94X  = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau_S16_94X", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2tau_S16_94X = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2tau_S16_94X", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4e_S16_94X      = FWLiteSample.fromDAS("GluGluToContinToZZTo4e_S16_94X", "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4mu_S16_94X     = FWLiteSample.fromDAS("GluGluToContinToZZTo4mu_S16_94X", "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4tau_S16_94X    = FWLiteSample.fromDAS("GluGluToContinToZZTo4tau_S16_94X", "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

gluglu = [
    GluGluHToZZTo4L_S16_94X,
    GluGluToContinToZZTo2e2mu_S16_94X,
    GluGluToContinToZZTo2e2tau_S16_94X,
    GluGluToContinToZZTo2mu2tau_S16_94X,
    GluGluToContinToZZTo4e_S16_94X,
    GluGluToContinToZZTo4mu_S16_94X,
    GluGluToContinToZZTo4tau_S16_94X,
]

allSamples = DY + DY_HT + ST_4f + ST_5f + TTJets + TTX + WJets + WJetsToLNu_HT + diboson + multiboson + gluglu

for sample in allSamples:
    sample.isData = False
