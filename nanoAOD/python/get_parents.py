#!/usr/bin/env python
import imp, os, sys
from optparse import OptionParser
import re
import subprocess


parser = OptionParser()
parser.add_option("--module",           dest="module",                  help="Which module X in Samples.nanoAOD.X?")
parser.add_option("--check_in_miniAOD",           dest="check_in_miniAOD", default = None,                  help="Which module X in Samples.miniAOD.X?")
( options, args ) = parser.parse_args()

module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/nanoAOD/%s.py" % options.module )

try:
    tmp_module = imp.load_source( "allSamples", os.path.expandvars( module_file ) )
    allSamples = getattr(tmp_module, "allSamples")
except:
    raise RuntimeError( "Not found: Module: %s, module_file: %s" % (options.module, module_file) )

mAOD_samples = None
if options.check_in_miniAOD is not None:
    mAOD_module_file = os.path.expandvars( "$CMSSW_BASE/python/Samples/miniAOD/%s.py" % options.check_in_miniAOD )

    try:
        tmp_module = imp.load_source( "allSamples", os.path.expandvars( mAOD_module_file ) )
        mAOD_samples = getattr(tmp_module, "samples")
    except:
        raise RuntimeError( "Not found: Module: %s, module_file: %s" % (options.check_in_miniAOD, mAOD_module_file) )

for s in allSamples:
    miniAOD_parent = None
    if hasattr( s, "DAS"): 
        query = "parent dataset=%s"%s.DAS 
        proc = subprocess.Popen(['/cvmfs/cms.cern.ch/common/dasgoclient', '--query', query], stdout=subprocess.PIPE)
        miniAOD_parent = proc.stdout.readline().rstrip()
        if options.check_in_miniAOD is None:
            print "Needed:", miniAOD_parent 
    else:
        print "No DAS name found for %s" % s.name
    if mAOD_samples is not None and miniAOD_parent is not None:
        if mAOD_samples.find(miniAOD_parent): 
            print "Found in ", mAOD_samples.find(miniAOD_parent)
            pass
        else:
            print "NOT found:", miniAOD_parent 
