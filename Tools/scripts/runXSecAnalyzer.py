#!/usr/bin/env python

'''
Get x-secs for miniAOD samples from the GenXSec analyzer
Tested in CMSSW 10_2_9
'''

import imp, os, sys
import subprocess, shutil
from optparse import OptionParser
import re

## import all the samples
# 2016 FastSim
from Samples.miniAOD.Spring16_miniAODv2         import allSamples as Spring16_miniAODv2
from Samples.miniAOD.Summer16_Fast_miniAODv3    import allSamples as Summer16_Fast_miniAODv3
# 2017 FastSim
from Samples.miniAOD.Fall17_Fast_miniAODv2      import allSamples as Fall17_Fast_miniAODv2
# 2016 FullSim
from Samples.miniAOD.Summer16_miniAODv2         import allSamples as Summer16_miniAODv2
from Samples.miniAOD.Summer16_miniAODv3         import allSamples as Summer16_miniAODv3
# 2017 FullSim
from Samples.miniAOD.Fall17_miniAODv2           import allSamples as Fall17_miniAODv2
# 2018 FullSim
from Samples.miniAOD.Autumn18_miniAODv1         import allSamples as Autumn18_miniAODv1
# 2016 Data
from Samples.miniAOD.Run2016_17Jul2018          import allSamples as Run2016_17Jul2018
# 2017 Data
from Samples.miniAOD.Run2017_31Mar2018          import allSamples as Run2017_31Mar2018
# 2018 special HEM Data
from Samples.miniAOD.Run2018_26Sep2018          import allSamples as Run2018_26Sep2018
# 2018 prompt Data (in the end only for D!)
from Samples.miniAOD.Run2018_promptReco         import allSamples as Run2018_promptReco
# 2018 rereco Data (for A->C)
from Samples.miniAOD.Run2018_17Sep2018 import allSamples as Run2018_17Sep2018

## define modules and samples
all_modules  = [ "Spring16_miniAODv2", "Summer16_Fast_miniAODv3", "Fall17_Fast_miniAODv2", "Summer16_miniAODv2", "Summer16_miniAODv3", "Fall17_miniAODv2", "Autumn18_miniAODv1" ]
all_modules += [ "Run2016_17Jul2018", "Run2017_31Mar2018", "Run2018_26Sep2018", "Run2018_promptReco", "Run2018_17Sep2018", "Run2017_17Nov2017" ]

allSamples  = Spring16_miniAODv2 + Summer16_Fast_miniAODv3 + Fall17_Fast_miniAODv2 + Summer16_miniAODv2 + Summer16_miniAODv3 + Fall17_miniAODv2 + Autumn18_miniAODv1
allSamples += Run2016_17Jul2018 + Run2017_31Mar2018 + Run2018_26Sep2018 + Run2018_promptReco + Run2018_17Sep2018

parser = OptionParser(usage="python runXSecAnalyzer.py [options] component1 [ component2 ...]", \
                          description="Get x-secs using the CMSSW GenXSecAnalyzer. Interface similar to launch.py.")
parser.add_option("--module",   dest="module", choices = all_modules,   help="Which module X in Samples.miniAOD.X?")
parser.add_option("--sample",   dest="sample",                          help="Which sample?")
( options, args ) = parser.parse_args()

## default cmsRun cfg file
defaultCFG = """
import FWCore.ParameterSet.Config as cms
process = cms.Process("GenXSec")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('{FILEPATH}') )
process.dummy = cms.EDAnalyzer("GenXSecAnalyzer", genFilterInfoTag = cms.InputTag("genFilterEfficiencyProducer") )
process.p = cms.Path(process.dummy)"""

cfgFile     = 'xsecCfg.py'
identifier  = "After filter: final cross section ="

## load modules
module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/miniAOD/%s.py" % options.module )
try:
    tmp_module = imp.load_source( options.sample, os.path.expandvars( module_file ) ) 
    datasets   = getattr(tmp_module, options.sample)
except:
    raise RuntimeError( "Not found: Sample: %s, Module: %s, module_file: %s" % (options.sample, options.module, module_file) ) 

if not isinstance( datasets, list ): datasets = [ datasets ]

print "## Will process from module %s the following samples: %s"%(options.module,  ",".join( d.name for d in datasets ) )

for dataset in datasets:
    replaceString = {'FILEPATH': dataset.files[0]}
    cmsCfgString = defaultCFG.format( **replaceString )
    
    cmsRunCfg = open(cfgFile, 'w')
    cmsRunCfg.write(cmsCfgString)
    cmsRunCfg.close()

    print "Working on Dataset:", dataset.name

    p = subprocess.Popen(['cmsRun', cfgFile], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.stderr.readlines()
    for line in output:
        print line
        if line.startswith(identifier): result = line

    xsec, unc = float(result.split(identifier)[1].split('+-')[0]), float(result.split(identifier)[1].split('+-')[1].replace('pb',''))
    
    dataset.xsec = xsec

    os.remove(cfgFile)
    
print "Found the following x-secs:"
print "{:60}{:10}".format("Name", "x-sec (pb)")
for dataset in datasets:
    print "{:60}{:10}".format(dataset.name, dataset.xsec)


