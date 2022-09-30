# ReNanoTools
Tools to Re-Nano Run3 samples for the high mass dilepton search

## CMSSW setup:

```
cmsrel CMSSW_12_4_9
cd CMSSW_12_4_9/src
cmsenv
git cms-merge-topic JanFSchulte:nanoProdRun3
scram b -j 4
```

## Job submission setup

```
git clone https://github.com/JanFSchulte/ReNanoTools.git
cd ReNanoTools
git fetch
git switch Run3
```

The repository contains 3 types of files:

* CMSSW python configuration files for NanoAOD production for Run 3 Data and Run 3 MC from the Winter22 campaign
* a .txt containing a full list of all data and background samples that are needed (empty for now)
* a python scripts to submit crab jobs for the Nano workflows for both data and MC for the samples in the .txt file

