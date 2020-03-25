#!/bin/sh

# Take the v5 recipes, updated GT and checked with McM and DAS
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD#Instructions_for_NanoAODv5_produ
# All recipes must be run in CMSSW_10_2_18

# 2016 RunIISummer16MiniAODv3 MC: (change era modifier if you run on RunIISummer16MiniAODv2 80X MiniAOD)
# from MCM: cmsDriver.py step1 --filein "dbs:/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM" --fileout file:SUS-RunIISummer16NanoAODv6-00803.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_mcRun2_asymptotic_v7 --step NANO --nThreads 2 --era Run2_2016,run2_nanoAOD_94X2016 --python_filename SUS-RunIISummer16NanoAODv6-00803_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 
cmsDriver.py nano_v6_mc_10218_Summer16_nThreads2 -s NANO --nThreads 2 --mc --eventcontent NANOAODSIM --datatier NANOAODSIM  -n 100 --no_exec  --conditions 102X_mcRun2_asymptotic_v7 --era  Run2_2016,run2_nanoAOD_94X2016 --filein /store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/100000/FA3C5CA2-BDC2-E811-9518-B496910A0290.root --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"

#Fall17
# from MCM: cmsDriver.py step1 --filein "dbs:/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" --fileout file:MUO-RunIIFall17NanoAODv6-00011.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_mc2017_realistic_v7 --step NANO --nThreads 2 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --python_filename MUO-RunIIFall17NanoAODv6-00011_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 
cmsDriver.py nano_v6_mc_10218_Fall17 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM  -n 100 --no_exec  --conditions 102X_mc2017_realistic_v7 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --filein /store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/910000/ECC11159-F647-E811-A157-001E67792510.root --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"

#Autumn18
# from MCM: cmsDriver.py step1 --filein "dbs:/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" --fileout file:MUO-RunIIAutumn18NanoAODv6-00021.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v20 --step NANO --nThreads 2 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename MUO-RunIIAutumn18NanoAODv6-00021_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 
cmsDriver.py nano_v6_mc_10218_Autumn18 -s NANO --filein "dbs:/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v20 --era Run2_2018,run2_nanoAOD_102Xv1 -n 100 --no_exec --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))" 

# 2016 data (Run2016*-17Jul2018*):
cmsDriver.py nano_v6_10218_Run2016 -s NANO --data --era Run2_2016,run2_nanoAOD_94X2016 --conditions 102X_dataRun2_v12 --eventcontent NANOAOD --datatier NANOAOD --filein /store/data/Run2016B/DoubleMuon/MINIAOD/17Jul2018_ver2-v1/40000/FEEBCC39-F38B-E811-ACEF-3417EBE50720.root -n 100 --no_exec --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"

# 2017 data
cmsDriver.py nano_v6_10218_Run2017 -s NANO --data --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --conditions 102X_dataRun2_v12 --eventcontent NANOAOD --datatier NANOAOD --filein /store/data/Run2017D/DoubleMuon/MINIAOD/31Mar2018-v1/90000/F4659A94-7D37-E811-9703-3417EBE47C5E.root -n 100 --no_exec --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"

#Run2018ABC
cmsDriver.py nano_v6_10218_Run2018ABC -s NANO --data --era Run2_2018,run2_nanoAOD_102Xv1 --conditions 102X_dataRun2_v12 --eventcontent NANOAOD --datatier NANOAOD --filein /store/data/Run2018C/DoubleMuon/MINIAOD/17Sep2018-v1/110000/2845D503-F499-B047-8DC0-EE1FF9B886E2.root -n 100 --no_exec --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"
#Run2018D
cmsDriver.py nano_v6_10218_Run2018D -s NANO --data --era Run2_2018,run2_nanoAOD_102Xv1 --conditions 102X_dataRun2_Prompt_v15 --eventcontent NANOAOD --datatier NANOAOD --filein /store/data/Run2018D/DoubleMuon/MINIAOD/PromptReco-v2/000/325/175/00000/ACD8ED9B-F9B0-AE44-B0FD-E20DAB363018.root -n 100 --no_exec --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"
