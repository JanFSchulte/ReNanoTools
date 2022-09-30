from CRABClient.UserUtilities import config
import CRABClient

with open('samplesRun3.txt') as file:
    datasets = file.readlines()
    datasets = [line.rstrip() for line in datasets]

config = config()
config.General.workArea        = 'crab_nanoProd'
config.General.transferOutputs = True
config.General.transferLogs    = False
config.JobType.sendExternalFolder = True
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'run3Nano_Winter22MC_cfg_py_NANO.py'
config.JobType.maxMemoryMB = 3500
config.JobType.sendPythonFolder=True
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 20
config.Data.totalUnits  = -1
config.Data.outLFNDirBase = '/store/user/jschulte/'
config.JobType.outputFiles  = ['nano.root']
config.Data.publication = True
config.Data.allowNonValidInputDataset = True
config.JobType.allowUndistributedCMSSW=True
config.section_('Site')
config.Site.storageSite = 'T2_US_Purdue'
config.section_('Debug')
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    
    for data in datasets:
        print (data)
        config.Data.inputDataset = data
        if "Winter22" in data:
            dirName = data.split('/')[1]
            print (dirName)
            config.General.requestName     = dirName
            config.Data.outputDatasetTag     = 'Run3Winter22_ReNanoAOD_v1'
        else:
            config.JobType.psetName = "run3Nano_data_cfg.py"	
            dirName = data.split('/')[1] + "_" + data.split('/')[2].split("-")[0] 
            config.General.requestName     = dirName
            config.Data.outputDatasetTag     = data.split('/')[2] + "-NANOAOD"
	try:
            crabCommand('submit', config = config)
	except:
	    print("submission failed")
