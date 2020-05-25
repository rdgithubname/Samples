import os
from WMCore.Configuration import Configuration
config = Configuration()

# Set variables
production_label    = os.environ["CRAB_PROD_LABEL"]
dataset             = os.environ["CRAB_DATASET"]
cfgFile             = os.environ["CMSRUN_CFG"]
unitsPerJob         = int(os.environ["CRAB_UNITS_PER_JOB"])
publish             = True if os.environ["CRAB_PUBLISH"] == 'True' else False
runOnNonValid       = True if os.environ['CRAB_RUNONNONVALID'] == 'True' else False
inputDBS            = os.environ["CRAB_input_DBS"]
if "CRAB_TOTAL_UNITS" in os.environ: totalUnits = os.environ["CRAB_TOTAL_UNITS"]

config.section_("General")
config.General.transferLogs = True
config.General.requestName = production_label
config.General.workArea = 'crab_' + os.environ['ORIG_PROD_LABEL'] + "_" + os.environ["MAOD_SAMPLE_NAME"]# config.General.requestName

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = cfgFile
config.JobType.outputFiles = ['nanoAOD.root']
#config.JobType.numCores = 2
config.JobType.maxMemoryMB = 4000


config.section_("Data")
config.Data.inputDataset = dataset

config.Data.inputDBS = inputDBS
config.Data.splitting = 'FileBased'
#if "IS_DATA" in os.environ:
#    config.Data.lumiMask = 'json/Cert_314472-316723_13TeV_PromptReco_Collisions18_JSON.txt'
config.Data.ignoreLocality = True
config.Data.allowNonValidInputDataset = runOnNonValid

#config.Data.outLFNDirBase = '/store/user/%s/nanoAOD/%s/' % (os.environ['USER'], os.environ['ORIG_PROD_LABEL'])
config.Data.publication = publish
config.Data.unitsPerJob = unitsPerJob#10
if "CRAB_TOTAL_UNITS" in os.environ: config.Data.totalUnits = int(totalUnits)#8

config.section_("Site")
config.Site.blacklist = []
config.Site.whitelist = ['T3_US_UMD', 'T3_US_PuertoRico', 'T3_UK_ScotGrid_GLA', 'T3_UK_SGrid_Oxford', 'T3_UK_London_QMUL', 'T3_KR_KNU', 'T3_FR_IPNL', 'T2_US_Wisconsin', 'T2_US_Vanderbilt', 'T2_US_UCSD', 'T2_US_Purdue', 'T2_US_Nebraska', 'T2_US_MIT', 'T2_US_Florida', 'T2_US_Caltech', 'T2_UK_SGrid_RALPP', 'T2_UK_SGrid_Bristol', 'T2_UK_London_IC', 'T2_UA_KIPT', 'T2_TW_NCHC', 'T2_TR_METU', 'T2_RU_JINR', 'T2_RU_ITEP', 'T2_RU_INR', 'T2_RU_IHEP', 'T2_PT_NCG_Lisbon', 'T2_PL_Swierk', 'T2_PK_NCP', 'T2_KR_KISTI', 'T2_IT_Rome', 'T2_IT_Pisa', 'T2_IT_Legnaro', 'T2_IT_Bari', 'T2_IN_TIFR', 'T2_HU_Budapest', 'T2_GR_Ioannina', 'T2_FR_IPHC', 'T2_FR_GRIF_LLR', 'T2_FR_GRIF_IRFU', 'T2_FR_CCIN2P3', 'T2_FI_HIP', 'T2_ES_IFCA', 'T2_ES_CIEMAT', 'T2_EE_Estonia', 'T2_DE_RWTH', 'T2_DE_DESY', 'T2_CN_Beijing', 'T2_CH_CSCS', 'T2_CH_CERN', 'T2_BR_SPRACE', 'T2_BE_UCL', 'T2_BE_IIHE', 'T2_AT_Vienna', 'T1_US_FNAL', 'T1_UK_RAL', 'T1_RU_JINR', 'T1_IT_CNAF', 'T1_FR_CCIN2P3', 'T1_ES_PIC', 'T1_DE_KIT']
config.Site.storageSite = 'T2_AT_Vienna'

config.section_("User")

config.section_("Debug")
