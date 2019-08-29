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
dbFile = dbDir+"/DB_Autumn18_private_legacy.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO        = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",       "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=False, xSection=2075.14*3)
#DYJetsToLL_M50_LO_ext2   = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext2",  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M50           = Sample.nanoAODfromDAS("DYJetsToLL_M50",          "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M10to50_LO    = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",   "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18610)

# x-secs using runXSecAnalyzer
DYJetsToLL_M50_HT70to100      =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100",         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=146.5*1.23)
DYJetsToLL_M50_HT100to200     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200",        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=160.1*1.23)
DYJetsToLL_M50_HT200to400     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.22*1.23)
DYJetsToLL_M50_HT400to600     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v7_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=6.996*1.23)
DYJetsToLL_M50_HT400to600_ext =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600_ext",    "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext2-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=6.996*1.23)
DYJetsToLL_M50_HT600to800     =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800"   ,     "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.754*1.23 )
DYJetsToLL_M50_HT800to1200    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200"  ,     "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.8718*1.23 )
DYJetsToLL_M50_HT1200to2500   =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500" ,     "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1938*1.23 )
DYJetsToLL_M50_HT2500toInf    =   Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf"  ,     "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.003511*1.23 )

DYJetsM50HT = [
    DYJetsToLL_M50_HT70to100, 
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT400to600_ext,
    DYJetsToLL_M50_HT600to800  ,
    DYJetsToLL_M50_HT800to1200 ,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf ,
]

# x-secs using runXSecAnalyzer
DYJetsToLL_M4to50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT70to100"     , "/DYJetsToLL_M-4to50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=147.7) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT100to200"    , "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=203.2) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400"    , "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=54.06) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600"    , "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.696) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf"    , "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.843) #LO without 1.23 k-factor

DYJetsM4to50HT = [
   DYJetsToLL_M4to50_HT70to100,
   DYJetsToLL_M4to50_HT100to200,
   DYJetsToLL_M4to50_HT200to400,
   DYJetsToLL_M4to50_HT400to600,
   DYJetsToLL_M4to50_HT600toInf,
]


