#!/bin/sh

# Run2018ABC
python launch.py $@ --config data_94X_Run2017 --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Run2017_31Mar2018 --sample allSamples
