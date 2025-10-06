from netmiko import ConnectHandler
import json

device = {
	"device_type": "cisco_s300",
	"host": "192.168.10.21",
	"username": "clabman",
	"password": "password123",
}



conn = ConnectHandler(**device)

results = {}


for i in range (1, 25):
	interface=f"GE1/0/{i}"
	filename=f"/home/clabman/velo_switch/switchport21_{i}.txt"

	print(f"Collecting {interface} -> {filename}")

	output = conn.send_command(
		f"show interfaces switchport {interface}",
		expect_string=r"Proxmox-Switch-01>")

#	results[interface] = output

# conn.disconnect()

# with open("/home/clabman/smb_switch/switchport25.json", "w") as f:
#	json.dump(results, f, indent=4)


	with open(filename, "w") as f:
		f.write(output)

output = conn.send_command(
	f"show interfaces configuration",
	expect_string=r"Proxmox-Switch-01>")

with open("/home/clabman/velo_switch/port_config21.txt", "w") as f:
	f.write(output)

conn.disconnect()
# conn = ConnectHandler(**device)
# output = conn.send_command("show interfaces switchport GE1", expect_string=r"proxmox-switch-04>")
# conn.disconnect()

# with open("/home/clabman/smb_switch/switchport25_1.txt", "w") as f:
#	f.write(output)

print("complete")

