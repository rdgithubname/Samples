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

mkdir -p /tmp/${USER}/GEN/
cd /tmp/${USER}/GEN/

export SCRAM_ARCH=slc6_amd64_gcc481
source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ -r CMSSW_7_1_41/src ] ; then 
    echo release CMSSW_7_1_41 already exists
else
    scram p CMSSW CMSSW_7_1_41
fi

cd CMSSW_7_1_41/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/.proxy
mkdir -p Configuration/GenProduction/python

# Copy fragment
cp ${fragmentPath} Configuration/GenProduction/python/${fragment}.py

[ -s Configuration/GenProduction/python/${fragment}.py ] || exit $?;

scram b

# GEN driver command
cmsDriver.py Configuration/GenProduction/python/${fragment}.py --fileout GEN_71X.root --mc --eventcontent RECOSIM --datatier GEN --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN --magField 38T_PostLS1 --python_filename tmp.py --no_exec -n 99999


#
# Modify config to run with launch_GEN.py
#

sed -i "s/nevts:99999'/nevts:%i'%options.maxEvents/g" tmp.py
sed -i "s/99999/options.maxEvents/g" tmp.py
sed -i "s/'GRIDPACK'/options.gridpack/g" tmp.py
cat ${headerFile} tmp.py > ${configPath}


#
# clean up
#

cd ../../
rm -r CMSSW_7_1_41
