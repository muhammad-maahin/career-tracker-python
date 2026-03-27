from tracker import add_goal, view_goals, mark_complete, delete_goal, edit_goal

def main():
    while True:
        print("\n=== Career Tracker ===")
        print("1. Add Goal")
        print("2. View Goals")
        print("3. Mark Goal Complete")
        print("4. Delete Goal")
        print("5. Edit Goal")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_goal()
        elif choice == "2":
            view_goals()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_goal()
        elif choice == "5":
            edit_goal()
        elif choice == "6":
            print("Exiting... Stay consistent!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
