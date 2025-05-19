# user.py
import uuid
import csv
import os

USER_FILE = 'users.csv'

def register_user():
    name = input("Enter your username: ").strip()

    # Check if name already exists
    if does_user_exist(name):
        print("Username already exists. Please choose a unique name.")
        return None

    age = input("Enter your age: ")
    weight = input("Enter your weight (kg): ")

    try:
        age = int(age)
        weight = float(weight)
    except ValueError:
        print("Invalid age or weight.")
        return None

    user_id = str(uuid.uuid4())
    user_record = {
        'user_id': user_id,
        'name': name,
        'age': age,
        'weight_kg': weight
    }

    file_exists = os.path.isfile(USER_FILE)
    with open(USER_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=user_record.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(user_record)

    print(f"\n New user '{name}' registered with User ID: {user_id}")
    return name

def does_user_exist(name):
    if not os.path.isfile(USER_FILE):
        return False
    with open(USER_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['name'].lower() == name.lower():
                return True
    return False

def get_user_by_name(name):
    if not os.path.isfile(USER_FILE):
        return None
    with open(USER_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['name'].lower() == name.lower():
                return row
    return None

