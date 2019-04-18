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

DYJetsToLL_M50_NLO_A18_102X    = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO_A18_102X", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_LO_A18_102X     = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_A18_102X", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M10to50_LO_A18_102X = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO_A18_102X", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M4to50_HT70to100_LO_A18_102X      = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT70to100_LO_A18_102X",      "/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) # https://cms-pdmv.cern.ch/pmp/historical?r=HIG-RunIIAutumn18MiniAOD-01083
DYJetsToLL_M4to50_HT100to200_LO_A18_102X     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT100to200_LO_A18_102X",     "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT200to400_LO_A18_102X     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT200to400_LO_A18_102X",     "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT400to600_LO_A18_102X     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT400to600_LO_A18_102X",     "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT600toInf_LO_A18_102X     = FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT600toInf_LO_A18_102X",     "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DYJetsToLL_M50_HT70to100_LO_A18_102X         = FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100_LO_A18_102X",         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200_LO_A18_102X        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200_LO_A18_102X",        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400_LO_A18_102X        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400_LO_A18_102X",        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_A18_102X        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_A18_102X",        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v7/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600_LO_A18_102X_ext2   = FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600_LO_A18_102X_ext2",   "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800_LO_A18_102X        = FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800_LO_A18_102X",        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200_LO_A18_102X       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200_LO_A18_102X",       "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500_LO_A18_102X      = FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500_LO_A18_102X",      "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True) # https://cms-pdmv.cern.ch/pmp/historical?r=B2G-RunIIAutumn18MiniAOD-00051
DYJetsToLL_M50_HT2500toInf_LO_A18_102X       = FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf_LO_A18_102X",       "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY_HT = [
    DYJetsToLL_M4to50_HT70to100_LO_A18_102X,
    DYJetsToLL_M4to50_HT100to200_LO_A18_102X,
    DYJetsToLL_M4to50_HT200to400_LO_A18_102X,
    DYJetsToLL_M4to50_HT400to600_LO_A18_102X,
    DYJetsToLL_M4to50_HT600toInf_LO_A18_102X,

    DYJetsToLL_M50_HT70to100_LO_A18_102X,
    DYJetsToLL_M50_HT100to200_LO_A18_102X,
    DYJetsToLL_M50_HT200to400_LO_A18_102X,
    DYJetsToLL_M50_HT400to600_LO_A18_102X,
    DYJetsToLL_M50_HT400to600_LO_A18_102X_ext2,
    DYJetsToLL_M50_HT600to800_LO_A18_102X,
    DYJetsToLL_M50_HT800to1200_LO_A18_102X,
    DYJetsToLL_M50_HT1200to2500_LO_A18_102X,
    DYJetsToLL_M50_HT2500toInf_LO_A18_102X,
]

DY = [
    DYJetsToLL_M50_NLO_A18_102X,
    DYJetsToLL_M50_LO_A18_102X,
    DYJetsToLL_M10to50_LO_A18_102X,
]

