from crud.auth import login, logout
from crud.auth import login
from crud.super_admin import show_all_admins, create_admin, delete_admin, show_statistics
from crud.admin import students_crud, groups_crud, assign_student_to_group, search_student, add_balance, teacher_crud, \
    assign_teacher_to_group
from crud.teacher import my_groups, show_group, start_lesson, homework_crud, logout as teacher_logout
from crud.student import show_groups, upload_homework, show_attendance, show_balance, make_payment, \
    logout as student_logout


def auth_menu():
    while True:
        try:
            print("""
                1. Login
                2. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                role = login()
                if role == "super_admin":
                    return "super_admin"
                elif role == "admin":
                    return "admin"
                elif role == "teacher":
                    return "teacher"
                elif role == "student":
                    return "student"
                else:
                    print("Please try again.")
            elif choice == "2":
                print("Good bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def super_admin_menu():
    while True:
        try:
            print("""
                1. Show all admins
                2. Create admin
                3. Delete admin
                4. Show statistics
                5. Logout    
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                show_all_admins()
            elif choice == "2":
                create_admin()
            elif choice == "3":
                delete_admin()
            elif choice == "4":
                show_statistics()
            elif choice == "5":
                print("Good bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def admin_menu():
    while True:
        try:
            print("""
                1. Students CRUD (login, password)
                2. Groups CRUD (start date, total lesson hours)
                3. Student to group
                4. Search student -> full data, balance
                5. Add to balance (payment)
                6. Teacher CRUD
                7. Teacher to group
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                students_crud()
            elif choice == "2":
                groups_crud()
            elif choice == "3":
                assign_student_to_group()
            elif choice == "4":
                search_student()
            elif choice == "5":
                add_balance()
            elif choice == "6":
                teacher_crud()
            elif choice == "7":
                assign_teacher_to_group()
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def teacher_menu():
    while True:
        try:
            print("""
                1. My groups
                2. Show group (by id)
                3. Start the lesson (group id)
                4. Homework CRUD (lesson id)
                5. Logout
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                my_groups()
            elif choice == "2":
                show_group()
            elif choice == "3":
                start_lesson()
            elif choice == "4":
                homework_crud()
            elif choice == "5":
                teacher_logout()
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def student_menu():
    while True:
        try:
            print("""
                1. Show groups
                2. Upload homework (id)
                3. Show my all attendance
                4. Show my balance
                5. Payment
                6. Logout
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                show_groups()
            elif choice == "2":
                upload_homework()
            elif choice == "3":
                show_attendance()
            elif choice == "4":
                show_balance()
            elif choice == "5":
                make_payment()
            elif choice == "6":
                student_logout()
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


if __name__ == "__main__":
    logout()
    auth_menu()
