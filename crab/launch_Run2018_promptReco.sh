#!/bin/sh

# Run2018D
python launch.py $@ --config data_102X_Run2018_promptReco --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample DoubleMuon_Run2018D_promptReco_v2
python launch.py $@ --config data_102X_Run2018_promptReco --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample MuonEG_Run2018D_promptReco_v2
python launch.py $@ --config data_102X_Run2018_promptReco --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample EGamma_Run2018D_promptReco_v2
python launch.py $@ --config data_102X_Run2018_promptReco --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample SingleMuon_Run2018D_promptReco_v2
python launch.py $@ --config data_102X_Run2018_promptReco --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample JetHT_Run2018D_promptReco_v2
python launch.py $@ --config data_102X_Run2018_promptReco --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_promptReco --sample MET_Run2018D_promptReco_v2
