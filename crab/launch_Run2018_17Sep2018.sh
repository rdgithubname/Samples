#!/bin/sh

# Run2018ABC
python launch.py $@ --config data_102X_Run2018_17Sep2018 --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Run2018_17Sep2018 --sample allSamples
