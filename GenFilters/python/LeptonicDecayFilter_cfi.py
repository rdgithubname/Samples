import FWCore.ParameterSet.Config as cms

leptonicDecayFilter = cms.EDFilter("LeptonicDecayFilter",
    src = cms.InputTag("source"),
    #src = cms.InputTag("externalLHEProducer"),
    minLeptonicWs = cms.int32(0),
    minLeptonicZs = cms.int32(0),
)   
