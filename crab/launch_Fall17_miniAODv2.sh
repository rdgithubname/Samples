#!/bin/sh

# DY
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_miniAODv2   --sample  DY

# single top
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ST_schannel_4f_NLO_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ST_5f

## TT
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_semilepFromT_LO_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_semilepFromTbar_LO_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_dilep_LO_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTTo2L2Nu_pow_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTTo2L2Nu_pow_PS_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTToSemiLeptonic_pow_F17_94X
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTToSemiLeptonic_pow_PS_F17_94X

# rest
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTX
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTVV
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  WJets
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  diboson
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  multiboson
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  gluglu

# SUSY
python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_150to250
python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_250to350
python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_350to400
python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v3 --remoteDir legacy_nano_v3 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_400to1200
