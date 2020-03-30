'''
miniAOD samples of Summer16 campaign, miniAODv3 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16*94X*/MINIAODSIM"
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
dbFile = dbDir+"Summer16_miniAODv3_private.sql"

logger.info("Using db file: %s", dbFile) 

## DY


# xSec    = 5.277e-05
yt_tZZ           = FWLiteSample.fromDAS("yt_tZZ",  "/tZZ1j_4l_rwgt/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", dbFile=dbFile, overwrite=ov, prefix=redirector_global, instance="phys03", skipCheck=True)
# xSec    = 0.2279
yt_tWZ01j        = FWLiteSample.fromDAS("yt_tWZ01j",  "/tWZ01j_rwgt/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", dbFile=dbFile, overwrite=ov, prefix=redirector_global, instance="phys03", skipCheck=True)
#tWZ01j_filter_efficiency = (601438./(30*10**6))*(10**6/363784.)
#xSec = 0.2279*tWZ01j_filter_efficiency
yt_tWZ01j_filter = FWLiteSample.fromDAS("yt_tWZ01j_filter",  "/tWZ01j_rwgt_filter_2/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", dbFile=dbFile, overwrite=ov, prefix=redirector_global, instance="phys03", skipCheck=True)

# xSec    = 0.02523
yt_tWW        = FWLiteSample.fromDAS("yt_tWW",  "/tWW1j_rwgt/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", dbFile=dbFile, overwrite=ov, prefix=redirector_global, instance="phys03", skipCheck=True)
# xSec    = 0.8324
yt_ttW        = FWLiteSample.fromDAS("yt_ttW",  "/ttW01j_rwgt_dim6top/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, instance="phys03", skipCheck=True)


tVV = [
    yt_tZZ,
    yt_tWZ01j,
    yt_tWZ01j_filter,
    yt_tWW,
    yt_ttW,
]


allSamples = tVV 

for sample in allSamples:
    sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
