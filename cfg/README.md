# cmsRun config files

Config files based on
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD

Important:
Output files should always be named nanoAOD.root, otherwise the transfer with the default crabConfig won't work.

If you want to publish your dataset on dbs, add `--publish`, and be sure that the following line is part of the OutputModule of the cmsRun config:
```
fakeNameForCrab =cms.untracked.bool(True),
```

Launch on crab with
```
python launch.py --era 94X_mc --production_label sampleTest_v1 --remoteDir sampleTest_v1 --unitsPerJob 1 --totalUnits 1 --sample DYJetsToLL_M50_S16_94X_MLM
```

