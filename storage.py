# storage.py
import csv
import os

CSV_FILE = 'sessions.csv'

def save_session_to_csv(session_data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=session_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(session_data)

