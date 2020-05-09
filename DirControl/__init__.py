import DirControl.Executables
import os

CURRENT_PATH = os.path.abspath(".")

Executables.updatePathsExe()
Executables.updateCurrentExe()

def update():
	CURRENT_PATH = os.path.abspath(".")

def chdir():
	pass