#!/bin/sh

# TTGamma private samples
#python launch.py --runOnLocal --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Fall17_private --sample  allSamples
python launch.py --runOnLocal --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Fall17_private --sample TTGamma_dilep_LO_F17_private #SPLIT15
python launch.py --runOnLocal --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Fall17_private --sample TTGamma_semilep_LO_F17_private #SPLIT15
python launch.py --runOnLocal --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v2 --remoteDir legacy_nano_v2 --unitsPerJob 20 --publish --module Fall17_private --sample TTGamma_had_LO_F17_private #SPLIT15
