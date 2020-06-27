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
    argParser.add_argument('--logLevel',    action='store', default='INFO', help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])

    return argParser

# Logging
if __name__=="__main__":
    options = get_parser().parse_args()
    import Samples.Tools.logger as logger
    logger = logger.get_logger(options.logLevel, logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )
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
DYJetsToLL_M10to50_LO                  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

#DYJetsToLL_M10to50                     = FWLiteSample.fromDAS("DYJetsToLL_M10to50", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
#DYJetsToLL_M10to50_ext                 = FWLiteSample.fromDAS("DYJetsToLL_M10to50_ext", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM")

DYJetsToLL_M4to50_HT100to200_LO       = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT100to200_LO",         "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) # card says M5-50
DYJetsToLL_M4to50_HT100to200_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT100to200_LO_ext1",    "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) # card says M5-50
DYJetsToLL_M4to50_HT200to400_LO = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT200to400_new_pmx_LO",       "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) 
DYJetsToLL_M4to50_HT200to400_old_pmx_LO=FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT200to400_LO",         "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT200to400_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT200to400_LO_ext1",    "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT400to600_LO       = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT400to600_LO",         "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT400to600_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT400to600_LO_ext1",    "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT600toInf_LO       = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT600toInf_LO",         "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT600toInf_LO_ext1  = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT600toInf_LO_ext1",    "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

# high mass
DYJetsToLL_M50_NLO                     = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO",     "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO                      = FWLiteSample.fromDAS("DYJetsToLL_M50_LO",      "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_ext1                 = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_ext1", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_HT70to100_LO            = FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100_LO", "/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO_ext1      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO_ext1", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_ext1      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_ext1", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_ext1      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_ext1", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800_LO           = FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800_LO", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200_LO          = FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200_LO", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500_LO         = FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500_LO", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT2500toInf_LO          = FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf_LO", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY = [
#    DYJetsToLL_M10to50,
#    DYJetsToLL_M10to50_ext,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50_NLO,
    DYJetsToLL_M50_LO,
    DYJetsToLL_M50_LO_ext1,
]

DY_HT = [
    DYJetsToLL_M4to50_HT100to200_LO,
    DYJetsToLL_M4to50_HT100to200_LO_ext1,
    DYJetsToLL_M4to50_HT200to400_old_pmx_LO,
    DYJetsToLL_M4to50_HT200to400_LO,
    DYJetsToLL_M4to50_HT200to400_LO_ext1,
    DYJetsToLL_M4to50_HT400to600_LO,
    DYJetsToLL_M4to50_HT400to600_LO_ext1,
    DYJetsToLL_M4to50_HT600toInf_LO,
    DYJetsToLL_M4to50_HT600toInf_LO_ext1,
    DYJetsToLL_M50_HT70to100_LO,
    DYJetsToLL_M50_HT100to200_LO,
    DYJetsToLL_M50_HT100to200_LO_ext1,
    DYJetsToLL_M50_HT200to400_LO,
    DYJetsToLL_M50_HT200to400_LO_ext1,
    DYJetsToLL_M50_HT400to600_LO,
    DYJetsToLL_M50_HT400to600_LO_ext1,
    DYJetsToLL_M50_HT600to800_LO,
    DYJetsToLL_M50_HT800to1200_LO,
    DYJetsToLL_M50_HT1200to2500_LO,
    DYJetsToLL_M50_HT2500toInf_LO,
]

