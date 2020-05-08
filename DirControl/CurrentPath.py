import os
import DirControl

def get():
	return os.path.abspath(".")

def set(path):
	os.chdir(path)
	PathControl.PATH = os.path.abspath(".")