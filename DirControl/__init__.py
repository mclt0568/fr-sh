import DirControl.Executables
import os

CURRENT_PATH = os.path.abspath(".")

Executables.updatePathsExe()
Executables.updateCurrentExe()

def updateCurrentPath():
	global CURRENT_PATH
	CURRENT_PATH = os.path.abspath(".")

def chdir(value):
	os.chdir(value)
	updateCurrentPath()
	Executables.updateCurrentExe()