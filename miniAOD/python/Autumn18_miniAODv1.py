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


RelValTTbar                 = FWLiteSample.fromDAS("RelValTTbar", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
RelValTTbar_HEM             = FWLiteSample.fromDAS("RelValTTbar_HEM", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12HEfail_v1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
RelValTTbar_HEMmitigation   = FWLiteSample.fromDAS("RelValTTbar_HEMmitigation", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12HEfail_v1_badHcalMitig-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

relvals = [
    RelValTTbar,
    RelValTTbar_HEM,
    RelValTTbar_HEMmitigation,
]

DYJetsToLL_M50_NLO_A18_102X    = FWLiteSample.fromDAS("DYJetsToLL_M50_NLO_A18_102X", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
DYJetsToLL_M50_LO_A18_102X     = FWLiteSample.fromDAS("DYJetsToLL_M50_LO_A18_102X", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

DYJetsToLL_M10to50_LO_A18_102X = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO_A18_102X", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

DY = [
    DYJetsToLL_M50_NLO_A18_102X,
    DYJetsToLL_M50_LO_A18_102X,
    DYJetsToLL_M10to50_LO_A18_102X,
]

# single top
ST_schannel_LO_A18_102X         = FWLiteSample.fromDAS("ST_schannel_LO_A18_102X", "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

ST_tW_antitop_pow_A18_102X      = FWLiteSample.fromDAS("ST_tW_antitop_pow_A18_102X", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
ST_tW_top_pow_A18_102X          = FWLiteSample.fromDAS("ST_tW_top_pow_A18_102X", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

ST_tWll_LO_A18_102X             = FWLiteSample.fromDAS("ST_tWll_LO_A18_102X", "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)


singleTop = [
    ST_schannel_LO_A18_102X,
    ST_tW_antitop_pow_A18_102X,
    ST_tW_top_pow_A18_102X,
    ST_tWll_LO_A18_102X,
]

TT_dilep_NLO_A18_102X         = FWLiteSample.fromDAS("TT_dilep_NLO_A18_102X", "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTTo2L2Nu_pow_A18_102X        = FWLiteSample.fromDAS("TTTo2L2Nu_pow_A18_102X", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTToHadronic_pow_A18_102X     = FWLiteSample.fromDAS("TTToHadronic_pow_A18_102X", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTToSemiLeptonic_pow_A18_102X = FWLiteSample.fromDAS("TTToSemiLeptonic_pow_A18_102X", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-NZSFlatPU28to62_102X_upgrade2018_realistic_v15_ext5-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

TTJets = [
    TT_dilep_NLO_A18_102X,
    TTTo2L2Nu_pow_A18_102X,
    TTToHadronic_pow_A18_102X,
    TTToSemiLeptonic_pow_A18_102X,
]

TTGamma_Dilept_LO_A18_102X              = FWLiteSample.fromDAS("TTGamma_Dilept_LO_A18_102X", "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTGamma_SingleLeptFromT_LO_A18_102X     = FWLiteSample.fromDAS("TTGamma_SingleLeptFromT_LO_A18_102X", "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTGamma_SingleLeptFromTbar_LO_A18_102X  = FWLiteSample.fromDAS("TTGamma_SingleLeptFromTbar_LO_A18_102X", "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTGamma_Hadronic_LO_A18_102X            = FWLiteSample.fromDAS("TTGamma_Hadronic_LO_A18_102X", "/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)


TTWJetsToLNu_NLO_A18_102X   = FWLiteSample.fromDAS("TTWJetsToLNu_NLO_A18_102X", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTWJetsToQQ_NLO_A18_102X    = FWLiteSample.fromDAS("TTWJetsToQQ_NLO_A18_102X", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

TTZToLLNuNu_M10_NLO_A18_102X= FWLiteSample.fromDAS("TTZToLLNuNu_M10_NLO_A18_102X", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTZToLL_M1to10_NLO_A18_102X = FWLiteSample.fromDAS("TTZToLL_M1to10_NLO_A18_102X", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TZQ_LL_NLO_A18_102X         = FWLiteSample.fromDAS("TZQ_LL_NLO_A18_102X", "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

TTWJets_LO_A18_102X         = FWLiteSample.fromDAS("TTWJets_LO_A18_102X", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTZJets_LO_A18_102X         = FWLiteSample.fromDAS("TTZJets_LO_A18_102X", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

TTWW_LO_A18_102X            = FWLiteSample.fromDAS("TTWW_LO_A18_102X", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTWZ_LO_A18_102X            = FWLiteSample.fromDAS("TTWZ_LO_A18_102X", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTWH_LO_A18_102X            = FWLiteSample.fromDAS("TTWH_LO_A18_102X", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTHH_LO_A18_102X            = FWLiteSample.fromDAS("TTHH_LO_A18_102X", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
TTZZ_LO_A18_102X            = FWLiteSample.fromDAS("TTZZ_LO_A18_102X", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

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
    TTWW_LO_A18_102X,
    TTWZ_LO_A18_102X,
    TTWH_LO_A18_102X,
    TTHH_LO_A18_102X,
    TTZZ_LO_A18_102X,
]

WW_A18_102X                 = FWLiteSample.fromDAS("WW_A18_102X", "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
WZ_A18_102X                 = FWLiteSample.fromDAS("WZ_A18_102X", "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
ZZ_A18_102X                 = FWLiteSample.fromDAS("ZZ_A18_102X", "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
ZH_HToBB_ZToLL_pow_A18_102X = FWLiteSample.fromDAS("ZH_HToBB_ZToLL_pow_A18_102X", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

diboson = [
    WW_A18_102X,
    ZZ_A18_102X,
    ZH_HToBB_ZToLL_pow_A18_102X,
]

WWZ_NLO_A18_102X            = FWLiteSample.fromDAS("WWZ_NLO_A18_102X", "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
WZZ_NLO_A18_102X            = FWLiteSample.fromDAS("WZZ_NLO_A18_102X", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
ZZZ_NLO_A18_102X            = FWLiteSample.fromDAS("ZZZ_NLO_A18_102X", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

multiboson = [
    WWZ_NLO_A18_102X,
    WZZ_NLO_A18_102X,
    ZZZ_NLO_A18_102X,
]

GluGluToContinToZZTo2e2mu_A18_102X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2mu_A18_102X", "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
GluGluToContinToZZTo2e2tau_A18_102X  = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2tau_A18_102X", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
GluGluToContinToZZTo2e2nu_A18_102X   = FWLiteSample.fromDAS("GluGluToContinToZZTo2e2nu_A18_102X", "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

gluglu = [
    GluGluToContinToZZTo2e2mu_A18_102X,
    GluGluToContinToZZTo2e2tau_A18_102X,
    GluGluToContinToZZTo2e2nu_A18_102X,
]


allSamples = relvals + DY + singleTop + TTJets + TTX + diboson + multiboson + gluglu
