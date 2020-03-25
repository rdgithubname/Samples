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
config.Data.ignoreLocality = False
config.Data.allowNonValidInputDataset = runOnNonValid

#config.Data.outLFNDirBase = '/store/user/%s/nanoAOD/%s/' % (os.environ['USER'], os.environ['ORIG_PROD_LABEL'])
config.Data.publication = publish
config.Data.unitsPerJob = unitsPerJob#10
if "CRAB_TOTAL_UNITS" in os.environ: config.Data.totalUnits = int(totalUnits)#8

config.section_("Site")
config.Site.blacklist = []
#config.Site.whitelist = ['T2_IT_Legnaro', 'T2_DE_DESY', 'T2_CH_CERN', 'T2_US_Florida', 'T2_PL_Swierk', 'T2_US_UCSD', 'T2_US_Caltech', 'T2_US_Wisconsin', 'T2_US_Nebraska', 'T2_RU_IHEP', 'T3_US_Baylor', 'T2_UK_SGrid_RALPP', 'T3_US_Colorado', 'T2_DE_RWTH', 'T2_US_MIT', 'T2_US_Vanderbilt', 'T2_UK_London_Brunel', 'T3_IT_Trieste', 'T3_UK_SGrid_Oxford', 'T3_US_UMD', 'T2_HU_Budapest', 'T2_UA_KIPT']
config.Site.storageSite = 'T2_AT_Vienna'

config.section_("User")

config.section_("Debug")
