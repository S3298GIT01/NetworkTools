#!/bin/bash

msfconsole -x "
use auxiliary/server/dhcp;
set SRVHOST 192.168.10.23;
set DHCPIPSTART 192.168.10.35;
set DHCPIPEND 192.168.10.200;
set NETMASK 255.255.255.0;
set ROUTER 192.168.10.1;
set DNSSERVER 1.1.1.1;
run"

