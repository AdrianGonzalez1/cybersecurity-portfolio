# Suspicious File Analysis

This project was part of a cybersecurity lab focused on analyzing a suspicious file to figure out if it was safe or harmful. The goal was to practice using tools and techniques to detect malicious files.

## What This Project Is About

- Looked at a file that seemed suspicious
- Checked to see if it was dangerous or not
- Collected any signs that showed what the file was doing
- Wrote down the steps and results

## Tools I Used

- **VirusTotal** – to scan the file and see if antivirus engines detect anything bad  
- **CyberChef** – for decoding or reading parts of the file  
- **Strings command** – to see readable text inside the file  
- **(Optional)** Sandbox tools like Any.run – to safely open the file and see what it does

## What I Did

1. **Scanned the file** using VirusTotal to get a quick look at possible threats
2. **Pulled out readable text** using the `strings` tool to look for clues like URLs or strange commands
3. **Looked at how the file was made**, like file type and format
4. **(If allowed)** Ran it in a safe environment to watch how it behaves

## What I Found

- The file was **malicious**
- It tried to run a hidden script using PowerShell
- It also tried to connect to a remote server, which is a big red flag

## Indicators of Compromise (IOCs)

These are things we found that help identify the file in the future:

| Type        | Value                             |
|-------------|-----------------------------------|
| File Hash   | `examplehash123abc456`            |
| File Name   | `suspicious.doc`                  |
| Domain      | `badsite.example.com`             |
| IP Address  | `192.168.100.50`                  |
| Behavior    | Used PowerShell to download more files |

## Final Notes

This analysis was done in a safe lab setup where nothing could be affected. It was a good learning experience in spotting malware and understanding how it works.

