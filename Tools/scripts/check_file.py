#!/usr/bin/env python

import os, sys

from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile

def get_parser():
    ''' Argument parser for post-processing module.
    '''
import argparse
argParser = argparse.ArgumentParser()

argParser.add_argument('f')

args = argParser.parse_args()

if os.path.exists(args.f) and checkRootFile( args.f, checkForObjects = ["Events"]) and deepCheckRootFile( args.f ):
    print "passed:", args.f 
else:
    print "failed:", args.f