DY = [
    DYJetsToLL_M50_LO,
#    DYJetsToLL_M50_LO_ext2,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50,
] + DYJetsM50HT + DYJetsM4to50HT

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((3*0.108)**2))
TTSingleLep_pow = Sample.nanoAODfromDAS("TTSingleLep_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTHad_pow       = Sample.nanoAODfromDAS("TTHad_pow",       "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((1-3*0.108)**2))
TTbar           = Sample.nanoAODfromDAS("TTbar",           "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, instance="phys03", overwrite=ov, redirector=redirector, xSection=831.762)
TTLep_NLO       = Sample.nanoAODfromDAS("TTLep_NLO",       "/TT_DiLept_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((3*0.108)**2))

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v4_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(7.20+4.16)*0.108*3)

T_tch_pow           = Sample.nanoAODfromDAS("T_tch_pow",        "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow        = Sample.nanoAODfromDAS("TBar_tch_pow",     "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=80.95) # inclusive sample

T_tWch              = Sample.nanoAODfromDAS("T_tWch",           "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85)
TBar_tWch           = Sample.nanoAODfromDAS("TBar_tWch",        "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85)

## ttH
TTHbbSemiLep        = Sample.nanoAODfromDAS("TTHbbSemiLep",     "/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(0.577)*(3*0.108)*(1-3*0.108)*2)
TTHbbLep            = Sample.nanoAODfromDAS("TTHbbLep",         "/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(0.577)*((3*0.108)**2))
TTHnobb_pow         = Sample.nanoAODfromDAS("TTHnobb_pow",      "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(1-0.577))

THQ                 = Sample.nanoAODfromDAS("THQ",              "/THQ_4f_Hincl_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.07096)
THW                 = Sample.nanoAODfromDAS("THW",              "/THW_5f_Hincl_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1472)

## ttV
TGJets              = Sample.nanoAODfromDAS("TGJets",     "/TGJets_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967)
#TGJets_ext          = Sample.nanoAODfromDAS("TGJets_ext", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967)
tZq_ll              = Sample.nanoAODfromDAS("tZq_ll",           "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                             dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.09418 ) #0.0758 )
tWll                = Sample.nanoAODfromDAS("tWll",             "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123)
tWnunu              = Sample.nanoAODfromDAS("tWnunu",           "/ST_tWnunu_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123*1.9822)
TTWToLNu            = Sample.nanoAODfromDAS("TTWToLNu",         "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2043)
TTWToQQ             = Sample.nanoAODfromDAS("TTWToQQ",          "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.40620)
TTW_LO              = Sample.nanoAODfromDAS("TTW_LO",           "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6105)
TTZToQQ             = Sample.nanoAODfromDAS("TTZToQQ",          "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-7c817823a2fb84971bb73c175ef352d5/USER",                       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297)
TTZToLLNuNu         = Sample.nanoAODfromDAS("TTZToLLNuNu",        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728)
TTZToLLNuNu_m1to10  = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0493)
TTZ_LO              = Sample.nanoAODfromDAS("TTZ_LO",           "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                                 dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297/0.692)
#TTGJets             = Sample.nanoAODfromDAS("TTGJets",          "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)
#TTGJets_ext         = Sample.nanoAODfromDAS("TTGJets_ext",      "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)
TTGHad              = Sample.nanoAODfromDAS("TTGHad",           "/TTGamma_Hadronic_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.794*3.062342569) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
TTGSemiTbar         = Sample.nanoAODfromDAS("TTGSemiTbar",      "/TTGamma_SingleLeptFromTbar_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.769*2.028673602) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
TTGSemiT            = Sample.nanoAODfromDAS("TTGSemiT",         "/TTGamma_SingleLeptFromT_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.769*2.028673602) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)
TTGLep              = Sample.nanoAODfromDAS("TTGLep",           "/TTGamma_Dilept_TuneCP5_13TeV_madgraph_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.607*1.574299835) # MadGraph LO xsec * k factor estimated in TOPAZ (TOP-18-010)

TTV = [
    TGJets,
#    TGJets_ext,
    TTGHad,
    TTGSemiT,
    TTGSemiTbar,
    TTGLep,
    tZq_ll,
    tWll,
    tWnunu,
    TTWToLNu,
    TTWToQQ,
    TTW_LO,
    TTZToQQ,
    TTZToLLNuNu,
    TTZToLLNuNu_m1to10,
    TTZ_LO,
#    TTGJets,
#    TTGJets_ext
]

top = [
    TTLep_pow,
    TTSingleLep_pow,
    TTHad_pow,
    TTbar,
    TTLep_NLO,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch,
    TBar_tWch,
    TTHbbLep,
    TTHbbSemiLep,
    TTHnobb_pow,
#    TTHnobb_mWCutfix_ext,
    THQ,
    THW,
    ] + TTV

## di/multiboson
WWTo2L2Nu           = Sample.nanoAODfromDAS("WWTo2L2Nu",        "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=12.178 )
WWDoubleTo2L        = Sample.nanoAODfromDAS("WWDoubleTo2L",         "/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1729)
WWToLNuQQ           = Sample.nanoAODfromDAS("WWToLNuQQ",        "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997)
#WWToLNuQQ_ext       = Sample.nanoAODfromDAS("WWToLNuQQ_ext",    "/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997)
WWTo1L1Nu2Q         = Sample.nanoAODfromDAS("WWTo1L1Nu2Q",          "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997)

ZZTo2L2Nu           = Sample.nanoAODfromDAS("ZZTo2L2Nu",            "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.564)
ZZTo2L2Q            = Sample.nanoAODfromDAS("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.28)
ZZTo2Q2Nu           = Sample.nanoAODfromDAS("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.04)
ZZTo4L              = Sample.nanoAODfromDAS("ZZTo4L",               "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                      dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.256*1.1)

WZTo1L3Nu           = Sample.nanoAODfromDAS("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=10.71)
WZTo2L2Q            = Sample.nanoAODfromDAS("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",           dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.60)
WZTo3LNu_ext        = Sample.nanoAODfromDAS("WZTo3LNu_ext",         "/WZTo3LNu_TuneCP5_13TeV-powheg-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.42965)
WZTo3LNu_amcatnlo   = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo",    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",              dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.666)

VVTo2L2Nu           = Sample.nanoAODfromDAS("VVTo2L2Nu",            "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=14.00)

WGToLNuG                = Sample.nanoAODfromDAS("WGToLNuG", "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=557.46) # NLO xsec from TOP-17-016 * NNLO scale factor from Tom Cornelis 489 (NLO) * 1.14
WGToLNuG_amcatnlo_ext1  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext1", "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=203.3)
#WGToLNuG_amcatnlo_ext3  = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo_ext3", "/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext3-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=203.3)
#WGJets              = Sample.nanoAODfromDAS("WGJets", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6637)
#ZNuNuGJets              = Sample.nanoAODfromDAS("ZNuNuGJets", "/ZNuNuGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1903)
#ZNuNuGJets_40130    = Sample.nanoAODfromDAS("ZNuNuGJets_40130", "/ZNuNuGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.816)

#ZH_HtoBB_ZtoLL      = Sample.nanoAODfromDAS("ZH_HtoBB_ZtoLL", "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=)
ZGToLLG             = Sample.nanoAODfromDAS("ZGToLLG",         "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=50.2)
ZGToLLG_lowMLL      = Sample.nanoAODfromDAS("ZGToLLG_lowMLL",  "/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=106.1*1.06) 
#NLO xsec * NNLO k-factor from 7TeV calculations (Tom) https://hypernews.cern.ch/HyperNews/CMS/get/generators/2772/1/1/1/1/1/1/1/1.html

WW                  = Sample.nanoAODfromDAS("WW",                   "/WW_TuneCP5_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
#WW_ext              = Sample.nanoAODfromDAS("WW_ext",               "/WW_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
WZ                  = Sample.nanoAODfromDAS("WZ",                   "/WZ_TuneCP5_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
#WZ_ext              = Sample.nanoAODfromDAS("WZ_ext",               "/WZ_TuneCUETP8M1_13TeV-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2_legacy_nano_v1-b9659cf3bef5e21efe24288a402778f7/USER",                    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
ZZ                  = Sample.nanoAODfromDAS("ZZ",                   "/ZZ_TuneCP5_13TeV-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",                         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=16.523)

WWW_4F              = Sample.nanoAODfromDAS("WWW_4F",               "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2086)
WWZ                 = Sample.nanoAODfromDAS("WWZ",                  "/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1651)
WZZ                 = Sample.nanoAODfromDAS("WZZ",                  "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.05565)
ZZZ                 = Sample.nanoAODfromDAS("ZZZ",                  "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER ",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01398)




boson = [
#    ZH_HtoBB_ZtoLL,
    WWTo2L2Nu,
    WWToLNuQQ,
#    WWToLNuQQ_ext,
    WWTo1L1Nu2Q,
    WWDoubleTo2L,
    ZZTo2L2Nu,
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo4L,
    WZTo1L3Nu,
#    WZTo1L1Nu2Q,
    WZTo2L2Q,
    WZTo3LNu_ext,
    WZTo3LNu_amcatnlo,
    VVTo2L2Nu,
    WGToLNuG,
    WGToLNuG_amcatnlo_ext1,
#    WGToLNuG_amcatnlo_ext3,
#    WGJets,
#    ZNuNuGJets_40130,
    ZGToLLG,
    ZGToLLG_lowMLL,
    WW,
#    WW_ext,
    WZ,
#    WZ_ext,
    ZZ,
    WWW_4F,
    WWZ,
    WZZ,
    ZZZ,
    ]

# W+jets
WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",           "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)
#WJetsToLNu_ext  = Sample.nanoAODfromDAS("WJetsToLNu_ext",       "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2_legacy_nano_v3-b9659cf3bef5e21efe24288a402778f7/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)

wjets = [
    WJetsToLNu,
#    WJetsToLNu_ext,
    ]

## rare
TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", xSection=0.009103)
#TTWH = Sample.nanoAODfromDAS("TTWH", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=) #sample is processed, xsec is missing
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.007829)
TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.001573)

rare = [
    TTTT,
#    TTWH,
    TTWW,
    TTWZ,
    TTZZ,
    ]

SMS_T2tt_mStop_175_mLSP_1   = Sample.nanoAODfromDAS("SMS_T2tt_mStop_175_mLSP_1", "/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-7c817823a2fb84971bb73c175ef352d5/USER"  , dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_250_mLSP_50  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250_mLSP_50", "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-7c817823a2fb84971bb73c175ef352d5/USER" , dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_250_mLSP_75  = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250_mLSP_75", "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75_TuneCP5_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-7c817823a2fb84971bb73c175ef352d5/USER" , dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_250_mLSP_100 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250_mLSP_100", "/SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-7c817823a2fb84971bb73c175ef352d5/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)

SMS_T2tt_mStop_650_mLSP_350 = Sample.nanoAODfromDAS("SMS_T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-7c817823a2fb84971bb73c175ef352d5/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)


#SMS_T2tt_mStop_150to250    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_150to250",     "/SMS-T2tt_mStop-150to250_TuneCP2_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3_legacy_nano_v4-36a19a6bcc34dfe82a820b9da3364231/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#SMS_T2tt_mStop_250to350    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250to350",     "/SMS-T2tt_mStop-250to350_TuneCP2_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3_legacy_nano_v4-36a19a6bcc34dfe82a820b9da3364231/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#SMS_T2tt_mStop_350to400    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_350to400",     "/SMS-T2tt_mStop-350to400_TuneCP2_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3_legacy_nano_v4-36a19a6bcc34dfe82a820b9da3364231/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
#SMS_T2tt_mStop_400to1200   = Sample.nanoAODfromDAS("SMS_T2tt_mStop_400to1200",    "/SMS-s2tt_mStop-400to1200_TuneCP2_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2_legacy_nano_v4-36a19a6bcc34dfe82a820b9da3364231/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)

SMS_T2tt_mStop_150to250     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_150to250", "/SMS-T2tt_mStop-150to250_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_250to350     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_250to350", "/SMS-T2tt_mStop-250to350_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_350to400     = Sample.nanoAODfromDAS("SMS_T2tt_mStop_350to400", "/SMS-T2tt_mStop-350to400_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v3_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_400to1200    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_400to1200", "/SMS-T2tt_mStop-400to1200_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T2tt_mStop_1200to2000    = Sample.nanoAODfromDAS("SMS_T2tt_mStop_1200to2000", "/SMS-T2tt_mStop-1200to2000_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)

SMS_T2bW    = Sample.nanoAODfromDAS("SMS_T2bW", "/SMS-T2bW_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)

SMS_T8bbllnunu_XCha0p5_XSlep0p05    = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05", "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1) #running
SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000    = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000", "/SMS-T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T8bbllnunu_XCha0p5_XSlep0p5    = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5", "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300    = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300", "/SMS-T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650    = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650", "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)
SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600    = Sample.nanoAODfromDAS("SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600", "/SMS-T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)


SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25 = Sample.nanoAODfromDAS("SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25",     "/SMS-T8bbstausnu_XCha0p5_mStop-200to1800_XStau0p25_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)

SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5 = Sample.nanoAODfromDAS("SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5",     "/SMS-T8bbstausnu_mStop-200to1800_XCha0p5_XStau0p5_TuneCP2_13TeV-madgraphMLM-pythia8/schoef-crab_RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v2_legacy_nano_v4-2f0de5761821e09504355ecf17f526b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1)

SUSY = [
    SMS_T2tt_mStop_175_mLSP_1,
    SMS_T2tt_mStop_250_mLSP_50,
    SMS_T2tt_mStop_250_mLSP_75,
    SMS_T2tt_mStop_250_mLSP_100,
    SMS_T2tt_mStop_650_mLSP_350,
    SMS_T2tt_mStop_150to250,
    SMS_T2tt_mStop_250to350,
    SMS_T2tt_mStop_350to400,
    SMS_T2tt_mStop_400to1200,
    SMS_T2tt_mStop_1200to2000,
    SMS_T2bW,
    SMS_T8bbllnunu_XCha0p5_XSlep0p05,
    SMS_T8bbllnunu_XCha0p5_XSlep0p05_mN1_700_1000,
    SMS_T8bbllnunu_XCha0p5_XSlep0p5,
    SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1300,
    SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_0_650,
    SMS_T8bbllnunu_XCha0p5_XSlep0p95_mN1_700_1600,
    SMS_T8bbstausnu_XCha0p5_mStop_200to1800_XStau0p25,
    SMS_T8bbstausnu_mStop_200to1800_XCha0p5_XStau0p5
    ]

GluGluHToZZTo4L             = Sample.nanoAODfromDAS("GluGluHToZZTo4L",             "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01297)
GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v6-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423)
GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v5-aaebd5a242d0ea19e5cbbb3204c402e0/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)



gluglu = [
    GluGluHToZZTo4L,
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo4tau,
]

QCD_Mu_pt15to20         = Sample.nanoAODfromDAS("QCD_Mu_pt15to20",         "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3629000.0)
QCD_Mu_pt20to30         = Sample.nanoAODfromDAS("QCD_Mu_pt20to30",         "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v4_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3168000.0)
QCD_Mu_pt30to50         = Sample.nanoAODfromDAS("QCD_Mu_pt30to50",         "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1649000.0)
QCD_Mu_pt50to80         = Sample.nanoAODfromDAS("QCD_Mu_pt50to80",         "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=445700.0)
QCD_Mu_pt80to120        = Sample.nanoAODfromDAS("QCD_Mu_pt80to120",        "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105500.0)
QCD_Mu_pt120to170       = Sample.nanoAODfromDAS("QCD_Mu_pt120to170",       "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25540.0)
QCD_Mu_pt120to170_ext   = Sample.nanoAODfromDAS("QCD_Mu_pt120to170_ext",   "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25540.0)
QCD_Mu_pt170to300       = Sample.nanoAODfromDAS("QCD_Mu_pt170to300",       "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=8670.0)
QCD_Mu_pt300to470       = Sample.nanoAODfromDAS("QCD_Mu_pt300to470",       "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=797.5)
QCD_Mu_pt300to470_ext   = Sample.nanoAODfromDAS("QCD_Mu_pt300to470_ext",   "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=797.5)
QCD_Mu_pt470to600       = Sample.nanoAODfromDAS("QCD_Mu_pt470to600",       "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=78.67)
QCD_Mu_pt600to800       = Sample.nanoAODfromDAS("QCD_Mu_pt600to800",       "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25.33)
#QCD_Mu_pt800to1000      = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000",      "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.715)
QCD_Mu_pt800to1000_ext  = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000_ext",  "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.715)
QCD_Mu_pt1000toInf      = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf",      "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.605)

QCD_Ele_pt20to30     = Sample.nanoAODfromDAS("QCD_Ele_pt20to30",    "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5533000.0)
QCD_Ele_pt30to50     = Sample.nanoAODfromDAS("QCD_Ele_pt30to50",    "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=6952000.0)
QCD_Ele_pt50to80     = Sample.nanoAODfromDAS("QCD_Ele_pt50to80",    "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2206000.0)
QCD_Ele_pt80to120    = Sample.nanoAODfromDAS("QCD_Ele_pt80to120",   "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=415400.0)
QCD_Ele_pt120to170   = Sample.nanoAODfromDAS("QCD_Ele_pt120to170",  "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=75820.0)
QCD_Ele_pt170to300   = Sample.nanoAODfromDAS("QCD_Ele_pt170to300",  "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18860.0)
QCD_Ele_pt300toInf   = Sample.nanoAODfromDAS("QCD_Ele_pt300toInf",  "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v2-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1210.0)

QCD = [
        QCD_Mu_pt15to20,
        QCD_Mu_pt20to30,
        QCD_Mu_pt30to50,
        QCD_Mu_pt50to80,
        QCD_Mu_pt80to120,
        QCD_Mu_pt120to170,
        QCD_Mu_pt120to170_ext,
        QCD_Mu_pt170to300,
        QCD_Mu_pt300to470,
        QCD_Mu_pt300to470_ext,
        QCD_Mu_pt470to600,
        QCD_Mu_pt600to800,
#        QCD_Mu_pt800to1000,
        QCD_Mu_pt800to1000_ext,
        QCD_Mu_pt1000toInf,

        QCD_Ele_pt20to30,
        QCD_Ele_pt30to50,
        QCD_Ele_pt50to80,
        QCD_Ele_pt80to120,
        QCD_Ele_pt120to170,
        QCD_Ele_pt170to300,
        QCD_Ele_pt300toInf,
]

GJets_HT40to100        = Sample.nanoAODfromDAS("GJets_HT40to100",      "/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=20730)
GJets_HT100to200       = Sample.nanoAODfromDAS("GJets_HT100to200",     "/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-4cores5k_102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9226)
GJets_HT200to400       = Sample.nanoAODfromDAS("GJets_HT200to400",     "/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2300)
GJets_HT400to600       = Sample.nanoAODfromDAS("GJets_HT400to600",     "/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=274.4)
GJets_HT600toInf       = Sample.nanoAODfromDAS("GJets_HT600toInf",     "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=93.38)
GJets_HT600toInf_ext   = Sample.nanoAODfromDAS("GJets_HT600toInf_ext", "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/llechner-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2_legacy_nano_v1-aaebd5a242d0ea19e5cbbb3204c402e0/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=93.38)

GJetsHT = [
           GJets_HT40to100,
           GJets_HT100to200,
           GJets_HT200to400,
           GJets_HT400to600,
           GJets_HT600toInf,
           GJets_HT600toInf_ext,
]


other = [
    ]

allSamples = DY + top + boson + wjets + rare + other + gluglu + QCD + GJetsHT + SUSY

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
