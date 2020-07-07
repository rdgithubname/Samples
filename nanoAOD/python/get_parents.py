#!/usr/bin/env python
import imp, os, sys
from optparse import OptionParser
import re
import subprocess
import json

parser = OptionParser()
parser.add_option("--module",           dest="module",                  help="Which module X in Samples.nanoAOD.X?")
parser.add_option("--check_in_miniAOD", dest="check_in_miniAOD", default = None,                  help="Which module X in Samples.miniAOD.X?")
parser.add_option("--json",             action='store_true', help="Dump a JSON file for TOP nanoAOD production?")
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

if os.path.exists( 'veto.txt' ):
    with open('veto.txt') as f:
        veto = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    veto = [x.strip() for x in veto]
else:
    veto = [] 

samples_dict = {}
for s in allSamples:
    miniAOD_parent = None
    if hasattr( s, "DAS"): 
        query = "parent dataset=%s"%s.DAS 
        proc = subprocess.Popen(['/cvmfs/cms.cern.ch/common/dasgoclient', '--query', query], stdout=subprocess.PIPE)
        miniAOD_parent = proc.stdout.readline().rstrip()
        if options.check_in_miniAOD is None:
            print "Needed:", miniAOD_parent

        # write json file for top nanoAOD production
        # https://github.com/cms-top/cmssw/blob/topNanoV6_from-CMSSW_10_2_18/PhysicsTools/NanoAOD/test/README.md
        # https://github.com/cms-top/cmssw/blob/topNanoV6_from-CMSSW_10_2_18/PhysicsTools/NanoAOD/test/topSamples.json
           
        if options.json:
            if "Summer16" in s.DAS or "Run2016" in s.DAS:
                year = "2016"
            elif "Fall17" in s.DAS or "Run2017" in s.DAS:
                year = "2017"
            elif "Autumn18" in s.DAS:
                year = "2018"
            elif "Run2018A" in s.DAS or "Run2018B" in s.DAS or "Run2018C" in s.DAS:
                year = "Run2018ABC"
            elif "Run2018D" in s.DAS:
                year = "Run2018D"

            if "Run201" in s.DAS:
                json_name = s.DAS.split('/')[1]+'_'+s.DAS.split('/')[2].split('-')[0]
            else:
                json_name = s.DAS.split('/')[1]
                era_str   =  s.DAS.split('/')[2]
                for ext_str in [ "ext%i"%i for i in range(1,10)] + ["ext"]:
                    if ext_str in era_str:
                        json_name+="_"+ext_str
                    break

            if not samples_dict.has_key(year):
                samples_dict[year] = {}
            if miniAOD_parent in veto:
                print "vetoed", miniAOD_parent
            else:
                samples_dict[year][miniAOD_parent] = {'name':json_name} 
             
    else:
        print "No DAS name found for %s" % s.name
    if mAOD_samples is not None and miniAOD_parent is not None:
        if mAOD_samples.find(miniAOD_parent): 
            print "Found in ", mAOD_samples.find(miniAOD_parent)
            pass
        else:
            print "NOT found:", miniAOD_parent 
if options.json:
    json.dump(samples_dict, file( options.module+'.json','w'))
