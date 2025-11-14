print("------- Student Management System -------")

students = []  

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

      
        personal_info = (roll, name, age)

       
        academic_info = {
            "marks": marks,
            "pass": marks >= 35  
        }

        subjects = {"Python", "Maths", "English"}

       
        student_record = {
            "personal": personal_info,
            "academic": academic_info,
            "subjects": subjects
        }

        students.append(student_record)
        print("Student added successfully!")


    elif choice == "2":
        print("\n----- Student List -----")
        if len(students) == 0:
            print("No students found!")
        else:
            for s in students:
                print("\nRoll No:", s["personal"][0])
                print("Name:", s["personal"][1])
                print("Age:", s["personal"][2])
                print("Marks:", s["academic"]["marks"])
                print("Passed:", s["academic"]["pass"])
                print("Subjects:", s["subjects"])

    
    elif choice == "3":
        roll_search = int(input("Enter roll number to search: "))
        found = False
        
        for s in students:
            if s["personal"][0] == roll_search:  
                found = True
                print("\nStudent Found!")
                print("Name:", s["personal"][1])
                print("Age:", s["personal"][2])
                print("Marks:", s["academic"]["marks"])
                print("Subjects:", s["subjects"])
                break

        if not found:
            print("No student found with that roll number.")


    elif choice == "4":
        roll_delete = int(input("Enter roll number to delete: "))
        deleted = False

        for s in students:
            if s["personal"][0] == roll_delete:
                students.remove(s)
                deleted = True
                print("Student removed!")
                break

        if not deleted:
            print("Student not found!")

    elif choice == "5":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
