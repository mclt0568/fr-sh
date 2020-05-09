import readchar,string

Instructions={
	"\x1b[A":"up",
	"\x1b[B":"down",
	"\x1b[D":"left",
	"\x1b[C":"right",
	"\n":"enter",
	"\x03":"^c",
	"\x1b\x03":"a^c",}


def getInstructionAsInput():
	c = readchar.readkey()
	if c in string.printable:
		return c
	elif c in Instructions:
		return Instructions[c]
	else:
		return None