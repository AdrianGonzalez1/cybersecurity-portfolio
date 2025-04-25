# 🔐 Failed SSH Login Log Parser (Python)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)

This Python script parses a system log file (such as `auth.log`) to identify failed SSH login attempts. It extracts the source IP addresses for each failed login, counts how many times each IP appears, and prints a summary showing the most frequent offenders.

This is a lightweight tool to help demonstrate basic log analysis techniques, useful for SOC analysts, security engineers, or anyone studying real-world incident response.

---

## 🚀 Features

- Scans log files for `"Failed password"` events
- Extracts IP addresses from each matching log line
- Counts total failed login attempts
- Tracks how many times each IP address attempted to log in
- Outputs a clean summary of results

---

## 📂 File Structure

<pre> ``` log-parser/ ├── log_parser.py # Main Python script └── mock_auth.log # Sample log file (optional) ``` </pre>

---

## 🛠 How to Run

1. Clone this repository or copy the `log_parser.py` script into your project
2. Make sure your target log file is named `mock_auth.log` or update the filename in the script
3. Run the script using Python 3:

```bash

python log_parser.py

## 🧪 Sample Output

[INFO] Failed login attempts by IP:
10.0.0.5: 3 attempts
172.16.0.3: 5 attempts
203.0.113.12: 4 attempts
192.168.1.10: 4 attempts

## 🧠 Why I Built This

This project is part of my cybersecurity portfolio to demonstrate practical scripting and log analysis skills.

I wanted to create a simple, real-world tool that mimics what a SOC analyst might do during an investigation — parse through log files, identify failed login patterns, and track attacker behavior by IP address. It’s one of those tasks that sounds simple but is incredibly valuable in real-world detection and response workflows.

It also gave me the chance to strengthen my Python fundamentals, work with dictionaries, string parsing, and build something that has real use in a security environment.
