# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/TOP-RunIISummer15wmLHEGS-00050-fragment.py --fileout file:TOP-RunIISummer15wmLHEGS-00050.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename TOP-RunIISummer15wmLHEGS-00050_1_cfg.py --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1551447881%100) -n options.maxEvents
import FWCore.ParameterSet.Config as cms

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

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
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
    annotation = cms.untracked.string('Configuration/GenProduction/python/TOP-RunIISummer15wmLHEGS-00050-fragment.py nevts:%i'%options.maxEvents),
    name = cms.untracked.string('Applications')
)

# Output definition
process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('GEN_LO_0j_71X.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
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
        processParameters = cms.vstring('TimeShower:nPartonsInBorn = 2', 
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'SpaceShower:alphaSvalue=0.1108', 
            'PDF:pSet=LHAPDF6:NNPDF30_lo_as_0130', 
            'MultipartonInteractions:pT0Ref=2.197139e+00', 
            'MultipartonInteractions:expPow=1.608572e+00', 
            'ColourReconnection:range=6.593269e+00'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'processParameters')
    )
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args               = cms.vstring(options.gridpack),
    nEvents            = cms.untracked.uint32(options.maxEvents),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
)


# Path and EndPath definitions
process.lhe_step              = cms.Path(process.externalLHEProducer)
process.generation_step       = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step           = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step    = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RECOSIMoutput_step)

# filter all path with the production filter sequence
for path in process.paths:
    if path in ['lhe_step']: continue
    getattr(process,path)._seq = process.generator * getattr(process,path)._seq

