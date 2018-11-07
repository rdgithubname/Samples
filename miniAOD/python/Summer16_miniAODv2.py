'''
miniAOD samples of Summer16 campaign, miniAODv2 (80X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*80X*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample


## DY
DYJetsToLL_M50_MLM_FS_S16_80X       = Sample("DYJetsToLL_M50_MLM_FS_S16_80X",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")
DYJetsToLL_M50_MLM_S16_80X          = Sample("DYJetsToLL_M50_MLM_S16_80X",     "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM")

DY = [
    DYJetsToLL_M50_MLM_FS_S16_80X,
    DYJetsToLL_M50_MLM_S16_80X,
]

## TTJets

TTJets_MLM_FS_S16_80X   = Sample("TTJets_MLM_FS_S16_80X",   "/TTJets_13TeV-madgraphMLM/RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
TTJets_MLM_S16_80X      = Sample("TTJets_MLM_S16_80X",      "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")

TTTo2L2Nu_pow_S16_80X       = Sample("TTTo2L2Nu_pow_S16_80X",       "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
ST_tW_antitop_pow_S16_80X   = Sample("ST_tW_antitop_pow_S16_80X",   "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")
ST_tW_top_pow_S16_80X       = Sample("ST_tW_top_pow_S16_80X",       "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")
ST_schannel_amc_S16_80X     = Sample("ST_schannel_amc_S16_80X",     "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
ST_tchannel_amc_S16_80X     = Sample("ST_tchannel_amc_S16_80X",     "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")


top = [
    TTJets_MLM_FS_S16_80X,
    TTJets_MLM_S16_80X,
    TTTo2L2Nu_pow_S16_80X,
    ST_tW_antitop_pow_S16_80X,
    ST_tW_top_pow_S16_80X,
    ST_schannel_amc_S16_80X,
    ST_tchannel_amc_S16_80X,
]



WW_S16_80X      = Sample("WW_S16_80X",      "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
WW_ext_S16_80X  = Sample("WW_ext_S16_80X",  "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")
WZ_S16_80X      = Sample("WZ_S16_80X",      "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
WZ_ext_S16_80X  = Sample("WZ_ext_S16_80X",  "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")
ZZ_S16_80X      = Sample("ZZ_S16_80X",      "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
ZZ_ext_S16_80X  = Sample("ZZ_ext_S16_80X",  "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")

multiboson = [
    WW_S16_80X,
    WW_ext_S16_80X,
    WZ_S16_80X,
    WZ_ext_S16_80X,
    ZZ_S16_80X,
    ZZ_ext_S16_80X,
]

allSamples = DY + top + multiboson

