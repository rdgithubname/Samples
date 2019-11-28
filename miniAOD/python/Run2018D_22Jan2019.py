'''
dasgoclient -query="dataset=/*/Run2018*22Jan2018*/MINIAOD"
'''

# two samples with new processing: https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable

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
dbFile = dbDir+"Run2018_17Sep2018.sql"

logger.info("Using db file: %s", dbFile)

SingleMuon_Run2018D_22Jan2019_v2 = FWLiteSample.fromDAS("SingleMuon_Run2018D_22Jan2019_v2", "/SingleMuon/Run2018D-22Jan2019-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018D_22Jan2019_v2     = FWLiteSample.fromDAS("EGamma_Run2018D_22Jan2019_v2", "/EGamma/Run2018D-22Jan2019-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

allSamples = [
    SingleMuon_Run2018D_22Jan2019_v2,
    EGamma_Run2018D_22Jan2019_v2
]

## sum up
for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
