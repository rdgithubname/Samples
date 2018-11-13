import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
if __name__=='__main__':
    import Samples.Tools.logger as logger
    logger = logger.get_logger('DEBUG', logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger('DEBUG', logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+'DB_Spring16_private.sql'

logger.info("Using db file: %s", dbFile)

# Signals
T2tt_mStop400to1200 = Sample.nanoAODfromDAS("T2tt_mStop400to1200", "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER", dbFile=dbFile, redirector=redirector, instance='phys03', xSection=1)

signals = [
    T2tt_mStop400to1200,
    ]

other = [
    ]

allSamples = signals

for s in allSamples:
    s.isData = False

