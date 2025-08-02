# Parses a log file and flags failed login attempts
with open("login_logs.txt", "r") as file:
    for line in file:
        if "FAILED" in line.upper():
            print(f"Failed login detected: {line.strip()}")