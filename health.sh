#!/bin/bash

Date=$(date '+%Y-%m-%d' %H:%M:%S')
disk=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
echo "===System Health Monitor==="
echo "Date: $Date"
echo "Disk usage:"
if [ $disk -gt 40 ]
then 
echo"WARNING:disk usage is $disk%"
fi
echo "Memory usage:"
free -f
echo "CPU load:"
uptime 
echo "==========================="
