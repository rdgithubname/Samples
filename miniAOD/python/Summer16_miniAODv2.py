'''
miniAOD samples of Summer16 campaign, miniAODv2 (80X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*80X*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample


## DY
DYJetsToLL_M50_S16_80X_MLM_FS       = Sample("DYJetsToLL_M50_S16_80X_MLM_FS",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM")
DYJetsToLL_M50_S16_80X_MLM          = Sample("DYJetsToLL_M50_S16_80X_MLM",     "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM")

DY = [
    DYJetsToLL_M50_S16_80X_MLM_FS,
    DYJetsToLL_M50_S16_80X_MLM,
]

## TTJets

TTJets_S16_MLM_FS   = Sample("TTJets_S16_MLM_FS",   "/TTJets_13TeV-madgraphMLM/RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
TTJets_S16_MLM      = Sample("TTJets_S16_MLM",      "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")


top = [
    TTJets_S16_MLM_FS,
    TTJets_S16_MLM,
]


allSamples = DY + top

