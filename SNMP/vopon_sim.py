# version: 0.45
# Release notes:
#  0.45 - Fixed Vertiv trap errors using IPv4, corrected IAD battery traps
#  0.40 - Change Vertiv Trap to use IAD IPv4 address
#  0.35 - IPv4 Adtran and IPv6 
from calendar import c
import time
from scapy.all import *
import json
import os
import random

def loadConfig(config_file):
    print("Loading config file => " + config_file)
    print()
    try:
        with open(config_file, "r") as f:
            result = json.load(f)
            print(result)
            #return json.load(f)
            return result
    except FileNotFoundError as err:
        print(err)

def displayAddresses(active_config):
    print("Address Information:")
    print("\tIAD's IPv4 Source:\t"+active_config["ipv4Src"])
    print("\tNetcool IPv4 Dest:\t"+active_config["ipv4Dst"])
    print()
#    print("\tIPv6 Interface:\t"+active_config["v6iface"])
#    print("\tIPv6 Src MAC:\t"+active_config["ipv6EthSrcMac"])
    print("\tVertiv UPS MAC Address:\t"+active_config["upsMac"])
#    print("\tIPv6 Dest Mac:\t"+active_config["ipv6EthDstMac"])
#    print("\tIPv6 Source:\t"+active_config["ipv6Src"])
#    print("\tIPv6 Dest:\t"+active_config["ipv6Dst"])

def displaySnmp(active_config):
    print("SNMP Information:")
    print("\tIAD Community string:\t"+active_config["adtranCommunity"])
#    print("\tIPv6 Community:\t"+active_config["v6Community"])
    print("\tUPS Community string:\t"+active_config["upsCommunity"])

def addressesMenu(active_config):
    print("==== Addresses Menu ====")
    displayAddresses(active_config)
    print()
    #print("Ctech Macon Rtr: 54:a6:19:e1:b7:6f    Multicast: 33:33:00:01:00:02")
    #print("QA1 Router     : ??                   VertivUPS: 54:a6:19:e1:b7:6f")
    #print()
    print("1) Change IAD's IPv4 Source")
    print("2) Change Netcool IPv4 Dest")
#   print("3) Change IPv6 Interface")
#   print("4) Change IPv6 Source MAC")
    print("4) Change Vertiv UPS MAC")
#   print("5) Change IPv6 Dest MAC")
#   print("6) Change IPv6 Source")
#   print("7) Change IPv6 Dest")
    print("0) <- Back")
    print()

def handleAddresses(active_config):
    addressesMenu(active_config)
    try:
        option = int(input("Enter your choice =>\t"))
    except ValueError as err:
        option = 0 

    while option != 0:
        if option == 1:
            print()
            temp = input("Enter new IAD IPv4 Source\t["+active_config["ipv4Src"]+"]:\t")
            if temp != "":
                active_config["ipv4Src"] = temp
        elif option == 2:
            print()
            temp = input("Enter new Netcool IPv4 Dest\t["+active_config["ipv4Dst"]+"]:\t")
            if temp != "":
                active_config["ipv4Dst"] = temp
#        elif option == 3:
#            print()
#            temp = input("Enter new IPv6 Interface\t["+active_config["v6iface"]+"]:\t")
#            if temp != "":
#                active_config["v6iface"] = temp
#        elif option == 4:
#            print()
#            temp = input("Enter new IPv6 Source MAC\t["+active_config["ipv6EthSrcMac"]+"]:\t")
#            if temp != "":
#                active_config["ipv6EthSrcMac"] = temp
        elif option == 4:
            print()
            temp = input("Enter new Vertiv UPS MAC\t["+active_config["upsMac"]+"]:\t")
            if temp != "":
                active_config["upsMac"] = temp
#        elif option == 5:
#            print()
#            temp = input("Enter new IPv6 Dest MAC\t["+active_config["ipv6EthDstMac"]+"]:\t")
#            if temp != "":
#                active_config["ipv6EthDstMac"] = temp
#        elif option == 6:
#            print()
#            temp = input("Enter new IPv6 Source\t["+active_config["ipv6Src"]+"]:\t")
#            if temp != "":
#                active_config["ipv6Src"] = temp
#        elif option == 7:
#            print()
#            temp = input("Enter new IPv6 Dest\t["+active_config["ipv6Dst"]+"]:\t")
#            if temp != "":
#                active_config["ipv6Dst"] = temp
        else:
            print("====> Invalid option")
    
        print()
        addressesMenu(active_config)
        try:
            option = int(input("Enter your choice =>\t"))
        except ValueError as err:
            option = 0 

