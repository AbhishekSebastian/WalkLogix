import uuid
import csv
import os
from calculator import calculate_calories
from storage import save_session_to_csv
from user import get_user_by_name

SESSION_FILE = 'sessions.csv'

# ==========================
# Start a New Workout Session
# ==========================

def start_session(name):
    user = get_user_by_name(name)
    if user is None:
        print("No such user found.")
        return

    user_id = user['user_id']
    weight = float(user['weight_kg'])
    session_id = str(uuid.uuid4())

    print(f"\nStarting new session for {name} (Session ID: {session_id})")

    try:
        laps = int(input("Enter number of laps completed: "))
        perimeter = float(input("Enter park perimeter (in km): "))
        time_min = float(input("Enter time elapsed (in minutes): "))

        result = calculate_calories(weight, laps, perimeter, time_min)

        session_record = {
            'user_id': user_id,
            'name': name,
            'session_id': session_id,
            'weight_kg': weight,
            'laps': laps,
            'park_perimeter_km': perimeter,
            'time_min': time_min,
            'distance_km': result['distance_km'],
            'pace_kmph': result['pace_kmph'],
            'calories_burned': result['calories_burned']
        }

        save_session_to_csv(session_record)
        display_summary(result, session_id)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def display_summary(result, session_id):
    print("\nSession Summary:")
    print(f"Distance Covered: {result['distance_km']} km")
    print(f"Average Pace: {result['pace_kmph']} km/h")
    print(f"Estimated Calories Burned: {result['calories_burned']} kcal")
    print(f"Session ID: {session_id}")

# ==========================
# Show Existing Session Stats
# ==========================

def show_session_stats(name):
    if not os.path.isfile(SESSION_FILE):
        print("No session data found.")
        return

    user_sessions = []

    with open(SESSION_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['name'].lower() == name.lower():
                user_sessions.append(row)

    if not user_sessions:
        print(f"No sessions found for user '{name}'.")
        return

    print("\nChoose Stats View Option:")
    print("1. View Latest Session")
    print("2. Search by Session ID")
    choice = input("Your choice: ").strip()

    if choice == '1':
        latest = user_sessions[-1]
        display_session(latest)

    elif choice == '2':
        session_id = input("Enter Session ID: ").strip()
        found = next((s for s in user_sessions if s['session_id'] == session_id), None)
        if found:
            display_session(found)
        else:
            print("No matching session ID found.")

    else:
        print("Invalid choice.")

def display_session(session):
    print("\nSession Stats")
    print(f"Session ID       : {session['session_id']}")
    print(f"User             : {session['name']} (Weight: {session['weight_kg']} kg)")
    print(f"Laps             : {session['laps']}")
    print(f"Park Perimeter   : {session['park_perimeter_km']} km")
    print(f"Time Elapsed     : {session['time_min']} minutes")
    print(f"Distance         : {session['distance_km']} km")
    print(f"Pace             : {session['pace_kmph']} km/h")
    print(f"Calories Burned  : {session['calories_burned']} kcal")

