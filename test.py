import time,sys
for i in range(10):
	sys.stdout.write(f"\r{i}")
	time.sleep(1)
	sys.stdout.write("")
