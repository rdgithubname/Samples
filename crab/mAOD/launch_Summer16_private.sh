#!/bin/sh

# TTGamma private samples
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Summer16_private --sample allSamples
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Summer16_private --sample TTGamma_dilep_LO_S16_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Summer16_private --sample TTGamma_semilep_LO_S16_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Summer16_private --sample TTGamma_had_LO_S16_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 50 --publish --module Summer16_private --sample TTGamma_nofullyhad_LO_S16_private #SPLIT20

python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Summer16_miniAODv3 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 50 --publish --module Summer16_private --sample ZGToLLG_LO_S16_private #SPLIT1
