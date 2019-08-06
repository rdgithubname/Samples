# Header for gen production configs

import os

import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing ('standard')
options.register('gridpack',  '$CMSSW_BASE/src/Samples/cfg/gridpack.tar.xz',  VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,  "Which Gridpack?")
options.register('outputDir', './',                 VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,  "Where to store the output root file?")
options.maxEvents=1000 # maxEvents is a registered option. 

options.outputDir = os.path.expandvars( options.outputDir )
options.gridpack  = os.path.expandvars( options.gridpack )

if not 'ipython' in VarParsing.sys.argv[0]: options.parseArguments()
else: print "No parsing of arguments!"

if not os.path.isdir(options.outputDir):
    os.makedirs(options.outputDir)



# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/pythiaFragmentCUEP8M1_NLO_01j.py --fileout GEN_LO_0j_71X.root --mc --eventcontent RECOSIM --datatier GEN --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN --magField 38T_PostLS1 --python_filename tmp.py --no_exec -n options.maxEvents
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/pythiaFragmentCUEP8M1_NLO_01j.py nevts:%i'%options.maxEvents),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('GEN_LO_0j_71X.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8aMCatNLOSettings = cms.vstring('SpaceShower:pTmaxMatch = 1', 
            'SpaceShower:pTmaxFudge = 1', 
            'SpaceShower:MEcorrections = off', 
            'TimeShower:pTmaxMatch = 1', 
            'TimeShower:pTmaxFudge = 1', 
            'TimeShower:MEcorrections = off', 
            'TimeShower:globalRecoil = on', 
            'TimeShower:limitPTmaxGlobal = on', 
            'TimeShower:nMaxGlobalRecoil = 1', 
            'TimeShower:globalRecoilMode = 2', 
            'TimeShower:nMaxGlobalBranch = 1', 
            'TimeShower:weightGluonToQuark = 1'),
        processParameters = cms.vstring('JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = options.maxEvents.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 30.', 
            'JetMatching:doFxFx = on', 
            'JetMatching:qCutME = 10.', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 1', 
            'TimeShower:mMaxGamma = 4.0'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'pythia8aMCatNLOSettings', 
            'processParameters')
    )
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(options.maxEvents),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    args = cms.vstring(options.gridpack)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RECOSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

