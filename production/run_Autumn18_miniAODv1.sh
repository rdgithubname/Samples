# General settings
events=200
fragment=pythiaFragmentCUEP8M1_LO_0123j
gridpack=ZAToLLA0123j_5f_LO_MLM_slc6_amd64_gcc630_CMSSW_9_3_8
gridpackDir=/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/VGamma_LO/ZGamma/

# List of jobs
start=1
end=1
for i in $(eval echo "{${start}..${end}}")
do
    productionNumber=${i} events=${events} gridpack=${gridpack} gridpackDir=${gridpackDir} fragment=${fragment} ./prod_Autumn18_miniAODv1.sh
done
