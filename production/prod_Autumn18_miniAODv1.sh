#!/bin/bash
# Define Variables for productionNumber, events, fragment, gridpack and gridpackDir
# run the script with "productionNumber=NUMBER events=EVENTS gridpack=GRIDPACK gridpackDir=PATH_TO_GRIDPACK fragment=FRAGMENT ./SCRIPTNAME"
# runs about 30 min for 10 events!
# runs about 6 hours for 1000 events!

#
# Outer Settings
#

# Quit if productionNumber is not set
if [ -z ${productionNumber} ]; then
    echo "Production Number not found!"
    exit
fi

echo "Running production number: ${productionNumber}"

# Quit if events is not set
if [ -z ${events} ]; then
    echo "Number of Events not found!"
    exit
fi

echo "Running ${events} events"

# Quit if fragment is not set
if [ -z ${fragment} ]; then
    echo "Fragment not found!"
    exit
fi

echo "Using fragment $fragment"

# Quit if gridpack is not set
if [ -z ${gridpack} ]; then
    echo "Gridpack not found!"
    exit
fi

echo "Using gridpack $gridpack"

# Quit if gridpackDir is not set
if [ -z ${gridpackDir} ]; then
    echo "Gridpack directory not found!"
    exit
fi

echo "Using gridpack directory $gridpackDir"


#
# Settings
#

# Set number of threads
threads=1

# Set fragment
fragmentPath=$CMSSW_BASE/src/Samples/fragments/${fragment}.py

# Quit if fragment does not exist
if [ ! -f ${fragmentPath} ]; then
    echo "Fragment not found: ${fragmentPath}"
    exit
fi

# Set gridpack path
gridpackPath=${gridpackDir}/${gridpack}_tarball.tar.xz
shortName="${gridpack%_slc*}"

# Quit if gridpack does not exist
if [ ! -f ${gridpackPath} ]; then
    echo "Gridpack not found: ${gridpackPath}"
    exit
fi


#
# Default Directory Setup
#

tmp_dir=${gridpack}_Autumn18_miniAODv1/${productionNumber}
mkdir -p /tmp/${USER}/
cd /tmp/${USER}/

# Quit if file already exists
if [ -d ${tmp_dir} ]; then
    echo "Directory still in use by other job: /tmp/${USER}/${tmp_dir}"
    exit
fi

mkdir -p ${tmp_dir}
cd ${tmp_dir}


#
# GEN-SIM
#

export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_10_2_3/src ] ; then 
    echo release CMSSW_10_2_3 already exists
else
    scram p CMSSW CMSSW_10_2_3
fi

cd CMSSW_10_2_3/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/.proxy
mkdir -p Configuration/GenProduction/python

# Copy fragment and change the gridpack path
cat ${fragmentPath} | sed "s/GRIDPACK/$(echo ${gridpackPath} | sed 's/\//\\\//g')/" > Configuration/GenProduction/python/${fragment}.py

[ -s Configuration/GenProduction/python/${fragment}.py ] || exit $?;

scram b
cd ../../

# GEN-SIM driver command
cmsDriver.py Configuration/GenProduction/python/${fragment}.py --fileout file:RunIIAutumn18_privProd_GENSIM_${shortName}.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2018 --python_filename RunIIAutumn18_privProd_GENSIM_${shortName}_cfg.py --no_exec -n $events || exit $? ;

echo "process.RandomNumberGeneratorService.generator.initialSeed = ${productionNumber}" >> RunIIAutumn18_privProd_GENSIM_${shortName}_cfg.py
echo "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = ${productionNumber}" >> RunIIAutumn18_privProd_GENSIM_${shortName}_cfg.py
sed -i "s/process.source = cms.Source(\"EmptySource\")/process.source = cms.Source(\"EmptySource\",firstRun=cms.untracked.uint32(${productionNumber}))/g" RunIIAutumn18_privProd_GENSIM_${shortName}_cfg.py

# run GEN-SIM
cmsRun -e -j RunIIAutumn18_privProd_GENSIM_${shortName}_rt.xml RunIIAutumn18_privProd_GENSIM_${shortName}_cfg.py || exit $? ;

sleep 10


#
# PU mixing
#

export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_10_2_5/src ] ; then 
    echo release CMSSW_10_2_5 already exists
else
    scram p CMSSW CMSSW_10_2_5
fi

cd CMSSW_10_2_5/src
eval `scram runtime -sh`

scram b
cd ../../

# PU mixing driver command
cmsDriver.py step1 --filein file:RunIIAutumn18_privProd_GENSIM_${shortName}.root --fileout file:RunIIAutumn18_privProd_Premix_${shortName}.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --nThreads ${threads} --procModifiers premix_stage2 --datamix PreMix --era Run2_2018 --python_filename RunIIAutumn18_privProd_Premix_${shortName}_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ;

# run PU mixing
cmsRun -e -j RunIIAutumn18_privProd_Premix_${shortName}_rt.xml RunIIAutumn18_privProd_Premix_${shortName}_cfg.py || exit $? ;


#
# DIGI-RECO + AOD
# Could not combine AOD + miniAOD step yet
#
# AOD driver command
cmsDriver.py step2 --filein file:RunIIAutumn18_privProd_Premix_${shortName}.root --fileout file:RunIIAutumn18_privProd_AODSIM_${shortName}.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --nThreads ${threads} --era Run2_2018 --python_filename RunIIAutumn18_privProd_AODSIM_${shortName}_cfg.py --no_exec --procModifiers premix_stage2 --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ;

# run AOD
cmsRun -e -j RunIIAutumn18_privProd_AODSIM_${shortName}_rt.xml RunIIAutumn18_privProd_AODSIM_${shortName}_cfg.py || exit $? ; 

sleep 10


#
# miniAODv1
#

export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_10_2_5/src ] ; then 
    echo release CMSSW_10_2_5 already exists
else
    scram p CMSSW CMSSW_10_2_5
fi

cd CMSSW_10_2_5/src
eval `scram runtime -sh`

scram b
cd ../../

# driver command for up to miniAODv1
cmsDriver.py step1 --filein file:RunIIAutumn18_privProd_AODSIM_${shortName}.root --fileout file:RunIIAutumn18_privProd_MINIAODSIM_${shortName}.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads ${threads} --geometry DB:Extended --era Run2_2018 --python_filename RunIIAutumn18_privProd_miniAODv1_${shortName}_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ; 

sed -i "/# Additional output definition/a process.MINIAODSIMoutput.outputCommands.append('keep recoTrack*_displaced*Muons__RECO')" RunIIAutumn18_privProd_miniAODv1_${shortName}_cfg.py

# run up to miniAODv1
cmsRun -e -j RunIIAutumn18_privProd_miniAODv1_${shortName}_rt.xml RunIIAutumn18_privProd_miniAODv1_${shortName}_cfg.py || exit $? ;

sleep 10


#
# Copy to DPM
#

xrdcp -f RunIIAutumn18_privProd_MINIAODSIM_${shortName}.root root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/${USER}/miniAOD/RunIIAutumn18_privProd_miniAODv1/${shortName}/
echo "Copied produced sample to root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/${USER}/miniAOD/RunIIAutumn18_privProd_miniAODv1/${shortName}/RunIIAutumn18_privProd_miniAODv1_${shortName}_${productionNumber}.root"

#
# clean up
#

cd ../../
rm -r ${tmp_dir}
