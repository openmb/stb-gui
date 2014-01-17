from enigma import getDistro, getMachineBrand as getMachineBrand2, getMachineName as getMachineName2, getImageVersionString, getBuildVersionString, getDriverDateString, getBoxType as getBoxType2

def getBoxType():
	return getBoxType2()

def getMachineName():
	return getMachineName2()

def getImageDistro():
	return getDistro()
      
def getImageVersion():
	return getImageVersionString()
      
def getImageBuild():
	return getBuildVersionString()