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

DYJetsToLL_M50_FXFX_A18_102X    = Sample("DYJetsToLL_M50_FXFX_A18_102X", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
DYJetsToLL_M50_MLM_A18_102X     = Sample("DYJetsToLL_M50_MLM_A18_102X",  "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")

DY = [
    DYJetsToLL_M50_FXFX_A18_102X,
    DYJetsToLL_M50_MLM_A18_102X,
]

TT_DiLept_amc_A18_102X        = Sample("TT_DiLept_amc_A18_102X",        "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTTo2L2Nu_pow_A18_102X        = Sample("TTTo2L2Nu_pow_A18_102X",        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
TTToHadronic_pow_A18_102X     = Sample("TTToHadronic_pow_A18_102X",     "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
TTToSemiLeptonic_pow_A18_102X = Sample("TTToSemiLeptonic_pow_A18_102X", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-NZSFlatPU28to62_102X_upgrade2018_realistic_v15_ext5-v1/MINIAODSIM")
ST_schannel_A18_102X          = Sample("ST_schannel_A18_102X",          "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1/MINIAODSIM")
TTWZ_A18_102X                 = Sample("TTWZ_A18_102X",                 "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTHH_A18_102X                 = Sample("TTHH_A18_102X",                 "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
TTZZ_A18_102X                 = Sample("TTZZ_A18_102X",                 "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

top = [
    TT_DiLept_amc_A18_102X,
    TTTo2L2Nu_pow_A18_102X,
    TTToHadronic_pow_A18_102X,
    TTToSemiLeptonic_pow_A18_102X,
    ST_schannel_A18_102X,
    TTWZ_A18_102X,
    TTHH_A18_102X,
    TTZZ_A18_102X,
]

WW_A18_102X             = Sample("WW_A18_102X", "/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")
ZZ_A18_102X             = Sample("ZZ_A18_102X", "/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")
ZH_HToBB_ZToLL_A18_102X = Sample("ZH_HToBB_ZToLL_A18_102X", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM")

diboson = [
    WW_A18_102X,
    ZZ_A18_102X,
    ZH_HToBB_ZToLL_A18_102X,
]

WWZ_A18_102X            = Sample("WWZ_A18_102X", "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
WZZ_A18_102X            = Sample("WZZ_A18_102X", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")
ZZZ_A18_102X            = Sample("ZZZ_A18_102X", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM")

multiboson = [
    WWZ_A18_102X,
    WZZ_A18_102X,
    ZZZ_A18_102X,
]

GluGluToContinToZZTo2e2mu_A18_102X   = Sample("GluGluToContinToZZTo2e2mu_A18_102X",  "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
GluGluToContinToZZTo2e2tau_A18_102X  = Sample("GluGluToContinToZZTo2e2tau_A18_102X", "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
GluGluToContinToZZTo2e2nu_A18_102X   = Sample("GluGluToContinToZZTo2e2nu_A18_102X",  "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM")

gluglu = [
    GluGluToContinToZZTo2e2mu_A18_102X,
    GluGluToContinToZZTo2e2tau_A18_102X,
    GluGluToContinToZZTo2e2nu_A18_102X,
]


allSamples = relvals + DY + top + diboson + multiboson + gluglu




