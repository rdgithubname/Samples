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
    if "clip" in os.getenv("HOSTNAME").lower():
        from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Fall17_private.sql"

logger.info("Using db file: %s", dbFile)

#TTGNoFullyHad_priv  = Sample.nanoAODfromDAS("TTGNoFullyHad_priv",  "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Fall17_private_TTGamma_nofullyhad_LO_F17_private/", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994+1.512*1.616, maxN=1)
TTGHad_priv         = Sample.nanoAODfromDAS("TTGHad_priv",         "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Fall17_private_TTGamma_had_LO_F17_private/",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.213*2.565)
TTGSemi_priv        = Sample.nanoAODfromDAS("TTGSemi_priv",        "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Fall17_private_TTGamma_semilep_LO_F17_private/",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994)
TTGLep_priv         = Sample.nanoAODfromDAS("TTGLep_priv",         "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Fall17_private_TTGamma_dilep_LO_F17_private/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.512*1.616)

TTGNoFullyHad_fnal  = Sample.nanoAODfromDAS("TTGNoFullyHad_fnal",  "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v6/ttgamma_noFullyHad_fnal_2017/", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.125*1.994+1.512*1.616)

TTX = [
#    TTGNoFullyHad_priv,
    TTGHad_priv,
    TTGSemi_priv,
    TTGLep_priv,
    TTGNoFullyHad_fnal,
    ]

# LO xsec
#ZGToLLG_LO_priv = Sample.nanoAODfromDAS("ZGToLLG_LO_priv", "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v3/Fall17_private_ZGToLLG_LO_F17_private/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=445.8)


VGamma = [
#    ZGToLLG_LO_priv,
]

signals = [
    ]

other = [
    ]

allSamples = TTX + signals + other + VGamma

for s in allSamples:
    s.isData = False
