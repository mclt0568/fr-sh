import VariableControl,DirControl
from Interface.ReadCharControl import getInstructionAsInput
from sys import stdout


tempCmd = ""

def run():
	global tempCmd
	Prompt = VariableControl.PREVAR["PROMPT_BASIC"]["value"].format(DirControl.CURRENT_PATH)
	while True:
		stdout.write(f"\r{Prompt}{tempCmd}")
		c = getInstructionAsInput()
		if c == "^c":
			break
		else:
			tempCmd += c