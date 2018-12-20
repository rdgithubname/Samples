## examples to launch. Remove dryrun to actually submit to crab

# Summer16 miniAODv3
python launch.py --era mc_94X_Summer16_miniAODv3        --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample DYJetsToLL_M50_MLM_S16_94X_ext1
# Fall17 miniAODv2
python launch.py --era mc_94X_Fall17_miniAODv2          --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample DYJetsToLL_M10to50_HT100to200_F17_94X
# Autumn18 miniAODv1
python launch.py --era mc_102X_Autumn18_miniAODv1       --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample DYJetsToLL_M50_MLM_A18_102X
# Run2016
python launch.py --era data_94X_Run2016                 --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample DoubleMuon_Run2016C_17Jul2018
# Run2017
python launch.py --era data_94X_Run2017                 --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample DoubleEG_Run2017C_31Mar2018
# Run2018 A->C
python launch.py --era data_102X_Run2018_17Sep2018      --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample DoubleMuon_Run2018B_17Sep2018_v1
# Run2018 D
python launch.py --era data_102X_Run2018_promptReco     --dryrun --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --sample EGamma_Run2018D_promptReco_v2
