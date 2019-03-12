'''
miniAOD samples of Fall17 campaign, miniAODv2 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*TuneCP5*/RunIIFall17MiniAODv2*/MINIAODSIM"
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
dbFile = dbDir+"DB_Fall17_miniAODv2.sql"

logger.info("Using db file: %s", dbFile)


## DY

# low mass
DYJetsToLL_M10to50_LO_F17_94X                  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO_F17_94X", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M10to50_HT100to200_LO_F17_94X       = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT100to200_LO_F17_94X", "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT100to200_LO_F17_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT100to200_LO_F17_94X_ext1", "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT200to400_LO_F17_94X       = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT200to400_LO_F17_94X", "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT200to400_LO_F17_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT200to400_LO_F17_94X_ext1", "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT400to600_LO_F17_94X       = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT400to600_LO_F17_94X", "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT400to600_LO_F17_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT400to600_LO_F17_94X_ext1", "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT600toInf_LO_F17_94X       = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT600toInf_LO_F17_94X", "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_HT600toInf_LO_F17_94X_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_HT600toInf_LO_F17_94X_ext1", "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

# high mass
DYJetsToLL_M50_NLO_F17_94X                     = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO_F17_94X", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_F17_94X                      = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_F17_94X", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_F17_94X_ext1                 = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_F17_94X_ext1", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_HT70to100_LO_F17_94X            = FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100_LO_F17_94X", "/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO_F17_94X           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO_F17_94X", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO_F17_94X_ext1      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO_F17_94X_ext1", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_F17_94X           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_F17_94X", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_F17_94X_ext1      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_F17_94X_ext1", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_F17_94X           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_F17_94X", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_F17_94X_ext1      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_F17_94X_ext1", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800_LO_F17_94X           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800_LO_F17_94X", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200_LO_F17_94X          = FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200_LO_F17_94X", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500_LO_F17_94X         = FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500_LO_F17_94X", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT2500toInf_LO_F17_94X          = FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf_LO_F17_94X", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY = [
    DYJetsToLL_M10to50_LO_F17_94X,
    DYJetsToLL_M50_NLO_F17_94X,
    DYJetsToLL_M50_LO_F17_94X,
    DYJetsToLL_M50_LO_F17_94X_ext1,
]

DY_HT = [
    DYJetsToLL_M10to50_HT100to200_LO_F17_94X,
    DYJetsToLL_M10to50_HT100to200_LO_F17_94X_ext1,
    DYJetsToLL_M10to50_HT200to400_LO_F17_94X,
    DYJetsToLL_M10to50_HT200to400_LO_F17_94X_ext1,
    DYJetsToLL_M10to50_HT400to600_LO_F17_94X,
    DYJetsToLL_M10to50_HT400to600_LO_F17_94X_ext1,
    DYJetsToLL_M10to50_HT600toInf_LO_F17_94X,
    DYJetsToLL_M10to50_HT600toInf_LO_F17_94X_ext1,
    DYJetsToLL_M50_HT70to100_LO_F17_94X,
    DYJetsToLL_M50_HT100to200_LO_F17_94X,
    DYJetsToLL_M50_HT100to200_LO_F17_94X_ext1,
    DYJetsToLL_M50_HT200to400_LO_F17_94X,
    DYJetsToLL_M50_HT200to400_LO_F17_94X_ext1,
    DYJetsToLL_M50_HT400to600_LO_F17_94X,
    DYJetsToLL_M50_HT400to600_LO_F17_94X_ext1,
    DYJetsToLL_M50_HT600to800_LO_F17_94X,
    DYJetsToLL_M50_HT800to1200_LO_F17_94X,
    DYJetsToLL_M50_HT1200to2500_LO_F17_94X,
    DYJetsToLL_M50_HT2500toInf_LO_F17_94X,
]

# single top
ST_schannel_4f_NLO_F17_94X                      = FWLiteSample.fromDAS("ST_schannel_4f_NLO_F17_94X", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_schannel_4f_NLO_PS_F17_94X                   = FWLiteSample.fromDAS("ST_schannel_4f_NLO_PS_F17_94X", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_4f_incl_pow_F17_94X         = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_incl_pow_F17_94X", "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_incl_pow_F17_94X             = FWLiteSample.fromDAS("ST_tchannel_top_4f_incl_pow_F17_94X", "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_4f = [ 
    ST_schannel_4f_NLO_F17_94X,
    ST_schannel_4f_NLO_PS_F17_94X,
    ST_tchannel_antitop_4f_incl_pow_F17_94X,
    ST_tchannel_top_4f_incl_pow_F17_94X,
]

ST_tchannel_antitop_5f_pow_PS_F17_94X           = FWLiteSample.fromDAS("ST_tchannel_antitop_5f_pow_PS_F17_94X", "/ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_5f_pow_F17_94X                  = FWLiteSample.fromDAS("ST_tchannel_top_5f_pow_F17_94X", "/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_NoFullyHad_5f_pow_PS_F17_94X      = FWLiteSample.fromDAS("ST_tW_antitop_NoFullyHad_5f_pow_PS_F17_94X", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_incl_5f_pow_F17_94X               = FWLiteSample.fromDAS("ST_tW_antitop_incl_5f_pow_F17_94X", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_incl_5f_pow_PS_F17_94X            = FWLiteSample.fromDAS("ST_tW_antitop_incl_5f_pow_PS_F17_94X", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow_F17_94X             = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow_F17_94X", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow_PS_F17_94X          = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow_PS_F17_94X", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_incl_5f_pow_F17_94X                   = FWLiteSample.fromDAS("ST_tW_top_incl_5f_pow_F17_94X", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_incl_5f_pow_PS_F17_94X                = FWLiteSample.fromDAS("ST_tW_top_incl_5f_pow_PS_F17_94X", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tWll_5f_LO_S16_94X                           = FWLiteSample.fromDAS("ST_tWll_5f_LO_S16_94X", "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_5f = [
    ST_tchannel_antitop_5f_pow_PS_F17_94X,
    ST_tchannel_top_5f_pow_F17_94X,
    ST_tW_antitop_NoFullyHad_5f_pow_PS_F17_94X,
    ST_tW_antitop_incl_5f_pow_F17_94X,
    ST_tW_antitop_incl_5f_pow_PS_F17_94X,
    ST_tW_top_NoFullyHad_5f_pow_F17_94X,
    ST_tW_top_NoFullyHad_5f_pow_PS_F17_94X,
    ST_tW_top_incl_5f_pow_F17_94X,
    ST_tW_top_incl_5f_pow_PS_F17_94X,
    ST_tWll_5f_LO_S16_94X,

]

TTJets_NLO_F17_94X                              = FWLiteSample.fromDAS("TTJets_NLO_F17_94X", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_LO_F17_94X                               = FWLiteSample.fromDAS("TTJets_LO_F17_94X", "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromT_LO_F17_94X                  = FWLiteSample.fromDAS("TTJets_semilepFromT_LO_F17_94X", "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromTbar_LO_F17_94X               = FWLiteSample.fromDAS("TTJets_semilepFromTbar_LO_F17_94X", "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_dilep_LO_F17_94X                         = FWLiteSample.fromDAS("TTJets_dilep_LO_F17_94X", "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromT_genMET150_LO_F17_94X        = FWLiteSample.fromDAS("TTJets_semilepFromT_genMET150_LO_F17_94X", "/TTJets_SingleLeptFromT_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromTbar_genMET150_LO_F17_94X     = FWLiteSample.fromDAS("TTJets_semilepFromTbar_genMET150_LO_F17_94X", "/TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_dilep_genMET150_LO_F17_94X               = FWLiteSample.fromDAS("TTJets_dilep_genMET150_LO_F17_94X", "/TTJets_DiLept_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTo2L2Nu_pow_F17_94X                           = FWLiteSample.fromDAS("TTTo2L2Nu_pow_F17_94X", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow_PS_F17_94X                        = FWLiteSample.fromDAS("TTTo2L2Nu_pow_PS_F17_94X", "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow_F17_94X                        = FWLiteSample.fromDAS("TTToHadronic_pow_F17_94X", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow_PS_F17_94X                     = FWLiteSample.fromDAS("TTToHadronic_pow_PS_F17_94X", "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemiLeptonic_pow_F17_94X                    = FWLiteSample.fromDAS("TTToSemiLeptonic_pow_F17_94X", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemiLeptonic_pow_PS_F17_94X                 = FWLiteSample.fromDAS("TTToSemiLeptonic_pow_PS_F17_94X", "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets = [
    TTJets_NLO_F17_94X,
    TTJets_LO_F17_94X,
    TTJets_semilepFromT_LO_F17_94X,
    TTJets_semilepFromTbar_LO_F17_94X,
    TTJets_dilep_LO_F17_94X,
    TTJets_semilepFromT_genMET150_LO_F17_94X,
    TTJets_semilepFromTbar_genMET150_LO_F17_94X,
    TTJets_dilep_genMET150_LO_F17_94X,
    TTTo2L2Nu_pow_F17_94X,
    TTTo2L2Nu_pow_PS_F17_94X,
    TTToHadronic_pow_F17_94X,
    TTToHadronic_pow_PS_F17_94X,
    TTToSemiLeptonic_pow_F17_94X,
    TTToSemiLeptonic_pow_PS_F17_94X,
]

# t(t)g(g)
TGJets_NLO_F17_94X                              = FWLiteSample.fromDAS("TGJets_NLO_F17_94X", "/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TGJets_lep_NLO_PS_F17_94X                       = FWLiteSample.fromDAS("TGJets_lep_NLO_PS_F17_94X", "/TGJets_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGG_0Jets_NLO_F17_94X                          = FWLiteSample.fromDAS("TTGG_0Jets_NLO_F17_94X", "/TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGJets_NLO_F17_94X                             = FWLiteSample.fromDAS("TTGJets_NLO_F17_94X", "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_F17_94X                        = FWLiteSample.fromDAS("TTGamma_dilep_LO_F17_94X", "/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_had_LO_F17_94X                          = FWLiteSample.fromDAS("TTGamma_had_LO_F17_94X", "/TTGamma_Hadronic_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilepFromT_LO_F17_94X                 = FWLiteSample.fromDAS("TTGamma_semilepFromT_LO_F17_94X", "/TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilepFromTbar_LO_F17_94X              = FWLiteSample.fromDAS("TTGamma_semilepFromTbar_LO_F17_94X", "/TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTJ_LO_F17_94X                                 = FWLiteSample.fromDAS("TTTJ_LO_F17_94X", "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTT_NLO_F17_94X                                = FWLiteSample.fromDAS("TTTT_NLO_F17_94X", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTT_NLO_PS_F17_94X                             = FWLiteSample.fromDAS("TTTT_NLO_PS_F17_94X", "/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTW_LO_F17_94X                                 = FWLiteSample.fromDAS("TTTW_LO_F17_94X", "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToLNu_NLO_F17_94X                        = FWLiteSample.fromDAS("TTWJetsToLNu_NLO_F17_94X", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToLNu_NLO_PS_F17_94X                     = FWLiteSample.fromDAS("TTWJetsToLNu_NLO_PS_F17_94X", "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToQQ_NLO_F17_94X                         = FWLiteSample.fromDAS("TTWJetsToQQ_NLO_F17_94X", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJets_LO_F17_94X                              = FWLiteSample.fromDAS("TTWJets_LO_F17_94X", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJets_LO_F17_94X_ext1                         = FWLiteSample.fromDAS("TTWJets_LO_F17_94X_ext1", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLLNuNu_M10_NLO_F17_94X                     = FWLiteSample.fromDAS("TTZToLLNuNu_M10_NLO_F17_94X", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLL_M1to10_NLO_F17_94X                      = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO_F17_94X", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToQQ_NLO_F17_94X                             = FWLiteSample.fromDAS("TTZToQQ_NLO_F17_94X", "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZJets_LO_F17_94X                              = FWLiteSample.fromDAS("TTZJets_LO_F17_94X", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZJets_LO_F17_94X_ext1                         = FWLiteSample.fromDAS("TTZJets_LO_F17_94X_ext1", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_Zhad_Wlept_4f_NLO_F17_94X                   = FWLiteSample.fromDAS("TZQ_Zhad_Wlept_4f_NLO_F17_94X", "/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_ll_4f_NLO_F17_94X                           = FWLiteSample.fromDAS("TZQ_ll_4f_NLO_F17_94X", "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_nunu_4f_NLO_F17_94X                         = FWLiteSample.fromDAS("TZQ_nunu_4f_NLO_F17_94X", "/tZq_nunu_4f_ckm_NLO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THQ_Hincl_LO_F17_94X                            = FWLiteSample.fromDAS("THQ_Hincl_LO_F17_94X", "/THQ_4f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THW_Hincl_LO_F17_94X                            = FWLiteSample.fromDAS("THW_Hincl_LO_F17_94X", "/THW_5f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHToNonbb_pow_F17_94X                          = FWLiteSample.fromDAS("ttHToNonbb_pow_F17_94X", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_pow_F17_94X                             = FWLiteSample.fromDAS("ttHTobb_pow_F17_94X", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttH_pow_F17_94X                                 = FWLiteSample.fromDAS("ttH_pow_F17_94X", "/ttH_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTX = [
    TGJets_NLO_F17_94X,
    TGJets_lep_NLO_PS_F17_94X,
    TTGG_0Jets_NLO_F17_94X,
    TTGJets_NLO_F17_94X,
    TTGamma_dilep_LO_F17_94X,
    TTGamma_had_LO_F17_94X,
    TTGamma_semilepFromT_LO_F17_94X,
    TTGamma_semilepFromTbar_LO_F17_94X,
    TTTW_LO_F17_94X,
    TTWJetsToLNu_NLO_F17_94X,
    TTWJetsToLNu_NLO_PS_F17_94X,
    TTWJetsToQQ_NLO_F17_94X,
    TTWJets_LO_F17_94X,
    TTWJets_LO_F17_94X_ext1,
    TTZToLLNuNu_M10_NLO_F17_94X,
    TTZToLL_M1to10_NLO_F17_94X,
    TTZToQQ_NLO_F17_94X,
    TTZJets_LO_F17_94X,
    TTZJets_LO_F17_94X_ext1,
    TZQ_Zhad_Wlept_4f_NLO_F17_94X,
    TZQ_ll_4f_NLO_F17_94X,
    TZQ_nunu_4f_NLO_F17_94X,
    THQ_Hincl_LO_F17_94X,
    THW_Hincl_LO_F17_94X,
    ttHToNonbb_pow_F17_94X,
    ttHTobb_pow_F17_94X,
    ttH_pow_F17_94X,
    TTTJ_LO_F17_94X,
    TTTT_NLO_F17_94X,
    TTTT_NLO_PS_F17_94X,
]

TTHH_LO_F17_94X                                    = FWLiteSample.fromDAS("TTHH_LO_F17_94X", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZH_LO_F17_94X                                    = FWLiteSample.fromDAS("TTZH_LO_F17_94X", "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWH_LO_F17_94X                                    = FWLiteSample.fromDAS("TTWH_LO_F17_94X", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWW_LO_F17_94X                                    = FWLiteSample.fromDAS("TTWW_LO_F17_94X", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWZ_LO_F17_94X                                    = FWLiteSample.fromDAS("TTWZ_LO_F17_94X", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZZ_LO_F17_94X                                    = FWLiteSample.fromDAS("TTZZ_LO_F17_94X", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTVV = [
    TTHH_LO_F17_94X,
    TTZH_LO_F17_94X,
    TTWH_LO_F17_94X,
    TTWW_LO_F17_94X,
    TTWZ_LO_F17_94X,
    TTZZ_LO_F17_94X,
]

TTJets_HT600to800_LO_F17_94X                       = FWLiteSample.fromDAS("TTJets_HT600to800_LO_F17_94X", "/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_HT800to1200_LO_F17_94X                      = FWLiteSample.fromDAS("TTJets_HT800to1200_LO_F17_94X", "/TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_HT1200to2500_LO_F17_94X                     = FWLiteSample.fromDAS("TTJets_HT1200to2500_LO_F17_94X", "/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_HT2500toInf_LO_F17_94X                      = FWLiteSample.fromDAS("TTJets_HT2500toInf_LO_F17_94X", "/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets_HT = [
    TTJets_HT600to800_LO_F17_94X,
    TTJets_HT800to1200_LO_F17_94X,
    TTJets_HT1200to2500_LO_F17_94X,
    TTJets_HT2500toInf_LO_F17_94X,
]

WJetsToLNu_LO_F17_94X                          = FWLiteSample.fromDAS("WJetsToLNu_LO_F17_94X", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_LO_F17_94X_ext1                     = FWLiteSample.fromDAS("WJetsToLNu_LO_F17_94X_ext1", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJets = [
    WJetsToLNu_LO_F17_94X,
    WJetsToLNu_LO_F17_94X_ext1,
]

WJetsToLNu_HT100to200_LO_F17_94X                   = FWLiteSample.fromDAS("WJetsToLNu_HT100to200_LO_F17_94X", "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200to400_LO_F17_94X                   = FWLiteSample.fromDAS("WJetsToLNu_HT200to400_LO_F17_94X", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400to600_LO_F17_94X                   = FWLiteSample.fromDAS("WJetsToLNu_HT400to600_LO_F17_94X", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600to800_LO_F17_94X                   = FWLiteSample.fromDAS("WJetsToLNu_HT600to800_LO_F17_94X", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800to1200_LO_F17_94X                  = FWLiteSample.fromDAS("WJetsToLNu_HT800to1200_LO_F17_94X", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200to2500_LO_F17_94X                 = FWLiteSample.fromDAS("WJetsToLNu_HT1200to2500_LO_F17_94X", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500toInf_LO_F17_94X                  = FWLiteSample.fromDAS("WJetsToLNu_HT2500toInf_LO_F17_94X", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_HT = [
    WJetsToLNu_HT100to200_LO_F17_94X,
    WJetsToLNu_HT200to400_LO_F17_94X,
    WJetsToLNu_HT400to600_LO_F17_94X,
    WJetsToLNu_HT600to800_LO_F17_94X,
    WJetsToLNu_HT800to1200_LO_F17_94X,
    WJetsToLNu_HT1200to2500_LO_F17_94X,
    WJetsToLNu_HT2500toInf_LO_F17_94X,
]

VVTo2L2Nu_NLO_F17_94X                          = FWLiteSample.fromDAS("VVTo2L2Nu_NLO_F17_94X", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WW_DoubleScattering_F17_94X                    = FWLiteSample.fromDAS("WW_DoubleScattering_F17_94X", "/WW_DoubleScattering_13TeV-pythia8_TuneCP5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WW_F17_94X                                     = FWLiteSample.fromDAS("WW_F17_94X", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_F17_94X                                     = FWLiteSample.fromDAS("WZ_F17_94X", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ_F17_94X                                     = FWLiteSample.fromDAS("ZZ_F17_94X", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu_pow_PS_F17_94X                       = FWLiteSample.fromDAS("WWTo2L2Nu_pow_PS_F17_94X", "/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWToLNuQQ_pow_PS_F17_94X                       = FWLiteSample.fromDAS("WWToLNuQQ_pow_PS_F17_94X", "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WWTo4Q_pow_PS_F17_94X                          = FWLiteSample.fromDAS("WWTo4Q_pow_PS_F17_94X", "/WWTo4Q_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo1L1Nu2Q_NLO_F17_94X                        = FWLiteSample.fromDAS("WWTo1L1Nu2Q_NLO_F17_94X", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_NLO_F17_94X                           = FWLiteSample.fromDAS("WZTo3LNu_NLO_F17_94X", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2L2Q_NLO_F17_94X                           = FWLiteSample.fromDAS("WZTo2L2Q_NLO_F17_94X", "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L3Nu_NLO_F17_94X                          = FWLiteSample.fromDAS("WZTo1L3Nu_NLO_F17_94X", "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L1Nu2Q_NLO_F17_94X                        = FWLiteSample.fromDAS("WZTo1L1Nu2Q_NLO_F17_94X", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo2Q2Nu_NLO_F17_94X                          = FWLiteSample.fromDAS("ZZTo2Q2Nu_NLO_F17_94X", "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4l_pow_F17_94X                             = FWLiteSample.fromDAS("ZZTo4l_pow_F17_94X", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo4l_pow_F17_94X_ext1                        = FWLiteSample.fromDAS("ZZTo4l_NLO_F17_94X_ext1", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Q_NLO_F17_94X                           = FWLiteSample.fromDAS("ZZTo2L2Q_NLO_F17_94X", "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Nu_pow_F17_94X                          = FWLiteSample.fromDAS("ZZTo2L2Nu_pow_F17_94X", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO_F17_94X                            = FWLiteSample.fromDAS("WGToLNuG_LO_F17_94X", "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diboson = [
#    WW_DoubleScattering_F17_94X,
    VVTo2L2Nu_NLO_F17_94X,
    WW_F17_94X,
    WZ_F17_94X,
    ZZ_F17_94X,
    WWTo2L2Nu_pow_PS_F17_94X,
    WWToLNuQQ_pow_PS_F17_94X,
#    WWTo4Q_pow_PS_F17_94X,
    WWTo1L1Nu2Q_NLO_F17_94X,
    WZTo3LNu_NLO_F17_94X,
    WZTo2L2Q_NLO_F17_94X,
    WZTo1L3Nu_NLO_F17_94X,
    WZTo1L1Nu2Q_NLO_F17_94X,
#    ZZTo2Q2Nu_NLO_F17_94X,
    ZZTo4l_pow_F17_94X,
#    ZZTo4l_pow_F17_94X_ext1,
    ZZTo2L2Q_NLO_F17_94X,
    ZZTo2L2Nu_pow_F17_94X,
    WGToLNuG_LO_F17_94X,
]


WWW_NLO_F17_94X                                 = FWLiteSample.fromDAS("WWW_NLO_F17_94X", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWZ_NLO_F17_94X                                 = FWLiteSample.fromDAS("WWZ_NLO_F17_94X", "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZZ_NLO_F17_94X                                 = FWLiteSample.fromDAS("WZZ_NLO_F17_94X", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZZ_NLO_F17_94X                                 = FWLiteSample.fromDAS("ZZZ_NLO_F17_94X", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWG_NLO_F17_94X                                 = FWLiteSample.fromDAS("WWG_NLO_F17_94X", "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZG_NLO_F17_94X                                 = FWLiteSample.fromDAS("WZG_NLO_F17_94X", "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WWW_NLO_F17_94X,
    WWZ_NLO_F17_94X,
    WZZ_NLO_F17_94X,
    ZZZ_NLO_F17_94X,
    WWG_NLO_F17_94X,
    WZG_NLO_F17_94X,
]

GluGluToContinToZZTo4e_F17_94X      = FWLiteSample.fromDAS("GluGluToContinToZZTo4e_F17_94X", "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2mu_F17_94X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu_F17_94X", "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2tau_F17_94X  = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau_F17_94X", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4mu_F17_94X     = FWLiteSample.fromDAS("GluGluToContinToZZTo4mu_F17_94X", "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2tau_F17_94X = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2tau_F17_94X", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2nu_F17_94X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2nu_F17_94X", "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2nu_F17_94X  = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2nu_F17_94X", "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

gluglu = [
    GluGluToContinToZZTo4e_F17_94X,
    GluGluToContinToZZTo2e2mu_F17_94X,
    GluGluToContinToZZTo2e2tau_F17_94X,
    GluGluToContinToZZTo4mu_F17_94X,
    GluGluToContinToZZTo2mu2tau_F17_94X,
    GluGluToContinToZZTo2e2nu_F17_94X,
    GluGluToContinToZZTo2mu2nu_F17_94X,
]

## sum up
allSamples = DY + DY_HT + ST_4f + ST_5f + TTJets_HT + TTJets + TTX + TTVV + WJets + WJetsToLNu_HT + diboson + multiboson + gluglu

for sample in allSamples:
    sample.isData = False
