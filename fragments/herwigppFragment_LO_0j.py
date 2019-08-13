# HERWIG++ fragment created for ttgamma LO (no extra jets)
import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('GRIDPACK'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.HerwigppDefaults_cfi      import *
from Configuration.Generator.HerwigppUE_EE_5C_cfi      import *
from Configuration.Generator.HerwigppPDF_CTEQ6_LO_cfi  import *
from Configuration.Generator.HerwigppEnergy_13TeV_cfi  import *
from Configuration.Generator.HerwigppLHEFile_cfi       import *
from Configuration.Generator.HerwigppMECorrections_cfi import *

generator = cms.EDFilter("ThePEGHadronizerFilter",
    herwigDefaultsBlock,
    herwigppUESettingsBlock,
    herwigppPDFSettingsBlock,
    herwigppEnergySettingsBlock,
    herwigppLHEFileSettingsBlock,
    herwigppMECorrectionsSettingsBlock,

    configFiles = cms.vstring(),
        hwpp_pdf_NNPDF30NNLO_Hard = cms.vstring(
            'create ThePEG::LHAPDF /Herwig/Partons/cmsHardPDFSet ThePEGLHAPDF.so',
            'set /Herwig/Partons/cmsHardPDFSet:PDFName NNPDF30_nnlo_as_0118.LHgrid',
            'set /Herwig/Partons/cmsHardPDFSet:RemnantHandler /Herwig/Partons/HadronRemnants',      
        ),
    parameterSets = cms.vstring(
        'hwpp_cmsDefaults',
        'hwpp_ue_EE5C',
        'hwpp_cm_13TeV',
        'hwpp_pdf_CTEQ6L1',                 # Shower PDF matching with the tune
        'hwpp_pdf_NNPDF30NNLO_Hard',        # PDF of hard subprocess
        'hwpp_LHE_MadGraph_DifferentPDFs',
        'hwpp_MECorr_Off',                  # Switch off ME corrections while showering LHE files as recommended by Herwig++ authors
    ),

        crossSection     = cms.untracked.double(-1),
        filterEfficiency = cms.untracked.double(1.0),
)

ProductionFilterSequence = cms.Sequence(generator)
