# log_parser.py
# This script parses a log file for failed SSH login attempts and summarizes them by IP address.


def parse_failed_logins(log): # Parses through log to find failed login attempts
    counter = 0 # Tracks total failed logins 
    ip_counter = {} # Tracks total failed logins per IP

    with open(log, 'r') as file: # Opens the file in read mode
        for line in file: # Iterates through each line in the file
            # print(line) 
            if "Failed password" in line: # Checks if the line contains a failed login attempt
                    counter += 1 # Counter increases each time a failed login is found
                    # print("Failed password attempts:", counter, line.strip())
                    parts = line.split()
                    ip = parts[10]
                    if ip in ip_counter:
                        ip_counter[ip] += 1 # Increases the count for that IP
                    else:
                        ip_counter[ip] = 1 # Adds the IP with a count of 1
    print("\n[INFO] Failed login attempts by IP:")
    for ip, count in ip_counter.items(): # Gets the total number of times an failed IP is found
        print(f"{ip}: {count} attempts") 
    print(f"\n[INFO] Total failed logins: {counter}")

parse_failed_logins("logs/mock_auth.log")