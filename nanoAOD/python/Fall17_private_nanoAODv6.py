import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
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
        if __name__ == "__main__" and not options.check_completeness:
            from Samples.Tools.config import redirector_global as redirector
        else:
            from Samples.Tools.config import redirector_clip_local as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Fall17_private_nanoAODv6.sql'

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_LO      = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO",      "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M50_LO_ext1 = Sample.nanoAODfromDAS("DYJetsToLL_M50_LO_ext1", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M50_ext1    = Sample.nanoAODfromDAS("DYJetsToLL_M50_ext1",    "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",     dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2075.14*3)
DYJetsToLL_M10to50_LO  = Sample.nanoAODfromDAS("DYJetsToLL_M10to50_LO",  "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",               dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18610)


## x-secs from runXSecAnalyzer
DYJetsToLL_M50_HT70to100      = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT70to100" ,      "/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",             dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=147.7*1.23) 
DYJetsToLL_M50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT100to200",      "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=161.1*1.23) 
DYJetsToLL_M50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400",      "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",            dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=48.58*1.23) 
DYJetsToLL_M50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT200to400_ext",  "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER",       dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=48.58*1.23) 
DYJetsToLL_M50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT400to600",      "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=6.979*1.23) 
DYJetsToLL_M50_HT600to800     = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT600to800",      "/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.738*1.23 ) 
DYJetsToLL_M50_HT800to1200    = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT800to1200",     "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.8077*1.23 ) 
DYJetsToLL_M50_HT1200to2500   = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT1200to2500",    "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",          dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1926*1.23 ) 
DYJetsToLL_M50_HT2500toInf    = Sample.nanoAODfromDAS("DYJetsToLL_M50_HT2500toInf",     "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.003435*1.23 )

DYJetsM50HT = [
    DYJetsToLL_M50_HT70to100,
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,
    DYJetsToLL_M50_HT200to400_ext,
    DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT600to800,
    DYJetsToLL_M50_HT800to1200,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf,
]

## x-secs from runXSecAnalyzer
DYJetsToLL_M4to50_HT100to200     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT100to200" ,    "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=205.4) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT200to400     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400" ,    "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=54.56) #LO without 1.23 k-factor 
DYJetsToLL_M4to50_HT200to400_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT200to400_ext", "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=54.56) #LO without 1.23 k-factor 
DYJetsToLL_M4to50_HT400to600     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600",     "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.717) #LO without 1.23 k-factor 
DYJetsToLL_M4to50_HT400to600_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT400to600_ext", "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.717) #LO without 1.23 k-factor 
DYJetsToLL_M4to50_HT600toInf     = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf" ,    "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.841) #LO without 1.23 k-factor 
DYJetsToLL_M4to50_HT600toInf_ext = Sample.nanoAODfromDAS("DYJetsToLL_M4to50_HT600toInf_ext", "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER",   dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.841) #LO without 1.23 k-factor 

DYJetsM5to50HT = [
    DYJetsToLL_M4to50_HT100to200,
    DYJetsToLL_M4to50_HT200to400,
    DYJetsToLL_M4to50_HT200to400_ext,
    DYJetsToLL_M4to50_HT400to600,
    DYJetsToLL_M4to50_HT400to600_ext,
    DYJetsToLL_M4to50_HT600toInf,
    DYJetsToLL_M4to50_HT600toInf_ext,
]


