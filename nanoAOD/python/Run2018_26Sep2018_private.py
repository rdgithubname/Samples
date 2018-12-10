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
dbFile = dbDir+'DB_Run2018_26Sep2018_private.sql'

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2018B_26Sep2018               = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_26Sep2018",                "/DoubleMuon/dspitzba-crab_Run2018B-26Sep2018-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')
DoubleMuon_Run2018B_26Sep2018_HEM           = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_26Sep2018_HEM",            "/DoubleMuon/dspitzba-crab_Run2018B-26Sep2018_HEM-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')
DoubleMuon_Run2018B_26Sep2018_HEMmitigation = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_26Sep2018_HEMmitigation",  "/DoubleMuon/dspitzba-crab_Run2018B-26Sep2018_HEMmitigation-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')

DoubleMuon = [
    DoubleMuon_Run2018B_26Sep2018,
    DoubleMuon_Run2018B_26Sep2018_HEM,
    DoubleMuon_Run2018B_26Sep2018_HEMmitigation,
    ]

# MuonEG
MuonEG_Run2018B_26Sep2018               = Sample.nanoAODfromDAS("MuonEG_Run2018B_26Sep2018",                "/MuonEG/dspitzba-crab_Run2018B-26Sep2018-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')
MuonEG_Run2018B_26Sep2018_HEM           = Sample.nanoAODfromDAS("MuonEG_Run2018B_26Sep2018_HEM",            "/MuonEG/dspitzba-crab_Run2018B-26Sep2018_HEM-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')
MuonEG_Run2018B_26Sep2018_HEMmitigation = Sample.nanoAODfromDAS("MuonEG_Run2018B_26Sep2018_HEMmitigation",  "/MuonEG/dspitzba-crab_Run2018B-26Sep2018_HEMmitigation-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')

MuonEG = [
    MuonEG_Run2018B_26Sep2018,
    MuonEG_Run2018B_26Sep2018_HEM,
    MuonEG_Run2018B_26Sep2018_HEMmitigation,
    ]

# EGamma
EGamma_Run2018B_26Sep2018               = Sample.nanoAODfromDAS("EGamma_Run2018B_26Sep2018",                "/EGamma/dspitzba-crab_Run2018B-26Sep2018-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')
EGamma_Run2018B_26Sep2018_HEM           = Sample.nanoAODfromDAS("EGamma_Run2018B_26Sep2018_HEM",            "/EGamma/dspitzba-crab_Run2018B-26Sep2018_HEM-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')
EGamma_Run2018B_26Sep2018_HEMmitigation = Sample.nanoAODfromDAS("EGamma_Run2018B_26Sep2018_HEMmitigation",  "/EGamma/dspitzba-crab_Run2018B-26Sep2018_HEMmitigation-v1_HEM_v1-f5b5b303bc0ef563b98283b4e4ebaa8d/USER", dbFile=dbFile, redirector=redirector, instance='phys03')

EGamma = [
    EGamma_Run2018B_26Sep2018,
    EGamma_Run2018B_26Sep2018_HEM,
    EGamma_Run2018B_26Sep2018_HEMmitigation,
    ]

allSamples = DoubleMuon + MuonEG + EGamma

for s in allSamples:
    s.isData = True