def snmpMenu(active_config):
    print("==== SNMP Menu ====")
    displaySnmp(active_config)
    print()
    print("1) Change Adtran Community string")
#    print("2) Change IPv6 Community")
    print("2) Change Vertiv UPS Community string")
    print("0) <- Back")
    print()

def handleSnmp(active_config):
    snmpMenu(active_config)
    try:
        option = int(input("Enter your choice =>\t"))
    except ValueError as err:
        option = 0

    while option != 0:
        if option == 1:
            print()
            temp = input("Enter new Adtran Community string\t["+active_config["adtranCommunity"]+"]:\t")
            if temp != "":
                active_config["adtranCommunity"] = temp
#        elif option == 2:
#            print()
#            temp = input("Enter new IPv6 Community\t["+active_config["v6Community"]+"]:\t")
#            if temp != "":
#                active_config["v6Community"] = temp
        elif option == 2:
            print()
            temp = input("Enter new Vertiv UPS Community string\t["+active_config["upsCommunity"]+"]:\t")
            if temp != "":
                active_config["upsCommunity"] = temp
        else:
            print("====> Invalid option")
    
        print()
        snmpMenu(active_config)
        try:
            option = int(input("Enter your choice =>\t"))
        except ValueError as err:
            option = 0

def sendv4Trap(packetDesc,packet):
    print("Sending "+packetDesc+" -->")
    try:
        send(packet[0])
    except Exception as err:
        print(err)
    #if send(packet[0]) != 0:
    #    print("**** Error sending "+packetDesc+"!")
    #else:
    #    print("Sent "+packetDesc)

def adtranMenu(active_config):
    print("==== Adtran Menu ====")
    print("IAD's IPv4 Source:\t"+active_config["ipv4Src"])
    print("Netcool IPv4 Dest:\t"+active_config["ipv4Dst"])
    print("Adtran Community string:\t"+active_config["adtranCommunity"])
    print()
    print("1) Send Battery Disco")
    print("2) Send Battery Connected")
    print("3) Send Low Battery")
    print("4) Send Battery Aging")
    print("5) Send Track Fail")
    print("6) Send Track Pass")
    #print("7) Send Power on AC")
    #print("8) Send Power on Battery")    
    print("0) <- Back")
    print()