# single top
ST_schannel_LO_A18_102X             = FWLiteSample.fromDAS("ST_schannel_LO_A18_102X", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tchannel_antitop_4f_pow_A18_102X = FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow_A18_102X", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_top_4f_pow_A18_102X     = FWLiteSample.fromDAS("ST_tchannel_top_4f_pow_A18_102X", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tW_antitop_pow_A18_102X          = FWLiteSample.fromDAS("ST_tW_antitop_pow_A18_102X", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_pow_A18_102X              = FWLiteSample.fromDAS("ST_tW_top_pow_A18_102X", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ST_tWll_LO_A18_102X                 = FWLiteSample.fromDAS("ST_tWll_LO_A18_102X", "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TGJets_lep_NLO_A18_102X            = FWLiteSample.fromDAS("TGJets_lep_NLO_A18_102X", "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

singleTop = [
    ST_schannel_LO_A18_102X,
    ST_tchannel_antitop_4f_pow_A18_102X,
    ST_tchannel_top_4f_pow_A18_102X,
    ST_tW_antitop_pow_A18_102X,
    ST_tW_top_pow_A18_102X,
    ST_tWll_LO_A18_102X,
    TGJets_lep_NLO_A18_102X,
]

TT_dilep_NLO_A18_102X         = FWLiteSample.fromDAS("TT_dilep_NLO_A18_102X", "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTTo2L2Nu_pow_A18_102X        = FWLiteSample.fromDAS("TTTo2L2Nu_pow_A18_102X", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToHadronic_pow_A18_102X     = FWLiteSample.fromDAS("TTToHadronic_pow_A18_102X", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTToSemiLeptonic_pow_A18_102X = FWLiteSample.fromDAS("TTToSemiLeptonic_pow_A18_102X", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-NZSFlatPU28to62_102X_upgrade2018_realistic_v15_ext5-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTJets = [
    TT_dilep_NLO_A18_102X,
    TTTo2L2Nu_pow_A18_102X,
    TTToHadronic_pow_A18_102X,
    TTToSemiLeptonic_pow_A18_102X,
]

TTGamma_Dilept_LO_A18_102X              = FWLiteSample.fromDAS("TTGamma_Dilept_LO_A18_102X", "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_SingleLeptFromT_LO_A18_102X     = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_LO_A18_102X", "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_SingleLeptFromTbar_LO_A18_102X  = FWLiteSample.fromDAS("TTGamma_SingleLeptFromTbar_LO_A18_102X", "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTGamma_Hadronic_LO_A18_102X            = FWLiteSample.fromDAS("TTGamma_Hadronic_LO_A18_102X", "/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


TTWJetsToLNu_NLO_A18_102X   = FWLiteSample.fromDAS("TTWJetsToLNu_NLO_A18_102X", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWJetsToQQ_NLO_A18_102X    = FWLiteSample.fromDAS("TTWJetsToQQ_NLO_A18_102X", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTZToLLNuNu_M10_NLO_A18_102X= FWLiteSample.fromDAS("TTZToLLNuNu_M10_NLO_A18_102X", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZToLL_M1to10_NLO_A18_102X = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO_A18_102X", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TZQ_LL_NLO_A18_102X         = FWLiteSample.fromDAS("TZQ_LL_NLO_A18_102X", "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTWJets_LO_A18_102X         = FWLiteSample.fromDAS("TTWJets_LO_A18_102X", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZJets_LO_A18_102X         = FWLiteSample.fromDAS("TTZJets_LO_A18_102X", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ttHToNonbb_pow_A18_102X         = FWLiteSample.fromDAS("ttHToNonbb_pow_A18_102X",       "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_dilep_pow_A18_102X      = FWLiteSample.fromDAS("ttHTobb_dilep_pow_A18_102X",    "/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttHTobb_semilep_pow_A18_102X    = FWLiteSample.fromDAS("ttHTobb_semilep_pow_A18_102X",  "/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTWW_LO_A18_102X            = FWLiteSample.fromDAS("TTWW_LO_A18_102X", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWZ_LO_A18_102X            = FWLiteSample.fromDAS("TTWZ_LO_A18_102X", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTWH_LO_A18_102X            = FWLiteSample.fromDAS("TTWH_LO_A18_102X", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTHH_LO_A18_102X            = FWLiteSample.fromDAS("TTHH_LO_A18_102X", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTZZ_LO_A18_102X            = FWLiteSample.fromDAS("TTZZ_LO_A18_102X", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

TTX = [
    TTGamma_Dilept_LO_A18_102X,
    TTGamma_SingleLeptFromT_LO_A18_102X,
    TTGamma_SingleLeptFromTbar_LO_A18_102X,
    TTGamma_Hadronic_LO_A18_102X,
    TTWJetsToLNu_NLO_A18_102X,
    TTWJetsToQQ_NLO_A18_102X,
    TTZToLLNuNu_M10_NLO_A18_102X,
    TTZToLL_M1to10_NLO_A18_102X,
    TZQ_LL_NLO_A18_102X,
    TTWJets_LO_A18_102X,
    TTZJets_LO_A18_102X,
    ttHToNonbb_pow_A18_102X,
    ttHTobb_dilep_pow_A18_102X,
    ttHTobb_semilep_pow_A18_102X,
    TTWW_LO_A18_102X,
    TTWZ_LO_A18_102X,
    TTWH_LO_A18_102X,
    TTHH_LO_A18_102X,
    TTZZ_LO_A18_102X,
]

VVTo2L2Nu_NLO_A18_102X      = FWLiteSample.fromDAS("VVTo2L2Nu_NLO_A18_102X", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WW_A18_102X                 = FWLiteSample.fromDAS("WW_A18_102X", "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZ_A18_102X                 = FWLiteSample.fromDAS("WZ_A18_102X", "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZ_A18_102X                 = FWLiteSample.fromDAS("ZZ_A18_102X", "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZH_HToBB_ZToLL_pow_A18_102X = FWLiteSample.fromDAS("ZH_HToBB_ZToLL_pow_A18_102X", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WWTo1L1Nu2Q_A18_102X        = FWLiteSample.fromDAS("WWTo1L1Nu2Q_A18_102X",  "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo2L2Nu_A18_102X          = FWLiteSample.fromDAS("WWTo2L2Nu_A18_102X",    "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",          dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WZTo1L3Nu_A18_102X          = FWLiteSample.fromDAS("WZTo1L3Nu_A18_102X", "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2L2Q_A18_102X           = FWLiteSample.fromDAS("WZTo2L2Q_A18_102X",  "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",      dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_A18_102X           = FWLiteSample.fromDAS("WZTo3LNu_A18_102X",  "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZZTo2L2Nu_A18_102X          = FWLiteSample.fromDAS("ZZTo2L2Nu_A18_102X", "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",      dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2L2Q_A18_102X           = FWLiteSample.fromDAS("ZZTo2L2Q_A18_102X",  "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM",      dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4L_A18_102X             = FWLiteSample.fromDAS("ZZTo4L_A18_102X",    "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM",         dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZGTo2LG_NLO_A18_102X_ext1    = FWLiteSample.fromDAS("ZGTo2LG_NLO_A18_102X_ext1", "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WGToLNuG_LO_A18_102X         = FWLiteSample.fromDAS("WGToLNuG_LO_A18_102X", "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diboson = [
    VVTo2L2Nu_NLO_A18_102X,
    WW_A18_102X,
    WZ_A18_102X,
    ZZ_A18_102X,
    ZH_HToBB_ZToLL_pow_A18_102X,
    WWTo1L1Nu2Q_A18_102X,
    WWTo2L2Nu_A18_102X,
    WZTo1L3Nu_A18_102X,
    WZTo2L2Q_A18_102X,
    WZTo3LNu_A18_102X,
    ZZTo2L2Nu_A18_102X,
    ZZTo2L2Q_A18_102X,
    ZZTo4L_A18_102X,
    ZGTo2LG_NLO_A18_102X_ext1,
    WGToLNuG_LO_A18_102X,
]

WJetsToLNu_LO_A18_102X       = FWLiteSample.fromDAS("WJetsToLNu_LO_A18_102X", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJets = [
    WJetsToLNu_LO_A18_102X,
]

WWW_NLO_A18_102X            = FWLiteSample.fromDAS("WWW_NLO_A18_102X", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWZ_NLO_A18_102X            = FWLiteSample.fromDAS("WWZ_NLO_A18_102X", "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZZ_NLO_A18_102X            = FWLiteSample.fromDAS("WZZ_NLO_A18_102X", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZZ_NLO_A18_102X            = FWLiteSample.fromDAS("ZZZ_NLO_A18_102X", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

multiboson = [
    WWW_NLO_A18_102X,
    WWZ_NLO_A18_102X,
    WZZ_NLO_A18_102X,
    ZZZ_NLO_A18_102X,
]

GluGluToContinToZZTo2e2mu_A18_102X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu_A18_102X", "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2tau_A18_102X  = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau_A18_102X", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
GluGluToContinToZZTo2e2nu_A18_102X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2nu_A18_102X", "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

gluglu = [
    GluGluToContinToZZTo2e2mu_A18_102X,
    GluGluToContinToZZTo2e2tau_A18_102X,
    GluGluToContinToZZTo2e2nu_A18_102X,
]


allSamples = relvals + DY + DY_HT + singleTop + TTJets + TTX + diboson + multiboson + gluglu + WJets

for sample in allSamples:
    sample.isData = False
