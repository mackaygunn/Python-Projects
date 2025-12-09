import storage  # new: our simple text file storage

def add_student(students):

    print("\n===== Add student =====")

    add_more_students = True 

    while add_more_students == True:
        student_name = input("Enter student name: ")
        student_ID = input("Enter student ID: ")
        student_age = input("Enter student age: ")
        student_marks = input("Enter students marks: ")

        student_details = dict(name=student_name, ID=student_ID, age=student_age, marks=student_marks)

        students.append(student_details)
        storage.save_students(students)

        print("Student added successfully!")

        add_more = input("Do you wanta to add more students? --> (Y/N) ")

        if add_more.upper() == "N":
            add_more_students = False

    pass

def view_students(students):

    print("\n===== Student List =====")
    for student in students:
        print(f"ID: {student['ID']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")

    pass

def search_student(students):

    print("\n===== search for student =====")

    required_student = input("Enter student ID: ")

    for student in students:
        
        if required_student == student['ID']:
            print(f"ID: {student['ID']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
            return
    
    print("Student not found!")
    pass

def update_student(students):

    print("\n===== Update student information =====")

    update_name = input("Enter student ID: ")

    for student in students:
        if student['ID'] == update_name:
            student['age'] = input("Enter student age: ")
            student['marks'] = input("Enter students marks: ")

            storage.save_students(students)

            print("Student details updated successfully!")
            return

    print("Student not found")
    pass

def delete_student(students):

    print("\n===== Delete student =====")

    delete_name = input("Enter student ID to delete: ")

    for student in students:
        if delete_name == student['ID']:
            students.remove(student)
            storage.save_students(students)
            print(f"Student {student['name']} successfully removed from the database")
            return
    
    print("Student not found")

    pass
