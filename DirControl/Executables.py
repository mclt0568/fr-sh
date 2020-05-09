import os
import VariableControl
import DirControl

EXECUTABLES_PATHS = []
EXECUTABLES_CURRENT = []

PATHS = VariableControl.ENVVAR["PATH"].split(":")

def updatePathsExe():
	global EXECUTABLES_PATHS
	EXECUTABLES_PATHS = []
	for i in PATHS:
		f = []
		for (dirpath, dirnames, filenames) in os.walk(i):
			f.extend(filenames)
			break
		for j in f:
			if os.access(i+"/"+j,os.X_OK):
				EXECUTABLES_PATHS.append(j)
def updateCurrentExe():
	global EXECUTABLES_CURRENT
	EXECUTABLES_CURRENT = []
	f=[]
	for (dirpath, dirnames, filenames) in os.walk(DirControl.CURRENT_PATH):
		f.extend(filenames)
		break
	for j in f:
		if os.access(DirControl.CURRENT_PATH+"/"+j,os.X_OK):
			EXECUTABLES_CURRENT.append(j)