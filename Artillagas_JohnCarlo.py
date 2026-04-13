while True:
    print("\n=== Student Record Menu ===")
    print("1 - Add Student Record")
    print("2 - View Saved Records")
    print("3 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")

        with open("students.txt", "a") as file:
            file.write(f"{name},{grade}\n")

        print("Record saved successfully.")

    elif choice == "2":
        print("\n=== Saved Records ===")
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    name, grade = line.strip().split(",")
                    print(f"Name: {name} | Grade: {grade}")
        except FileNotFoundError:
            print("No records found yet.")

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")