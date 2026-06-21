student=[]
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("4. Delete Student Selected")

    choice = input("Enter your choice: ")

    if choice == "1":
        stud=input("Enter student name: ")
        student.append(stud)
    
    elif choice == "2":
        for i in range(1,len(student)+1):
            print(i,". ",student[i-1])
    
    elif choice == "3":
        print("Exiting program...")
        break
    elif choice == "4":
        stud=input("Enter student name to remove: ")
        student.remove(stud)
    
    else:
        print("Invalid choice, try again")
