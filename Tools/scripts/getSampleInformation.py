#!/usr/bin/env python
import imp, os, sys
from optparse import OptionParser
import re

parser = OptionParser(usage="python getSampleInformation.py [options] component1", \
                          description="Get all important information (number of files, events, DAS name) of the selected sample file")
parser.add_option("--module",           dest="module",                  help="Which module X in Samples.nanoAOD.X?")
parser.add_option("--showDAS",         action="store_true",             help="Show DAS name?")
parser.add_option("--sortedByNEvents", action="store_true",             help="Sort by number of events?")
( options, args ) = parser.parse_args()


module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/nanoAOD/%s.py" % options.module )
try:
    tmp_module = imp.load_source( "allSamples", os.path.expandvars( module_file ) )
    allSamples = getattr(tmp_module, "allSamples")
except:
    raise RuntimeError( "Not found: Module: %s, module_file: %s" % (options.module, module_file) )


print
print "Module %s contains the following samples:"%options.module
if options.showDAS:
    print "{:40}{:8}{:10}{:100}".format("Name", "NFiles", "NEvts (M)", "DAS")
    if options.sortedByNEvents:
        allSamples.sort(key = lambda x: -x.nEvents)
    for sample in allSamples:
        print "{:40}{:<8}{:<10.2f}{:100}".format(sample.name, len(sample.files), sample.nEvents/1e6, sample.DAS)
else:
    print "{:40}{:8}{:10}".format("Name", "NFiles", "NEvts (M)")
    if options.sortedByNEvents:
        allSamples.sort(key = lambda x: -x.nEvents)
    for sample in allSamples:
        print "{:40}{:<8}{:<10.2f}".format(sample.name, len(sample.files), sample.nEvents/1e6)


