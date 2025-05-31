import os
import shutil
from datetime import datetime
from collections import Counter

def isolate_suspicious_files():
    suspicious_path = input("Enter the full path to the suspicious directory (e.g., /network/shared_docs): ").strip()

    if not os.path.isdir(suspicious_path):
        print("The provided path is not valid.")
        return

    file_activity_counter = Counter()

    for file in os.listdir(suspicious_path):
        full_path = os.path.join(suspicious_path, file)

        # Skip if it's a directory
        if not os.path.isfile(full_path):
            continue

        # Get last modified timestamp
        mod_time = os.path.getmtime(full_path)
        mod_date = datetime.fromtimestamp(mod_time)
        month_year = mod_date.strftime("%B-%Y")  # Example: April-2025

        # Update counter for reporting
        file_activity_counter[month_year] += 1

        # Create Month-Year directory if it doesn't exist
        target_folder = os.path.join(suspicious_path, month_year)
        os.makedirs(target_folder, exist_ok=True)

        # Move file into Month-Year folder
        target_path = os.path.join(target_folder, file)
        shutil.move(full_path, target_path)

    print("\nFile activity summary by Month-Year:")
    for month_year, count in sorted(file_activity_counter.items()):
        print(f"  {month_year}: {count} file(s)")

    print("\nFiles have been grouped accordingly. Investigate any unexpected spikes or unusual timing.")

if __name__ == "__main__":
    isolate_suspicious_files()
