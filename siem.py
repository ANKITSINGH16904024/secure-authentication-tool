import re
import sys
import json

# Check command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 siem.py <threshold>")
    exit()

# Validate threshold input
try:
    threshold = int(sys.argv[1])
except ValueError:
    print("Threshold must be a number ❌")
    exit()

# Read log file safely
try:
    file = open("auth.log", "r")
    logs = file.readlines()
    file.close()
except FileNotFoundError:
    print("Log file not found ❌")
    exit()

ip_count = {}

# Count failed login attempts
for line in logs:
    if "Failed password" in line:
        match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
        if match:
            ip = match.group()
            ip_count[ip] = ip_count.get(ip, 0) + 1

# Identify suspicious IPs
suspicious = []

for ip, count in ip_count.items():
    if count >= threshold:
        suspicious.append({
            "ip": ip,
            "attempts": count
        })

# Display results
print("\nSuspicious IPs (above threshold):\n")

for item in suspicious:
    print(f"IP: {item['ip']} | Attempts: {item['attempts']}")

# Save to JSON
with open("blocked_ips.json", "w") as f:
    json.dump(suspicious, f, indent=4)

print("\nResults saved to blocked_ips.json ✅")
