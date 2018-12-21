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
dbFile = dbDir+"DB_Run2018.sql"

# specify a local directory if you want to create (and afterwards automatically use) a local copy of the sample, otherwise use the grid.

## DoubleMuon
DoubleMuon_Run2018A_14Sep2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_14Sep2018_ver1",   "/DoubleMuon/Run2018A-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018A_14Sep2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_14Sep2018_ver2",   "/DoubleMuon/Run2018A-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018A_14Sep2018_ver3  = Sample.nanoAODfromDAS("DoubleMuon_Run2018A_14Sep2018_ver3",   "/DoubleMuon/Run2018A-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018B_14Sep2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_14Sep2018_ver1",   "/DoubleMuon/Run2018B-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018B_14Sep2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2018B_14Sep2018_ver2",   "/DoubleMuon/Run2018B-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018C_14Sep2018_ver1  = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_14Sep2018_ver1",   "/DoubleMuon/Run2018C-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018C_14Sep2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_14Sep2018_ver2",   "/DoubleMuon/Run2018C-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018C_14Sep2018_ver3  = Sample.nanoAODfromDAS("DoubleMuon_Run2018C_14Sep2018_ver3",   "/DoubleMuon/Run2018C-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
DoubleMuon_Run2018D_14Sep2018_ver2  = Sample.nanoAODfromDAS("DoubleMuon_Run2018D_14Sep2018_ver2",   "/DoubleMuon/Run2018D-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)

DoubleMuon_Run2018 = [\
    DoubleMuon_Run2018A_14Sep2018_ver1,
    DoubleMuon_Run2018A_14Sep2018_ver2,
    DoubleMuon_Run2018A_14Sep2018_ver3,
    DoubleMuon_Run2018B_14Sep2018_ver1,
    DoubleMuon_Run2018B_14Sep2018_ver2,
    DoubleMuon_Run2018C_14Sep2018_ver1,
    DoubleMuon_Run2018C_14Sep2018_ver2,
    DoubleMuon_Run2018C_14Sep2018_ver3,
    DoubleMuon_Run2018D_14Sep2018_ver2,
    ]

## MuonEG
MuonEG_Run2018A_14Sep2018_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2018A_14Sep2018_ver1",   "/MuonEG/Run2018A-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018A_14Sep2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2018A_14Sep2018_ver2",   "/MuonEG/Run2018A-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018A_14Sep2018_ver3  = Sample.nanoAODfromDAS("MuonEG_Run2018A_14Sep2018_ver3",   "/MuonEG/Run2018A-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018B_14Sep2018_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2018B_14Sep2018_ver1",   "/MuonEG/Run2018B-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018B_14Sep2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2018B_14Sep2018_ver2",   "/MuonEG/Run2018B-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018C_14Sep2018_ver1  = Sample.nanoAODfromDAS("MuonEG_Run2018C_14Sep2018_ver1",   "/MuonEG/Run2018C-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018C_14Sep2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2018C_14Sep2018_ver2",   "/MuonEG/Run2018C-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018C_14Sep2018_ver3  = Sample.nanoAODfromDAS("MuonEG_Run2018C_14Sep2018_ver3",   "/MuonEG/Run2018C-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
MuonEG_Run2018D_14Sep2018_ver2  = Sample.nanoAODfromDAS("MuonEG_Run2018D_14Sep2018_ver2",   "/MuonEG/Run2018D-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)

MuonEG_Run2018 = [\
    MuonEG_Run2018A_14Sep2018_ver1,
    MuonEG_Run2018A_14Sep2018_ver2,
    MuonEG_Run2018A_14Sep2018_ver3,
    MuonEG_Run2018B_14Sep2018_ver1,
    MuonEG_Run2018B_14Sep2018_ver2,
    MuonEG_Run2018C_14Sep2018_ver1,
    MuonEG_Run2018C_14Sep2018_ver2,
    MuonEG_Run2018C_14Sep2018_ver3,
    MuonEG_Run2018D_14Sep2018_ver2,
    ]

## DoubleEG
EGamma_Run2018A_14Sep2018_ver1  = Sample.nanoAODfromDAS("EGamma_Run2018A_14Sep2018_ver1",   "/EGamma/Run2018A-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018A_14Sep2018_ver2  = Sample.nanoAODfromDAS("EGamma_Run2018A_14Sep2018_ver2",   "/EGamma/Run2018A-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018A_14Sep2018_ver3  = Sample.nanoAODfromDAS("EGamma_Run2018A_14Sep2018_ver3",   "/EGamma/Run2018A-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018B_14Sep2018_ver1  = Sample.nanoAODfromDAS("EGamma_Run2018B_14Sep2018_ver1",   "/EGamma/Run2018B-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018B_14Sep2018_ver2  = Sample.nanoAODfromDAS("EGamma_Run2018B_14Sep2018_ver2",   "/EGamma/Run2018B-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018C_14Sep2018_ver1  = Sample.nanoAODfromDAS("EGamma_Run2018C_14Sep2018_ver1",   "/EGamma/Run2018C-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018C_14Sep2018_ver2  = Sample.nanoAODfromDAS("EGamma_Run2018C_14Sep2018_ver2",   "/EGamma/Run2018C-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018C_14Sep2018_ver3  = Sample.nanoAODfromDAS("EGamma_Run2018C_14Sep2018_ver3",   "/EGamma/Run2018C-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
EGamma_Run2018D_14Sep2018_ver2  = Sample.nanoAODfromDAS("EGamma_Run2018D_14Sep2018_ver2",   "/EGamma/Run2018D-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)

EGamma_Run2018 = [\
    EGamma_Run2018A_14Sep2018_ver1,
    EGamma_Run2018A_14Sep2018_ver2,
    EGamma_Run2018A_14Sep2018_ver3,
    EGamma_Run2018B_14Sep2018_ver1,
    EGamma_Run2018B_14Sep2018_ver2,
    EGamma_Run2018C_14Sep2018_ver1,
    EGamma_Run2018C_14Sep2018_ver2,
    EGamma_Run2018C_14Sep2018_ver3,
    EGamma_Run2018D_14Sep2018_ver2,
    ]


## SingleMuon
SingleMuon_Run2018A_14Sep2018_ver1  = Sample.nanoAODfromDAS("SingleMuon_Run2018A_14Sep2018_ver1",   "/SingleMuon/Run2018A-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018A_14Sep2018_ver2  = Sample.nanoAODfromDAS("SingleMuon_Run2018A_14Sep2018_ver2",   "/SingleMuon/Run2018A-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018A_14Sep2018_ver3  = Sample.nanoAODfromDAS("SingleMuon_Run2018A_14Sep2018_ver3",   "/SingleMuon/Run2018A-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018B_14Sep2018_ver1  = Sample.nanoAODfromDAS("SingleMuon_Run2018B_14Sep2018_ver1",   "/SingleMuon/Run2018B-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018B_14Sep2018_ver2  = Sample.nanoAODfromDAS("SingleMuon_Run2018B_14Sep2018_ver2",   "/SingleMuon/Run2018B-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018C_14Sep2018_ver1  = Sample.nanoAODfromDAS("SingleMuon_Run2018C_14Sep2018_ver1",   "/SingleMuon/Run2018C-14Sep2018_ver1-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018C_14Sep2018_ver2  = Sample.nanoAODfromDAS("SingleMuon_Run2018C_14Sep2018_ver2",   "/SingleMuon/Run2018C-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018C_14Sep2018_ver3  = Sample.nanoAODfromDAS("SingleMuon_Run2018C_14Sep2018_ver3",   "/SingleMuon/Run2018C-14Sep2018_ver3-v1/NANOAOD", dbFile=dbFile, redirector=redirector)
SingleMuon_Run2018D_14Sep2018_ver2  = Sample.nanoAODfromDAS("SingleMuon_Run2018D_14Sep2018_ver2",   "/SingleMuon/Run2018D-14Sep2018_ver2-v1/NANOAOD", dbFile=dbFile, redirector=redirector)

SingleMuon_Run2018 = [\
    SingleMuon_Run2018A_14Sep2018_ver1,
    SingleMuon_Run2018A_14Sep2018_ver2,
    SingleMuon_Run2018A_14Sep2018_ver3,
    SingleMuon_Run2018B_14Sep2018_ver1,
    SingleMuon_Run2018B_14Sep2018_ver2,
    SingleMuon_Run2018C_14Sep2018_ver1,
    SingleMuon_Run2018C_14Sep2018_ver2,
    SingleMuon_Run2018C_14Sep2018_ver3,
    SingleMuon_Run2018D_14Sep2018_ver2,
    ]

allSamples = DoubleMuon_Run2018 + MuonEG_Run2018 + EGamma_Run2018 + SingleMuon_Run2018

for s in allSamples:
    s.isData = True
