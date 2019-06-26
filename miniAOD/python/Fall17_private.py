'''
miniAOD samples of TTGamma private production (Tom)
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

from Samples.Tools.config import dbDir, redirector_BE
dbFile = dbDir+"Fall17_private.sql"

logger.info("Using db file: %s", dbFile) 

## TTGamma private new samples
TTGamma_dilep_LO_F17_private         = FWLiteSample.fromDPMDirectory("TTGamma_dilep_LO_F17_private",      "/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/prompt/ttGamma_Dilept_5f_ckm_LO_1line",     dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_semilep_LO_F17_private       = FWLiteSample.fromDPMDirectory("TTGamma_semilep_LO_F17_private",    "/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/prompt/ttGamma_SemiLept_5f_ckm_LO_1line",   dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_had_LO_F17_private           = FWLiteSample.fromDPMDirectory("TTGamma_had_LO_F17_private",        "/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/prompt/ttGamma_Had_5f_ckm_LO_1line",        dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_nofullyhad_LO_F17_private    = FWLiteSample.fromDPMDirectory("TTGamma_nofullyhad_LO_F17_private", "/store/user/tomc/heavyNeutrinoMiniAOD/Fall17/prompt/ttGamma_NoFullyHad_5f_ckm_LO_1line", dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)

TTX = [
       TTGamma_dilep_LO_F17_private,
       TTGamma_semilep_LO_F17_private,
       TTGamma_had_LO_F17_private,
       TTGamma_nofullyhad_LO_F17_private,
]

allSamples = TTX

for sample in allSamples:
    sample.isData = False
