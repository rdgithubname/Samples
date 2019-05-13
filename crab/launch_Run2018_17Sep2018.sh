#!/bin/sh

# Run2018ABC
python launch.py $@ --config nano_data_102X_Run2018_17Sep2018 --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Run2018_17Sep2018 --sample lepSamples
