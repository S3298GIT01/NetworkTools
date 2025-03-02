#!/bin/bash

timeout 86400
while true; do
    iperf3 -c <server_ip> -t 60 | grep "0.00-60.0[0-9]" >> iperf_log.txt
    sleep 3600  # Run every hour
done
