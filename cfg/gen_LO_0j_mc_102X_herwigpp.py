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
# with command line options: Configuration/GenProduction/python/herwigppFragment_LO_0j.py --fileout GEN_LO_0j_102X.root --mc --eventcontent RECOSIM --datatier GEN --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN --geometry DB:Extended --era Run2_2018 --python_filename tmp.py --no_exec -n options.maxEvents
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('GEN',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
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
    annotation = cms.untracked.string('Configuration/GenProduction/python/herwigppFragment_LO_0j.py nevts:%i'%options.maxEvents),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
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
    fileName = cms.untracked.string('GEN_LO_0j_102X.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v11', '')

process.generator = cms.EDFilter("ThePEGHadronizerFilter",
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(-1),
    dataLocation = cms.string('${HERWIGPATH}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    hwpp_LHE_Common = cms.vstring(
        'create ThePEG::Cuts /Herwig/Cuts/NoCuts', 
        'create ThePEG::LesHouchesInterface /Herwig/EventHandlers/LHEReader', 
        'set /Herwig/EventHandlers/LHEReader:Cuts /Herwig/Cuts/NoCuts', 
        'set /Herwig/EventHandlers/LHEReader:MomentumTreatment RescaleEnergy', 
        'set /Herwig/EventHandlers/LHEReader:WeightWarnings 0', 
        'set /Herwig/EventHandlers/LHEReader:InitPDFs 0', 
        'create ThePEG::LesHouchesEventHandler /Herwig/EventHandlers/LHEHandler', 
        'insert /Herwig/EventHandlers/LHEHandler:LesHouchesReaders 0 /Herwig/EventHandlers/LHEReader', 
        'set /Herwig/EventHandlers/LHEHandler:WeightOption VarNegWeight', 
        'set /Herwig/EventHandlers/LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor', 
        'set /Herwig/EventHandlers/LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
        'set /Herwig/EventHandlers/LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
        'set /Herwig/EventHandlers/LHEHandler:DecayHandler /Herwig/Decays/DecayHandler', 
        'insert /Herwig/EventHandlers/LHEHandler:PreCascadeHandlers 0 /Herwig/NewPhysics/DecayHandler', 
        'set /Herwig/Generators/LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler', 
        'set /Herwig/Shower/Evolver:MaxTry 100', 
        'set /Herwig/Shower/Evolver:HardVetoScaleSource Read', 
        'set /Herwig/Shower/KinematicsReconstructor:ReconstructionOption General', 
        'set /Herwig/Shower/KinematicsReconstructor:InitialInitialBoostOption LongTransBoost', 
        '+hwpp_MECorr_Common'
    ),
    hwpp_LHE_MadGraph = cms.vstring(
        '+hwpp_LHE_Common', 
        'set /Herwig/EventHandlers/LHEReader:PDFA /Herwig/Partons/cmsPDFSet', 
        'set /Herwig/EventHandlers/LHEReader:PDFB /Herwig/Partons/cmsPDFSet'
    ),
    hwpp_LHE_MadGraph_DifferentPDFs = cms.vstring(
        '+hwpp_LHE_Common', 
        'set /Herwig/EventHandlers/LHEReader:PDFA /Herwig/Partons/cmsHardPDFSet', 
        'set /Herwig/EventHandlers/LHEReader:PDFB /Herwig/Partons/cmsHardPDFSet'
    ),
    hwpp_LHE_Powheg = cms.vstring(
        '+hwpp_LHE_Powheg_Common', 
        'set /Herwig/EventHandlers/LHEReader:PDFA /Herwig/Partons/cmsPDFSet', 
        'set /Herwig/EventHandlers/LHEReader:PDFB /Herwig/Partons/cmsPDFSet'
    ),
    hwpp_LHE_Powheg_Common = cms.vstring(
        '+hwpp_LHE_Common', 
        'set /Herwig/Shower/Evolver:HardVetoMode Yes', 
        'set /Herwig/Shower/Evolver:HardVetoReadOption PrimaryCollision'
    ),
    hwpp_LHE_Powheg_DifferentPDFs = cms.vstring(
        '+hwpp_LHE_Powheg_Common', 
        'set /Herwig/EventHandlers/LHEReader:PDFA /Herwig/Partons/cmsHardPDFSet', 
        'set /Herwig/EventHandlers/LHEReader:PDFB /Herwig/Partons/cmsHardPDFSet'
    ),
    hwpp_MECorr_Common = cms.vstring('set /Herwig/Shower/Evolver:MECorrMode No'),
    hwpp_MECorr_HardOn = cms.vstring(
        '+hwpp_MECorr_Common', 
        'set /Herwig/Shower/Evolver:MECorrMode Hard'
    ),
    hwpp_MECorr_Off = cms.vstring('+hwpp_MECorr_Common'),
    hwpp_MECorr_On = cms.vstring(
        '+hwpp_MECorr_Common', 
        'set /Herwig/Shower/Evolver:MECorrMode Yes'
    ),
    hwpp_MECorr_SoftOn = cms.vstring(
        '+hwpp_MECorr_Common', 
        'set /Herwig/Shower/Evolver:MECorrMode Soft'
    ),
    hwpp_basicSetup = cms.vstring(
        'create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
        'set /Herwig/Generators/LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
        'set /Herwig/Generators/LHCGenerator:NumberOfEvents 10000000', 
        'set /Herwig/Generators/LHCGenerator:DebugLevel 1', 
        'set /Herwig/Generators/LHCGenerator:UseStdout 0', 
        'set /Herwig/Generators/LHCGenerator:PrintEvent 0', 
        'set /Herwig/Generators/LHCGenerator:MaxErrors 10000'
    ),
    hwpp_cm_13TeV = cms.vstring(
        'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 13000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV'
    ),
    hwpp_cmsDefaults = cms.vstring(
        '+hwpp_basicSetup', 
        '+hwpp_setParticlesStableForDetector'
    ),
    hwpp_pdf_CTEQ6L1 = cms.vstring(
        '+hwpp_pdf_CTEQ6L1_Common', 
        '+hwpp_ue_EE5C'
    ),
    hwpp_pdf_CTEQ6L1_CUETHS1 = cms.vstring(
        '+hwpp_pdf_CTEQ6L1_Common', 
        '+hwpp_ue_CUETHS1'
    ),
    hwpp_pdf_CTEQ6L1_Common = cms.vstring(
        'create ThePEG::LHAPDF /Herwig/Partons/cmsPDFSet ThePEGLHAPDF.so', 
        'set /Herwig/Partons/cmsPDFSet:PDFName cteq6ll.LHpdf', 
        'set /Herwig/Partons/cmsPDFSet:RemnantHandler /Herwig/Partons/HadronRemnants', 
        'set /Herwig/Particles/p+:PDF /Herwig/Partons/cmsPDFSet', 
        'set /Herwig/Particles/pbar-:PDF /Herwig/Partons/cmsPDFSet'
    ),
    hwpp_pdf_CTEQ6L1_Hard = cms.vstring(
        '+hwpp_pdf_CTEQ6L1_Hard_Common', 
        '+hwpp_ue_EE5C'
    ),
    hwpp_pdf_CTEQ6L1_Hard_CUETHS1 = cms.vstring(
        '+hwpp_pdf_CTEQ6L1_Hard_Common', 
        '+hwpp_ue_CUETHS1'
    ),
    hwpp_pdf_CTEQ6L1_Hard_Common = cms.vstring(
        'create ThePEG::LHAPDF /Herwig/Partons/cmsHardPDFSet ThePEGLHAPDF.so', 
        'set /Herwig/Partons/cmsHardPDFSet:PDFName cteq6ll.LHpdf', 
        'set /Herwig/Partons/cmsHardPDFSet:RemnantHandler /Herwig/Partons/HadronRemnants'
    ),
    hwpp_pdf_CTEQ6LL = cms.vstring('+hwpp_pdf_CTEQ6L1'),
    hwpp_pdf_CTEQ6LL_CUETHS1 = cms.vstring('+hwpp_pdf_CTEQ6L1_CUETHS1'),
    hwpp_pdf_CTEQ6LL_Hard = cms.vstring('+hwpp_pdf_CTEQ6L1_Hard'),
    hwpp_pdf_CTEQ6LL_Hard_CUETHS1 = cms.vstring('+hwpp_pdf_CTEQ6L1_Hard_CUETHS1'),
    hwpp_pdf_NNPDF30NNLO_Hard = cms.vstring(
        'create ThePEG::LHAPDF /Herwig/Partons/cmsHardPDFSet ThePEGLHAPDF.so', 
        'set /Herwig/Partons/cmsHardPDFSet:PDFName NNPDF30_nnlo_as_0118.LHgrid', 
        'set /Herwig/Partons/cmsHardPDFSet:RemnantHandler /Herwig/Partons/HadronRemnants'
    ),
    hwpp_setParticlesStableForDetector = cms.vstring(
        'set /Herwig/Particles/mu-:Stable Stable', 
        'set /Herwig/Particles/mu+:Stable Stable', 
        'set /Herwig/Particles/Sigma-:Stable Stable', 
        'set /Herwig/Particles/Sigmabar+:Stable Stable', 
        'set /Herwig/Particles/Lambda0:Stable Stable', 
        'set /Herwig/Particles/Lambdabar0:Stable Stable', 
        'set /Herwig/Particles/Sigma+:Stable Stable', 
        'set /Herwig/Particles/Sigmabar-:Stable Stable', 
        'set /Herwig/Particles/Xi-:Stable Stable', 
        'set /Herwig/Particles/Xibar+:Stable Stable', 
        'set /Herwig/Particles/Xi0:Stable Stable', 
        'set /Herwig/Particles/Xibar0:Stable Stable', 
        'set /Herwig/Particles/Omega-:Stable Stable', 
        'set /Herwig/Particles/Omegabar+:Stable Stable', 
        'set /Herwig/Particles/pi+:Stable Stable', 
        'set /Herwig/Particles/pi-:Stable Stable', 
        'set /Herwig/Particles/K+:Stable Stable', 
        'set /Herwig/Particles/K-:Stable Stable', 
        'set /Herwig/Particles/K_S0:Stable Stable', 
        'set /Herwig/Particles/K_L0:Stable Stable'
    ),
    hwpp_ue_EE5C = cms.vstring(
        '+hwpp_ue_EE5CEnergyExtrapol', 
        'set /Herwig/Hadronization/ColourReconnector:ColourReconnection Yes', 
        'set /Herwig/Hadronization/ColourReconnector:ReconnectionProbability 0.49', 
        'set /Herwig/Partons/RemnantDecayer:colourDisrupt 0.80', 
        'set /Herwig/UnderlyingEvent/MPIHandler:InvRadius 2.30', 
        'set /Herwig/UnderlyingEvent/MPIHandler:softInt Yes', 
        'set /Herwig/UnderlyingEvent/MPIHandler:twoComp Yes', 
        'set /Herwig/UnderlyingEvent/MPIHandler:DLmode 2'
    ),
    hwpp_ue_EE5CEnergyExtrapol = cms.vstring(
        'set /Herwig/UnderlyingEvent/MPIHandler:EnergyExtrapolation Power', 
        'set /Herwig/UnderlyingEvent/MPIHandler:ReferenceScale 7000.*GeV', 
        'set /Herwig/UnderlyingEvent/MPIHandler:Power 0.33', 
        'set /Herwig/UnderlyingEvent/MPIHandler:pTmin0 3.91*GeV'
    ),
    parameterSets = cms.vstring(
        'hwpp_cmsDefaults', 
        'hwpp_ue_EE5C', 
        'hwpp_cm_13TeV', 
        'hwpp_pdf_CTEQ6L1', 
        'hwpp_pdf_NNPDF30NNLO_Hard', 
        'hwpp_LHE_MadGraph_DifferentPDFs', 
        'hwpp_MECorr_Off'
    ),
    repository = cms.string('HerwigDefaults.rpo'),
    run = cms.string('LHC')
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring(options.gridpack),
    nEvents = cms.untracked.uint32(options.maxEvents),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
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
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