def handleAdtran(active_config):
    adtranMenu(active_config)
    try:
        option = int(input("Enter your choice =>\t"))
    except ValueError as err:
        option = 0

    while option != 0:
        ts = round(time.time() % 86400)
        src_port = random.randint(20000,30000)
        packetDesc = ""
        packet = []
        v4Src = active_config["ipv4Src"]
        v4Dst = active_config["ipv4Dst"]
        adtranCommunity = active_config["adtranCommunity"]        
        if option == 1:
            print()
            packetDesc = "battery disco trap"
            packet.append(IP(proto=17,src=v4Src,dst=v4Dst)/
            UDP(sport=src_port,dport=162)/SNMP(version=ASN1_INTEGER(1),community=ASN1_STRING(bytes(adtranCommunity,'utf8')),
            PDU=SNMPtrapv2(id=ASN1_INTEGER(16),error=ASN1_INTEGER(0),error_index=ASN1_INTEGER(0),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.6.3.1.1.4.1.0"),value=ASN1_OID(".1.3.6.1.2.1.233.0.7")),
            ])))
            sendv4Trap(packetDesc,packet)              
        elif option == 2:
            print()
            packetDesc = "battery connected trap"
            packet.append(IP(proto=17,src=v4Src,dst=v4Dst)/
            UDP(sport=src_port,dport=162)/SNMP(version=ASN1_INTEGER(1),community=ASN1_STRING(bytes(adtranCommunity,'utf8')),
            PDU=SNMPtrapv2(id=ASN1_INTEGER(16),error=ASN1_INTEGER(0),error_index=ASN1_INTEGER(0),
            varbindlist=[ \
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.6.3.1.1.4.1.0"),value=ASN1_OID(".1.3.6.1.2.1.233.0.6")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.1.1"),value=ASN1_STRING(""))
            ])))
            sendv4Trap(packetDesc,packet)                        
        elif option == 3:
            print()
            packetDesc = "low battery trap"
            packet.append(IP(proto=17,src=v4Src,dst=v4Dst)/
            UDP(sport=src_port,dport=162)/SNMP(version=ASN1_INTEGER(1),community=ASN1_STRING(bytes(adtranCommunity,'utf8')),
            PDU=SNMPtrapv2(id=ASN1_INTEGER(16),error=ASN1_INTEGER(0),error_index=ASN1_INTEGER(0),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.6.3.1.1.4.1.0"),value=ASN1_OID(".1.3.6.1.2.1.233.0.2")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.15.1"),value=ASN1_GAUGE32(4294967295)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.16.1"),value=ASN1_GAUGE32(4294967295)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.25.1"),value=ASN1_STRING(""))
            ])))
            sendv4Trap(packetDesc,packet)
        elif option == 4:
            print()
            packetDesc = "battery aging trap"
            packet.append(IP(proto=17,src=v4Src,dst=v4Dst)/
            UDP(sport=src_port,dport=162)/SNMP(version=ASN1_INTEGER(1),community=ASN1_STRING(bytes(adtranCommunity,'utf8')),
            PDU=SNMPtrapv2(id=ASN1_INTEGER(16),error=ASN1_INTEGER(0),error_index=ASN1_INTEGER(0),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.6.3.1.1.4.1.0"),value=ASN1_OID(".1.3.6.1.2.1.233.0.5")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.10.1"),value=ASN1_GAUGE32(4294967295)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.11.1"),value=ASN1_GAUGE32(4294967295)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.233.1.1.1.25.1"),value=ASN1_STRING(""))
            ])))
            sendv4Trap(packetDesc,packet)
        elif option == 5:
            print()
            packetDesc = "Track Fail trap"
            packet.append(IP(proto=17,src=v4Src,dst=v4Dst)/
            UDP(sport=src_port,dport=162)/SNMP(version=ASN1_INTEGER(1),community=ASN1_STRING(bytes(adtranCommunity,'utf8')),
            PDU=SNMPtrapv2(id=ASN1_INTEGER(16),error=ASN1_INTEGER(0),error_index=ASN1_INTEGER(0),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.6.3.1.1.4.1.0"),value=ASN1_OID(".1.3.6.1.4.1.664.5.53.2.2.0.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.664.5.53.2.2.14.1.1.2"),value=ASN1_INTEGER(2)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.664.5.53.2.2.14.1.2.2"),value=ASN1_STRING("nfpaline1"))
            ])))
            sendv4Trap(packetDesc,packet)
        elif option == 6:
            print()
            packetDesc = "Track Pass trap"
            packet.append(IP(proto=17,src=v4Src,dst=v4Dst)/
            UDP(sport=src_port,dport=162)/SNMP(version=ASN1_INTEGER(1),community=ASN1_STRING(bytes(adtranCommunity,'utf8')),
            PDU=SNMPtrapv2(id=ASN1_INTEGER(16),error=ASN1_INTEGER(0),error_index=ASN1_INTEGER(0),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.6.3.1.1.4.1.0"),value=ASN1_OID(".1.3.6.1.4.1.664.5.53.2.2.0.2")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.664.5.53.2.2.14.1.1.2"),value=ASN1_INTEGER(2)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.664.5.53.2.2.14.1.2.2"),value=ASN1_STRING("nfpaline1"))
            ])))
            sendv4Trap(packetDesc,packet)
        else:
            print("====> Invalid option")
    
        print()
        adtranMenu(active_config)
        try:
            option = int(input("Enter your choice =>\t"))
        except ValueError as err:
            option = 0

def sendv6Trap(packetDesc,packet,active_config):
    print("Sending "+packetDesc+" --> "+active_config["v6iface"])
    try:
        sendp(packet[0],iface=active_config["v6iface"])
    except Exception as err:
        print(err)

def vertivMenu(active_config):
    print("==== Vertiv Menu ========================================================================================")
