#!/bin/sh

# TTGamma private samples
#python launch.py --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Summer16_private --sample allSamples
python launch.py --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Summer16_private --sample TTGamma_dilep_LO_S16_private #SPLIT15
python launch.py --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Summer16_private --sample TTGamma_semilep_LO_S16_private #SPLIT15
python launch.py --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Summer16_private --sample TTGamma_had_LO_S16_private #SPLIT15
