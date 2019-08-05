#!/bin/bash
# Define Variables for cfgName, fragment
# run the script with "cfgName=CFGNAME fragment=FRAGMENT ./SCRIPTNAME"


#
# Outer Settings
#

# Quit if fragment is not set
if [ -z ${fragment} ]; then
    echo "Fragment not found!"
    exit
fi

echo "Using fragment $fragment"

# Quit if cfgName is not set
if [ -z ${cfgName} ]; then
    echo "Config name not found!"
    exit
fi

echo "Using config name $cfgName"


#
# Create GEN config
#

fragmentPath=$CMSSW_BASE/src/Samples/fragments/${fragment}.py
configPath=$CMSSW_BASE/src/Samples/cfg/${cfgName}.py
headerFile=$CMSSW_BASE/src/Samples/Tools/data/header.dat

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

# Copy fragment
cp ${fragmentPath} Configuration/GenProduction/python/${fragment}.py

[ -s Configuration/GenProduction/python/${fragment}.py ] || exit $?;

scram b

# GEN driver command
cmsDriver.py Configuration/GenProduction/python/${fragment}.py --fileout GEN_LO_0j_93X.root --mc --eventcontent RECOSIM --datatier GEN --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --geometry DB:Extended --era Run2_2017 --python_filename tmp.py --no_exec -n 999


#
# Modify config to run with launch_GEN.py
#

sed -i "s/nevts:999'/nevts:%i'%options.maxEvents/g" tmp.py
sed -i "s/999/options.maxEvents/g" tmp.py
sed -i "s/'GRIDPACK'/options.gridpack/g" tmp.py
cat ${headerFile} tmp.py > ${configPath}


#
# clean up
#

cd ../../
rm -r CMSSW_9_3_15_patch2