#    print("IPv6 Src MAC:\t"+active_config["ipv6EthSrcMac"])
#    print("IPv6 Dest MAC:\t"+active_config["ipv6EthDstMac"])
#    print("IPv6 Source:\t"+active_config["ipv6Src"])
#    print("IPv6 Dest:\t"+active_config["ipv6Dst"])
#    print("IPv6 Community:\t"+active_config["v6Community"])
    print("IAD's IPv4 Source:\t"+active_config["ipv4Src"])
    print("Netcool IPv4 Dest:\t"+active_config["ipv4Dst"])
    print("Vertiv UPS Community string:\t"+active_config["upsCommunity"])    
    print("===================================== High Level traps =================================================")
    # abcdhimnloprstz
    print("c) Send (c)oldstart")
    print("h) Send (h)eartbeat                n) Send Sys(n)ormal                l) Send (l)ow Battery Warning")
    print("s) Send communication(s) lost      d) Send (d)ns lookup failure       i) Send (i)nternal fault")
    print("t) Send battery (t)est failed      o) Send output (o)verload          p) Send (p)ower module failure")
    print("b) Send (b)attery module failure   m) Send control (m)odule failure   ")
    print("r) Send module (r)emoved           a) Send module (a)dded             ")
    print("============================ lgpEventConditionEntryAdded subalarm traps=================================")
    print("aa) OutputToLoadOverload      bb) SystemOverTemperature   cc) UtilityFailure    dd) LoadOnBattery")
    print("ee) ReplaceBattery            ff) UpsShutdownPending      gg) OutputToLoadOff   hh) BatteryTestFailed")
    print("ii) InverterFailure           jj) RectifierFailure        kk) SystemFanFailure  ll) SystemOutputFault")
    print("mm) UnspecifiedGeneralEvent   nn) ChargerFailure          oo) InputWiringFault  pp) DCtoDCConverterFault")
    print("qq) ExtBatteryCabinetRemoved")
    print()
    print("z) <- Back") 

def handleVertiv(active_config):
    vertivMenu(active_config)
    try:
        option = input("Enter your choice => ").upper()
    except ValueError as err:
        option = ""
    conditions = 0
    #newpcap.append(Ether(src=pcap[i][Ether].src,dst=pcap[i][Ether].dst,type=0x86dd)/IPv6(nh=pcap[i][IP].proto,src=v6src,dst=v6dst)/pcap[i][IP].payload)
    while option != "Z":
        print("option is "+option)
        ts = round(time.time() % 86400)
        src_port = random.randint(20000,30000)
        packetDesc = ""
        packet = []
#        ethv6Src = active_config["ipv6EthSrcMac"]
#        ethv6Dst = active_config["ipv6EthDstMac"]
#        v6Src = active_config["ipv6Src"]
#        v4Src = active_config["ipv4Src"]
#        v6Dst = active_config["ipv6Dst"]
#        v6Community = active_config["v6Community"]
        v4Src = active_config["ipv4Src"]
        v4Dst = active_config["ipv4Dst"]
        upsCommunity = active_config["upsCommunity"]
        upsMac =  active_config["upsMac"]         
        #e = Ether(src=ethv6Src,dst=ethv6Dst,type=0x86dd) - row 1
