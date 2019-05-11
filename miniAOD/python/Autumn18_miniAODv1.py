'''
miniAOD samples of Autumn18 campaign, miniAOD (102X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIIAutumn18*/MINIAODSIM"
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
dbFile = dbDir+"DB_Autumn18_miniAODv1.sql"

logger.info("Using db file: %s", dbFile)

RelValTTbar                 = FWLiteSample.fromDAS("RelValTTbar", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
RelValTTbar_HEM             = FWLiteSample.fromDAS("RelValTTbar_HEM", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12HEfail_v1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
RelValTTbar_HEMmitigation   = FWLiteSample.fromDAS("RelValTTbar_HEMmitigation", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12HEfail_v1_badHcalMitig-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

relvals = [
    RelValTTbar,
    RelValTTbar_HEM,
    RelValTTbar_HEMmitigation,
]

DYJetsToLL_M50_NLO    = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO     = FWLiteSample.fromDAS("DYJetsToLL_M50_LO", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M10to50_LO = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M4to50_HT70to100_LO      = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT70to100_LO",      "/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) # https://cms-pdmv.cern.ch/pmp/historical?r=HIG-RunIIAutumn18MiniAOD-01083
DYJetsToLL_M4to50_HT100to200_LO     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT100to200_LO",     "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT200to400_LO     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT200to400_LO",     "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT400to600_LO     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT400to600_LO",     "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT600toInf_LO     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT600toInf_LO",     "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_HT70to100_LO         = FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100_LO",         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO",        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO",        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO",        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v7/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_ext2   = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_ext2",   "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800_LO        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800_LO",        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200_LO       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200_LO",       "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500_LO      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500_LO",      "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) # https://cms-pdmv.cern.ch/pmp/historical?r=B2G-RunIIAutumn18MiniAOD-00051
DYJetsToLL_M50_HT2500toInf_LO       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf_LO",       "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY_HT = [
    DYJetsToLL_M4to50_HT70to100_LO,
    DYJetsToLL_M4to50_HT100to200_LO,
    DYJetsToLL_M4to50_HT200to400_LO,
    DYJetsToLL_M4to50_HT400to600_LO,
    DYJetsToLL_M4to50_HT600toInf_LO,

    DYJetsToLL_M50_HT70to100_LO,
    DYJetsToLL_M50_HT100to200_LO,
    DYJetsToLL_M50_HT200to400_LO,
    DYJetsToLL_M50_HT400to600_LO,
    DYJetsToLL_M50_HT400to600_LO_ext2,
    DYJetsToLL_M50_HT600to800_LO,
    DYJetsToLL_M50_HT800to1200_LO,
    DYJetsToLL_M50_HT1200to2500_LO,
    DYJetsToLL_M50_HT2500toInf_LO,
]

DY = [
    DYJetsToLL_M50_NLO,
    DYJetsToLL_M50_LO,
    DYJetsToLL_M10to50_LO,
]

# single top
ST_schannel_LO             = FWLiteSample.fromDAS("ST_schannel_LO", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tchannel_antitop_4f_pow = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_pow     = FWLiteSample.fromDAS("ST_tchannel_top_4f_pow", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tW_antitop_pow          = FWLiteSample.fromDAS("ST_tW_antitop_pow", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_pow              = FWLiteSample.fromDAS("ST_tW_top_pow", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tWll_LO                 = FWLiteSample.fromDAS("ST_tWll_LO",   "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tWnunu_LO               = FWLiteSample.fromDAS("ST_tWnunu_LO", "/ST_tWnunu_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TGJets_lep_NLO            = FWLiteSample.fromDAS("TGJets_lep_NLO", "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

singleTop = [
    ST_schannel_LO,
    ST_tchannel_antitop_4f_pow,
    ST_tchannel_top_4f_pow,
    ST_tW_antitop_pow,
    ST_tW_top_pow,
    ST_tWll_LO,
    ST_tWnunu_LO,
    TGJets_lep_NLO,
]

TT_LO                = FWLiteSample.fromDAS("TT_LO", "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TT_dilep_NLO         = FWLiteSample.fromDAS("TT_dilep_NLO", "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow        = FWLiteSample.fromDAS("TTTo2L2Nu_pow", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow     = FWLiteSample.fromDAS("TTToHadronic_pow", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemiLeptonic_pow = FWLiteSample.fromDAS("TTToSemiLeptonic_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-NZSFlatPU28to62_102X_upgrade2018_realistic_v15_ext5-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets = [
    TT_LO,
    TT_dilep_NLO,
    TTTo2L2Nu_pow,
    TTToHadronic_pow,
    TTToSemiLeptonic_pow,
]

TTGamma_Dilept_LO              = FWLiteSample.fromDAS("TTGamma_Dilept_LO", "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_SingleLeptFromT_LO     = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_LO", "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_SingleLeptFromTbar_LO  = FWLiteSample.fromDAS("TTGamma_SingleLeptFromTbar_LO", "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_Hadronic_LO            = FWLiteSample.fromDAS("TTGamma_Hadronic_LO", "/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


TTWJetsToLNu_NLO   = FWLiteSample.fromDAS("TTWJetsToLNu_NLO", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToQQ_NLO    = FWLiteSample.fromDAS("TTWJetsToQQ_NLO", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTZToLLNuNu_M10_NLO= FWLiteSample.fromDAS("TTZToLLNuNu_M10_NLO", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLL_M1to10_NLO = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_LL_NLO         = FWLiteSample.fromDAS("TZQ_LL_NLO", "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTWJets_LO         = FWLiteSample.fromDAS("TTWJets_LO", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZJets_LO         = FWLiteSample.fromDAS("TTZJets_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ttHToNonbb_pow         = FWLiteSample.fromDAS("ttHToNonbb_pow",       "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_dilep_pow      = FWLiteSample.fromDAS("ttHTobb_dilep_pow",    "/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_semilep_pow    = FWLiteSample.fromDAS("ttHTobb_semilep_pow",  "/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

THQ_Hincl_LO       = FWLiteSample.fromDAS("THQ_Hincl_LO", "/THQ_4f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
THW_Hincl_LO       = FWLiteSample.fromDAS("THW_Hincl_LO", "/THW_5f_Hincl_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTWW_LO            = FWLiteSample.fromDAS("TTWW_LO", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWZ_LO            = FWLiteSample.fromDAS("TTWZ_LO", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWH_LO            = FWLiteSample.fromDAS("TTWH_LO", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTHH_LO            = FWLiteSample.fromDAS("TTHH_LO", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZZ_LO            = FWLiteSample.fromDAS("TTZZ_LO", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTTT_NLO           = FWLiteSample.fromDAS("TTTT_NLO", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTX = [
    TTGamma_Dilept_LO,
    TTGamma_SingleLeptFromT_LO,
    TTGamma_SingleLeptFromTbar_LO,
    TTGamma_Hadronic_LO,
    TTWJetsToLNu_NLO,
    TTWJetsToQQ_NLO,
    TTZToLLNuNu_M10_NLO,
    TTZToLL_M1to10_NLO,
    TZQ_LL_NLO,
    TTWJets_LO,
    TTZJets_LO,
    ttHToNonbb_pow,
    ttHTobb_dilep_pow,
    ttHTobb_semilep_pow,
    THQ_Hincl_LO,
    THW_Hincl_LO,
    TTWW_LO,
    TTWZ_LO,
    TTWH_LO,
    TTHH_LO,
    TTZZ_LO,
    TTTT_NLO,
]

VVTo2L2Nu_NLO      = FWLiteSample.fromDAS("VVTo2L2Nu_NLO", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WW                 = FWLiteSample.fromDAS("WW", "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ                 = FWLiteSample.fromDAS("WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ                 = FWLiteSample.fromDAS("ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZH_HToBB_ZToLL_pow = FWLiteSample.fromDAS("ZH_HToBB_ZToLL_pow", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WWTo1L1Nu2Q                = FWLiteSample.fromDAS("WWTo1L1Nu2Q",  "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu_DoubleScattering = FWLiteSample.fromDAS("WWTo2L2Nu_DoubleScattering",    "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu                  = FWLiteSample.fromDAS("WWTo2L2Nu",    "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWToLNuQQ                  = FWLiteSample.fromDAS("WWToLNuQQ",    "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WZTo1L3Nu          = FWLiteSample.fromDAS("WZTo1L3Nu",     "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2L2Q           = FWLiteSample.fromDAS("WZTo2L2Q",      "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",      dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu           = FWLiteSample.fromDAS("WZTo3LNu",      "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_pow       = FWLiteSample.fromDAS("WZTo3LNu_pow",  "/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZZTo2L2Nu          = FWLiteSample.fromDAS("ZZTo2L2Nu", "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Q           = FWLiteSample.fromDAS("ZZTo2L2Q",  "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2Q2Nu          = FWLiteSample.fromDAS("ZZTo2Q2Nu", "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4L             = FWLiteSample.fromDAS("ZZTo4L",    "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",             dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZGTo2LG_NLO_ext1    = FWLiteSample.fromDAS("ZGTo2LG_NLO_ext1", "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO         = FWLiteSample.fromDAS("WGToLNuG_LO",  "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_NLO        = FWLiteSample.fromDAS("WGToLNuG_NLO", "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diboson = [
    VVTo2L2Nu_NLO,
    WW,
    WZ,
    ZZ,
    ZH_HToBB_ZToLL_pow,
    WWTo1L1Nu2Q,
    WWTo2L2Nu,
    WWToLNuQQ,
    WZTo1L3Nu,
    WZTo2L2Q,
    WZTo3LNu,
    WZTo3LNu_pow,
    ZZTo2L2Nu,
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo4L,
    ZGTo2LG_NLO_ext1,
    WGToLNuG_LO,
    WGToLNuG_NLO,
]

WJetsToLNu_LO       = FWLiteSample.fromDAS("WJetsToLNu_LO", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJets = [
    WJetsToLNu_LO,
]

WWW_NLO            = FWLiteSample.fromDAS("WWW_NLO", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWZ_NLO            = FWLiteSample.fromDAS("WWZ_NLO", "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZZ_NLO            = FWLiteSample.fromDAS("WZZ_NLO", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZZ_NLO            = FWLiteSample.fromDAS("ZZZ_NLO", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WWW_NLO,
    WWZ_NLO,
    WZZ_NLO,
    ZZZ_NLO,
]

GluGluHToZZTo4L              = FWLiteSample.fromDAS("GluGluHToZZTo4L",             "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2mu    = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2tau   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2nu    = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2nu",   "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2mu2tau  = FWLiteSample.fromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4e       = FWLiteSample.fromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4mu      = FWLiteSample.fromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo4tau     = FWLiteSample.fromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

gluglu = [
    GluGluHToZZTo4L,
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
    GluGluToContinToZZTo2e2nu,
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo4tau,
]


allSamples = relvals + DY + DY_HT + singleTop + TTJets + TTX + diboson + multiboson + gluglu + WJets

for sample in allSamples:
    sample.isData = False

