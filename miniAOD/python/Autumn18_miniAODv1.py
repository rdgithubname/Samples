'''
miniAOD samples of Autumn18 campaign, miniAOD (102X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIIAutumn18*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample

RelValTTbar                 = Sample("RelValTTbar",               "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12-v1/MINIAODSIM")
RelValTTbar_HEM             = Sample("RelValTTbar_HEM",           "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12HEfail_v1-v1/MINIAODSIM")
RelValTTbar_HEMmitigation   = Sample("RelValTTbar_HEMmitigation", "/RelValTTbar_13/CMSSW_10_2_4-PU25ns_102X_upgrade2018_realistic_v12HEfail_v1_badHcalMitig-v1/MINIAODSIM")

relvals = [
    RelValTTbar,
    RelValTTbar_HEM,
    RelValTTbar_HEMmitigation,
]

DYJetsToLL_M50_NLO_A18_102X    = Sample("DYJetsToLL_M50_NLO_A18_102X",      "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
DYJetsToLL_M50_LO_A18_102X     = Sample("DYJetsToLL_M50_LO_A18_102X",       "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")

DYJetsToLL_M10to50_LO_A18_102X = Sample("DYJetsToLL_M10to50_LO_A18_102X",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")

DY = [
    DYJetsToLL_M50_NLO_A18_102X,
    DYJetsToLL_M50_LO_A18_102X,
    DYJetsToLL_M10to50_LO_A18_102X,
]

# single top
ST_schannel_LO_A18_102X         = Sample("ST_schannel_LO_A18_102X",         "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM")

ST_tW_antitop_pow_A18_102X      = Sample("ST_tW_antitop_pow_A18_102X",      "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM")
ST_tW_top_pow_A18_102X          = Sample("ST_tW_top_pow_A18_102X",          "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM")

ST_tWll_LO_A18_102X             = Sample("ST_tWll_LO_A18_102X",             "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM")


singleTop = [
    ST_schannel_LO_A18_102X,
    ST_tW_antitop_pow_A18_102X,
    ST_tW_top_pow_A18_102X,
    ST_tWll_LO_A18_102X,
]

TT_dilep_NLO_A18_102X         = Sample("TT_dilep_NLO_A18_102X",         "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTTo2L2Nu_pow_A18_102X        = Sample("TTTo2L2Nu_pow_A18_102X",        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
TTToHadronic_pow_A18_102X     = Sample("TTToHadronic_pow_A18_102X",     "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
TTToSemiLeptonic_pow_A18_102X = Sample("TTToSemiLeptonic_pow_A18_102X", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-NZSFlatPU28to62_102X_upgrade2018_realistic_v15_ext5-v1/MINIAODSIM")

TTJets = [
    TT_dilep_NLO_A18_102X,
    TTTo2L2Nu_pow_A18_102X,
    TTToHadronic_pow_A18_102X,
    TTToSemiLeptonic_pow_A18_102X,
]

TTGamma_Dilept_LO_A18_102X              = Sample("TTGamma_Dilept_LO_A18_102X",              "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTGamma_SingleLeptFromT_LO_A18_102X     = Sample("TTGamma_SingleLeptFromT_LO_A18_102X",     "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTGamma_SingleLeptFromTbar_LO_A18_102X  = Sample("TTGamma_SingleLeptFromTbar_LO_A18_102X",  "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

TTWJetsToLNu_NLO_A18_102X   = Sample("TTWJetsToLNu_NLO_A18_102X",   "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTWJetsToQQ_NLO_A18_102X    = Sample("TTWJetsToQQ_NLO_A18_102X",    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")

TTZToLLNuNu_M10_NLO_A18_102X= Sample("TTZToLLNuNu_M10_NLO_A18_102X","/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTZToLL_M1to10_NLO_A18_102X = Sample("TTZToLL_M1to10_NLO_A18_102X", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
TZQ_LL_NLO_A18_102X         = Sample("TZQ_LL_NLO_A18_102X",         "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

TTWJets_LO_A18_102X         = Sample("TTWJets_LO_A18_102X",         "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTZJets_LO_A18_102X         = Sample("TTZJets_LO_A18_102X",         "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

TTWW_LO_A18_102X            = Sample("TTWW_LO_A18_102X",            "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTWZ_LO_A18_102X            = Sample("TTWZ_LO_A18_102X",            "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTWH_LO_A18_102X            = Sample("TTWH_LO_A18_102X",            "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTHH_LO_A18_102X            = Sample("TTHH_LO_A18_102X",            "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTZZ_LO_A18_102X            = Sample("TTZZ_LO_A18_102X",            "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

TTX = [
    TTGamma_Dilept_LO_A18_102X,
    TTGamma_SingleLeptFromT_LO_A18_102X,
    TTGamma_SingleLeptFromTbar_LO_A18_102X,
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

WW_A18_102X                 = Sample("WW_A18_102X",                 "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")
WZ_A18_102X                 = Sample("WZ_A18_102X",                 "/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM")
ZZ_A18_102X                 = Sample("ZZ_A18_102X",                 "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")
ZH_HToBB_ZToLL_pow_A18_102X = Sample("ZH_HToBB_ZToLL_pow_A18_102X", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")

diboson = [
    WW_A18_102X,
    ZZ_A18_102X,
    ZH_HToBB_ZToLL_pow_A18_102X,
]

WWZ_NLO_A18_102X            = Sample("WWZ_NLO_A18_102X", "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
WZZ_NLO_A18_102X            = Sample("WZZ_NLO_A18_102X", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
ZZZ_NLO_A18_102X            = Sample("ZZZ_NLO_A18_102X", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

multiboson = [
    WWZ_NLO_A18_102X,
    WZZ_NLO_A18_102X,
    ZZZ_NLO_A18_102X,
]

GluGluToContinToZZTo2e2mu_A18_102X   = Sample("GluGluToContinToZZTo2e2mu_A18_102X",  "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
GluGluToContinToZZTo2e2tau_A18_102X  = Sample("GluGluToContinToZZTo2e2tau_A18_102X", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
GluGluToContinToZZTo2e2nu_A18_102X   = Sample("GluGluToContinToZZTo2e2nu_A18_102X",  "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")

gluglu = [
    GluGluToContinToZZTo2e2mu_A18_102X,
    GluGluToContinToZZTo2e2tau_A18_102X,
    GluGluToContinToZZTo2e2nu_A18_102X,
]


allSamples = relvals + DY + singleTop + TTJets + TTX + diboson + multiboson + gluglu




