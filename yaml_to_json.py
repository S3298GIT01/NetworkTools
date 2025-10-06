import json
import os
import re

base_path = "/home/clabman/smb_switch"
output_json = "/home/clabman/smb_switch/switch_data.json"

data = {}

for filename in os.listdir(base_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(base_path, filename)
        interface_name = filename.replace(".txt", "")

        with open(filepath) as f:
            text = f.read()

        # Parse simple key-value pairs (like "Switchport: enable")
        info = {}
        for line in text.splitlines():
            match = re.match(r"^(.*?):\s*(.*)$", line.strip())
            if match:
                key = match.group(1).strip().lower().replace(" ", "_")
                value = match.group(2).strip()
                info[key] = value

        data[interface_name] = info

# Save everything into JSON
with open(output_json, "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ Saved parsed data to {output_json}")
