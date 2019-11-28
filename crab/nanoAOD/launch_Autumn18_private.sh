#!/bin/sh

# TTGamma private samples
#python launch.py $@ --sorted --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Autumn18_private --sample allSamples
#python launch.py $@ --sorted --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Autumn18_private --sample TTGamma_dilep_LO_A18_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Autumn18_private --sample TTGamma_semilep_LO_A18_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Autumn18_private --sample TTGamma_had_LO_A18_private #SPLIT20
python launch.py $@ --sorted --runOnLocal --config nano_mc_102X_Autumn18_miniAODv1 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 50 --publish --module Autumn18_private --sample TTGamma_nofullyhad_LO_A18_private #SPLIT20
