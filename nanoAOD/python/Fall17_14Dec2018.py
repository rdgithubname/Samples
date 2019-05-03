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
dbFile = dbDir+"/DB_Fall17_14Dec2018.sql"

logger.info("Using db file: %s", dbFile)

# specify a local directory if you want to create (and afterwards automatically use) a local copy of the sample, otherwise use the grid.

## DY
#DYJetsToLL_M50_LO       = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",      "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2008.*3, overwrite=ov)
#DYJetsToLL_M50_LO_ext1  = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext1", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2008.*3, overwrite=ov)
DYJetsToLL_M50        = Sample.nanoAODfromDAS("DYJetsToLL_M50",        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",              dbFile=dbFile, redirector=redirector, xSection=2008.*3, overwrite=ov)
DYJetsToLL_M50_ext1   = Sample.nanoAODfromDAS("DYJetsToLL_M50_ext1",   "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2008.*3, overwrite=ov)
DYJetsToLL_M10to50_LO = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, xSection=18610,   overwrite=ov)

DY = [
    DYJetsToLL_M50,
    DYJetsToLL_M50_ext1,
    DYJetsToLL_M10to50_LO,
#    DYJetsToLL_M50_LO,
#    DYJetsToLL_M50_LO_ext1,
#    DYJetsToLL_M5to50_LO,
    ]

# DY HT bins, M_{ll} [50, inf]
DYJetsToLL_M50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100",      "/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, xSection=170.4*1.23,    overwrite=ov)
DYJetsToLL_M50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200",     "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, xSection=147.4*1.23,    overwrite=ov)
DYJetsToLL_M50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200_ext", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, xSection=147.4*1.23,    overwrite=ov)
DYJetsToLL_M50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",     "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, xSection=40.99*1.23,    overwrite=ov)
DYJetsToLL_M50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400_ext", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, xSection=40.99*1.23,    overwrite=ov)
DYJetsToLL_M50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",     "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, xSection=5.678*1.23,    overwrite=ov)
DYJetsToLL_M50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600_ext", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, xSection=5.678*1.23,    overwrite=ov)
DYJetsToLL_M50_HT600to800     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800",     "/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, xSection=1.367*1.23,    overwrite=ov)
DYJetsToLL_M50_HT800to1200    = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200",    "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.6304*1.23,   overwrite=ov)
DYJetsToLL_M50_HT1200to2500   = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500",   "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, xSection=0.1514*1.23,   overwrite=ov)
DYJetsToLL_M50_HT2500toInf    = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf",    "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.003565*1.23, overwrite=ov)

DYJetsM50HT = [
    DYJetsToLL_M50_HT70to100, 
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT100to200_ext,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT200to400_ext,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT400to600_ext,
    DYJetsToLL_M50_HT600to800,
    DYJetsToLL_M50_HT800to1200,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf,
    ]


# DY HT bins, M_{ll} [4, 50]
#DYJetsToLL_M4to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT70to100",      "/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM",                     dbFile=dbFile, redirector=redirector, xSection=303.4, overwrite=ov) #LO without 1.23 k-factor # NOTE: missing
DYJetsToLL_M4to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT100to200",     "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, xSection=224.2, overwrite=ov) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT100to200_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT100to200_ext", "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, xSection=224.2, overwrite=ov) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400",     "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=37.2,  overwrite=ov) #LO without 1.23 k-factor
#DYJetsToLL_M4to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400",     "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, xSection=37.2,  overwrite=ov) #LO without 1.23 k-factor # NOTE: superseded by new pmx?
DYJetsToLL_M4to50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400_ext", "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, xSection=37.2,  overwrite=ov) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600",     "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, xSection=3.581, overwrite=ov) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600_ext", "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, xSection=3.581, overwrite=ov) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf",     "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, xSection=1.124, overwrite=ov) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT600toInf_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf_ext", "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, xSection=1.124, overwrite=ov) #LO without 1.23 k-factor


DYJetsM5to50HT = [
    #DYJetsToLL_M4to50_HT70to100,
    DYJetsToLL_M4to50_HT100to200,
    DYJetsToLL_M4to50_HT100to200_ext,
    DYJetsToLL_M4to50_HT200to400,
    DYJetsToLL_M4to50_HT200to400_ext,
    DYJetsToLL_M4to50_HT400to600,
    DYJetsToLL_M4to50_HT400to600_ext,
    DYJetsToLL_M4to50_HT600toInf,
    DYJetsToLL_M4to50_HT600toInf_ext,
]

