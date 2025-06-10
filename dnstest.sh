#!/bin/bash

# Set the URL to test
url="1a-dual-wired-internet-no-load-b-wvtndwmwrv.dynamic-m.com" # Replace with your desired URL

while true; do
  # Print the date and time
  timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  echo "[$timestamp] Starting DNS test for $url"

  # Perform DNS lookup (using dig)
  dig +short "$url"

 # Alternative using nslookup (less detailed output):
 # nslookup "$url"


  # Clear the DNS cache (systemd-resolved)
  #Does not work in pods
  # resolvectl flush-caches

  # Alternative for older systems or different resolvers:
  # /etc/init.d/dns-clean restart (or the appropriate command for your system)
  # sudo rndc flush  (if you're using BIND)


  # Print completion message
  echo "[$timestamp] DNS test complete. Cache flushed."


  # Set the interval (in seconds) between tests
  sleep_interval=10  #  Test every 60 seconds (adjust as needed)
  sleep "$sleep_interval"

done
