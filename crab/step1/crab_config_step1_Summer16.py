tag = '20-05-25'

from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_step1_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../cfg/step1_RunIISummer16_8031.py'
config.JobType.disableAutomaticOutputCollection = False
#config.JobType.numCores = 1

config.section_("Data")
#config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.totalUnits  = 500000 
config.Data.unitsPerJob = 500
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
config.Site.whitelist = ['T2_CERN_CH', 'T1_US_FNAL_Disk'] #Run where the PU dataset is, not where the sample is
config.section_("User")

if __name__ == '__main__':

    for input_dataset in [
       '/tWZ_NLO_v16_ext3/schoef-tWZ_NLO_v16_ext3-a1e791adef4fc0a2f32451f12fdbd583/USER',
       '/tOrtbar_WZ01j_OLRLL_LO_ext5/schoef-tOrtbar_WZ01j_OLRLL_LO_ext5-c88179374d61ba4483b39a09a725f437/USER'
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        config.Data.outputDatasetTag = tag 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
