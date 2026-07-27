import subprocess
import datetime

def get_disk():
	output=subprocess.run(['df','-h','/'],capture_output=True,text=True)
	lines=output.stdout.split('\n')
	percent=int(lines[1].split()[4].replace('%',''))

	if percent>40:
		return f"WARNING:Disk at {percent}%\n{output.stdout}"
	else:
		return f"OK:Disk usage at {percent}%\n{output.stdout}"

def get_memory():
	output=subprocess.run(['free','-h'],capture_output=True,text=True)
	return output.stdout

def get_CPU():
	output=subprocess.run(['uptime'],capture_output=True,text=True)
	return output.stdout

time=datetime.datetime.now()

report=f"""
===System Health Report===
Time:{time}

Disk usage:
{get_disk()} 
Memory:
{get_memory()}
CPU load:
{get_CPU()}
==========================
"""
print(report)

with open("health.log","a") as f:
	f.write(report)
