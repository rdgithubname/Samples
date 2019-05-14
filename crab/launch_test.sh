## examples to launch. Remove dryrun to actually submit to crab
# Summer16 miniAODv3
python launch.py --config nano_mc_94X_Summer16_miniAODv3        --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Summer16_miniAODv3 --sample DYJetsToLL_M50_LO_ext1
# Fall17 miniAODv2
python launch.py --config nano_mc_94X_Fall17_miniAODv2          --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample DYJetsToLL_M10to50_HT100to200_NLO
# Autumn18 miniAODvconfig
python launch.py --config nano_mc_102X_Autumn18_miniAODv1       --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Autumn18_miniAODv1 --sample DYJetsToLL_M50_LO
# Run2016
python launch.py --config nano_data_94X_Run2016                 --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2016_17Jul2018  --sample DoubleMuon_Run2016C_17Jul2018
# Run2017
python launch.py --config nano_data_94X_Run2017                 --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2017_31Mar2018  --sample DoubleEG_Run2017C_31Mar2018
# Run2018 A->C
python launch.py --config nano_data_102X_Run2018_17Sep2018      --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_17Sep2018  --sample DoubleMuon_Run2018B_17Sep2018_v1
# Run2018 D
python launch.py --config nano_data_102X_Run2018_promptReco     --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample EGamma_Run2018D_promptReco_v2
