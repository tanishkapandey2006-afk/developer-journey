while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("4. Delete Student Selected")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Student selected")
    
    elif choice == "2":
        print("View Students selected")
    
    elif choice == "3":
        print("Exiting program...")
        break
    elif choice == "4":
    print("Delete Student selected")
    
    else:
        print("Invalid choice, try again")
