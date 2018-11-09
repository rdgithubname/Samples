import os
import glob
import argparse

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--dir', action='store', default='crab_', help="Which crab directories?")
argParser.add_argument('--resubmit', action='store_true', help="Automatically resubmit?")
args = argParser.parse_args()


dirs = glob.glob(args.dir+'*')

fullDirs = []
for d in dirs:
    fullDirs += glob.glob(d+'/*')

nSuccess    = 0
nFailed     = 0
nUnknown    = 0
nRunning    = 0

for d in fullDirs:
    print "------------------------"
    print "- Working on directory -"
    print d
    try:
        res = crabCommand('status', d)
    except HTTPException:
        print "CRAB service issue"
        continue
    if res['status'] == 'FAILED':
        nFailed += 1
        if args.resubmit:
            try:
                resub = crabCommand('resubmit', d)
                print "Resubmitted job..."
            except HTTPException:
                print "Couldn't resubmit the job."
    elif res['status'] == 'COMPLETED':
        nSuccess += 1
    elif res['status'] == 'SUBMITTED':
        nRunning +=1
    else:
        nUnknown += 1
    
    if res.has_key('publication'):
        if res['publication'].has_key('failed'):
            try:
                resub_pub = crabCommand('resubmit', '--publication', d)
                print "Publication resubmitted"
            except HTTPException:
                print "Couldn't resubmit the publication."
            

print "######### SUMMARY ##########"
print "Successfull jobs:", nSuccess
print "Failed jobs:", nFailed
print "Running jobs:", nRunning
print "Unknonw status:", nUnknown


