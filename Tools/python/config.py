'''
Some definitions.
'''
import os

## This definition might not work for everybody. Update with whatever you like.
if os.environ['USER'] in ['llechner']:
    dbDir = '/afs/hephy.at/data/llechner01/TTGammaEFT/cache/samples/'
elif os.environ['USER'] in ['dspitzba', 'dspitzbart']:
    dbDir = '/afs/hephy.at/data/dspitzbart01/nanoAOD/'
elif os.environ['USER'] in ['phussain']:
    dbDir = '/afs/hephy.at/data/rschoefbeck01/nanoAOD/'
elif os.environ['USER'] in ['schoef']:
    dbDir = '/afs/hephy.at/data/rschoefbeck01/nanoAOD/'
elif os.environ['USER'] in ['mzarucki']:
    dbDir = '/afs/hephy.at/data/mzarucki02/nanoAOD/caches'
else:
    dbDir = '/afs/hephy.at/data/%s01/nanoAOD/'%os.environ['USER']

redirector        = 'root://hephyse.oeaw.ac.at/'
redirector_BE     = 'root://maite.iihe.ac.be/'
redirector_global = 'root://cms-xrd-global.cern.ch/'

if not os.path.isdir(dbDir): os.makedirs(dbDir)
