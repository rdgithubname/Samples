 #!/bin/sh

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_3LinePatched/"
#gridpack="TTGamma_SingleLeptFromT_3LinePatched_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromT_3LinePatched_SM_GENSIM"

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_1Line/"
#gridpack="TTGamma_SingleLeptFromT_1Line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromT_1Line_SM_GENSIM_v2"

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/EFT/TTGamma_DiLept_1Line_EFT/"
#gridpack="TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_DiLept_1Line_EFT_GENSIM_v3"

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_SingleLeptFromT_1line_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromT_1line_5f_ckm_LO_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_SingleLeptFromT_1line_5f_ckm_LO_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_SingleLeptFromTbar_1line_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromTbar_1line_5f_ckm_LO_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_SingleLeptFromTbar_1line_5f_ckm_LO_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_SingleLeptFromT_5f_ckm_LO/"
gridpack="ttGamma_SingleLeptFromT_5f_ckm_LO_tarball.tar.xz"
label="ttGamma_SingleLeptFromT_5f_ckm_LO_central_v3"
python launch_GEN.py $@ --config gen_LO_mc_7125 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_SingleLeptFromTbar_5f_ckm_LO/"
gridpack="ttGamma_SingleLeptFromTbar_5f_ckm_LO_tarball.tar.xz"
label="ttGamma_SingleLeptFromTbar_5f_ckm_LO_central_v3"
python launch_GEN.py $@ --config gen_LO_mc_7125 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_Dilept_5f_ckm_LO/"
#gridpack="ttGamma_Dilept_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_Dilept_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_mc_7125 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_Hadronic_5f_ckm_LO/"
gridpack="ttGammaHadronic_5f_ckm_LO_tarball.tar.xz"
label="ttGamma_Hadronic_5f_ckm_LO_central_v3"
python launch_GEN.py $@ --config gen_LO_mc_7125 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

