#!/bin/sh

# all
python launch.py $@ --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v1 --remoteDir legacy_nano_v1 --unitsPerJob 2 --publish --module Autumn18_miniAODv1 --sample allSamples
