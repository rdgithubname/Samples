#run in CMSSW_9_4_7
tag = 'test-copy'

from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.workArea = tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../cfg/cfg_copy.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.totalUnits  = 500000 
config.Data.unitsPerJob = 1
#config.Data.totalUnits  = 50000 
config.Data.publication = True
#config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
config.Data.inputDataset = '/ADDGravToGG_MS-5000_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.ignoreLocality = True
config.General.requestName = config.Data.inputDataset.split('/')[1] 
config.Data.outputDatasetTag = tag 

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_CERN_CH', 'T1_US_FNAL_Disk'] #Run where the PU dataset is, not where the sample is
config.section_("User")

#if __name__ == '__main__':
#
#    for input_dataset in [
#       '/ADDGravToGG_MS-5000_NED-4_KK-1_M-2000To3000_13TeV-sherpa/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#    ]:
#        config.Data.inputDataset = input_dataset
#        config.Data.outputDatasetTag = tag 
#        
#        #crabCommand('submit', '--dryrun', config = config)
#        crabCommand('submit', config = config)
