#!/bin/sh

# DY
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Fall17_miniAODv2   --sample  DY

# single top
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ST_schannel_4f_NLO
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ST_5f

## TT
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_semilepFromT_LO
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_semilepFromTbar_LO
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTJets_dilep_LO
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTTo2L2Nu_pow
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTTo2L2Nu_pow_PS
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTToSemiLeptonic_pow
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTToSemiLeptonic_pow_PS

# rest
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTX
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  TTVV
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  WJets
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  diboson
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  multiboson
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  gluglu
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample  ZGToLLG_NLO

#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample ST_tWnunu_5f_LO
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample ST_tWll_5f_LO
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample GluGluHToZZTo4L
#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample GluGluToContinToZZTo4tau

#python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample WGToLNuG_NLO
python launch.py $@ --config nano_mc_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 2 --publish --module Fall17_miniAODv2   --sample TTToHadronic_pow_PS

# SUSY
#python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_150to250
#python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_250to350
#python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_350to400
#python launch.py $@ --config nano_mc_fast_94X_Fall17_miniAODv2  --production_label legacy_nano_v4 --remoteDir legacy_nano_v4 --unitsPerJob 1 --publish --module Fall17_Fast_miniAODv2   --sample SMS_T2tt_mStop_400to1200
