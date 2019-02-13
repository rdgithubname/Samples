#!/bin/sh

# DY
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_miniAODv2   --sample  DY
python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_miniAODv2   --sample  DY_HT

## single top
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ST_schannel_4f_NLO_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ST_5f
#
### TT
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_semilepFromT_LO_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_semilepFromTbar_LO_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_dilep_LO_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTTo2L2Nu_pow_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTTo2L2Nu_pow_PS_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTToSemiLeptonic_pow_F17_94X
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTToSemiLeptonic_pow_PS_F17_94X
#
## rest
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTX
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTVV
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  WJets
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  diboson
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  multiboson
#python launch.py $@ --config mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  gluglu
