from user import register_user, does_user_exist
from session import start_session, show_session_stats  # <--- ADD THIS

def main():
    print("=== DLICP Calorie Burn Tracker ===")
    while True:
        print("\n1. Register New User")
        print("2. Start New Session (by name)")
        print("3. Show Session Stats")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = register_user()
            if name:
                print(f"Use your name '{name}' to log future sessions.")
        elif choice == '2':
            name = input("Enter your name: ").strip()
            if does_user_exist(name):
                start_session(name)
            else:
                print("No such user found.")
        elif choice == '3':
            name = input("Enter your name to view stats: ").strip()
            if does_user_exist(name):
                show_session_stats(name)
            else:
                print("No such user found.")
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

