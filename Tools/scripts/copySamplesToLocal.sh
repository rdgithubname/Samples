#!/bin/bash

# run copy script to copy samples from DPM to local
# execute copy command with: copySamplesToLocal.sh Run2016_14Dec2018 True
# test copy command with: copySamplesToLocal.sh Run2016_14Dec2018

if [ "${2}" = "True" ]
then
    flag="True"
else
    flag="False"
fi
echo -e "import Samples.Tools.logger as logger;logger = logger.get_logger('INFO', logFile = None);from Samples.nanoAOD.${1} import samples\nsamples.copy_to_local(do_it=${flag})" | python
