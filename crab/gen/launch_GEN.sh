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

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_SingleLeptFromT_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromT_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_SingleLeptFromT_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_SingleLeptFromTbar_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromTbar_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_SingleLeptFromTbar_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_Dilept_5f_ckm_LO/"
#gridpack="ttGamma_Dilept_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_Dilept_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_Hadronic_5f_ckm_LO/"
#gridpack="ttGammaHadronic_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_Hadronic_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/newEFT/TTGamma_SingleLeptFromT_1Line_EFT/"
#gridpack="TTGamma_SingleLeptFromT_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromT_1Line_EFT_GENSIM_v3"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/newEFT/TTGamma_SingleLeptFromTbar_1Line_EFT/"
#gridpack="TTGamma_SingleLeptFromTbar_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromTbar_1Line_EFT_GENSIM_v3"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTXPheno/gridpacks/WJetsToLNu3Jets"
#gridpack="WJetsToLNu_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz"
#label="WJetsToLNu"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTXPheno/gridpacks/WJetsToLNu"
#gridpack="WJetsToLNu_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="WJetsToLNu4Jets"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard"
#gridpack="ttGamma_CMS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_ATLASrunCard"
#gridpack="ttGamma_ATLAS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_ATLASrunCard"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard"
#gridpack="ttGamma_CMS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_small"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_ATLASrunCard"
#gridpack="ttGamma_ATLAS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_ATLASrunCard_small"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTZRun2EFT/gridpacks/EFT/ttZ_ll_LO_order4_6weights_ref/"
#gridpack="ttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttZ_order4_6weights_EFT"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR/"
#gridpack="ttGamma_CMS_deltaR_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut/"
#gridpack="ttGamma_CMS_jetPt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_xqcut/"
#gridpack="ttGamma_CMS_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_xqcut/"
#gridpack="ttGamma_CMS_deltaR_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut/"
#gridpack="ttGamma_CMS_deltaR_jetPt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut/"
#gridpack="ttGamma_CMS_deltaR_jetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut_xqcut/"
#gridpack="ttGamma_CMS_jetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut_xqcut_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut/"
#gridpack="ttGamma_CMS_deltaR_jetPt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta/"
#gridpack="ttGamma_CMS_dR_ptj_xq_etal_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_largeBJetPt_xqcut/"
#gridpack="ttGamma_CMS_largeBJetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_largeBJetPt_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_largeJetPt_xqcut/"
#gridpack="ttGamma_CMS_largeJetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_largeJetPt_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_TTBarrunCard/"
#gridpack="ttGamma_ttbar_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_TTBarrunCard_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_TTBarrunCard_modified/"
#gridpack="ttGamma_ttbarMod_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_TTBarrunCard_modified"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_TTBarrunCard_mllOnly/"
#gridpack="ttGamma_ttbarModmllOnly_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_TTBarrunCard_mllOnly"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish


#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_Dilept/"
#gridpack="ttGamma_Dilept_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_Dilept"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_SemiLept/"
#gridpack="ttGamma_SemiLept_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_SemiLept"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_Had/"
#gridpack="ttGamma_Had_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_Had"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_NoFullyHad/"
#gridpack="ttGamma_NoFullyHad_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_NoFullyHad"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_NoFullyHad_noAuto/"
#gridpack="ttGamma_NoFullyHad_5f_ckm_LO_1line_noAuto_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_NoFullyHad_noAuto"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish


dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/"
gridpack="ttW01j_rwgt_mg265_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz"
label="ttW01j_rwgt_mg265_v1"
python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

