from CRABClient.UserUtilities import config
import CRABClient

#datasets = [
#'/bsll_4FermionCI_M_1000To2000_Lambda1TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_1000To2000_Lambda2TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_1000To2000_Lambda4TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_1000To2000_Lambda8TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_2000ToInf_Lambda1TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_2000ToInf_Lambda2TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_2000ToInf_Lambda4TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_2000ToInf_Lambda8TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_200To500_Lambda1TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_200To500_Lambda2TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_200To500_Lambda4TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_200To500_Lambda8TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_500To1000_Lambda1TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_500To1000_Lambda2TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_500To1000_Lambda4TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
#'/bsll_4FermionCI_M_500To1000_Lambda8TeV_13TeV_MadgraphMLM/jschulte-RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v3_MINIAOD-97622907258fdd18c13ba019aa6dffb1/USER',
 #          ]

with open('samples2017Fix.txt') as file:
    datasets = file.readlines()
    datasets = [line.rstrip() for line in datasets]

config = config()
config.General.workArea        = 'crab_nanoProd2017'
config.General.transferOutputs = True
config.General.transferLogs    = False
config.JobType.sendExternalFolder = True
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'NanoAODv9_2017_cfg.py'
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
	if "mc2017" in data:
		dirName = data.split('/')[1]
		print ("doing it right")
		config.General.requestName     = dirName
       		config.Data.outputDatasetTag     = 'RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_NANOAOD_v2'
        else:
		config.JobType.psetName = "NanoAODv9_2017_Data_cfg.py"	
		dirName = data.split('/')[1] + "_" + data.split('/')[2].split("-")[0] 
		config.General.requestName     = dirName
		config.Data.outputDatasetTag     = data.split('/')[2] + "-NANOAOD"
	try:
	        crabCommand('submit', config = config)
	except:
		print ("task submitted already, skipping")
