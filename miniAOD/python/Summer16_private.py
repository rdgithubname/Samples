'''
miniAOD samples of TTGamma private production (Tom)
'''

import copy, os, sys
from RootTools.fwlite.FWLiteSample import FWLiteSample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--logLevel',    action='store', default='INFO', help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
    return argParser
    
# Logging
if __name__=="__main__":
    options = get_parser().parse_args()        
    import Samples.Tools.logger as logger      
    logger = logger.get_logger(options.logLevel, logFile = None )
    import RootTools.core.logger as logger_rt  
    logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )
    ov = options.overwrite

else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

from Samples.Tools.config import dbDir, redirector_BE, redirector
dbFile = dbDir+"Summer16_private.sql"

logger.info("Using db file: %s", dbFile) 

## TTGamma private new samples
TTGamma_dilep_LO_S16_private         = FWLiteSample.fromDPMDirectory("TTGamma_dilep_LO_S16_private",      "/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018_miniAODv3/prompt/ttGamma_Dilept_5f_ckm_LO_1line",   dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_semilep_LO_S16_private       = FWLiteSample.fromDPMDirectory("TTGamma_semilep_LO_S16_private",    "/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018_miniAODv3/prompt/ttGamma_SemiLept_5f_ckm_LO_1line", dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_had_LO_S16_private           = FWLiteSample.fromDPMDirectory("TTGamma_had_LO_S16_private",        "/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018_miniAODv3/prompt/ttGamma_Had_5f_ckm_LO_1line",      dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_nofullyhad_LO_S16_private    = FWLiteSample.fromDPMDirectory("TTGamma_nofullyhad_LO_S16_private", "/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018_miniAODv3/prompt/ttGamma_NoFullyHad_5f_ckm_LO_1line",      dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)

TTX = [
       TTGamma_dilep_LO_S16_private,
       TTGamma_semilep_LO_S16_private,
       TTGamma_had_LO_S16_private,
       TTGamma_nofullyhad_LO_S16_private,
]

#ZGToLLG_LO_S16_private = FWLiteSample.fromDPMDirectory("ZGToLLG_LO_S16_private",      "/dpm/oeaw.ac.at/home/cms/store/user/llechner/miniAOD/RunIISummer16_privProd_miniAODv3/ZAToLLA0123j_5f_LO_MLM/",   dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

VGamma = [
#    ZGToLLG_LO_S16_private,
]


# xSec    = 5.277e-05
# model: Yt
# reweight_pkl = '/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/tZZ1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.pkl' 
tZZ1j_4l_rwgt = FWLiteSample.fromDAS("tZZ1j_4l_rwgt", "/tZZ1j_4l_rwgt/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

# xSec    = 0.2279
# model: Yt
# reweight_pkl = '/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/tZZ1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.pkl'#same
tWZ01j_rwgt   = FWLiteSample.fromDAS("tWZ01j_rwgt", "/tWZ01j_rwgt/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

# tWZ01j_filter_efficiency = (601438./(30*10**6))*(10**6/363784.)
# xSec = 0.2279*tWZ01j_filter_efficiency
# model: yt
# reweight_pkl = '/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/tZZ1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.pkl'#same
tWZ01j_rwgt_filter   = FWLiteSample.fromDAS("tWZ01j_rwgt_filter", "/tWZ01j_rwgt_filter_2/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

# xSec    = 0.02523,
# model: yt
# reweight_pkl = '/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/tZZ1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.pkl' #same
tWW1j_rwgt    = FWLiteSample.fromDAS("tWW1j_rwgt", "/tWW1j_rwgt/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

# xSec    = 0.8324,
# model: dim6top
# reweight_pkl = '/afs/hephy.at/data/rschoefbeck01/gridpacks/dim6top/ttW01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.pkl' 
ttW01j_rwgt_dim6top = FWLiteSample.fromDAS("ttW01j_rwgt_dim6top", "/ttW01j_rwgt_dim6top/ttschida-Summer16-mAOD949-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

# tWZ NLO and LO
tWZ_NLO = FWLiteSample.fromDAS("tWZ_NLO", "/tWZ_NLO_v16_ext3/schoef-Summer16-mAOD949-v3-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

tOrtbar_WZ01j_OLRLL_LO = FWLiteSample.fromDAS("tOrtbar_WZ01j_OLRLL_LO", "/tOrtbar_WZ01j_OLRLL_LO_ext5/schoef-Summer16-mAOD949-v3-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER", "phys03", dbFile=dbFile, overwrite=ov, prefix='root://hephyse.oeaw.at/', skipCheck=True)

BSM_tVV_ttV = [
    tZZ1j_4l_rwgt,
    tWZ01j_rwgt,
    tWZ01j_rwgt_filter,
    tWW1j_rwgt,
    ttW01j_rwgt_dim6top,
    tWZ_NLO,
    tOrtbar_WZ01j_OLRLL_LO,
]

allSamples = TTX + VGamma + BSM_tVV_ttV

for sample in allSamples:
    sample.isData = False
