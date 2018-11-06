'''
miniAOD samples of Summer16 campaign, miniAODv3 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*94X*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample


## DY
DYJetsToLL_M50_S16_94X_MLM      = Sample("DYJetsToLL_M50_S16_94X_MLM",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM") #50M
DYJetsToLL_M50_S16_94X_FxFx     = Sample("DYJetsToLL_M50_S16_94X_FxFx", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM") #121M

DY = [
    DYJetsToLL_M50_S16_94X_MLM,
    DYJetsToLL_M50_S16_94X_FxFx
]

## TTJets
TTTo2L2Nu_noSC_S16_94X_pow      = Sample("TTTo2L2Nu_noSC_S16_94X_pow", "/TTTo2L2Nu_noSC_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM")

top = [
    TTTo2L2Nu_noSC_S16_94X_pow,
]


allSamples = DY + top

