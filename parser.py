import re

LOG_FILE = "/var/log/auth.log"  # Change this to your log file path

def parse_logs():
    suspicious_entries = []

    # Regex patterns for failed SSH logins and brute-force attempts
    ssh_fail_pattern = r"Failed password for (invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+) port"

    with open(LOG_FILE, "r") as log:
        for line in log:
            match = re.search(ssh_fail_pattern, line)
            if match:
                username = match.group(2)
                ip_address = match.group(3)
                suspicious_entries.append((username, ip_address, line.strip()))

    return suspicious_entries

if __name__ == "__main__":
    logs = parse_logs()
    for entry in logs:
        print(f"🚨 Suspicious Login Attempt - User: {entry[0]}, IP: {entry[1]}")
