import FWCore.ParameterSet.Config as cms

process = cms.Process('COPY')

#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')

process.options = cms.untracked.PSet(
  SkipEvent = cms.untracked.vstring('ProductNotFound'),
  wantSummary = cms.untracked.bool(False),
  allowUnscheduled = cms.untracked.bool( True )
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('root://hephyse.oeaw.ac.at//store/user/llechner/ttW01j_rwgt_mg265_v2/ttW01j_rwgt_mg265_v2/190827_122759/0005/GENSIM_LO_01j_93X_5000.root'),
    fileNames = cms.untracked.vstring('root://hephyse.oeaw.ac.at//store/user/llechner/nanoAOD/legacy_nano_v4/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2_legacy_nano_v4/190906_121057/0000/nanoAOD_326.root'),
    secondaryFileNames = cms.untracked.vstring()
)

# Output definition
process.out = cms.OutputModule("PoolOutputModule",
     #verbose = cms.untracked.bool(True),
     SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
     fileName = cms.untracked.string("Events.root"),
     outputCommands = cms.untracked.vstring('keep *') 
)

process.p = cms.Path()

process.outpath = cms.EndPath(process.out)