# x-secs using runXSecAnalyzer
DYJetsToNuNu_HT100to200     = Sample.nanoAODfromDAS("DYJetsToNuNu_HT100to200",   "/ZJetsToNuNu_HT-100To200_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=280.35*1.23)
DYJetsToNuNu_HT200to400     = Sample.nanoAODfromDAS("DYJetsToNuNu_HT200to400",   "/ZJetsToNuNu_HT-200To400_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=77.67*1.23)
DYJetsToNuNu_HT400to600     = Sample.nanoAODfromDAS("DYJetsToNuNu_HT400to600",   "/ZJetsToNuNu_HT-400To600_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=10.73*1.23)
DYJetsToNuNu_HT600to800     = Sample.nanoAODfromDAS("DYJetsToNuNu_HT600to800",   "/ZJetsToNuNu_HT-600To800_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.559*1.23)
DYJetsToNuNu_HT800to1200    = Sample.nanoAODfromDAS("DYJetsToNuNu_HT800to1200",  "/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.1796*1.23)
DYJetsToNuNu_HT1200to2500   = Sample.nanoAODfromDAS("DYJetsToNuNu_HT1200to2500", "/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.28833*1.23)
DYJetsToNuNu_HT2500toInf    = Sample.nanoAODfromDAS("DYJetsToNuNu_HT2500toInf",  "/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",        dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.006945*1.23)

DYJetsNuNuHT = [
   DYJetsToNuNu_HT100to200,
   DYJetsToNuNu_HT200to400,
   DYJetsToNuNu_HT400to600,
   DYJetsToNuNu_HT600to800,
   DYJetsToNuNu_HT800to1200,
   DYJetsToNuNu_HT1200to2500,
   DYJetsToNuNu_HT2500toInf,
]

DY = [
    DYJetsToLL_M50_LO,
    DYJetsToLL_M50_LO_ext1,
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50_ext1, ] + DYJetsM50HT + DYJetsM5to50HT + DYJetsNuNuHT    

## ttbar
TTLep_pow       = Sample.nanoAODfromDAS("TTLep_pow",       "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((3*0.108)**2))
TTSingleLep_pow = Sample.nanoAODfromDAS("TTSingleLep_pow",   "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTHad_pow       = Sample.nanoAODfromDAS("TTHad_pow",       "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=831.762*((1-3*0.108)**2))

## single top
TToLeptons_sch_amcatnlo = Sample.nanoAODfromDAS("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(7.20+4.16)*0.108*3)
#TToHad_sch              = Sample.nanoAODfromDAS("TToHad_sch", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(7.20+4.16)*(1-0.108*3))

T_tch_pow               = Sample.nanoAODfromDAS("T_tch_pow",               "/ST_t-channel_top_5f_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=136.02) # inclusive sample
TBar_tch_pow            = Sample.nanoAODfromDAS("TBar_tch_pow",            "/ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=80.95) # inclusive sample

T_tWch_ext              = Sample.nanoAODfromDAS("T_tWch_ext",              "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext           = Sample.nanoAODfromDAS("TBar_tWch_ext",           "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect

T_tWch_incl             = Sample.nanoAODfromDAS("T_tWch_incl",             "/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85)
TBar_tWch_incl          = Sample.nanoAODfromDAS("TBar_tWch_incl",          "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=35.85)

## ttH
TTHbb       = Sample.nanoAODfromDAS("TTHbb",       "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(0.577))
TTHnobb_pow = Sample.nanoAODfromDAS("TTHnobb_pow", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5085*(1-0.577))

THQ = Sample.nanoAODfromDAS("THQ", "/THQ_4f_Hincl_13TeV_madgraph_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.07096)
THW = Sample.nanoAODfromDAS("THW", "/THW_5f_Hincl_13TeV_madgraph_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1472)

## ttV
TGJets     = Sample.nanoAODfromDAS("TGJets",     "/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967)
TGJets_lep = Sample.nanoAODfromDAS("TGJets_lep", "/TGJets_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.967*0.108*3)

#tZq_Zhad_WLept = Sample.nanoAODfromDAS("tZq_Zhad_WLept", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=)
tZq_ll         = Sample.nanoAODfromDAS("tZq_ll",         "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.09418 ) #0.0758 ) 
tZq_nunu       = Sample.nanoAODfromDAS("tZq_nunu",       "/tZq_nunu_4f_ckm_NLO_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728)

tWll   = Sample.nanoAODfromDAS("tWll",   "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01123)

TTW_LO      = Sample.nanoAODfromDAS("TTW_LO",      "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6105)
TTW_LO_ext1 = Sample.nanoAODfromDAS("TTW_LO_ext1", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.6105)
TTWToLNu    = Sample.nanoAODfromDAS("TTWToLNu",    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2043)
TTWToQQ     = Sample.nanoAODfromDAS("TTWToQQ",     "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.40620)

TTZToQQ            = Sample.nanoAODfromDAS("TTZToQQ",            "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297)
TTZToLLNuNu        = Sample.nanoAODfromDAS("TTZToLLNuNu",        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2728)
TTZToLLNuNu_m1to10 = Sample.nanoAODfromDAS("TTZToLLNuNu_m1to10", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0493)
TTZ_LO             = Sample.nanoAODfromDAS("TTZ_LO",             "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297/0.692)
TTZ_LO_ext1        = Sample.nanoAODfromDAS("TTZ_LO_ext1",        "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.5297/0.692)

TTGJets     = Sample.nanoAODfromDAS("TTGJets",     "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.697)

# fixed samples!!
TTGHad_LO                   = Sample.nanoAODfromDAS("TTGHad_LO",             "/TTGamma_Hadronic_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.149*2.565)
TTGHad_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGHad_ptG100To200_LO", "/TTGamma_Hadronic_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1249*2.565)
TTGHad_ptG200_LO            = Sample.nanoAODfromDAS("TTGHad_ptG200_LO",      "/TTGamma_Hadronic_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.02687*2.565)

TTGSingleLep_LO             = Sample.nanoAODfromDAS("TTGSingleLep_LO",             "/TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.056*1.994)
TTGSingleLep_TuneUp_LO      = Sample.nanoAODfromDAS("TTGSingleLep_TuneUp_LO",      "/TTGamma_SingleLept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.056*1.994)
TTGSingleLep_TuneDown_LO    = Sample.nanoAODfromDAS("TTGSingleLep_TuneDown_LO",    "/TTGamma_SingleLept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.056*1.994)
TTGSingleLep_erdOn_LO       = Sample.nanoAODfromDAS("TTGSingleLep_erdOn_LO",       "/TTGamma_SingleLept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.056*1.994)
TTGSingleLep_ptG100To200_LO = Sample.nanoAODfromDAS("TTGSingleLep_ptG100To200_LO", "/TTGamma_SingleLept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1309*1.994)
TTGSingleLep_ptG200_LO      = Sample.nanoAODfromDAS("TTGSingleLep_ptG200_LO",      "/TTGamma_SingleLept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.02685*1.994)

TTGLep_LO                   = Sample.nanoAODfromDAS("TTGLep_LO",             "/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.495*1.616)
TTGLep_TuneUp_LO            = Sample.nanoAODfromDAS("TTGLep_TuneUp_LO",      "/TTGamma_Dilept_TuneCP5Up_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.495*1.616)
TTGLep_TuneDown_LO          = Sample.nanoAODfromDAS("TTGLep_TuneDown_LO",    "/TTGamma_Dilept_TuneCP5Down_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.495*1.616)
TTGLep_erdOn_LO             = Sample.nanoAODfromDAS("TTGLep_erdOn_LO",       "/TTGamma_Dilept_TuneCP5_erdON_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.495*1.616)
TTGLep_ptG100To200_LO       = Sample.nanoAODfromDAS("TTGLep_ptG100To200_LO", "/TTGamma_Dilept_ptGamma100-200_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.03412*1.616)
TTGLep_ptG200_LO            = Sample.nanoAODfromDAS("TTGLep_ptG200_LO",      "/TTGamma_Dilept_ptGamma200inf_TuneCP5_PSweights_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.006797*1.616)

#tWll_thad_Wlept_DR  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DR",  "/TWZToLL_thad_Wlept_5f_DR_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
#tWll_thad_Wlept_DS  = Sample.nanoAODfromDAS("tWll_thad_Wlept_DS",  "/TWZToLL_thad_Wlept_5f_DS_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
#tWll_tlept_Whad_DR  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DR",  "/TWZToLL_tlept_Whad_5f_DR_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
#tWll_tlept_Whad_DS  = Sample.nanoAODfromDAS("tWll_tlept_Whad_DS",  "/TWZToLL_tlept_Whad_5f_DS_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.003004 )
#tWll_tlept_Wlept_DR = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DR", "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )
#tWll_tlept_Wlept_DS = Sample.nanoAODfromDAS("tWll_tlept_Wlept_DS", "/TWZToLL_tlept_Wlept_5f_DS_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER",  dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=0.001501 )

TTV = [
    TGJets,
    TGJets_lep,
    tZq_ll,
    tZq_nunu,
    tWll,
    TTWToLNu,
    TTWToQQ,
    TTW_LO,
    TTW_LO_ext1,
    TTZToQQ,
    TTZToLLNuNu,
    TTZToLLNuNu_m1to10,
    TTZ_LO,
    TTZ_LO_ext1,
    TTGJets,
    TTGHad_LO,
    TTGHad_ptG100To200_LO,
    TTGHad_ptG200_LO,
    TTGSingleLep_LO,
    TTGSingleLep_TuneUp_LO,
    TTGSingleLep_TuneDown_LO,
    TTGSingleLep_erdOn_LO,
    TTGSingleLep_ptG100To200_LO,
    TTGSingleLep_ptG200_LO,
    TTGLep_LO,
    TTGLep_TuneUp_LO,
    TTGLep_TuneDown_LO,
    TTGLep_erdOn_LO,
    TTGLep_ptG100To200_LO,
    TTGLep_ptG200_LO,
]

top = [
#    tWll_thad_Wlept_DR,
#    tWll_thad_Wlept_DS,
#    tWll_tlept_Whad_DR,
#    tWll_tlept_Whad_DS,
#    tWll_tlept_Wlept_DR,
#    tWll_tlept_Wlept_DS,
    TTLep_pow,
    TTSingleLep_pow,
    TTHad_pow,
    TToLeptons_sch_amcatnlo,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
    T_tWch_incl,
    TBar_tWch_incl,
    TTHbb,
    TTHnobb_pow,
    THQ,
    THW,
    ] + TTV

## di/multiboson
WWTo2L2Nu     = Sample.nanoAODfromDAS("WWTo2L2Nu",     "/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=12.178)
WWToLNuQQ     = Sample.nanoAODfromDAS("WWToLNuQQ",     "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=49.997)
WWTo4Q        = Sample.nanoAODfromDAS("WWTo4Q",        "/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=51.723 )

ZZTo2L2Nu       = Sample.nanoAODfromDAS("ZZTo2L2Nu",       "/ZZTo2L2Nu_13TeV_powheg_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.564)
ZZTo2L2Q        = Sample.nanoAODfromDAS("ZZTo2L2Q",        "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.28)
ZZTo2Q2Nu       = Sample.nanoAODfromDAS("ZZTo2Q2Nu",       "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.04)
ZZTo4L          = Sample.nanoAODfromDAS("ZZTo4L",          "/ZZTo4L_13TeV_powheg_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.256*1.1)
ZZTo4L_amcatnlo = Sample.nanoAODfromDAS("ZZTo4L_amcatnlo", "/ZZTo4L_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.256*1.1)

WZTo1L3Nu         = Sample.nanoAODfromDAS("WZTo1L3Nu",         "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=(47.13)*(3*0.108)*(0.2) ) 
WZTo1L1Nu2Q       = Sample.nanoAODfromDAS("WZTo1L1Nu2Q",       "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=10.71) 
WZTo2L2Q          = Sample.nanoAODfromDAS("WZTo2L2Q",          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5.60) 
WZTo3LNu_ext      = Sample.nanoAODfromDAS("WZTo3LNu_ext",      "/WZTo3LNu_13TeV-powheg-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.42965) 
WZTo3LNu_amcatnlo = Sample.nanoAODfromDAS("WZTo3LNu_amcatnlo", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.666)

VVTo2L2Nu = Sample.nanoAODfromDAS("VVTo2L2Nu", "/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=14.00)

WGToLNuG               = Sample.nanoAODfromDAS("WGToLNuG",            "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=463.9*1.295) # NLO xsec from TOP-17-016 for 2016 -> extract k-factor (compare with xsec analyzer for 2016) and apply k-factor to other years (xsec= analyser * k)
WGToLNuG_amcatnlo      = Sample.nanoAODfromDAS("WGToLNuG_amcatnlo",   "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=203.3)
ZGToLLG                = Sample.nanoAODfromDAS("ZGToLLG",             "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=50.2)
ZGToLLG_lowMLL         = Sample.nanoAODfromDAS("ZGToLLG_lowMLL",      "/ZGToLLG_01J_5f_lowMLL_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105.4 ) #NLO xsec * NNLO k-factor from 7TeV calculations (Tom) https://hypernews.cern.ch/HyperNews/CMS/get/generators/2772/1/1/1/1/1/1/1/1.html
ZGToLLG_LoosePtlPtg    = Sample.nanoAODfromDAS("ZGToLLG_LoosePtlPtg", "/ZGToLLG_01J_LoosePtlPtg_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=124.9) #SMP 19 013

WW     = Sample.nanoAODfromDAS("WW",           "/WW_TuneCP5_13TeV-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=63.21 * 1.82)
WZ     = Sample.nanoAODfromDAS("WZ",     "/WZ_TuneCP5_13TeV-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=47.13)
ZZ     = Sample.nanoAODfromDAS("ZZ",     "/ZZ_TuneCP5_13TeV-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=16.523)

WWW_4F = Sample.nanoAODfromDAS("WWW_4F", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.2086)
WWZ_4F = Sample.nanoAODfromDAS("WWZ_4F", "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.1651)
WZZ    = Sample.nanoAODfromDAS("WZZ",    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.05565)
ZZZ    = Sample.nanoAODfromDAS("ZZZ",    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01398)




boson = [
    WWTo2L2Nu,
    WWToLNuQQ,
    WWTo4Q,
    ZZTo2L2Nu,
    ZZTo2L2Q,
    ZZTo2Q2Nu,
    ZZTo4L,
    ZZTo4L_amcatnlo,
    WZTo1L3Nu,
    WZTo1L1Nu2Q,
    WZTo2L2Q,
    WZTo3LNu_ext,
    WZTo3LNu_amcatnlo,
    VVTo2L2Nu,
    WGToLNuG,
    WGToLNuG_amcatnlo,
    ZGToLLG,
    ZGToLLG_lowMLL,
    ZGToLLG_LoosePtlPtg,
    WW,
    WZ,
    ZZ,
    WWW_4F,
    WWZ_4F,
    WZZ,
    ZZZ,
    ]

# W+jets
WJetsToLNu      = Sample.nanoAODfromDAS("WJetsToLNu",      "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)
WJetsToLNu_ext1 = Sample.nanoAODfromDAS("WJetsToLNu_ext1", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-6_2017_ext1-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3* 20508.9)

# cross sections from https://hypernews.cern.ch/HyperNews/CMS/get/generators/3883/1/1.html
# 0To50 and 50To150 use the same gridpacks with different filters in the fragment, pre-matched xsec stays the same, filter efficiency and matching efficiency changes
#W1JetsToLNu_NLO_pT0To50        = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT0To50",        "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=34710*0.6777*0.2)
#W1JetsToLNu_NLO_pT50To150      = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT50To150",      "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2661)
#W1JetsToLNu_NLO_pT50To150_ext  = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT50To150_ext",  "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2661)
#W1JetsToLNu_NLO_pT150To250     = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT150To250",     "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=71.9)
#W1JetsToLNu_NLO_pT150To250_ext = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT150To250_ext", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=71.9)
#W1JetsToLNu_NLO_pT250To400     = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT250To400",     "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=8.05)
#W1JetsToLNu_NLO_pT250To400_ext = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT250To400_ext", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=8.05)
#W1JetsToLNu_NLO_pT400ToInf     = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT400ToInf",     "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.885)
#W1JetsToLNu_NLO_pT400ToInf_ext = Sample.nanoAODfromDAS("W1JetsToLNu_NLO_pT400ToInf_ext", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.885)


#W2JetsToLNu_NLO_pT0To50        = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT0To50",        "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=16870*0.5616*0.1)
#W2JetsToLNu_NLO_pT50To150      = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT50To150",      "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1687)
#W2JetsToLNu_NLO_pT50To150_ext  = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT50To150_ext",  "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1687)
#W2JetsToLNu_NLO_pT150To250     = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT150To250",     "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105.9)
#W2JetsToLNu_NLO_pT150To250_ext = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT150To250_ext", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105.9)
#W2JetsToLNu_NLO_pT250To400     = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT250To400",     "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18.67)
#W2JetsToLNu_NLO_pT250To400_ext = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT250To400_ext", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18.67)
#W2JetsToLNu_NLO_pT400ToInf     = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT400ToInf",     "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.037)
#W2JetsToLNu_NLO_pT400ToInf_ext = Sample.nanoAODfromDAS("W2JetsToLNu_NLO_pT400ToInf_ext", "", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.037)


W1JetsToLNu     = Sample.nanoAODfromDAS("W1JetsToLNu",           "/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=11524.) #NLO xsec from AN-2016/289
W2JetsToLNu     = Sample.nanoAODfromDAS("W2JetsToLNu",           "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3788.) #NLO xsec from AN-2016/289
W3JetsToLNu     = Sample.nanoAODfromDAS("W3JetsToLNu",           "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1144.) #NLO xsec from AN-2016/289
W4JetsToLNu     = Sample.nanoAODfromDAS("W4JetsToLNu",           "/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=636.) #NLO xsec from AN-2016/289

W1JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W1JetsToLNu_NuPt_200", "/W1JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2.397)
W2JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W2JetsToLNu_NuPt_200", "/W2JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.897)
W3JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W3JetsToLNu_NuPt_200", "/W3JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3.298)
W4JetsToLNu_NuPt_200 = Sample.nanoAODfromDAS("W4JetsToLNu_NuPt_200", "/W4JetsToLNu_NuPt-200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",         dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.453)

wjets = [
    WJetsToLNu,
    WJetsToLNu_ext1,
    W1JetsToLNu,
    W2JetsToLNu,
    W3JetsToLNu,
    W4JetsToLNu,
    W1JetsToLNu_NuPt_200,
    W2JetsToLNu_NuPt_200,
    W3JetsToLNu_NuPt_200,
    W4JetsToLNu_NuPt_200,
#    W1JetsToLNu_NLO_pT0To50,
#    W1JetsToLNu_NLO_pT50To150,
#    W1JetsToLNu_NLO_pT50To150_ext,
#    W1JetsToLNu_NLO_pT150To250,
#    W1JetsToLNu_NLO_pT150To250_ext,
#    W1JetsToLNu_NLO_pT250To400,
#    W1JetsToLNu_NLO_pT250To400_ext,
#    W1JetsToLNu_NLO_pT400ToInf,
#    W1JetsToLNu_NLO_pT400ToInf_ext,
#    W2JetsToLNu_NLO_pT0To50,
#    W2JetsToLNu_NLO_pT50To150,
#    W2JetsToLNu_NLO_pT50To150_ext,
#    W2JetsToLNu_NLO_pT150To250,
#    W2JetsToLNu_NLO_pT150To250_ext,
#    W2JetsToLNu_NLO_pT250To400,
#    W2JetsToLNu_NLO_pT250To400_ext,
#    W2JetsToLNu_NLO_pT400ToInf,
#    W2JetsToLNu_NLO_pT400ToInf_ext,
    ]

## rare
TTTT = Sample.nanoAODfromDAS("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.009103)
TTWW = Sample.nanoAODfromDAS("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.007829)
TTWZ = Sample.nanoAODfromDAS("TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.002919)
TTZZ = Sample.nanoAODfromDAS("TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.001573)

rare = [
    TTTT,
    TTWW,
    TTWZ,
    TTZZ,
    ]


GluGluHToZZTo4L             = Sample.nanoAODfromDAS("GluGluHToZZTo4L",   "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER",    dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.01297)
GluGluToContinToZZTo2e2mu   = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2mu",   "/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423) 
GluGluToContinToZZTo2e2tau  = Sample.nanoAODfromDAS("GluGluToContinToZZTo2e2tau",  "/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423) 
GluGluToContinToZZTo2mu2tau = Sample.nanoAODfromDAS("GluGluToContinToZZTo2mu2tau", "/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.005423) 
GluGluToContinToZZTo4e      = Sample.nanoAODfromDAS("GluGluToContinToZZTo4e",      "/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027) 
GluGluToContinToZZTo4mu     = Sample.nanoAODfromDAS("GluGluToContinToZZTo4mu",     "/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)
GluGluToContinToZZTo4tau    = Sample.nanoAODfromDAS("GluGluToContinToZZTo4tau",    "/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=0.0027)

gluglu = [
    GluGluHToZZTo4L,
    GluGluToContinToZZTo2e2mu,
    GluGluToContinToZZTo2e2tau,
    GluGluToContinToZZTo2mu2tau,
    GluGluToContinToZZTo4e,
    GluGluToContinToZZTo4mu,
    GluGluToContinToZZTo4tau,
]

QCD_Mu_pt15to20     = Sample.nanoAODfromDAS("QCD_Mu_pt15to20",     "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3629000.0)
QCD_Mu_pt20to30     = Sample.nanoAODfromDAS("QCD_Mu_pt20to30",     "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=3168000.0)
QCD_Mu_pt30to50     = Sample.nanoAODfromDAS("QCD_Mu_pt30to50",     "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1649000.0)
QCD_Mu_pt50to80     = Sample.nanoAODfromDAS("QCD_Mu_pt50to80",     "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=445700.0)
QCD_Mu_pt80to120    = Sample.nanoAODfromDAS("QCD_Mu_pt80to120",    "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=105500.0)
QCD_Mu_pt120to170   = Sample.nanoAODfromDAS("QCD_Mu_pt120to170",   "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25540.0)
QCD_Mu_pt170to300   = Sample.nanoAODfromDAS("QCD_Mu_pt170to300",   "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=8670.0)
QCD_Mu_pt300to470   = Sample.nanoAODfromDAS("QCD_Mu_pt300to470",   "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=797.5)
QCD_Mu_pt470to600   = Sample.nanoAODfromDAS("QCD_Mu_pt470to600",   "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=78.67)
QCD_Mu_pt600to800   = Sample.nanoAODfromDAS("QCD_Mu_pt600to800",   "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=25.33)
QCD_Mu_pt800to1000  = Sample.nanoAODfromDAS("QCD_Mu_pt800to1000",  "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=4.715)
QCD_Mu_pt1000toInf  = Sample.nanoAODfromDAS("QCD_Mu_pt1000toInf",  "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.605)

QCD_Ele_pt20to30        = Sample.nanoAODfromDAS("QCD_Ele_pt20to30",    "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=5533000.0)
QCD_Ele_pt30to50        = Sample.nanoAODfromDAS("QCD_Ele_pt30to50",    "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9928000.)
QCD_Ele_pt50to80        = Sample.nanoAODfromDAS("QCD_Ele_pt50to80",    "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2890800.0)
QCD_Ele_pt80to120       = Sample.nanoAODfromDAS("QCD_Ele_pt80to120",   "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=415400.0)
QCD_Ele_pt120to170      = Sample.nanoAODfromDAS("QCD_Ele_pt120to170",  "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=75820.0)
QCD_Ele_pt170to300      = Sample.nanoAODfromDAS("QCD_Ele_pt170to300",  "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=18860.0)
QCD_Ele_pt300toInf      = Sample.nanoAODfromDAS("QCD_Ele_pt300toInf",  "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1210.0)

QCD = [
        QCD_Mu_pt15to20,
        QCD_Mu_pt20to30,
        QCD_Mu_pt30to50,
        QCD_Mu_pt50to80,
        QCD_Mu_pt80to120,
        QCD_Mu_pt120to170,
        QCD_Mu_pt170to300,
        QCD_Mu_pt300to470,
        QCD_Mu_pt470to600,
        QCD_Mu_pt600to800,
        QCD_Mu_pt800to1000,
        QCD_Mu_pt1000toInf,

        QCD_Ele_pt20to30,
        QCD_Ele_pt30to50,
        QCD_Ele_pt50to80,
        QCD_Ele_pt80to120,
        QCD_Ele_pt120to170,
        QCD_Ele_pt170to300,
        QCD_Ele_pt300toInf,
]


GJets_HT40to100        = Sample.nanoAODfromDAS("GJets_HT40to100",    "/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=20730)
GJets_HT100to200       = Sample.nanoAODfromDAS("GJets_HT100to200",   "/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=9226)
GJets_HT200to400       = Sample.nanoAODfromDAS("GJets_HT200to400",   "/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=2300)
GJets_HT400to600       = Sample.nanoAODfromDAS("GJets_HT400to600",   "/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=274.4)
GJets_HT600toInf       = Sample.nanoAODfromDAS("GJets_HT600toInf",   "/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/schoef-TopNanoAODv6-1-2-3_2017-a11761155c05d04d6fed5a2401fa93e8/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=93.38)

GJetsHT = [
           GJets_HT40to100,
           GJets_HT100to200,
           GJets_HT200to400,
           GJets_HT400to600,
           GJets_HT600toInf,
]

other = [
    ]


## combined samples (needed for proper PUProfileCache)
DYJetsToLL_M50_LO_comb  = Sample.combine("DYJetsToLL_M50_LO_comb",  [DYJetsToLL_M50_LO, DYJetsToLL_M50_LO_ext1])
if hasattr(DYJetsToLL_M50_LO, 'nEvents'):
    DYJetsToLL_M50_LO_comb.nEvents = DYJetsToLL_M50_LO.nEvents + DYJetsToLL_M50_LO_ext1.nEvents

TTW_LO_comb             = Sample.combine("TTW_LO_comb",             [TTW_LO, TTW_LO_ext1])
if hasattr(TTW_LO, 'nEvents'):
    TTW_LO_comb.nEvents = TTW_LO.nEvents + TTW_LO_ext1.nEvents

TTZ_LO_comb             = Sample.combine("TTZ_LO_comb",             [TTZ_LO, TTZ_LO_ext1])
if hasattr(TTZ_LO, 'nEvents'):
    TTZ_LO_comb.nEvents = TTZ_LO.nEvents + TTZ_LO_ext1.nEvents

WJetsToLNu_comb         = Sample.combine("WJetsToLNu_comb",         [WJetsToLNu, WJetsToLNu_ext1])
if hasattr(WJetsToLNu, 'nEvents'):
    WJetsToLNu_comb.nEvents = WJetsToLNu.nEvents + WJetsToLNu_ext1.nEvents

DYJetsToLL_M50_HT200to400_comb = Sample.combine("DYJetsToLL_M50_HT200to400_comb",         [DYJetsToLL_M50_HT200to400, DYJetsToLL_M50_HT200to400_ext])
DYJetsToLL_M4to50_HT200to400_comb = Sample.combine("DYJetsToLL_M4to50_HT200to400_comb",     [DYJetsToLL_M4to50_HT200to400, DYJetsToLL_M4to50_HT200to400_ext])
DYJetsToLL_M4to50_HT400to600_comb = Sample.combine("DYJetsToLL_M4to50_HT400to600_comb",     [DYJetsToLL_M4to50_HT400to600, DYJetsToLL_M4to50_HT400to600_ext])
DYJetsToLL_M4to50_HT600toInf_comb = Sample.combine("DYJetsToLL_M4to50_HT600toInf_comb",     [DYJetsToLL_M4to50_HT600toInf, DYJetsToLL_M4to50_HT600toInf_ext])

combinedSamples = [
    DYJetsToLL_M50_LO_comb,
    TTW_LO_comb,
    TTZ_LO_comb,
    WJetsToLNu_comb,
    DYJetsToLL_M50_HT200to400_comb,
    DYJetsToLL_M4to50_HT200to400_comb,
    DYJetsToLL_M4to50_HT400to600_comb,
    DYJetsToLL_M4to50_HT600toInf_comb,
]


allSamples = DY + top + boson + wjets + rare + other + gluglu + QCD + GJetsHT # + combinedSamples

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=10 )
