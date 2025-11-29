# Challenge 1: The "Log Parser" (Strings & Lists)
# Scenario: You are analyzing server logs. A log line looks like this: "INFO:User123:LoginSuccess"
logs = [
    "ERROR:DB_Connection:Fail",
    "INFO:User_Swaraj:LoginSuccess",
    "WARNING:Disk_Space:Low"
]
log_parser = [log.split(':') for log in logs ]
for item in log_parser:
    level=item[0]
    source=item[1]
    message=item[2]
    print(f"[{level}] reported by [{source}:{message}]")