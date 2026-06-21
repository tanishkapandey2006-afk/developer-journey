students = []
def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student Selected")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        student = {"name": name,"marks": marks}
        students.append(student)
    
    elif choice == "2":
        for i, student in enumerate(students, start=1):
            print(i, student["name"], "-", student["marks"])

    elif choice== "3":
        search_name = input("Enter student name to search: ")
        for student in students:
            if student["name"] == search_name:
                print("Student found.")
                print("Student Name: ",search_name,"\nStudent Marks: ",student["marks"])
                break
        else:
            print("Student not found.")
    
    elif choice == "4":
        stud=input("Enter student name to remove: ")
        for student in students:
            if student["name"] == stud:
                students.remove(student)
                print("Student removed.")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        return False
    
    else:
        print("Invalid choice, try again")
    return True
while True:
    if not display_menu():
        break
    
