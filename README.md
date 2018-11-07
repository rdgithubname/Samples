# Samples

Preliminary recipe

```
cmsrel CMSSW_9_4_10
cd CMSSW_9_4_10/src
cmsenv
git cms-init

# This repository
git clone https://github.com/HephyAnalysisSW/Samples.git
cd $CMSSW_BASE/src

# RootTools (needed for nanoAOD sample handling. If you just plan to produce nanoAOD tuples from miniAOD, this is not needed)
git clone https://github.com/HephyAnalysisSW/RootTools.git

cd $CMSSW_BASE/src
scram b -j 8

```

Checkout your custom modules to nanoAOD. This is just an example, adding the not yet merged computation of sumPt as well as FastSim support. sumPt is needed to recompute MET significance.

```
cd $CMSSW_BASE/src
cp sparse-checkout .git/info/sparse-checkout
git remote add ownFork https://github.com/danbarto/cmssw.git
git fetch ownFork
git checkout ownFork/sumPtForMETSig
scram b -j 8
```
