import DirControl.Executables,os

VALUE = []

for i in DirControl.Executables.PATHS:
	f = []
	for (dirpath, dirnames, filenames) in os.walk(i):
		f.extend(filenames)
		break
	for j in f:
		if os.access(f"{i}/{j}", os.X_OK):
			VALUE.append(j)

