# System-health-monitor
A Bash script that monitors servers system health on AWS EC2.

## What it does?
-checks the disk usage and warns if usage is above 40%
-monitors memory usage
-tracks CPU load
-Displays timestamp of each check

## Tech Stack
-Bash scripting
-AWS ec2(ubuntu)
-Linux commands (df, free, uptime)

## How to run
./health.sh
python3 monitor.py
docker build -t health-monitor
