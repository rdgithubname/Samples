# check the Samples files if variable name == sample name and if the variable name contains LO/NLO/pow

import os, imp
from optparse import OptionParser

parser = OptionParser(usage="python checkSampleName.py [options]", description="Check sample files if variable name == sample.name" )
parser.add_option("--file",   dest="file",   type=str, help="Which file to check?")
parser.add_option("--module", dest="module", default="", help="Which module X in Samples.miniAOD.X?")
( options, args ) = parser.parse_args()

if options.module == "":
    options.module = options.file

with open( options.file + ".py", "r" ) as f:
    lines = f.readlines()

counter = 0
allSampleNames = []
for line in lines:
    if line.startswith("#"): continue
    sampleLine = line.split("Sample(")
    if len( sampleLine ) <= 1: continue
    counter   += 1
    varName    = sampleLine[0].split(" ")[0]
    sampleName = sampleLine[1].split("\"")[1]
    allSampleNames.append(sampleName)
    if not any( [ (order in varName) for order in ['LO', 'NLO', 'pow'] ] ):
        print "No calculation order given in samplename %s!"%sampleName
    if varName != sampleName:
        print "Samplename of %s does not match variable name!"%sampleName


module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/miniAOD/%s.py" % options.module )
try:
    tmp_module = imp.load_source( "allSamples", os.path.expandvars( module_file ) )
    datasets   = getattr( tmp_module, "allSamples" )
except:
    raise RuntimeError( "Not found: Module: %s, module_file: %s" % (options.module, module_file) )

samples = [sample.name for sample in datasets]
if counter != len( samples ):
    print "Not all samples in allSamples! counter = %i, len(allSamples) = %i"%(counter, len( allSamples ))
    print "Missing Samples:"
    print list( set(allSampleNames) - set(samples) )
    print "Double entries in allSamples:"
    print list( set( [ x for x in samples if samples.count(x) > 1] ) )
