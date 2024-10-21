#!/bin/bash

while true; do
    iperf3 -c <server_ip> -t 60 | grep "0.00-60.00|\0.00-60.01" >> iperf_log.txt
    sleep 3600  # Run every hour
done