DY += DYJetsM50HT + DYJetsM5to50HT

### TTbar
TTLep_pow      = Sample.nanoAODfromDAS("TTLep_pow",     "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=831.762*((3*0.108)**2) , overwrite=ov)
TTSemiLep_pow  = Sample.nanoAODfromDAS("TTSemiLep_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",    dbFile=dbFile, redirector=redirector, xSection=831.762*(3*0.108)*(1-3*0.108)*2 , overwrite=ov)
TTHad_pow      = Sample.nanoAODfromDAS("TTHad_pow",     "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, xSection=831.762*((1-3*0.108)**2) , overwrite=ov)
#TTbar          = Sample.nanoAODfromDAS("TTbar", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PUMoriond17_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=831.762, overwrite=ov)

## TTbar+jets
TTJets_amcatnlo   = Sample.nanoAODfromDAS("TTJets_amcatnlo",   "/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM",          dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=831.762)

# leptonic
TTJets_DiLept     = Sample.nanoAODfromDAS("TTJets_DiLept",     "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=87.31483776) # NOTE: genMET-150 version exists

TTJets_SingleLeptonFromT        = Sample.nanoAODfromDAS("TTJets_SingleLeptonFromT",        "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=182.17540224) # NOTE: genMET-150 version exists
TTJets_SingleLeptonFromTbar     = Sample.nanoAODfromDAS("TTJets_SingleLeptonFromTbar",     "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",      dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=182.17540224) # NOTE: genMET-150 version exists

TTJets = [
    TTJets_amcatnlo,
    TTJets_DiLept,
    TTJets_SingleLeptonFromT,
    TTJets_SingleLeptonFromTbar,
    ]

### Single Top
# NOTE: x-check xsecs (https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma)

#TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=(7.20+4.16)*0.108*3, overwrite=ov)

T_tch_powheg    = Sample.nanoAODfromDAS("T_tch_powheg",    "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, xSection=136.02, overwrite=ov) # inclusive sample # NOTE: PSweights version
#T_tch_powheg    = Sample.nanoAODfromDAS("T_tch_powheg",    "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=136.02, overwrite=ov) # inclusive sample # NOTE: PSweights version exists - supersedes this?
TBar_tch_powheg = Sample.nanoAODfromDAS("TBar_tch_powheg", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, xSection=80.95,  overwrite=ov) # inclusive sample # NOTE: PSweights version
#TBar_tch_powheg = Sample.nanoAODfromDAS("TBar_tch_powheg", "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, xSection=80.95,  overwrite=ov) # inclusive sample # NOTE: PSweights version exists - supersedes this?

# NOTE: what about ST_t-channel_(anti)top_5f?

T_tWch          = Sample.nanoAODfromDAS("T_tWch",          "/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, xSection=35.85, overwrite=ov) # NOTE: NNLO xsec from twiki # NOTE: PSweights version
#T_tWch          = Sample.nanoAODfromDAS("T_tWch",          "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",                          dbFile=dbFile, redirector=redirector, xSection=35.85, overwrite=ov) # NOTE: NNLO xsec from twiki # NOTE: PSweights version exists - supersedes this?
TBar_tWch       = Sample.nanoAODfromDAS("TBar_tWch",       "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",            dbFile=dbFile, redirector=redirector, xSection=35.85, overwrite=ov) # NOTE: NNLO xsec from twiki # NOTE: PSweights version
#TBar_tWch       = Sample.nanoAODfromDAS("TBar_tWch",       "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",                      dbFile=dbFile, redirector=redirector, xSection=35.85, overwrite=ov) # NOTE: NNLO xsec from twiki # NOTE: PSweights version exists - supersedes this?

## ttH
#TTHbb                   = Sample.nanoAODfromDAS("TTHbb",                  "/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.5085*(0.577), overwrite=ov)
#TTHnobb_pow             = Sample.nanoAODfromDAS("TTHnobb_pow",            "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.5085*(1-0.577), overwrite=ov)
#TTHnobb_mWCutfix_ext    = Sample.nanoAODfromDAS("TTHnobb_mWCutfix_ext",   "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.5085*(1-0.577), overwrite=ov)

#THQ = Sample.nanoAODfromDAS("THQ", "/THQ_4f_Hincl_13TeV_madgraph_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.07096, overwrite=ov)
#THW = Sample.nanoAODfromDAS("THW", "/THW_5f_Hincl_13TeV_madgraph_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.1472, overwrite=ov)

## ttV
TTW_LO              = Sample.nanoAODfromDAS("TTW_LO", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, xSection=0.6105 , overwrite=ov)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.5297/0.692, overwrite=ov)

#TGJets              = Sample.nanoAODfromDAS("TGJets",     "/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2.967, overwrite=ov)
tZq_ll_ext          = Sample.nanoAODfromDAS("tZq_ll_ext", "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.09418 , overwrite=ov) #0.0758 )
#tWll                = Sample.nanoAODfromDAS("tWll",       "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.01123, overwrite=ov)
#tWnunu              = Sample.nanoAODfromDAS("tWnunu",     "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.01123*1.9822 , overwrite=ov)

#TTWToLNu            = Sample.nanoAODfromDAS("TTWToLNu", "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.2043, overwrite=ov)
#TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ", "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.40620, overwrite=ov)
#TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ","/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.5297, overwrite=ov)
#TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.2728, overwrite=ov)
#TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.0493, overwrite=ov)

TTGJets             = Sample.nanoAODfromDAS("TTGJets",    "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=3.697, overwrite=ov)
#TTGJets_ext         = Sample.nanoAODfromDAS("TTGJets_ext","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=3.697, overwrite=ov)

#TTGHad              = Sample.nanoAODfromDAS("TTGHad",      "/TTGamma_Hadronic_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.794*3.062342569, overwrite=ov)
#TTGSemiTbar         = Sample.nanoAODfromDAS("TTGSemiTbar", "/TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.769*2.028673602, overwrite=ov)
#TTGSemiT            = Sample.nanoAODfromDAS("TTGSemiT",    "/TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.769*2.028673602, overwrite=ov)
#TTGLep              = Sample.nanoAODfromDAS("TTGLep",      "/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.607*1.574299835, overwrite=ov)

TTV_LO = [
    TTW_LO,
    TTZ_LO,
    ]

TTV = [
#    TGJets,
#    TGJets_ext,
    tZq_ll_ext,
#    tWll,
#    tWnunu,
#    TTWToLNu,
#    TTWToQQ,
#    TTZToQQ,
#    TTZToLLNuNu,
#    TTZToLLNuNu_m1to10,
    TTGJets,
#    TTGJets_ext,
#    TTGHad,
#    TTGSemiTbar,
#    TTGSemiT,
#    TTGLep,
    ] + TTV_LO

ST = [
    #TToLeptons_sch_amcatnlo,
    T_tch_powheg,
    TBar_tch_powheg,
    T_tWch,
    TBar_tWch,
    ]

top = [
    TTLep_pow,
    TTSemiLep_pow,
    TTHad_pow,
#    TTbar,
#    TTHbb,
#    TTHnobb_pow,
#    TTHnobb_mWCutfix_ext,
#    THQ,
#    THW,
    ] + TTJets + ST + TTV

### di/multiboson
# NOTE: x-check xsec (https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson)

WWTo2L2Nu     = Sample.nanoAODfromDAS("WWTo2L2Nu",     "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",                dbFile=dbFile, redirector=redirector, xSection=12.178, overwrite=ov) # NOTE: NNLO x-sec from twiki
WWTo2L2Nu_ext = Sample.nanoAODfromDAS("WWTo2L2Nu_ext", "/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=12.178, overwrite=ov) # NOTE: NNLO x-sec from twiki # NOTE: PS weights version
WWToLNuQQ     = Sample.nanoAODfromDAS("WWToLNuQQ",     "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",        dbFile=dbFile, redirector=redirector, xSection=49.997, overwrite=ov) # NOTE: NNLO x-sec from twiki
WWToLNuQQ_ext = Sample.nanoAODfromDAS("WWToLNuQQ_ext", "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=49.997, overwrite=ov) # NOTE: NNLO x-sec from twiki # NOTE: PS weights version 
#WWToLNuQQ_ext = Sample.nanoAODfromDAS("WWToLNuQQ_ext", "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",           dbFile=dbFile, redirector=redirector, xSection=49.997, overwrite=ov) # NOTE: PSweights version exists - supersedes this?
WWTo1L1Nu2Q   = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",   "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",                dbFile=dbFile, redirector=redirector, xSection=49.997, overwrite=ov)

WZTo1L3Nu         = Sample.nanoAODfromDAS("WZTo1L3Nu",         "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",     dbFile=dbFile, redirector=redirector, xSection=(47.13)*(3*0.108)*(0.2), overwrite=ov)
WZTo1L1Nu2Q       = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",       "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",      dbFile=dbFile, redirector=redirector, xSection=10.71,    overwrite=ov)
WZTo2L2Q          = Sample.nanoAODfromDAS("WZTo2L2Q",          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, redirector=redirector, xSection=5.60,     overwrite=ov)
WZTo3LNu          = Sample.nanoAODfromDAS("WZTo3LNu",          "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=4.42965,  overwrite=ov)

WZTo3LNu_amcatnlo = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=4.666,    overwrite=ov)
#WZTo3LNu_mllmin01 =Sample.nanoAODfromDAS("WZTo3LNu_mllmin01", "/WZTo3LNu_mllmin01_13TeV-powheg-pythia8_ext1/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=58.59, overwrite=ov)
# NOTE: WZTo3LNu_*Jets_MLL-* samples exist

#WZJToLLLNu      = Sample.nanoAODfromDAS("WZJToLLLNu",  "/WZJToLLLNu_TuneCUETP8M1_13TeV-amcnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"  , "CMS", ".*root", 4.708 , overwrite=ov)

ZZTo2L2Nu       = Sample.nanoAODfromDAS("ZZTo2L2Nu",   "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",                       dbFile=dbFile, redirector=redirector, xSection=0.564,     overwrite=ov)
ZZTo2L2Q        = Sample.nanoAODfromDAS("ZZTo2L2Q",    "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",          dbFile=dbFile, redirector=redirector, xSection=3.28,      overwrite=ov)
ZZTo2Q2Nu       = Sample.nanoAODfromDAS("ZZTo2Q2Nu",   "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=4.04,      overwrite=ov)
ZZTo4L          = Sample.nanoAODfromDAS("ZZTo4L",      "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",                  dbFile=dbFile, redirector=redirector, xSection=1.256*1.1, overwrite=ov)
#ZZTo4L          = Sample.nanoAODfromDAS("ZZTo4L",      "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",                          dbFile=dbFile, redirector=redirector, xSection=1.256*1.1, overwrite=ov) # NOTE: superseded by new pmx?
ZZTo4L_ext1     = Sample.nanoAODfromDAS("ZZTo4L_ext1", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM",                     dbFile=dbFile, redirector=redirector, xSection=1.256*1.1, overwrite=ov)

VVTo2L2Nu       = Sample.nanoAODfromDAS("VVTo2L2Nu","/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, xSection=11.95, overwrite=ov)
#VVTo2L2Nu_ext   = Sample.nanoAODfromDAS("VVTo2L2Nu_ext" ,"/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM",  dbFile=dbFile, redirector=redirector, xSection=11.95, overwrite=ov)

#WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", "/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=585.8, overwrite=ov)
#WGToLNuG_amcatnlo_ext1  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext1", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=585.8, overwrite=ov) # cross section copied from MLM sample above, to be checked
#WGToLNuG_amcatnlo_ext3  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext3", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=585.8, overwrite=ov) # cross section copied from MLM sample above, to be checked

#WGJets              = Sample.nanoAODfromDAS("WGJets", "/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.6637, overwrite=ov)
#ZNuNuGJets              = Sample.nanoAODfromDAS("ZNuNuGJets", "/ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.1903, overwrite=ov)
#ZNuNuGJets_40130    = Sample.nanoAODfromDAS("ZNuNuGJets_40130", "/ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=2.816, overwrite=ov)

#ZGTo2NuG            = Sample.nanoAODfromDAS("ZGTo2NuG","/ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=28.05, overwrite=ov)
#ZGTo2LG_ext         = Sample.nanoAODfromDAS("ZGTo2LG_ext", "/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=131.3, overwrite=ov)

#WWDoubleTo2L    = Sample.nanoAODfromDAS("WWDoubleTo2L", "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.1729, overwrite=ov)
#WpWpJJ          = Sample.nanoAODfromDAS("WpWpJJ", "/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.03711, overwrite=ov)


#WW      = Sample.nanoAODfromDAS("WW", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=63.21 * 1.82, overwrite=ov)
#WZ      = Sample.nanoAODfromDAS("WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=47.13, overwrite=ov)
#ZZ      = Sample.nanoAODfromDAS("ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=16.523, overwrite=ov)

#WWW_4F  = Sample.nanoAODfromDAS("WWW_4F", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.2086, overwrite=ov)
#WWZ     = Sample.nanoAODfromDAS("WWZ", "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.1651, overwrite=ov)
#WZG     = Sample.nanoAODfromDAS("WZG", "/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.04123, overwrite=ov)
#WZZ     = Sample.nanoAODfromDAS("WZZ", "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.05565, overwrite=ov)
#ZZZ     = Sample.nanoAODfromDAS("ZZZ", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.01398, overwrite=ov)

VV_NLO = [
    WWTo2L2Nu,
    WWTo2L2Nu_ext,
    WWToLNuQQ,
    WWToLNuQQ_ext,
    WWTo1L1Nu2Q,
    
    WZTo1L3Nu,
    WZTo1L1Nu2Q,
    WZTo2L2Q,
    WZTo3LNu,
    
    ZZTo2L2Nu,
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo4L,
    ZZTo4L_ext1,
    ]

boson = [
#    WZTo3LNu_mllmin01,
    WZTo3LNu_amcatnlo,
    VVTo2L2Nu,
#    VVTo2L2Nu_ext,
#    WGToLNuG,
#    WGToLNuG_amcatnlo_ext1,
#    WGToLNuG_amcatnlo_ext3,
#    WGJets,
#    ZNuNuGJets_40130,
#    ZGTo2NuG,
#    ZGTo2LG_ext,
#    WWDoubleTo2L,
#    WpWpJJ,
#    WW,
#    WZ,
#    ZZ,
#    WWW_4F,
#    WWZ,
#    WZG,
#    WZZ,
#    ZZZ,
    ] + VV_NLO

### W+jets

## inclusive
WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",     "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=3* 20508.9, overwrite=ov)
WJetsToLNu_ext  = Sample.nanoAODfromDAS("WJetsToLNu_ext", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=3* 20508.9, overwrite=ov)

wjets_inc = [
    WJetsToLNu,
    WJetsToLNu_ext,
    ]

## HT-binned
#WJetsToLNu_HT70to100    = Sample.nanoAODfromDAS("WJetsToLNu_HT70to100",    "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1637.13) # NOTE: missing
WJetsToLNu_HT100to200   = Sample.nanoAODfromDAS("WJetsToLNu_HT100to200",   "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1627.45)
WJetsToLNu_HT200to400   = Sample.nanoAODfromDAS("WJetsToLNu_HT200to400",   "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=435.237)
WJetsToLNu_HT400to600   = Sample.nanoAODfromDAS("WJetsToLNu_HT400to600",   "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=59.1811)
WJetsToLNu_HT600to800   = Sample.nanoAODfromDAS("WJetsToLNu_HT600to800",   "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=14.5805)
WJetsToLNu_HT800to1200  = Sample.nanoAODfromDAS("WJetsToLNu_HT800to1200",  "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6.65621)
WJetsToLNu_HT1200to2500 = Sample.nanoAODfromDAS("WJetsToLNu_HT1200to2500", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.60809)
WJetsToLNu_HT2500toInf  = Sample.nanoAODfromDAS("WJetsToLNu_HT2500toInf",  "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",  dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.0389136)

wjets_ht = [
    #WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    WJetsToLNu_HT200to400,
    WJetsToLNu_HT400to600,
    WJetsToLNu_HT600to800,
    WJetsToLNu_HT800to1200,
    WJetsToLNu_HT1200to2500,
    WJetsToLNu_HT2500toInf,
    ]

wjets = wjets_inc + wjets_ht

## rare
#TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_pilot_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.009103, overwrite=ov)
#TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.007829, overwrite=ov)
#TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.002919, overwrite=ov)
#TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.001573, overwrite=ov)

rare = [
#    TTTT,
#    TTWW,
#    TTWZ,
#    TTZZ,
    ]


## Signals
#T2tt_mStop_1200_mLSP_100 = Sample.nanoAODfromDAS("T2tt_mStop_1200_mLSP_100", "/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1, overwrite=ov)
#T2tt_mStop_850_mLSP_100 = Sample.nanoAODfromDAS("T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1, overwrite=ov)
#T2tt_mStop_650_mLSP_350 = Sample.nanoAODfromDAS("T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=1, overwrite=ov)


#GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.005423, overwrite=ov)
#GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.005423, overwrite=ov)
#GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.005423, overwrite=ov)
#GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.0027, overwrite=ov)
#GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.0027, overwrite=ov)
#GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/NANOAODSIM", dbFile=dbFile, redirector=redirector, xSection=0.0027, overwrite=ov)

gluglu = [
#    GluGluToContinToZZTo2e2mu,
#    GluGluToContinToZZTo2e2tau,
#    GluGluToContinToZZTo2mu2tau,
#    GluGluToContinToZZTo4e,
#    GluGluToContinToZZTo4mu,
#    GluGluToContinToZZTo4tau,
]

### QCD

## QCD HT bins (cross sections from McM)

#QCD_HT50to100    = Sample.nanoAODfromDAS("QCD_HT50to100",    "/QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=246400000.0) #NOTE: missing
QCD_HT100to200   = Sample.nanoAODfromDAS("QCD_HT100to200",   "/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=27850000.0)
QCD_HT200to300   = Sample.nanoAODfromDAS("QCD_HT200to300",   "/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1717000)
QCD_HT300to500   = Sample.nanoAODfromDAS("QCD_HT300to500",   "/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=351300)
QCD_HT500to700   = Sample.nanoAODfromDAS("QCD_HT500to700",   "/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=31630)
QCD_HT700to1000  = Sample.nanoAODfromDAS("QCD_HT700to1000",  "/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=6802)
QCD_HT1000to1500 = Sample.nanoAODfromDAS("QCD_HT1000to1500", "/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1206)
QCD_HT1500to2000 = Sample.nanoAODfromDAS("QCD_HT1500to2000", "/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",       dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=120.4)
QCD_HT2000toInf  = Sample.nanoAODfromDAS("QCD_HT2000toInf",  "/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",        dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=25.25)

QCD = [
    #QCD_HT50to100,
    QCD_HT100to200,
    QCD_HT200to300,
    QCD_HT300to500,
    QCD_HT500to700,
    QCD_HT700to1000,
    QCD_HT1000to1500,
    QCD_HT1500to2000,
    QCD_HT2000toInf,
    ]

### Zinv
# NOTE: x-check xsecs (https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#DY_Z)

ZJetsToNuNu_HT100to200   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT100to200",   "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",           dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=344.9781)
ZJetsToNuNu_HT200to400   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT200to400",   "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",           dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=96.3828)
ZJetsToNuNu_HT400to600   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT400to600",   "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=13.4562)
#ZJetsToNuNu_HT400to600   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT400to600",   "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",           dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=13.4562) # NOTE: superseded by new pmx?
ZJetsToNuNu_HT600to800   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT600to800",   "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM",   dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.96183)
#ZJetsToNuNu_HT600to800   = Sample.nanoAODfromDAS("ZJetsToNuNu_HT600to800",   "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",           dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=3.96183) # NOTE: superseded by new pmx?
ZJetsToNuNu_HT800to1200  = Sample.nanoAODfromDAS("ZJetsToNuNu_HT800to1200",  "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",          dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1.81302)
ZJetsToNuNu_HT1200to2500 = Sample.nanoAODfromDAS("ZJetsToNuNu_HT1200to2500", "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_new_pmx_102X_mc2017_realistic_v6-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.441078)
#ZJetsToNuNu_HT1200to2500 = Sample.nanoAODfromDAS("ZJetsToNuNu_HT1200to2500", "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",         dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.441078) # NOTE: superseded by new pmx?
ZJetsToNuNu_HT2500toInf  = Sample.nanoAODfromDAS("ZJetsToNuNu_HT2500toInf",  "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1/NANOAODSIM",          dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.01008969)

Zinv = [
    ZJetsToNuNu_HT100to200,
    ZJetsToNuNu_HT200to400,
    ZJetsToNuNu_HT400to600,
    ZJetsToNuNu_HT600to800,
    ZJetsToNuNu_HT800to1200,
    ZJetsToNuNu_HT1200to2500,
    ZJetsToNuNu_HT2500toInf,
    ]

### Signals
signals = [
    ]

### Other
other = [
    ]

allSamples = DY + top + boson + wjets + rare + gluglu + QCD + Zinv + signals + other

soft1LepSamples = wjets + TTJets + Zinv + QCD + DYJetsM50HT + DYJetsM5to50HT + ST + TTV_LO + VV_NLO + signals

for s in allSamples:
    s.isData = False
