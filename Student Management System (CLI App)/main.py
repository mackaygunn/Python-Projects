from student import *
import storage

def main():
    print("===== Student Management System =====")

    students = storage.load_students()

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            option = int(input("Enter your option (1-6): "))
        except ValueError:
            print(">>> Invalid input! Please enter a number.")
            continue


        if option == 1:
            add_student(students)
        elif option == 2:
            view_students(students)
        elif option == 3:
            search_student(students)
        elif option == 4:
            update_student(students)
        elif option == 5:
            delete_student(students)
        elif option == 6:
            print("Thank you!")
            break
        else:
            print(">>> Invalid option! Please enter 1-6.")

if __name__ == "__main__":
    main()