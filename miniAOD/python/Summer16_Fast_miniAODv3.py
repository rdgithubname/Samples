'''
miniAOD FastSim samples of Summer16 campaign, miniAODv3 (94X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer16MiniAODv3*Fast*/MINIAODSIM"
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
dbFile = dbDir+"DB_Summer16_Fast_miniAODv3.sql"

logger.info("Using db file: %s", dbFile)

## T2tt
SMS_T2tt_mStop_150to250     = FWLiteSample.fromDAS("SMS_T2tt_mStop_150to250"  , "/SMS-T2tt_mStop-150to250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_250to350     = FWLiteSample.fromDAS("SMS_T2tt_mStop_250to350"  , "/SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_350to400     = FWLiteSample.fromDAS("SMS_T2tt_mStop_350to400"  , "/SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_400to1200    = FWLiteSample.fromDAS("SMS_T2tt_mStop_400to1200" , "/SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_1200to2000   = FWLiteSample.fromDAS("SMS_T2tt_mStop_1200to2000", "/SMS-T2tt_mStop-1200to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T2tt = [
    SMS_T2tt_mStop_150to250  ,
    SMS_T2tt_mStop_250to350  ,
    SMS_T2tt_mStop_350to400  ,
    SMS_T2tt_mStop_400to1200 ,
    SMS_T2tt_mStop_1200to2000,
]


SMS_T2bW = FWLiteSample.fromDAS("SMS_T2bW", "/SMS-T2bW_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T2bW = [SMS_T2bW]

SMS_T8bbllnunu_XCha0p5_XSlep0p05                      = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05"                 , "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000         = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000"    , "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p5                       = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5"                  , "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300          = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300"     , "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p95                      = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95"                 , "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600         = FWLiteSample.fromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600"    , "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T8bbllnunu = [ SMS_T8bbllnunu_XCha0p5_XSlep0p05, SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000, SMS_T8bbllnunu_XCha0p5_XSlep0p5, SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300, SMS_T8bbllnunu_XCha0p5_XSlep0p95, SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600 ]

SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25     = FWLiteSample.fromDAS("SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25", "/SMS-T8bbstausnu_XCha0p5_mStop-200to1800_XStau0p25_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5      = FWLiteSample.fromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5" , "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75     = FWLiteSample.fromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75", "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p75_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T8bbstausnu = [ SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25, SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5, SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p75 ]

SMS_T2tt_dM_10to80 = FWLiteSample.fromDAS("SMS_T2tt_dM_10to80" , "/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

T2tt_dm10to80 = [SMS_T2tt_dM_10to80]

## sum up
allSamples = T2tt + T2bW + T8bbllnunu + T8bbstausnu + T2tt_dm10to80

for sample in allSamples:
    sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
