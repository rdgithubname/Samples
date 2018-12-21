# Samples

Preliminary recipe for 102X (should work with all kind of samples)

```
cmsrel CMSSW_10_2_9
cd CMSSW_10_2_9/src
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
cp Samples/sparse-checkout .git/info/sparse-checkout
git remote add METSig https://github.com/danbarto/cmssw.git -f -t sumPtForMETSig_102Xv2
git checkout -b sumPtForMETSig_102Xv2 METSig/sumPtForMETSig_102Xv2
scram b -j 8
```
