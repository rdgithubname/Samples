'''
dasgoclient -query="dataset=/SingleMuon/Run2017*17Nov2017*/MINIAOD"
'''

import copy, os, sys
from RootTools.fwlite.FWLiteSample import FWLiteSample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite

else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"DB_Run2017_17Nov2017.sql"

logger.info("Using db file: %s", dbFile)

## FSQJet1
FSQJet1_Run2017H_17Nov2017   = FWLiteSample.fromDAS("FSQJet1_Run2017H_17Nov2017", "/FSQJet1/Run2017H-17Nov2017-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
FSQJet2_Run2017H_17Nov2017   = FWLiteSample.fromDAS("FSQJet2_Run2017H_17Nov2017", "/FSQJet2/Run2017H-17Nov2017-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

FSQJet = [
    FSQJet1_Run2017H_17Nov2017,
    FSQJet2_Run2017H_17Nov2017,
]


## sum up
allSamples = FSQJet 

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
