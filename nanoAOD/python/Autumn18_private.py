import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    from Samples.Tools.config import  redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Autumn18_private.sql"

logger.info("Using db file: %s", dbFile)

TTGHad_priv  = Sample.nanoAODfromDPM("TTGHad_priv",  "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v3/Autumn18_private_TTGamma_had_LO_A18_private/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.213*2.565)
TTGSemi_priv = Sample.nanoAODfromDPM("TTGSemi_priv", "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v3/Autumn18_private_TTGamma_semilep_LO_A18_private/",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
TTGLep_priv  = Sample.nanoAODfromDPM("TTGLep_priv",  "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v3/Autumn18_private_TTGamma_dilep_LO_A18_private/",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)


TTX = [
    TTGHad_priv,
    TTGSemi_priv,
    TTGLep_priv,
    ]

signals = [
    ]

other = [
    ]

allSamples = TTX + signals + other

for s in allSamples:
    s.isData = False