#        e = Ether(type=0x86dd)
#        i = IPv6(nh=17,src=v6Src,dst=v6Dst)
        i = IP(proto=17,src=v4Src,dst=v4Dst)
        u = UDP(sport=src_port,dport=162)
        if option == "C":
            
            packetDesc = "coldStart trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(0),
            specific_trap=ASN1_INTEGER(0),time_stamp=ASN1_TIME_TICKS(ts))))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "H":
            # Vertiv-SNMP_traps_lgpNotifications-sub-alarms-20220429 - row 11
            print()
            packetDesc = "heartbeat trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.2.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(7),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.2"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.2.1.6"),value=ASN1_INTEGER(1)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "N":
            #frames 42 & 43 - Vertiv_GXT5_20min-Utility_Power_Fail_Discharge_Charge-20220427.pcapng
            #specific trap = 2 is CLEAR
            print()
            conditions = 0
            packetDesc = "SysNormal traps"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.7.8"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(2),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.2.1.6"),value=ASN1_INTEGER(1)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
            packet = []
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.7.8"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.7.7"),value=ASN1_STRING("Message: System Return to Normal")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "L":
            # Vertiv-SNMP_traps_lgpNotifications-sub-alarms-20220429 - row 38
            print()
            conditions = conditions + 1
            packetDesc = "low Battery Warning trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.117")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "S":
            # lgpAgentDeviceCommunicationLost - .1.3.6.1.4.1.476.1.42.2.3.0.1 (LIEBERT-GP-AGENT-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "communications lost trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.2.3.0.1"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "D":
            # lgpAgentDnsLookupFailure - .1.3.6.1.4.1.476.1.42.2.3.0.8 (LIEBERT-GP-AGENT-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "dns lookup failure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.2.3.0.8"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3.0"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.6"),value=ASN1_STRING("some.fqdn.com")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "I":
            # lgpEventInternalFault - .1.3.6.1.4.1.476.1.42.3.3.0.5 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "internal fault trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.5"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "T":
            # lgpEventBatteryTestFailed - .1.3.6.1.4.1.476.1.42.3.3.0.6 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "battery test failed trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.6"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "O":
            # lgpEventOutputOverload - .1.3.6.1.4.1.476.1.42.3.3.0.7 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "output overload trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.7"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "P":
            # lgpEventPowerModuleFailure - .1.3.6.1.4.1.476.1.42.3.3.0.10 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "power module failure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.10"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "B":
            # lgpEventBatteryModuleFailure - .1.3.6.1.4.1.476.1.42.3.3.0.11 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "battery module failure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.11"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "M":
            # lgpEventControlModuleFailure - .1.3.6.1.4.1.476.1.42.3.3.0.12 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "control module failure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.12"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "R":
            # lgpEventModuleRemoved - .1.3.6.1.4.1.476.1.42.3.3.0.20 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "module removed trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.20"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.10.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.8.40.20")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.10.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.8.40.20.1.5")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "A":
            # lgpEventModuleAdded - .1.3.6.1.4.1.476.1.42.3.3.0.19 (LIEBERT-GP-NOTIFICATIONS-MIB)
            print()
            conditions = conditions - 1
            packetDesc = "module added trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.0.19"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.10.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.8.40.19")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3.10.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.8.40.19.1.5")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "AA":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionOutputToLoadOverload - .1.3.6.1.4.1.476.1.42.3.2.1.40.6 (LIEBERT-GP-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "OutputToLoadOverload trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.40.6")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "BB":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionSystemOverTemperature - .1.3.6.1.4.1.476.1.42.3.2.1.59.3 (LIEBERT-GP-CONDITIONS-MIB)            
            print()
            conditions = conditions + 1
            packetDesc = "SystemOverTemperature trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.59.3")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "CC":
            #frames 8 & 40 - Vertiv_GXT5_20min-Utility_Power_Fail_Discharge_Charge-20220427.pcapng
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionUtilityFailure - .1.3.6.1.4.1.476.1.42.3.2.1.70 (LIEBERT-GP-CONDITIONS-MIB)             
            print()
            conditions = conditions + 1
            packetDesc = "UtilityFailure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.70")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "DD":
            #frames 12 & 36 - Vertiv_GXT5_20min-Utility_Power_Fail_Discharge_Charge-20220427.pcapng
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionLoadOnBattery - .1.3.6.1.4.1.476.1.42.3.2.1.72 (LIEBERT-GP-CONDITIONS-MIB)                 
            print()
            conditions = conditions + 1
            packetDesc = "LoadOnBattery trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.72")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "EE":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionReplaceBattery - .1.3.6.1.4.1.476.1.42.3.2.1.74 (LIEBERT-GP-CONDITIONS-MIB)              
            print()
            conditions = conditions + 1
            packetDesc = "ReplaceBattery trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.74")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "FF":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionUpsShutdownPending - .1.3.6.1.4.1.476.1.42.3.2.1.75 (LIEBERT-GP-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "UpsShutdownPending trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.75")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "GG":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionOutputToLoadOff - .1.3.6.1.4.1.476.1.42.3.2.1.102 (LIEBERT-GP-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "OutputToLoadOff trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.102")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "HH":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpConditionBatteryTestFailed - .1.3.6.1.4.1.476.1.42.3.2.1.119 (LIEBERT-GP-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "BatteryTestFailed trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.1.119")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "II":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId4233InverterFailure - .1.3.6.1.4.1.476.1.42.3.2.7.1.4233 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "InverterFailure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.4233")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.4233")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "JJ":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId4295RectifierFailure - .1.3.6.1.4.1.476.1.42.3.2.7.1.4295 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "RectifierFailure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.4295")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.4295")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "KK":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId4311SystemFanFailure - .1.3.6.1.4.1.476.1.42.3.2.7.1.4311 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "SystemFanFailure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.4311")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.4311")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "LL":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId4389SystemOutputFault - .1.3.6.1.4.1.476.1.42.3.2.7.1.4389 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "SystemOutputFault trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.4389")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.4389")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "MM":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId5588UnspecifiedGeneralEvent - .1.3.6.1.4.1.476.1.42.3.2.7.1.5588 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "UnspecifiedGeneralEvent trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.5588")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.5588")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "NN":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId6254ChargerFailure - .1.3.6.1.4.1.476.1.42.3.2.7.1.6254 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "ChargerFailure trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.6254")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.6254")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "OO":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId6453InputWiringFault - .1.3.6.1.4.1.476.1.42.3.2.7.1.6453 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "InputWiringFault trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.6453")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.6453")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "PP":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId6454DCtoDCConverterFault - .1.3.6.1.4.1.476.1.42.3.2.7.1.6454 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "DCtoDCConverterFault trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.6454")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.6454")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        elif option == "QQ":
            # lgpEventConditionEntryAdded - .1.3.6.1.4.1.476.1.42.3.3.0.1 (LIEBERT-GP-NOTIFICATIONS-MIB)
            # lgpCondId8120ExternalBatteryCabinetRemoved - .1.3.6.1.4.1.476.1.42.3.2.7.1.8120 (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB)
            print()
            conditions = conditions + 1
            packetDesc = "ExtBatteryCabinetRemoved trap"
            packet.append(i/u/SNMP(version=ASN1_INTEGER(0),community=ASN1_STRING(bytes(upsCommunity,'utf8')),
            PDU=SNMPtrapv1(enterprise=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.3"),agent_addr=ASN1_IPADDRESS("192.168.1.2"),generic_trap=ASN1_INTEGER(6),
            specific_trap=ASN1_INTEGER(1),time_stamp=ASN1_TIME_TICKS(ts),
            varbindlist=[
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.1"),value=ASN1_INTEGER(conditions)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.2"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.7.1.8120")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.3"),value=ASN1_TIME_TICKS(ts)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.5"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.2.3.1.6"),value=ASN1_OID(".1.3.6.1.4.1.476.1.42.3.9.20.1.10.1.2.100.8120")),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.5.0"),value=ASN1_STRING(upsMac)),
                SNMPvarbind(oid=ASN1_OID(".1.3.6.1.2.1.1.6.0"),value=ASN1_STRING("Uninitialized"))
            ])))
            #ls(packet[0].PDU)
            sendv4Trap(packetDesc,packet)
        else:
            print("====> Invalid option")

        print()
        vertivMenu(active_config)
        try:
            option = input("Enter your choice => ").upper()
            if option == "":
                option = "Z"
        except ValueError as err:
            print(err)
            option = "Z"  