# single top
ST_schannel_4f_NLO                      = FWLiteSample.fromDAS("ST_schannel_4f_NLO", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_schannel_4f_NLO_PS                   = FWLiteSample.fromDAS("ST_schannel_4f_NLO_PS", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_4f_incl_pow         = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_incl_pow", "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_incl_pow             = FWLiteSample.fromDAS("ST_tchannel_top_4f_incl_pow", "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_4f = [ 
    ST_schannel_4f_NLO,
    ST_schannel_4f_NLO_PS,
    ST_tchannel_antitop_4f_incl_pow,
    ST_tchannel_top_4f_incl_pow,
]


ST_tchannel_antitop_5f_pow_PS           = FWLiteSample.fromDAS("ST_tchannel_antitop_5f_pow_PS", "/ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_5f_pow_PS_old_pmx   = FWLiteSample.fromDAS("ST_tchannel_antitop_5f_pow_PS_old_pmx", "/ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_5f_pow_old_pmx          = FWLiteSample.fromDAS("ST_tchannel_top_5f_pow_old_pmx", "/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_5f_pow                  = FWLiteSample.fromDAS("ST_tchannel_top_5f_pow", "/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_NoFullyHad_5f_pow_PS      = FWLiteSample.fromDAS("ST_tW_antitop_NoFullyHad_5f_pow_PS", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_incl_5f_pow               = FWLiteSample.fromDAS("ST_tW_antitop_incl_5f_pow", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_incl_5f_pow_PS            = FWLiteSample.fromDAS("ST_tW_antitop_incl_5f_pow_PS", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow             = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow_PS          = FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow_PS", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_incl_5f_pow                   = FWLiteSample.fromDAS("ST_tW_top_incl_5f_pow", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_incl_5f_pow_PS                = FWLiteSample.fromDAS("ST_tW_top_incl_5f_pow_PS", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tWll_5f_LO                           = FWLiteSample.fromDAS("ST_tWll_5f_LO",   "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tWnunu_5f_LO                         = FWLiteSample.fromDAS("ST_tWnunu_5f_LO", "/ST_tWnunu_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_5f = [
    ST_tchannel_antitop_5f_pow_PS,
    ST_tchannel_top_5f_pow,
    ST_tchannel_top_5f_pow_old_pmx,
    ST_tchannel_antitop_5f_pow_PS_old_pmx,
    ST_tW_antitop_NoFullyHad_5f_pow_PS,
    ST_tW_antitop_incl_5f_pow,
    ST_tW_antitop_incl_5f_pow_PS,
    ST_tW_top_NoFullyHad_5f_pow,
    ST_tW_top_NoFullyHad_5f_pow_PS,
    ST_tW_top_incl_5f_pow,
    ST_tW_top_incl_5f_pow_PS,
    ST_tWll_5f_LO,
    ST_tWnunu_5f_LO,
]

TTJets_NLO                              = FWLiteSample.fromDAS("TTJets_NLO", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_LO                               = FWLiteSample.fromDAS("TTJets_LO", "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromT_LO                  = FWLiteSample.fromDAS("TTJets_semilepFromT_LO", "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromTbar_LO               = FWLiteSample.fromDAS("TTJets_semilepFromTbar_LO", "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_dilep_LO                         = FWLiteSample.fromDAS("TTJets_dilep_LO", "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromT_genMET150_LO        = FWLiteSample.fromDAS("TTJets_semilepFromT_genMET150_LO", "/TTJets_SingleLeptFromT_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_semilepFromTbar_genMET150_LO     = FWLiteSample.fromDAS("TTJets_semilepFromTbar_genMET150_LO", "/TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_dilep_genMET150_LO               = FWLiteSample.fromDAS("TTJets_dilep_genMET150_LO", "/TTJets_DiLept_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTo2L2Nu_pow                           = FWLiteSample.fromDAS("TTTo2L2Nu_pow", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow_PS                        = FWLiteSample.fromDAS("TTTo2L2Nu_pow_PS", "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow                        = FWLiteSample.fromDAS("TTToHadronic_pow", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow_PS                     = FWLiteSample.fromDAS("TTToHadronic_pow_PS", "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemiLeptonic_pow                    = FWLiteSample.fromDAS("TTToSemiLeptonic_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemiLeptonic_pow_PS                 = FWLiteSample.fromDAS("TTToSemiLeptonic_pow_PS", "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets = [
    TTJets_NLO,
    TTJets_LO,
    TTJets_semilepFromT_LO,
    TTJets_semilepFromTbar_LO,
    TTJets_dilep_LO,
    TTJets_semilepFromT_genMET150_LO,
    TTJets_semilepFromTbar_genMET150_LO,
    TTJets_dilep_genMET150_LO,
    TTTo2L2Nu_pow,
    TTTo2L2Nu_pow_PS,
    TTToHadronic_pow,
    TTToHadronic_pow_PS,
    TTToSemiLeptonic_pow,
    TTToSemiLeptonic_pow_PS,
]

# t(t)g(g)
TGJets_NLO                              = FWLiteSample.fromDAS("TGJets_NLO", "/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TGJets_lep_NLO_PS                       = FWLiteSample.fromDAS("TGJets_lep_NLO_PS", "/TGJets_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGG_0Jets_NLO                          = FWLiteSample.fromDAS("TTGG_0Jets_NLO", "/TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGJets_NLO                             = FWLiteSample.fromDAS("TTGJets_NLO", "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTGamma_dilep_LO                        = FWLiteSample.fromDAS("TTGamma_dilep_LO",             "/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_TuneUp                 = FWLiteSample.fromDAS("TTGamma_dilep_LO_TuneUp",      "/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_TuneDown               = FWLiteSample.fromDAS("TTGamma_dilep_LO_TuneDown",    "/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_erdOn                  = FWLiteSample.fromDAS("TTGamma_dilep_LO_erdOn",       "/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_ptG100To200            = FWLiteSample.fromDAS("TTGamma_dilep_LO_ptG100To200", "/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_dilep_LO_ptG200                 = FWLiteSample.fromDAS("TTGamma_dilep_LO_ptG200",      "/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTGamma_had_LO                          = FWLiteSample.fromDAS("TTGamma_had_LO",              "/TTGamma_Hadronic_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_had_LO_ptG100To200              = FWLiteSample.fromDAS("TTGamma_had_LO_ptG100To200",  "/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_had_LO_ptG200                   = FWLiteSample.fromDAS("TTGamma_had_LO_ptG200",       "/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTGamma_semilep_LO                      = FWLiteSample.fromDAS("TTGamma_semilep_LO",             "/TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_TuneUp               = FWLiteSample.fromDAS("TTGamma_semilep_LO_TuneUp",      "/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_TuneDown             = FWLiteSample.fromDAS("TTGamma_semilep_LO_TuneDown",    "/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_erdOn                = FWLiteSample.fromDAS("TTGamma_semilep_LO_erdOn",       "/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_ptG100To200          = FWLiteSample.fromDAS("TTGamma_semilep_LO_ptG100To200", "/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_semilep_LO_ptG200               = FWLiteSample.fromDAS("TTGamma_semilep_LO_ptG200",      "/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTJ_LO                                 = FWLiteSample.fromDAS("TTTJ_LO", "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTT_NLO                                = FWLiteSample.fromDAS("TTTT_NLO", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTT_NLO_PS                             = FWLiteSample.fromDAS("TTTT_NLO_PS", "/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTW_LO                                 = FWLiteSample.fromDAS("TTTW_LO", "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToLNu_NLO                        = FWLiteSample.fromDAS("TTWJetsToLNu_NLO", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToLNu_NLO_PS                     = FWLiteSample.fromDAS("TTWJetsToLNu_NLO_PS", "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToQQ_NLO                         = FWLiteSample.fromDAS("TTWJetsToQQ_NLO", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJets_LO                              = FWLiteSample.fromDAS("TTWJets_LO", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJets_LO_ext1                         = FWLiteSample.fromDAS("TTWJets_LO_ext1", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLLNuNu_M10_NLO                     = FWLiteSample.fromDAS("TTZToLLNuNu_M10_NLO", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLL_M1to10_NLO                      = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToQQ_NLO                             = FWLiteSample.fromDAS("TTZToQQ_NLO", "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZJets_LO                              = FWLiteSample.fromDAS("TTZJets_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZJets_LO_ext1                         = FWLiteSample.fromDAS("TTZJets_LO_ext1", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_Zhad_Wlept_4f_NLO                   = FWLiteSample.fromDAS("TZQ_Zhad_Wlept_4f_NLO", "/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_ll_4f_NLO                           = FWLiteSample.fromDAS("TZQ_ll_4f_NLO", "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_nunu_4f_NLO                         = FWLiteSample.fromDAS("TZQ_nunu_4f_NLO", "/tZq_nunu_4f_ckm_NLO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THQ_Hincl_LO                            = FWLiteSample.fromDAS("THQ_Hincl_LO", "/THQ_4f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THW_Hincl_LO                            = FWLiteSample.fromDAS("THW_Hincl_LO", "/THW_5f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHToNonbb_pow                          = FWLiteSample.fromDAS("ttHToNonbb_pow", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_pow                             = FWLiteSample.fromDAS("ttHTobb_pow", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttH_pow                                 = FWLiteSample.fromDAS("ttH_pow", "/ttH_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTX = [
    TGJets_NLO,
    TGJets_lep_NLO_PS,
    TTGG_0Jets_NLO,
    TTGJets_NLO,
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
    TTTW_LO,
    TTWJetsToLNu_NLO,
    TTWJetsToLNu_NLO_PS,
    TTWJetsToQQ_NLO,
    TTWJets_LO,
    TTWJets_LO_ext1,
    TTZToLLNuNu_M10_NLO,
    TTZToLL_M1to10_NLO,
    TTZToQQ_NLO,
    TTZJets_LO,
    TTZJets_LO_ext1,
    TZQ_Zhad_Wlept_4f_NLO,
    TZQ_ll_4f_NLO,
    TZQ_nunu_4f_NLO,
    THQ_Hincl_LO,
    THW_Hincl_LO,
    ttHToNonbb_pow,
    ttHTobb_pow,
    ttH_pow,
    TTTJ_LO,
    TTTT_NLO,
    TTTT_NLO_PS,
]

TTHH_LO                                    = FWLiteSample.fromDAS("TTHH_LO", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZH_LO                                    = FWLiteSample.fromDAS("TTZH_LO", "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWH_LO                                    = FWLiteSample.fromDAS("TTWH_LO", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWW_LO                                    = FWLiteSample.fromDAS("TTWW_LO", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWZ_LO                                    = FWLiteSample.fromDAS("TTWZ_LO", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZZ_LO                                    = FWLiteSample.fromDAS("TTZZ_LO", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTVV = [
    TTHH_LO,
    TTZH_LO,
    TTWH_LO,
    TTWW_LO,
    TTWZ_LO,
    TTZZ_LO,
]

TTJets_HT600to800_LO                       = FWLiteSample.fromDAS("TTJets_HT600to800_LO", "/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_HT800to1200_LO                      = FWLiteSample.fromDAS("TTJets_HT800to1200_LO", "/TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_HT1200to2500_LO                     = FWLiteSample.fromDAS("TTJets_HT1200to2500_LO", "/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets_HT2500toInf_LO                      = FWLiteSample.fromDAS("TTJets_HT2500toInf_LO", "/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets_HT = [
    TTJets_HT600to800_LO,
    TTJets_HT800to1200_LO,
    TTJets_HT1200to2500_LO,
    TTJets_HT2500toInf_LO,
]

WJetsToLNu_LO                          = FWLiteSample.fromDAS("WJetsToLNu_LO", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_LO_ext1                     = FWLiteSample.fromDAS("WJetsToLNu_LO_ext1", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJets = [
    WJetsToLNu_LO,
    WJetsToLNu_LO_ext1,
]

WJetsToLNu_HT100to200_LO                   = FWLiteSample.fromDAS("WJetsToLNu_HT100to200_LO", "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200to400_LO                   = FWLiteSample.fromDAS("WJetsToLNu_HT200to400_LO", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400to600_LO                   = FWLiteSample.fromDAS("WJetsToLNu_HT400to600_LO", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600to800_LO                   = FWLiteSample.fromDAS("WJetsToLNu_HT600to800_LO", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800to1200_LO                  = FWLiteSample.fromDAS("WJetsToLNu_HT800to1200_LO", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200to2500_LO                 = FWLiteSample.fromDAS("WJetsToLNu_HT1200to2500_LO", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500toInf_LO                  = FWLiteSample.fromDAS("WJetsToLNu_HT2500toInf_LO", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_HT = [
    WJetsToLNu_HT100to200_LO,
    WJetsToLNu_HT200to400_LO,
    WJetsToLNu_HT400to600_LO,
    WJetsToLNu_HT600to800_LO,
    WJetsToLNu_HT800to1200_LO,
    WJetsToLNu_HT1200to2500_LO,
    WJetsToLNu_HT2500toInf_LO,
]

W1JetsToLNu_NuPt_200        = FWLiteSample.fromDAS("W1JetsToLNu_NuPt_200", "/W1JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W2JetsToLNu_NuPt_200        = FWLiteSample.fromDAS("W2JetsToLNu_NuPt_200", "/W2JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W3JetsToLNu_NuPt_200        = FWLiteSample.fromDAS("W3JetsToLNu_NuPt_200", "/W3JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W4JetsToLNu_NuPt_200        = FWLiteSample.fromDAS("W4JetsToLNu_NuPt_200", "/W4JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

W1JetsToLNu                 = FWLiteSample.fromDAS("W1JetsToLNu", "/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W2JetsToLNu                 = FWLiteSample.fromDAS("W2JetsToLNu", "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W3JetsToLNu                 = FWLiteSample.fromDAS("W3JetsToLNu", "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
W4JetsToLNu                 = FWLiteSample.fromDAS("W4JetsToLNu", "/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_0J_NLO           = FWLiteSample.fromDAS("WJetsToLNu_0J_NLO", "/WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_1J_NLO           = FWLiteSample.fromDAS("WJetsToLNu_1J_NLO", "/WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_2J_NLO           = FWLiteSample.fromDAS("WJetsToLNu_2J_NLO", "/WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsNJetBinned = [
    W1JetsToLNu_NuPt_200,
    W2JetsToLNu_NuPt_200,
    W3JetsToLNu_NuPt_200,
    W4JetsToLNu_NuPt_200,
    W1JetsToLNu,
    W2JetsToLNu,
    W3JetsToLNu,
    W4JetsToLNu,

    WJetsToLNu_0J_NLO,
    WJetsToLNu_1J_NLO,
    WJetsToLNu_2J_NLO,
    ]

ZJetsToNuNu_HT_100To200  = FWLiteSample.fromDAS("ZJetsToNuNu_HT_100To200", "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_200To400  = FWLiteSample.fromDAS("ZJetsToNuNu_HT_200To400", "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_400To600  = FWLiteSample.fromDAS("ZJetsToNuNu_HT_400To600", "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_600To800  = FWLiteSample.fromDAS("ZJetsToNuNu_HT_600To800", "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_800To1200 = FWLiteSample.fromDAS("ZJetsToNuNu_HT_800To1200", "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_1200To2500= FWLiteSample.fromDAS("ZJetsToNuNu_HT_1200To2500", "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT_2500ToInf = FWLiteSample.fromDAS("ZJetsToNuNu_HT_2500ToInf", "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


ZJetsToNuNu_HT = [
    ZJetsToNuNu_HT_100To200,
    ZJetsToNuNu_HT_200To400,
    ZJetsToNuNu_HT_400To600,
    ZJetsToNuNu_HT_600To800,
    ZJetsToNuNu_HT_800To1200,
    ZJetsToNuNu_HT_1200To2500,
    ZJetsToNuNu_HT_2500ToInf,
]


VVTo2L2Nu_NLO                          = FWLiteSample.fromDAS("VVTo2L2Nu_NLO", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WW_DoubleScattering                    = FWLiteSample.fromDAS("WW_DoubleScattering", "/WW_DoubleScattering_13TeV-pythia8_TuneCP5/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WW                                     = FWLiteSample.fromDAS("WW", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ                                     = FWLiteSample.fromDAS("WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_PU2017_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ                                     = FWLiteSample.fromDAS("ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu_pow_PS                       = FWLiteSample.fromDAS("WWTo2L2Nu_pow_PS", "/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWToLNuQQ_pow_PS                       = FWLiteSample.fromDAS("WWToLNuQQ_pow_PS", "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo4Q_pow                             = FWLiteSample.fromDAS("WWTo4Q_pow", "/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WWTo4Q_pow_PS                          = FWLiteSample.fromDAS("WWTo4Q_pow_PS", "/WWTo4Q_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo1L1Nu2Q_NLO                        = FWLiteSample.fromDAS("WWTo1L1Nu2Q_NLO", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_NLO                           = FWLiteSample.fromDAS("WZTo3LNu_NLO", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_pow                           = FWLiteSample.fromDAS("WZTo3LNu_pow", "/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2L2Q_NLO                           = FWLiteSample.fromDAS("WZTo2L2Q_NLO", "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L3Nu_NLO                          = FWLiteSample.fromDAS("WZTo1L3Nu_NLO", "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L1Nu2Q_NLO                        = FWLiteSample.fromDAS("WZTo1L1Nu2Q_NLO", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo2Q2Nu_NLO                          = FWLiteSample.fromDAS("ZZTo2Q2Nu_NLO", "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4l_pow                             = FWLiteSample.fromDAS("ZZTo4l_pow", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo4l_pow_ext1                        = FWLiteSample.fromDAS("ZZTo4l_NLO_ext1", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Q_NLO                           = FWLiteSample.fromDAS("ZZTo2L2Q_NLO", "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Nu_pow                          = FWLiteSample.fromDAS("ZZTo2L2Nu_pow", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2Q2Nu_NLO                          = FWLiteSample.fromDAS("ZZTo2Q2Nu_NLO", "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO                            = FWLiteSample.fromDAS("WGToLNuG_LO",  "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_NLO                           = FWLiteSample.fromDAS("WGToLNuG_NLO", "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZGToLLG_NLO                            = FWLiteSample.fromDAS("ZGToLLG_NLO",        "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZGToLLG_LoosePtlPtg_NLO                = FWLiteSample.fromDAS("ZGToLLG_LoosePtlPtg_NLO", "/ZGToLLG_01J_LoosePtlPtg_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZGToLLG_NLO_lowMLL                     = FWLiteSample.fromDAS("ZGToLLG_NLO_lowMLL", "/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diboson = [
#    WW_DoubleScattering,
    VVTo2L2Nu_NLO,
    WW,
    WZ,
    ZZ,
    WWTo2L2Nu_pow_PS,
    WWToLNuQQ_pow_PS,
#    WWTo4Q_pow_PS,
    WWTo1L1Nu2Q_NLO,
    WZTo3LNu_NLO,
    WZTo3LNu_pow,
    WZTo2L2Q_NLO,
    WZTo1L3Nu_NLO,
    WZTo1L1Nu2Q_NLO,
    WWTo4Q_pow,
#    ZZTo2Q2Nu_NLO,
    ZZTo4l_pow,
#    ZZTo4l_pow_ext1,
    ZZTo2L2Q_NLO,
    ZZTo2L2Nu_pow,
    ZZTo2Q2Nu_NLO,
    WGToLNuG_LO,
    WGToLNuG_NLO,
    ZGToLLG_NLO,
    ZGToLLG_LoosePtlPtg_NLO,
    ZGToLLG_NLO_lowMLL,
]


WWW_NLO                                 = FWLiteSample.fromDAS("WWW_NLO", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWZ_NLO                                 = FWLiteSample.fromDAS("WWZ_NLO", "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZZ_NLO                                 = FWLiteSample.fromDAS("WZZ_NLO", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZZ_NLO                                 = FWLiteSample.fromDAS("ZZZ_NLO", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWG_NLO                                 = FWLiteSample.fromDAS("WWG_NLO", "/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZG_NLO                                 = FWLiteSample.fromDAS("WZG_NLO", "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WWW_NLO,
    WWZ_NLO,
    WZZ_NLO,
    ZZZ_NLO,
    WWG_NLO,
    WZG_NLO,
]

QCD_Mu_pt15to20         = FWLiteSample.fromDAS("QCD_Mu_pt15to20",         "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt20to30         = FWLiteSample.fromDAS("QCD_Mu_pt20to30",         "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt30to50         = FWLiteSample.fromDAS("QCD_Mu_pt30to50",         "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt50to80         = FWLiteSample.fromDAS("QCD_Mu_pt50to80",         "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt80to120        = FWLiteSample.fromDAS("QCD_Mu_pt80to120",        "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt120to170       = FWLiteSample.fromDAS("QCD_Mu_pt120to170",       "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt170to300       = FWLiteSample.fromDAS("QCD_Mu_pt170to300",       "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt300to470       = FWLiteSample.fromDAS("QCD_Mu_pt300to470",       "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt470to600       = FWLiteSample.fromDAS("QCD_Mu_pt470to600",       "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt600to800       = FWLiteSample.fromDAS("QCD_Mu_pt600to800",       "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt800to1000      = FWLiteSample.fromDAS("QCD_Mu_pt800to1000",      "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt1000toInf      = FWLiteSample.fromDAS("QCD_Mu_pt1000toInf",      "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD_Ele_pt20to30        = FWLiteSample.fromDAS("QCD_Ele_pt20to30",        "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt30to50        = FWLiteSample.fromDAS("QCD_Ele_pt30to50",        "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt50to80        = FWLiteSample.fromDAS("QCD_Ele_pt50to80",        "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt80to120       = FWLiteSample.fromDAS("QCD_Ele_pt80to120",       "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt120to170      = FWLiteSample.fromDAS("QCD_Ele_pt120to170",      "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt170to300      = FWLiteSample.fromDAS("QCD_Ele_pt170to300",      "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Ele_pt300toInf      = FWLiteSample.fromDAS("QCD_Ele_pt300toInf",      "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD = [
        QCD_Mu_pt15to20,
        QCD_Mu_pt20to30,
        QCD_Mu_pt30to50,
        QCD_Mu_pt50to80,
        QCD_Mu_pt80to120,
        QCD_Mu_pt120to170,
        QCD_Mu_pt170to300,
        QCD_Mu_pt300to470,
        QCD_Mu_pt470to600,
        QCD_Mu_pt600to800,
        QCD_Mu_pt800to1000,
        QCD_Mu_pt1000toInf,

        QCD_Ele_pt20to30,
        QCD_Ele_pt30to50,
        QCD_Ele_pt50to80,
        QCD_Ele_pt80to120,
        QCD_Ele_pt120to170,
        QCD_Ele_pt170to300,
        QCD_Ele_pt300toInf,
]

QCD_bEnriched_HT100to200   = FWLiteSample.fromDAS("QCD_bEnriched_HT100to200",   "/QCD_bEnriched_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT200to300   = FWLiteSample.fromDAS("QCD_bEnriched_HT200to300",   "/QCD_bEnriched_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v5/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT300to500   = FWLiteSample.fromDAS("QCD_bEnriched_HT300to500",   "/QCD_bEnriched_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT500to700   = FWLiteSample.fromDAS("QCD_bEnriched_HT500to700",   "/QCD_bEnriched_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT700to1000  = FWLiteSample.fromDAS("QCD_bEnriched_HT700to1000",  "/QCD_bEnriched_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT1000to1500 = FWLiteSample.fromDAS("QCD_bEnriched_HT1000to1500", "/QCD_bEnriched_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT1500to2000 = FWLiteSample.fromDAS("QCD_bEnriched_HT1500to2000", "/QCD_bEnriched_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bEnriched_HT2000toInf  = FWLiteSample.fromDAS("QCD_bEnriched_HT2000toInf",  "/QCD_bEnriched_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD_b = [
        QCD_bEnriched_HT100to200  ,
        QCD_bEnriched_HT200to300  ,
        QCD_bEnriched_HT300to500  ,
        QCD_bEnriched_HT500to700  ,
        QCD_bEnriched_HT700to1000 ,
        QCD_bEnriched_HT1000to1500,
        QCD_bEnriched_HT1500to2000,
        QCD_bEnriched_HT2000toInf ,
]

GJets_HT40to100        = FWLiteSample.fromDAS("GJets_HT40to100",        "/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT100to200       = FWLiteSample.fromDAS("GJets_HT100to200",       "/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT200to400       = FWLiteSample.fromDAS("GJets_HT200to400",       "/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT400to600       = FWLiteSample.fromDAS("GJets_HT400to600",       "/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GJets_HT600toInf       = FWLiteSample.fromDAS("GJets_HT600toInf",       "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

GJetsHT = [
           GJets_HT40to100,
           GJets_HT100to200,
           GJets_HT200to400,
           GJets_HT400to600,
           GJets_HT600toInf,
]


GluGluHToZZTo4L             = FWLiteSample.fromDAS("GluGluHToZZTo4L",             "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4e      = FWLiteSample.fromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2mu   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2tau  = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4mu     = FWLiteSample.fromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2tau = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2nu   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2nu",   "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2nu  = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2nu",  "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4tau    = FWLiteSample.fromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

gluglu = [
    GluGluHToZZTo4L,
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo2e2nu,
    GluGluToContinToZZTo2mu2nu,
    GluGluToContinToZZTo4tau,
]

## SUSY signals

SMS_T2tt_mStop_650_mLSP_350 = FWLiteSample.fromDAS("SMS_T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_850_mLSP_100 = FWLiteSample.fromDAS("SMS_T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SMS_T2tt_3J_xqcut_20_mStop_175_mLSP_1   = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_175_mLSP_1",     "/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_50  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_50",    "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_75  = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_75",    "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_100 = FWLiteSample.fromDAS("SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_100",   "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T2tt_FullSim = [
    SMS_T2tt_mStop_650_mLSP_350,
    SMS_T2tt_mStop_850_mLSP_100,
    SMS_T2tt_3J_xqcut_20_mStop_175_mLSP_1  ,
    SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_50 ,
    SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_75 ,
    SMS_T2tt_3J_xqcut_20_mStop_250_mLSP_100,

    ]

ttH_HToInvisible = FWLiteSample.fromDAS("ttH_HToInvisible", "/ttH_HToInvisible_M125_13TeV_TuneCP5_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ttH = [ ttH_HToInvisible ]

## DM signals
TTbarDMJets_Dilepton_scalar         = FWLiteSample.fromDAS("TTbarDMJets_Dilepton_scalar", "/TTbarDMJets_Dilepton_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTbarDMJets_Dilepton_pseudoscalar   = FWLiteSample.fromDAS("TTbarDMJets_Dilepton_pseudiscalar", "/TTbarDMJets_Dilepton_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTbarDMJets_scalar         = FWLiteSample.fromDAS("TTbarDMJets_scalar", "/TTbarDMJets_Inclusive_scalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTbarDMJets_pseudoscalar   = FWLiteSample.fromDAS("TTbarDMJets_pseudiscalar", "/TTbarDMJets_Inclusive_pseudoscalar_LO_TuneCP5_13TeV-madgraph-mcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DM = [TTbarDMJets_Dilepton_scalar, TTbarDMJets_Dilepton_pseudoscalar, TTbarDMJets_scalar, TTbarDMJets_pseudoscalar]

## sum up
allSamples = DY + DY_HT + ST_4f + ST_5f + TTJets_HT + TTJets + TTX + TTVV + WJets + WJetsToLNu_HT + WJetsNJetBinned + ZJetsToNuNu_HT + diboson + multiboson + gluglu + QCD + GJetsHT + T2tt_FullSim + ttH + DM

for sample in allSamples:
    sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
