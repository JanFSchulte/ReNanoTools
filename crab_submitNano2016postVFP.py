from CRABClient.UserUtilities import config
import CRABClient

with open('samples2016postVFPFix.txt') as file:
    datasets = file.readlines()
    datasets = [line.rstrip() for line in datasets]

config = config()
config.General.workArea        = 'crab_nanoProd16postVFP'
config.General.transferOutputs = True
config.General.transferLogs    = False
config.JobType.sendExternalFolder = True
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'NanoAODv9_2016_postVFP_cfg.py'
#config.JobType.numCores    = 4
config.JobType.maxMemoryMB = 3500
#config.JobType.maxJobRuntimeMin= 180
#config.Data.ignoreLocality = True
config.JobType.sendPythonFolder=True
#config.Data.inputDBS = 'phys03'
config.Data.splitting   = 'EventAwareLumiBased'
config.Data.unitsPerJob = 200000
config.Data.totalUnits  = -1
config.Data.outLFNDirBase = '/store/user/jschulte/'
config.JobType.outputFiles  = ['nano.root']
config.Data.publication = True
config.Data.allowNonValidInputDataset = True
#config.Data.outputPrimaryDataset = 'Ztest-7TeV_M-1400To2300_13TeV-pythia8'
#config.Data.outputDatasetTag     = 'RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v7'
config.JobType.allowUndistributedCMSSW=True
config.section_('Site')
#config.Site.blacklist = ['T2_US_Caltech','T2_US_Florida','T2_US_MIT','T2_US_Nebraska','T2_US_Vanderbilt','T2_US_Wisconsin']
#config.Site.whitelist = ['T2_US_Purdue', 'T3_KR_KNU']
#config.Site.whitelist = ['T2_US_Purdue']
config.Site.storageSite = 'T2_US_Purdue'
config.section_('Debug')
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    
    for data in datasets:
        config.Data.inputDataset = data
	if "UL16MiniAODAPV" in data:
                print ("submitting MC sample")
		dirName = data.split('/')[1]
		config.General.requestName     = dirName
       		config.Data.outputDatasetTag     = 'RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_v1_NANOAOD'
        else:
		config.JobType.psetName = "NanoAODv9_2016_postVFP_Data_cfg.py"	
		dirName = data.split('/')[1] + "_" + data.split('/')[2].split("-")[0] 
                if "ver1" in data:
		    dirName = data.split('/')[1] + "_ver1" + "_" + data.split('/')[2].split("-")[0] 
                if "ver2" in data:
		    dirName = data.split('/')[1] + "_ver2" + "_" + data.split('/')[2].split("-")[0] 
		config.General.requestName     = dirName
		config.Data.outputDatasetTag     = data.split('/')[2] + "-NANOAOD"
        crabCommand('submit', config = config)