def saveConfig(config_file, active_config):
    print("Saving config file => " + config_file)
    print()
    with open(config_file, "w") as f:
        f.write(json.dumps(active_config,indent=4))
        f.close()
    print("Config file saved!")

def mainMenu(active_config):
    print("==== Main Menu v0.40 ====")
    displayAddresses(active_config)
    displaySnmp(active_config)
    print("1) Change Addresses")
    print("2) Change SNMP")
    print("3) Adtran Menu")
    print("4) Vertiv Menu")
    print("9) Save Config")
    print("0) <- Exit")
    print()

#========= MAIN

def main():

    #config_file = os.getcwd()+"\\VoPON\\vopon_sim\\vopon_sim.json"
    config_file = os.getcwd()+"\\vopon_sim.json"
    active_config = {}

    active_config = loadConfig(config_file)
    #print("config -> "+json.dumps(active_config))

    mainMenu(active_config)
    try:
        option = int(input("Enter your choice =>\t"))
    except ValueError as err:
        option = 0

    while option != 0:
        if option == 1:
            print()
            handleAddresses(active_config)
        elif option == 2:
            print()
            handleSnmp(active_config)
        elif option == 3:
            print()
            handleAdtran(active_config)
        elif option == 4:
            print()
            handleVertiv(active_config)
        elif option == 9:
            saveConfig(config_file, active_config)
        else:
            print("====> Invalid option")
        
        print()
        mainMenu(active_config)
        try:
            option = int(input("Enter your choice =>\t"))
        except ValueError as err:
            option = 0            
    print("Exiting...")

if __name__ == '__main__':
    main()