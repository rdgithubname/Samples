 #!/bin/sh

dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_1Line_test/"
gridpack="TTGamma_SingleLeptFromT_1Line_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"

python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label TTGamma_SingleLeptFromT_1Line_test_GENSIM --unitsPerJob 5000 --totalUnits 100000 --gridpackDir ${dir} --gridpack ${gridpack} --publish

dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_3LineBuggy_test/"
gridpack="TTGamma_SingleLeptFromT_3LineBuggy_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"

python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label TTGamma_SingleLeptFromT_3LineBuggy_test_GENSIM --unitsPerJob 5000 --totalUnits 100000 --gridpackDir ${dir} --gridpack ${gridpack} --publish

dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_3LinePatched_test/"
gridpack="TTGamma_SingleLeptFromT_3LinePatched_test_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"

python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label TTGamma_SingleLeptFromT_3LinePatched_test_GENSIM --unitsPerJob 5000 --totalUnits 100000 --gridpackDir ${dir} --gridpack ${gridpack} --publish
