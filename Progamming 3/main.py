from student import Student
from Student_repository import save_students, load_students, find_student_by_id

#driver

while True:
    print("\nStudent Registry")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Choice an option: ").strip()

    match choice:
        case "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            course = input("Enter Student Course: ").strip()

            if not student_id or not name or not course:
                print("A Student with that ID already exists.")
                continue
            existing_student = find_student_by_id(student_id)
            if existing_student is not None:
                print("A Student with that ID already exists.")
                continue

            student = Student(student_id, name, course)
            save_students(student)
            print("Student Saved.")
        case "2":
            students = load_students()
            
            if not students:
                print("No students saved yet.")
            else:
                print("\nSaved Students:")
                for student in students:
                    print(student)
        case "3":
            student_id = input("Enter Student ID to search: ").strip()

            if not student_id:
                print("Student ID cannot be empty.")

            else:
                student = find_student_by_id(student_id)
                if student is None:
                    print("Student not found.")
                else:
                    print("Student Found:")
                    print(student)

        case "4":
            print("Goodbye!")
            break
        
        case _:
            print("Invalid option. please choose 1, 2, 3, or 4.")