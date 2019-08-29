#!/bin/sh

# TTGamma private samples
#python launch.py --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Autumn18_private --sample allSamples
python launch.py --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Autumn18_private --sample TTGamma_dilep_LO_A18_private #SPLIT15
python launch.py --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Autumn18_private --sample TTGamma_semilep_LO_A18_private #SPLIT15
python launch.py --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Autumn18_private --sample TTGamma_had_LO_A18_private #SPLIT15
