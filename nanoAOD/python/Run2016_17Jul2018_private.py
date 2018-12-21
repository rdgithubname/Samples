import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
else:
    import logging
    logger = logging.getLogger(__name__)

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"DB_Run2016_17Jul2018_private.sql"

logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2016B_26Sep2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_26Sep2018_ver1",   "/DoubleMuon/dspitzba-crab_Run2016B-17Jul2018_ver1-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER", dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016B_26Sep2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_26Sep2018_ver2",   "/DoubleMuon/dspitzba-crab_Run2016B-17Jul2018_ver2-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER", dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016C_26Sep2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_26Sep2018",        "/DoubleMuon/dspitzba-crab_Run2016C-17Jul2018-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER",      dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016D_26Sep2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_26Sep2018",        "/DoubleMuon/dspitzba-crab_Run2016D-17Jul2018-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER",      dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016E_26Sep2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_26Sep2018",        "/DoubleMuon/dspitzba-crab_Run2016E-17Jul2018-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER",      dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016F_26Sep2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_26Sep2018",        "/DoubleMuon/dspitzba-crab_Run2016F-17Jul2018-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER",      dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016G_26Sep2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016G_26Sep2018",        "/DoubleMuon/dspitzba-crab_Run2016G-17Jul2018-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER",      dbFile=dbFile, redirector=redirector, instance="phys03")
DoubleMuon_Run2016H_26Sep2018       = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_26Sep2018",        "/DoubleMuon/dspitzba-crab_Run2016H-17Jul2018-v1_METSig_v1-fb9f80af3825225a6840a52a8872bb02/USER",      dbFile=dbFile, redirector=redirector, instance="phys03")

DoubleMuon = [
    DoubleMuon_Run2016B_26Sep2018_ver1,
    DoubleMuon_Run2016B_26Sep2018_ver2,
    DoubleMuon_Run2016C_26Sep2018,
    DoubleMuon_Run2016D_26Sep2018,
    DoubleMuon_Run2016E_26Sep2018,
    DoubleMuon_Run2016F_26Sep2018,
    DoubleMuon_Run2016G_26Sep2018,
    DoubleMuon_Run2016H_26Sep2018,
]

MuonEG = [
]

DoubleEG = [
]

allSamples = DoubleMuon + MuonEG + DoubleEG

for s in allSamples:
    s.isData = True
