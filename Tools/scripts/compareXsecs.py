#!/usr/bin/env python
import os
import importlib

cmsbase = os.getenv("CMSSW_BASE")

# user input
relDir = "Samples/nanoAOD"
baseFile = 'Summer16_05Feb2018' # base sample file to compare to 
files = ['Fall17_14Dec2018', 'Autumn18'] # files to compare to - if left empty, all files in directory will be looped over
#

absDir = "%s/src/%s/python"%(cmsbase, relDir)
allFiles_ = os.listdir(absDir)
allFiles = [x.replace('.py','') for x in allFiles_ if x.endswith('.py') and not x.startswith('__')]

if not files:
    files = allFiles

if baseFile not in files:
    files.append(baseFile)

filesDict = {}

for f in files:
    if f not in allFiles:
        print "%s not in %s. Ignoring this file."%(f, absDir) 
        continue

    filesDict[f] = importlib.import_module('{}.{}'.format(relDir, f).replace('/','.'))
    
    if not hasattr(filesDict[f], 'allSamples'):
        del filesDict[f]

samples = {}

for f in filesDict:
    samples[f] = filesDict[f].allSamples

outfile = open("xsecDifferences.txt", "w")

for baseSamp in samples[baseFile]:
    for f in samples:
        for samp in samples[f]:
            if samp.name == baseSamp.name:
                if samp.xSection != baseSamp.xSection:
                    text = "%s xsec %s from %s different to xsec %s from %s"%(samp.name, samp.xSection, f, baseSamp.xSection, baseFile)
                    print "========================================================================================="
                    print text 
                    outfile.write(text + '\n')

outfile.close()
