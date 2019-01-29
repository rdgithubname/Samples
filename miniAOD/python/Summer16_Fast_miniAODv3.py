'''
miniAOD FastSim samples of Summer16 campaign, miniAODv3 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16MiniAODv3*Fast*/MINIAODSIM"
'''

from Samples.Tools.Sample import Sample

## T2tt
SMS_T2tt_mStop_150to250     = Sample("SMS_T2tt_mStop_150to250"  ,   "/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM")
SMS_T2tt_mStop_250to350     = Sample("SMS_T2tt_mStop_250to350"  ,   "/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM")
SMS_T2tt_mStop_350to400     = Sample("SMS_T2tt_mStop_350to400"  ,   "/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM")
SMS_T2tt_mStop_400to1200    = Sample("SMS_T2tt_mStop_400to1200" ,   "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM")
SMS_T2tt_mStop_1200to2000   = Sample("SMS_T2tt_mStop_1200to2000",   "/SMS-T2tt_mStop-1200to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM")

T2tt = [
    SMS_T2tt_mStop_150to250  ,
    SMS_T2tt_mStop_250to350  ,
    SMS_T2tt_mStop_350to400  ,
    SMS_T2tt_mStop_400to1200 ,
    SMS_T2tt_mStop_1200to2000,
    ]


## sum up
allSamples = T2tt

