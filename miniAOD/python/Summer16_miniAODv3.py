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
DYJetsToLL_M10to50_LO          = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO",  "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_NLO         = FWLiteSample.fromDAS("DYJetsToLL_M10to50_NLO", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_NLO_ext1    = FWLiteSample.fromDAS("DYJetsToLL_M10to50_NLO_ext1", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M5to50_HT70to100_LO         = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT70to100_LO", "/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT100to200_LO        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT100to200_LO", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT100to200_LO_ext1   = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT100to200_LO_ext1", "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT200to400_LO        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT200to400_LO", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT200to400_LO_ext1   = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT200to400_LO_ext1", "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT400to600_LO        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT400to600_LO", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT400to600_LO_ext1   = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT400to600_LO_ext1", "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M5to50_HT600toInf_LO        = FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT600toInf_LO", "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_NLO_ext2        = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO_ext2", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M50_LO_FS       = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_FS", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_ext1         = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_ext1", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_ext2         = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_ext2", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_HT70to100_LO        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100_LO", "/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO_ext1", "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_ext1", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_ext1", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800_LO       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800_LO", "/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200_LO      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200_LO", "/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500_LO     = FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500_LO", "/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT2500toInf_LO      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf_LO", "/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY = [
    #DYJetsToLL_M50_LO_FS,
    DYJetsToLL_M50_LO_ext1,
    DYJetsToLL_M50_LO_ext2,
    DYJetsToLL_M50_NLO_ext2,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M10to50_NLO,
    DYJetsToLL_M10to50_NLO_ext1,
]

DY_HT = [
    DYJetsToLL_M50_HT70to100_LO,
    DYJetsToLL_M50_HT100to200_LO_ext1,
    DYJetsToLL_M50_HT200to400_LO,
    DYJetsToLL_M50_HT200to400_LO_ext1,
    DYJetsToLL_M50_HT400to600_LO,
    DYJetsToLL_M50_HT400to600_LO_ext1,
    DYJetsToLL_M50_HT600to800_LO,
    DYJetsToLL_M50_HT800to1200_LO,
    DYJetsToLL_M50_HT1200to2500_LO,
    DYJetsToLL_M50_HT2500toInf_LO,

    DYJetsToLL_M5to50_HT70to100_LO,
    DYJetsToLL_M5to50_HT100to200_LO,
    DYJetsToLL_M5to50_HT100to200_LO_ext1,
    DYJetsToLL_M5to50_HT200to400_LO,
    DYJetsToLL_M5to50_HT200to400_LO_ext1,
    DYJetsToLL_M5to50_HT400to600_LO,
    DYJetsToLL_M5to50_HT400to600_LO_ext1,
    DYJetsToLL_M5to50_HT600toInf_LO,
]

# single top

ST_schannel_4f_NLO                 = FWLiteSample.fromDAS("ST_schannel_4f_NLO", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_schannel_4f_CP5                 = FWLiteSample.fromDAS("ST_schannel_4f_CP5", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_4f_pow         = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow", "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_4f_pow_CP5     = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow_CP5", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_pow             = FWLiteSample.fromDAS("ST_tchannel_top_4f_pow", "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_pow_CP5         = FWLiteSample.fromDAS("ST_tchannel_top_4f_pow_CP5", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_4f = [
    ST_schannel_4f_NLO,
    ST_schannel_4f_CP5,
    ST_tchannel_antitop_4f_pow,
    ST_tchannel_antitop_4f_pow_CP5,
    ST_tchannel_top_4f_pow,
    ST_tchannel_top_4f_pow_CP5,
]


ST_tW_antitop_NoFullyHad_5f_pow    = FWLiteSample.fromDAS("ST_tW_antitop_NoFullyHad_5f_pow", "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_5f_pow_ext1          = FWLiteSample.fromDAS("ST_tW_antitop_5f_pow_ext1", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_5f_pow               = FWLiteSample.fromDAS("ST_tW_antitop_5f_pow", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_5f_pow_CP5           = FWLiteSample.fromDAS("ST_tW_antitop_5f_pow_CP5","/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow        = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow", "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow_ext    = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow_ext", "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_5f_pow_ext1              = FWLiteSample.fromDAS("ST_tW_top_5f_pow_ext1", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_5f_pow                   = FWLiteSample.fromDAS("ST_tW_top_5f_pow", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_5f_pow_CP5               = FWLiteSample.fromDAS("ST_tW_top_5f_pow_CP5","/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tWll_5f_LO                      = FWLiteSample.fromDAS("ST_tWll_5f_LO", "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tWnunu_5f_LO                    = FWLiteSample.fromDAS("ST_tWnunu_5f_LO", "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_5f = [
    ST_tW_antitop_NoFullyHad_5f_pow,
    ST_tW_antitop_5f_pow_ext1,
    ST_tW_antitop_5f_pow,
    ST_tW_antitop_5f_pow_CP5,
    ST_tW_top_NoFullyHad_5f_pow,
    ST_tW_top_NoFullyHad_5f_pow_ext,
    ST_tW_top_5f_pow_ext1,
    ST_tW_top_5f_pow,
    ST_tW_top_5f_pow_CP5,
    ST_tWll_5f_LO,
    ST_tWnunu_5f_LO,
]

# TTJets
#TTJets_LO_FS   = FWLiteSample.fromDAS("TTJets_LO_FS", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#TTJets_LO      = FWLiteSample.fromDAS("TTJets_LO", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTo2L2Nu_noSC_pow  = FWLiteSample.fromDAS("TTTo2L2Nu_noSC_pow", "/TTTo2L2Nu_noSC_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow_CP5   = FWLiteSample.fromDAS("TTTo2L2Nu_pow_CP5", "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow       = FWLiteSample.fromDAS("TTTo2L2Nu_pow", "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemilepton_pow  = FWLiteSample.fromDAS("TTToSemilepton_pow", "/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemilepton_pow_CP5 = FWLiteSample.fromDAS("TTToSemilepton_pow_CP5", "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TT_pow              = FWLiteSample.fromDAS("TT_pow", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow_CP5= FWLiteSample.fromDAS("TTToHadronic_pow_CP5", "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets = [
    TTTo2L2Nu_noSC_pow,
    TTTo2L2Nu_pow_CP5,
    TTTo2L2Nu_pow,
    TTToSemilepton_pow,
    TTToSemilepton_pow_CP5,
    TT_pow,
    TTToHadronic_pow_CP5,
]

# t(t)g(g)
THQ_LO                  = FWLiteSample.fromDAS("THQ_LO", "/THQ_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THW_LO                  = FWLiteSample.fromDAS("THW_LO", "/THW_Hincl_13TeV-madgraph-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
tZq_ll_NLO              = FWLiteSample.fromDAS("tZq_ll_NLO", "/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
tZq_nunu_NLO            = FWLiteSample.fromDAS("tZq_nunu_NLO", '/tZq_nunu_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTT_NLO                = FWLiteSample.fromDAS("TTTT_NLO", "/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWW_NLO                = FWLiteSample.fromDAS("TTWW_NLO", "/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWZ_NLO                = FWLiteSample.fromDAS("TTWZ_NLO", "/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZZ_NLO                = FWLiteSample.fromDAS("TTZZ_NLO", "/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTW_LO                  = FWLiteSample.fromDAS("TTW_LO",          "/ttWJets_13TeV_madgraphMLM/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToLNu_NLO        = FWLiteSample.fromDAS("TTWJetsToLNu_NLO", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToQQ_NLO         = FWLiteSample.fromDAS("TTWJetsToQQ_NLO", "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLLNuNu_NLO_ext2    = FWLiteSample.fromDAS("TTZToLLNuNu_NLO_ext2", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLLNuNu_NLO_ext3    = FWLiteSample.fromDAS("TTZToLLNuNu_NLO_ext3", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLL_M1to10_LO       = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO", "/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToQQ_NLO             = FWLiteSample.fromDAS("TTZToQQ_NLO", "/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttZJets_LO              = FWLiteSample.fromDAS("ttZJets_LO", "/ttZJets_13TeV_madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHToNonbb_pow          = FWLiteSample.fromDAS("ttHToNonbb_pow", "/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_pow             = FWLiteSample.fromDAS("ttHTobb_pow", "/ttHTobb_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TGG                     = FWLiteSample.fromDAS("TGG", "/TGGJets_leptonDecays_13TeV_MadGraph_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TGJets                  = FWLiteSample.fromDAS("TGJets", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TGJets_ext1             = FWLiteSample.fromDAS("TGJets_ext1", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TGJets_lep_NLO          = FWLiteSample.fromDAS("TGJets_lep_NLO_PS", "/TGJets_leptonDecays_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGJets_NLO             = FWLiteSample.fromDAS("TTGJets_NLO", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGJets_NLO_ext1        = FWLiteSample.fromDAS("TTGJets_NLO_ext1", "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTGamma_semilep_LO                      = FWLiteSample.fromDAS("TTGamma_semilep_LO",             "/TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_TuneUp               = FWLiteSample.fromDAS("TTGamma_semilep_LO_TuneUp",      "/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_TuneDown             = FWLiteSample.fromDAS("TTGamma_semilep_LO_TuneDown",    "/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_erdOn                = FWLiteSample.fromDAS("TTGamma_semilep_LO_erdOn",       "/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_ptG100To200          = FWLiteSample.fromDAS("TTGamma_semilep_LO_ptG100To200", "/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_ptG200               = FWLiteSample.fromDAS("TTGamma_semilep_LO_ptG200",      "/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTGamma_dilep_LO                        = FWLiteSample.fromDAS("TTGamma_dilep_LO",             "/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_TuneUp                 = FWLiteSample.fromDAS("TTGamma_dilep_LO_TuneUp",      "/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_TuneDown               = FWLiteSample.fromDAS("TTGamma_dilep_LO_TuneDown",    "/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_erdOn                  = FWLiteSample.fromDAS("TTGamma_dilep_LO_erdOn",       "/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_ptG100To200            = FWLiteSample.fromDAS("TTGamma_dilep_LO_ptG100To200", "/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_ptG200                 = FWLiteSample.fromDAS("TTGamma_dilep_LO_ptG200",      "/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTGamma_had_LO                          = FWLiteSample.fromDAS("TTGamma_had_LO",             "/TTGamma_Hadronic_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_had_LO_ptG100To200              = FWLiteSample.fromDAS("TTGamma_had_LO_ptG100To200", "/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_had_LO_ptG200                   = FWLiteSample.fromDAS("TTGamma_had_LO_ptG200",      "/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)



TTX = [
    TTW_LO,
    THQ_LO,
    THW_LO,
    tZq_ll_NLO,
    tZq_nunu_NLO,
    TTTT_NLO,
    TTWZ_NLO,
    TTWW_NLO,
    TTZZ_NLO,
    TTWJetsToLNu_NLO,
    TTWJetsToQQ_NLO,
    TTZToLL_M1to10_LO,
    TTZToLLNuNu_NLO_ext2,
    TTZToLLNuNu_NLO_ext3,
    TTZToQQ_NLO,
    ttZJets_LO,
    ttHToNonbb_pow,
    ttHTobb_pow,
    TGG,
    TGJets,
    TGJets_ext1,
    TGJets_lep_NLO,
    TTGJets_NLO,
    TTGJets_NLO_ext1,
    TTGamma_dilep_LO,
    TTGamma_dilep_LO_erdOn,
    TTGamma_dilep_LO_TuneUp,
    TTGamma_dilep_LO_TuneDown,
    TTGamma_dilep_LO_ptG100To200,
    TTGamma_dilep_LO_ptG200,
    TTGamma_semilep_LO,
    TTGamma_semilep_LO_erdOn,
    TTGamma_semilep_LO_TuneUp,
    TTGamma_semilep_LO_TuneDown,
    TTGamma_semilep_LO_ptG100To200,
    TTGamma_semilep_LO_ptG200,
    TTGamma_had_LO,
    TTGamma_had_LO_ptG100To200,
    TTGamma_had_LO_ptG200,
]



## W+jets
WJetsToLNu_LO                  = FWLiteSample.fromDAS("WJetsToLNu_LO", "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_LO_ext2             = FWLiteSample.fromDAS("WJetsToLNu_LO_ext2", "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJets = [
    WJetsToLNu_LO,
    WJetsToLNu_LO_ext2,
]

WJetsToLNu_HT70To100_LO            = FWLiteSample.fromDAS("WJetsToLNu_HT70To100_LO", "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT100To200_LO           = FWLiteSample.fromDAS("WJetsToLNu_HT100To200_LO", "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400_LO           = FWLiteSample.fromDAS("WJetsToLNu_HT200To400_LO", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400_LO_ext1      = FWLiteSample.fromDAS("WJetsToLNu_HT200To400_LO_ext1", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400_LO_ext2      = FWLiteSample.fromDAS("WJetsToLNu_HT200To400_LO_ext2", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400To600_LO           = FWLiteSample.fromDAS("WJetsToLNu_HT400To600_LO", "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400To600_LO_ext1      = FWLiteSample.fromDAS("WJetsToLNu_HT400To600_LO_ext1", "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600To800_LO           = FWLiteSample.fromDAS("WJetsToLNu_HT600To800_LO", "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600To800_LO_ext1      = FWLiteSample.fromDAS("WJetsToLNu_HT600To800_LO_ext1", "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800To1200_LO          = FWLiteSample.fromDAS("WJetsToLNu_HT800To1200_LO", "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800To1200_LO_ext1     = FWLiteSample.fromDAS("WJetsToLNu_HT800To1200_LO_ext1", "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200To2500_LO         = FWLiteSample.fromDAS("WJetsToLNu_HT1200To2500_LO", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200To2500_LO_ext1    = FWLiteSample.fromDAS("WJetsToLNu_HT1200To2500_LO_ext1", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500ToInf_LO          = FWLiteSample.fromDAS("WJetsToLNu_HT2500ToInf_LO", "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500ToInf_LO_ext1     = FWLiteSample.fromDAS("WJetsToLNu_HT2500ToInf_LO_ext1", "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_HT = [
    WJetsToLNu_HT70To100_LO,
    WJetsToLNu_HT100To200_LO,
    WJetsToLNu_HT200To400_LO,
    WJetsToLNu_HT200To400_LO_ext1,
    WJetsToLNu_HT200To400_LO_ext2,
    WJetsToLNu_HT400To600_LO,
    WJetsToLNu_HT400To600_LO_ext1,
    WJetsToLNu_HT600To800_LO,
    WJetsToLNu_HT600To800_LO_ext1,
    WJetsToLNu_HT800To1200_LO,
    WJetsToLNu_HT800To1200_LO_ext1,
    WJetsToLNu_HT1200To2500_LO,
    WJetsToLNu_HT1200To2500_LO_ext1,
    WJetsToLNu_HT2500ToInf_LO,
    WJetsToLNu_HT2500ToInf_LO_ext1,
]

W1JetsToLNu             = FWLiteSample.fromDAS("W1JetsToLNu", "/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W2JetsToLNu             = FWLiteSample.fromDAS("W2JetsToLNu", "/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W3JetsToLNu             = FWLiteSample.fromDAS("W3JetsToLNu", "/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W4JetsToLNu             = FWLiteSample.fromDAS("W4JetsToLNu", "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

W1JetsToLNu_NuPt_200    = FWLiteSample.fromDAS("W1JetsToLNu_NuPt_200", "/W1JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W2JetsToLNu_NuPt_200    = FWLiteSample.fromDAS("W2JetsToLNu_NuPt_200", "/W2JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W3JetsToLNu_NuPt_200    = FWLiteSample.fromDAS("W3JetsToLNu_NuPt_200", "/W3JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W4JetsToLNu_NuPt_200    = FWLiteSample.fromDAS("W4JetsToLNu_NuPt_200", "/W4JetsToLNu_NuPt-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsNJetBinned = [
    W1JetsToLNu,
    W2JetsToLNu,
    W3JetsToLNu,
    W4JetsToLNu,
    W1JetsToLNu_NuPt_200,
    W2JetsToLNu_NuPt_200,
    W3JetsToLNu_NuPt_200,
    W4JetsToLNu_NuPt_200,
]


# ZInv

ZJetsToNuNu_Zpt_100to200        = FWLiteSample.fromDAS("ZJetsToNuNu_Zpt_100to200", "/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_Zpt_200toInf        = FWLiteSample.fromDAS("ZJetsToNuNu_Zpt_200toInf", "/ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZJetsToNuNu_HT_100To200         = FWLiteSample.fromDAS("ZJetsToNuNu_HT_100To200", "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_100To200_ext1    = FWLiteSample.fromDAS("ZJetsToNuNu_HT_100To200_ext1", "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_200To400         = FWLiteSample.fromDAS("ZJetsToNuNu_HT_200To400", "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_200To400_ext1    = FWLiteSample.fromDAS("ZJetsToNuNu_HT_200To400_ext1", "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_400To600         = FWLiteSample.fromDAS("ZJetsToNuNu_HT_400To600", "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_600To800         = FWLiteSample.fromDAS("ZJetsToNuNu_HT_600To800", "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_800To1200        = FWLiteSample.fromDAS("ZJetsToNuNu_HT_800To1200", "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_1200To2500       = FWLiteSample.fromDAS("ZJetsToNuNu_HT_1200To2500","/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_1200To2500_ext1  = FWLiteSample.fromDAS("ZJetsToNuNu_HT_1200To2500_ext1","/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_2500ToInf        = FWLiteSample.fromDAS("ZJetsToNuNu_HT_2500ToInf", "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZJetsToNuNu = [
    ZJetsToNuNu_Zpt_100to200,
    ZJetsToNuNu_Zpt_200toInf,
    ZJetsToNuNu_HT_100To200,
    ZJetsToNuNu_HT_100To200_ext1,
    ZJetsToNuNu_HT_200To400,
    ZJetsToNuNu_HT_200To400_ext1,
    ZJetsToNuNu_HT_400To600,
    ZJetsToNuNu_HT_600To800,
    ZJetsToNuNu_HT_800To1200,
    ZJetsToNuNu_HT_1200To2500,
    ZJetsToNuNu_HT_1200To2500_ext1,
    ZJetsToNuNu_HT_2500ToInf,
]

## diboson samples

VVTo2L2Nu_NLO              = FWLiteSample.fromDAS("VVTo2L2Nu_NLO", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
VVTo2L2Nu_NLO_ext1         = FWLiteSample.fromDAS("VVTo2L2Nu_NLO_ext1", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo1L1Nu2Q_NLO            = FWLiteSample.fromDAS("WWTo1L1Nu2Q_NLO", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWToLNuQQ                  = FWLiteSample.fromDAS("WWToLNuQQ", "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu                  = FWLiteSample.fromDAS("WWTo2L2Nu", "/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo4Q                     = FWLiteSample.fromDAS("WWTo4Q", "/WWTo4Q_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu_DoubleScattering = FWLiteSample.fromDAS("WWTo2L2Nu_DoubleScattering", "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L1Nu2Q_NLO            = FWLiteSample.fromDAS("WZTo1L1Nu2Q_NLO", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L3Nu_NLO              = FWLiteSample.fromDAS("WZTo1L3Nu_NLO", "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2L2Q_NLO               = FWLiteSample.fromDAS("WZTo2L2Q_NLO", "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2Q2Nu_NLO              = FWLiteSample.fromDAS("WZTo2Q2Nu_NLO", "/WZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_pow               = FWLiteSample.fromDAS("WZTo3LNu", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_NLO               = FWLiteSample.fromDAS("WZTo3LNu_NLO", "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_pow_ext1          = FWLiteSample.fromDAS("WZTo3LNu_pow_ext1", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Nu_pow              = FWLiteSample.fromDAS("ZZTo2L2Nu_pow", "/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Q_pow               = FWLiteSample.fromDAS("ZZTo2L2Q_pow", "/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2Q2Nu_NLO              = FWLiteSample.fromDAS("ZZTo2Q2Nu_NLO", "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4L_pow                 = FWLiteSample.fromDAS("ZZTo4L_pow", "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WW                  = FWLiteSample.fromDAS("WW", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WW_ext1             = FWLiteSample.fromDAS("WW_ext1", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ                  = FWLiteSample.fromDAS("WZ", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_ext1             = FWLiteSample.fromDAS("WZ_ext1", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ                  = FWLiteSample.fromDAS("ZZ", "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZGTo2LG_NLO_ext1    = FWLiteSample.fromDAS("ZGTo2LG_NLO_ext1",   "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZGToLLG_NLO_LoosePtlPtg = FWLiteSample.fromDAS("ZGToLLG_NLO_LoosePtlPtg", "/ZGToLLG_01J_LoosePtlPtg_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZGToLLG_NLO         = FWLiteSample.fromDAS("ZGToLLG_NLO",        "/ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZGToLLG_NLO_lowMLL  = FWLiteSample.fromDAS("ZGToLLG_NLO_lowMLL", "/ZGToLLG_01J_5f_lowMLL_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO         = FWLiteSample.fromDAS("WGToLNuG_LO",        "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO_ptG130  = FWLiteSample.fromDAS("WGToLNuG_LO_ptG130", "/WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO_ptG500  = FWLiteSample.fromDAS("WGToLNuG_LO_ptG500", "/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_NLO        = FWLiteSample.fromDAS("WGToLNuG_NLO",       "/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diboson = [
    VVTo2L2Nu_NLO,
    VVTo2L2Nu_NLO_ext1,
    WWTo4Q,
    WWTo1L1Nu2Q_NLO,
    WWToLNuQQ,
    WWTo2L2Nu,
    WWTo2L2Nu_DoubleScattering, 
    WZTo1L1Nu2Q_NLO,
    WZTo1L3Nu_NLO,
    WZTo2L2Q_NLO,
    WZTo2Q2Nu_NLO,
    WZTo3LNu_NLO,
    WZTo3LNu_pow_ext1,
    WZTo3LNu_pow,
    ZZTo2L2Nu_pow,
    ZZTo2L2Q_pow,
    ZZTo2Q2Nu_NLO,
    ZZTo4L_pow,
    WW,
    WW_ext1,
    WZ,
    WZ_ext1,
    ZZ,
    ZGTo2LG_NLO_ext1,
    ZGToLLG_NLO,
    ZGToLLG_NLO_lowMLL,
    ZGToLLG_NLO_LoosePtlPtg, 
    WGToLNuG_LO,
    WGToLNuG_LO_ptG130,
    WGToLNuG_LO_ptG500,
    WGToLNuG_NLO,
]

## triboson samples and beyond

WWW_NLO = FWLiteSample.fromDAS("WWW_NLO", "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWZ_NLO = FWLiteSample.fromDAS("WWZ_NLO", "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZZ_NLO = FWLiteSample.fromDAS("WZZ_NLO", "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZZ_NLO = FWLiteSample.fromDAS("ZZZ_NLO", "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WWW_NLO,
    WWZ_NLO,
    WZZ_NLO,
    ZZZ_NLO,
]


## gluglu

GluGluHToZZTo4L             = FWLiteSample.fromDAS("GluGluHToZZTo4L", "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2mu   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu", "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2tau  = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2tau = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4e      = FWLiteSample.fromDAS("GluGluToContinToZZTo4e", "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4mu     = FWLiteSample.fromDAS("GluGluToContinToZZTo4mu", "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4tau    = FWLiteSample.fromDAS("GluGluToContinToZZTo4tau", "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

gluglu = [
    GluGluHToZZTo4L,
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo4tau,
]


QCD_Mu_pt15to20         = FWLiteSample.fromDAS("QCD_Mu_pt15to20",         "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt20to30         = FWLiteSample.fromDAS("QCD_Mu_pt20to30",         "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt30to50         = FWLiteSample.fromDAS("QCD_Mu_pt30to50",         "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt50to80         = FWLiteSample.fromDAS("QCD_Mu_pt50to80",         "/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt80to120        = FWLiteSample.fromDAS("QCD_Mu_pt80to120",        "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt80to120_ext1   = FWLiteSample.fromDAS("QCD_Mu_pt80to120_ext1",   "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt120to170       = FWLiteSample.fromDAS("QCD_Mu_pt120to170",       "/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt170to300       = FWLiteSample.fromDAS("QCD_Mu_pt170to300",       "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt170to300_ext1  = FWLiteSample.fromDAS("QCD_Mu_pt170to300_ext1",  "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt300to470       = FWLiteSample.fromDAS("QCD_Mu_pt300to470",       "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt300to470_ext1  = FWLiteSample.fromDAS("QCD_Mu_pt300to470_ext1",  "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt470to600       = FWLiteSample.fromDAS("QCD_Mu_pt470to600",       "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt470to600_ext1  = FWLiteSample.fromDAS("QCD_Mu_pt470to600_ext1",  "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt600to800       = FWLiteSample.fromDAS("QCD_Mu_pt600to800",       "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt600to800_ext1  = FWLiteSample.fromDAS("QCD_Mu_pt600to800_ext1",  "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt800to1000      = FWLiteSample.fromDAS("QCD_Mu_pt800to1000",      "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt800to1000_ext1 = FWLiteSample.fromDAS("QCD_Mu_pt800to1000_ext1", "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt1000toInf      = FWLiteSample.fromDAS("QCD_Mu_pt1000toInf",      "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt1000toInf_ext1 = FWLiteSample.fromDAS("QCD_Mu_pt1000toInf_ext1", "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD_Ele_pt20to30        = FWLiteSample.fromDAS("QCD_Ele_pt20to30",        "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt30to50        = FWLiteSample.fromDAS("QCD_Ele_pt30to50",        "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt30to50_ext1   = FWLiteSample.fromDAS("QCD_Ele_pt30to50_ext1",   "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt50to80        = FWLiteSample.fromDAS("QCD_Ele_pt50to80",        "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt50to80_ext1   = FWLiteSample.fromDAS("QCD_Ele_pt50to80_ext1",   "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt80to120       = FWLiteSample.fromDAS("QCD_Ele_pt80to120",       "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt80to120_ext1  = FWLiteSample.fromDAS("QCD_Ele_pt80to120_ext1",  "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt120to170      = FWLiteSample.fromDAS("QCD_Ele_pt120to170",      "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt120to170_ext1 = FWLiteSample.fromDAS("QCD_Ele_pt120to170_ext1", "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt170to300      = FWLiteSample.fromDAS("QCD_Ele_pt170to300",      "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt300toInf      = FWLiteSample.fromDAS("QCD_Ele_pt300toInf",      "/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD = [
        QCD_Mu_pt15to20,
        QCD_Mu_pt20to30,
        QCD_Mu_pt30to50,
        QCD_Mu_pt50to80,
        QCD_Mu_pt80to120,
        QCD_Mu_pt80to120_ext1,
        QCD_Mu_pt120to170,
        QCD_Mu_pt170to300,
        QCD_Mu_pt170to300_ext1,
        QCD_Mu_pt300to470,
        QCD_Mu_pt300to470_ext1,
        QCD_Mu_pt470to600,
        QCD_Mu_pt470to600_ext1,  
        QCD_Mu_pt600to800,   
        QCD_Mu_pt600to800_ext1,  
        QCD_Mu_pt800to1000,  
        QCD_Mu_pt800to1000_ext1, 
        QCD_Mu_pt1000toInf,  
        QCD_Mu_pt1000toInf_ext1,

        QCD_Ele_pt20to30,
        QCD_Ele_pt30to50,
        QCD_Ele_pt30to50_ext1,
        QCD_Ele_pt50to80,
        QCD_Ele_pt50to80_ext1,
        QCD_Ele_pt80to120,
        QCD_Ele_pt80to120_ext1,
        QCD_Ele_pt120to170,
        QCD_Ele_pt120to170_ext1,
        QCD_Ele_pt170to300,
        QCD_Ele_pt300toInf,
]

GJets_HT40to100        = FWLiteSample.fromDAS("GJets_HT40to100",        "/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT40to100_ext    = FWLiteSample.fromDAS("GJets_HT40to100_ext",    "/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT100to200       = FWLiteSample.fromDAS("GJets_HT100to200",       "/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT100to200_ext   = FWLiteSample.fromDAS("GJets_HT100to200_ext",   "/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT200to400       = FWLiteSample.fromDAS("GJets_HT200to400",       "/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT200to400_ext   = FWLiteSample.fromDAS("GJets_HT200to400_ext",   "/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT400to600       = FWLiteSample.fromDAS("GJets_HT400to600",       "/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT400to600_ext   = FWLiteSample.fromDAS("GJets_HT400to600_ext",   "/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT600toInf       = FWLiteSample.fromDAS("GJets_HT600toInf",       "/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT600toInf_ext   = FWLiteSample.fromDAS("GJets_HT600toInf_ext",   "/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

GJetsHT = [
           GJets_HT40to100,
           GJets_HT40to100_ext,
           GJets_HT100to200,
           GJets_HT100to200_ext,
           GJets_HT200to400,
           GJets_HT200to400_ext,
           GJets_HT400to600,
           GJets_HT400to600_ext,
           GJets_HT600toInf,
           GJets_HT600toInf_ext,
]

## T2tt FullSim signals for corridor studies
SMS_T2tt_mStop_650_mLSP_350             = FWLiteSample.fromDAS("SMS_T2tt_mStop_650_mLSP_350",               '/SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_850_mLSP_100             = FWLiteSample.fromDAS("SMS_T2tt_mStop_850_mLSP_100",               '/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_150_mLSP_50  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_150_mLSP_50",    "/SMS-T2tt_3J_xqcut-20_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_175_mLSP_1   = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_175_mLSP_1",     "/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_corridor_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_200_mLSP_50  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_200_mLSP_50",    "/SMS-T2tt_3J_xqcut-20_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_225_mLSP_50  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_225_mLSP_50",    "/SMS-T2tt_3J_xqcut-20_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_50  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_50",    "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_75  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_75",    "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_corridor_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_150 = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_150",   "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_300_mLSP_150 = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_300_mLSP_150",   "/SMS-T2tt_3J_xqcut-20_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_325_mLSP_150 = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_325_mLSP_150",   "/SMS-T2tt_3J_xqcut-20_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_350_mLSP_150 = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_350_mLSP_150",   "/SMS-T2tt_3J_xqcut-20_mStop-350_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
    
T2tt_FullSim = [
    SMS_T2tt_mStop_650_mLSP_350,
    SMS_T2tt_mStop_850_mLSP_100,
    SMS_T2tt_3J_xqcut_20_mStop_150_mLSP_50,
    SMS_T2tt_3J_xqcut_20_mStop_175_mLSP_1,
    SMS_T2tt_3J_xqcut_20_mStop_200_mLSP_50,
    SMS_T2tt_3J_xqcut_20_mStop_225_mLSP_50,
    SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_50,
    SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_75,
    SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_150,
    SMS_T2tt_3J_xqcut_20_mStop_300_mLSP_150,
    SMS_T2tt_3J_xqcut_20_mStop_325_mLSP_150,
    SMS_T2tt_3J_xqcut_20_mStop_350_mLSP_150,
    ]

ttH_HToInvisible = FWLiteSample.fromDAS("ttH_HToInvisible", "/ttH_HToInvisible_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ttH = [ ttH_HToInvisible ]

## DM signals
TTbarDMJets_Dilepton_scalar         = FWLiteSample.fromDAS("TTbarDMJets_Dilepton_scalar", "/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_rp_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTbarDMJets_Dilepton_pseudoscalar   = FWLiteSample.fromDAS("TTbarDMJets_Dilepton_pseudoscalar", "/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_rp_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DM = [TTbarDMJets_Dilepton_scalar, TTbarDMJets_Dilepton_pseudoscalar]

allSamples = DY + DY_HT + ST_4f + ST_5f + TTJets + TTX + WJets + WJetsToLNu_HT + WJetsNJetBinned + ZJetsToNuNu + diboson + multiboson + gluglu + QCD + GJetsHT + T2tt_FullSim + ttH + DM

for sample in allSamples:
    sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
