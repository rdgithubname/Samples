#!/usr/bin/env python

import os, sys
import subprocess

from Analysis.Tools.helpers import checkRootFile, deepCheckRootFile

redirector = "root://cms-xrd-global.cern.ch/"

def which(pgm):
    path=os.getenv('PATH')
    for p in path.split(os.path.pathsep):
        p=os.path.join(p,pgm)
        if os.path.exists(p) and os.access(p,os.X_OK):
            return p

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser()

    argParser.add_argument('--logLevel',  action='store', nargs='?',  choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],   default='INFO', help="Log level for logging" )
    argParser.add_argument('--file',      action='store', type=str, help="Which file?" )
    argParser.add_argument('--target',    action='store', nargs='?',  default='/scratch-cbe/users/hephy/tmp/', help="Where to go." )
    argParser.add_argument('--redirector',action='store', nargs='?',  default=redirector, help="Where to go." )
    argParser.add_argument('--noCheck',   action='store_true',    help="Run the file on a small sample (for test purpose), bool flag set to True if used" )
    argParser.add_argument('--noCopy',    action='store_true',    help="Don't copy" )

    return argParser

args = get_parser().parse_args()

source =  args.redirector+ args.file 
target =  args.target+     args.file 

if args.noCheck:
    if  os.path.exists(target):
        print "Found file %s. No check. Skip." % target
        sys.exit(0)
else:
    if os.path.exists(target) and checkRootFile( target, checkForObjects = ["Events"]) and deepCheckRootFile( target ):
        print "Found file %s. Checked it. Skip." % target
        sys.exit(0)

executable = ["echo", "xrdcp"] if args.noCopy else [which("xrdcp")]
 
cmd = executable + [ "-p", "-f", source, target]

subprocess.Popen( cmd )
