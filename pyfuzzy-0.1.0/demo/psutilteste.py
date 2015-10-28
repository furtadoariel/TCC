import psutil
psutil.cpu_times()
print psutil.cpu_count()
memory =0
for x in psutil.pids():
	p = psutil.Process(x)
	memory += p.memory_percent()
print memory