#!/bin/bash
# Define Variables for productionNumber, events, fragment, gridpack and gridpackDir
# run the script with "productionNumber=NUMBER events=EVENTS gridpack=GRIDPACK gridpackDir=PATH_TO_GRIDPACK fragment=FRAGMENT ./SCRIPTNAME"


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
threads=4

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

tmp_dir=${gridpack}_Fall17_miniAODv2/${productionNumber}
cd $CMSSW_BASE/../

# Quit if file already exists
if [ -d ${tmp_dir} ]; then
    echo "Directory still in use by other job: $CMSSW_BASE/../${tmp_dir}"
    exit
fi

mkdir -p ${tmp_dir}
cd ${tmp_dir}


#
# GEN-SIM
#

export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_9_3_15_patch2/src ] ; then
    echo release CMSSW_9_3_15_patch2 already exists
else
    scram p CMSSW CMSSW_9_3_15_patch2
fi

cd CMSSW_9_3_15_patch2/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/.proxy
mkdir -p Configuration/GenProduction/python

# Copy fragment and change the gridpack path
cat ${fragmentPath} | sed "s/GRIDPACK/$(echo ${gridpackPath} | sed 's/\//\\\//g')/" > Configuration/GenProduction/python/${fragment}.py

[ -s Configuration/GenProduction/python/${fragment}.py ] || exit $?;

scram b
cd ../../

# GEN-SIM driver command
cmsDriver.py Configuration/GenProduction/python/${fragment}.py --fileout file:RunIIFall17_privProd_GENSIM_${shortName}.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads ${threads} --geometry DB:Extended --era Run2_2017 --python_filename RunIIFall17_privProd_GENSIM_${shortName}_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ; 

echo "process.RandomNumberGeneratorService.generator.initialSeed = ${productionNumber}" >> RunIIFall17_privProd_GENSIM_${shortName}_cfg.py
echo "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = ${productionNumber}" >> RunIIFall17_privProd_GENSIM_${shortName}_cfg.py
sed -i "s/process.source = cms.Source(\"EmptySource\")/process.source = cms.Source(\"EmptySource\",firstRun=cms.untracked.uint32(${productionNumber}))/g" RunIIFall17_privProd_GENSIM_${shortName}_cfg.py

# run GEN-SIM
cmsRun -e -j RunIIFall17_privProd_GENSIM_${shortName}_rt.xml RunIIFall17_privProd_GENSIM_${shortName}_cfg.py || exit $? ;

sleep 10


#
# PU mixing
#

export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_9_4_7/src ] ; then 
    echo release CMSSW_9_4_7 already exists
else
    scram p CMSSW CMSSW_9_4_7
fi

cd CMSSW_9_4_7/src
eval `scram runtime -sh`

scram b
cd ../../

# PU mixing driver command
cmsDriver.py step1 --filein file:RunIIFall17_privProd_GENSIM_${shortName}.root --fileout file:RunIIFall17_privProd_Premix_${shortName}.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads ${threads} --datamix PreMix --era Run2_2017 --python_filename RunIIFall17_privProd_Premix_${shortName}_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ;

# run PU mixing
cmsRun -e -j RunIIFall17_privProd_Premix_${shortName}_rt.xml RunIIFall17_privProd_Premix_${shortName}_cfg.py || exit $? ;


#
# DIGI-RECO + AOD
# Could not combine AOD + miniAOD step yet
#

# AOD driver command
cmsDriver.py step2 --filein file:RunIIFall17_privProd_Premix_${shortName}.root --fileout file:RunIIFall17_privProd_AODSIM_${shortName}.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads ${threads} --era Run2_2017 --python_filename RunIIFall17_privProd_AODSIM_${shortName}_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ;

# run AOD
cmsRun -e -j RunIIFall17_privProd_AODSIM_${shortName}_rt.xml RunIIFall17_privProd_AODSIM_${shortName}_cfg.py || exit $? ;

sleep 10


#
# miniAODv2
#

export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_9_4_7/src ] ; then
    echo release CMSSW_9_4_7 already exists
else
    scram p CMSSW CMSSW_9_4_7
fi

cd CMSSW_9_4_7/src
eval `scram runtime -sh`

scram b
cd ../../

# driver command for up to miniAODv2
cmsDriver.py step1 --filein file:RunIIFall17_privProd_AODSIM_${shortName}.root --fileout file:RunIIFall17_privProd_MINIAODSIM_${shortName}.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT --nThreads ${threads} --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --python_filename RunIIFall17_privProd_miniAODv2_${shortName}_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $events || exit $? ;

sed -i "/# Additional output definition/a process.MINIAODSIMoutput.outputCommands.append('keep recoTrack*_displaced*Muons__RECO')" RunIIFall17_privProd_miniAODv2_${shortName}_cfg.py

# run up to miniAODv2
cmsRun -e -j RunIIFall17_privProd_miniAODv2_${shortName}_rt.xml RunIIFall17_privProd_miniAODv2_${shortName}_cfg.py || exit $? ;

sleep 10


#
# Copy to DPM
#

xrdcp -f RunIIFall17_privProd_MINIAODSIM_${shortName}.root root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/${USER}/miniAOD/RunIIFall17_privProd_miniAODv2/${shortName}/RunIIFall17_privProd_miniAODv2_${shortName}_${productionNumber}.root


#
# clean up
#

cd ../../
rm -r ${tmp_dir}
