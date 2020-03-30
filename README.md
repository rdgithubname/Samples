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

Private nanoAOD v4 (sumPt for MetSig):

```
cd $CMSSW_BASE/src
cp Samples/sparse-checkout .git/info/sparse-checkout
git remote add METSig https://github.com/danbarto/cmssw.git -f -t sumPtForMETSig_102Xv2
git checkout -b sumPtForMETSig_102Xv2 METSig/sumPtForMETSig_102Xv2
scram b -j 8
```
Private nanoAOD v6 (lepton MVA TTV and lepton MVA inputs):

```
cd $CMSSW_BASE/src
cp Samples/sparse-checkout .git/info/sparse-checkout
git remote add hephy https://github.com/HEPHYAnalysisSW/cmssw.git -f -t CMSSW_10_2_18_lepton_MVA_TTV
git fetch hephy 
git checkout -b CMSSW_10_2_18_lepton_MVA_TTV hephy/CMSSW_10_2_18_lepton_MVA_TTV
scram b -j 8
```
