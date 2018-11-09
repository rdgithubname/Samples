'''
miniAOD samples of Fall17 campaign, miniAODv2 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16MiniAODv2*80X*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample


## DY
DYJetsToLL_M50_MLM_F17_94X          = Sample("DYJetsToLL_M50_MLM_F17_94X",     "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")

DY = [
    DYJetsToLL_M50_MLM_F17_94X,
]

## TTJets

TTTo2L2Nu_pow_F17_94X           = Sample("TTTo2L2Nu_pow_F17_94X",           "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
TTTo2L2Nu_pow_PS_F17_94X        = Sample("TTTo2L2Nu_pow_PS_F17_94X",        "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
ST_tW_antitop_pow_F17_94X       = Sample("ST_tW_antitop_pow_F17_94X",       "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
ST_tW_top_pow_F17_94X           = Sample("ST_tW_top_pow_F17_94X",           "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
ST_schannel_amc_F17_94X         = Sample("ST_schannel_amc_F17_94X",         "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
ST_tchannel_antitop_pow_F17_94X = Sample("ST_tchannel_antitop_pow_F17_94X", "/ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
ST_tchannel_top_pow_F17_94X     = Sample("ST_tchannel_top_pow_F17_94X",     "/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")


top = [
    TTTo2L2Nu_pow_F17_94X,
    TTTo2L2Nu_pow_PS_F17_94X,
    ST_tW_antitop_pow_F17_94X,
    ST_tW_top_pow_F17_94X,
    ST_schannel_amc_F17_94X,
    ST_tchannel_antitop_pow_F17_94X,
    ST_tchannel_top_pow_F17_94X,
]



WW_F17_94X      = Sample("WW_F17_94X",      "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
WZ_F17_94X      = Sample("WZ_F17_94X",      "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
ZZ_F17_94X      = Sample("ZZ_F17_94X",      "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")

multiboson = [
    WW_F17_94X,
    WZ_F17_94X,
    ZZ_F17_94X,
]

allSamples = DY + top + multiboson

