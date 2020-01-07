#!/bin/sh

# Run2018ABC
#python launch.py $@ --config nano_data_102X_Run2018_17Sep2018 --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Run2018_17Sep2018 --sample lepSamples

# don't forget to run Promptreco for 2018D for everything except SingleMu, Egamma (below)

# Run2018D 
python launch.py $@ --config nano_data_102X_Run2018D --production_label legacy_nano_v5 --remoteDir legacy_nano_v5 --unitsPerJob 1 --publish --module Run2018D_22Jan2019 --sample allSamples
