'''
Some definitions.
To avoid changes of the file being pushed to github, e.g. when you define a different dbDir, use:
git update-index --skip-worktree config.py
'''
import os

## This definition might not work for everybody. Update with whatever you like.
dbDir               = '/afs/hephy.at/data/%s01/nanoAOD/'%os.environ['USER']
redirector          = 'root://hephyse.oeaw.ac.at/'
redirector_global   = 'root://cms-xrd-global.cern.ch/'

if not os.path.isdir(dbDir): os.makedirs(dbDir)


