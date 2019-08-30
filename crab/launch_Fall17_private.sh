#!/bin/sh

# TTGamma private samples
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Fall17_miniAODv2 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Fall17_private --sample  allSamples
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Fall17_miniAODv2 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Fall17_private --sample TTGamma_dilep_LO_F17_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Fall17_miniAODv2 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Fall17_private --sample TTGamma_semilep_LO_F17_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Fall17_miniAODv2 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 40 --publish --module Fall17_private --sample TTGamma_had_LO_F17_private #SPLIT20
#python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Fall17_miniAODv2 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 50 --publish --module Fall17_private --sample TTGamma_nofullyhad_LO_F17_private #SPLIT20

python launch.py $@ --sorted --runOnLocal --config nano_mc_94X_Fall17_miniAODv2 --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 50 --publish --module Fall17_private --sample ZGToLLG_LO_F17_private #SPLIT1
