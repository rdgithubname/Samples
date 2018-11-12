'''
miniAOD samples of Summer16 campaign, miniAODv2 (80X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*80X*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample


## DY
SMS_T2tt_mStop400to1200_FS_S16_80X       = Sample("SMS_T2tt_mStop400to1200_FS_S16_80X",  "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM")


signals = [
    SMS_T2tt_mStop400to1200_FS_S16_80X,
]

allSamples = signals

