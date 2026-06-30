from menu import (
    main_menu,
    student_menu,
    course_menu,
    enrollment_menu,
    grade_menu,
    reports_menu,
)

from modules.student import Student

while True:
    print(main_menu())
    choice = int(input("Enter 1-6:"))

    if choice == 1:
        while True:
            student_menu()
            st_choice = int(input("Enter 1-5:"))

            if st_choice == 1:
                name = input("Enter name:")
                id = int(input("Enter student id:"))
                email_address = input("Enter email address:")
                age = int(input("Enter student age:"))
                department = input("Enter student department:")

                Student.add_student(id, name, age, email_address, department)

            elif st_choice == 2:
                Student.get_all_students()

            elif st_choice == 3:
                id = int(input("Enter student ID:"))
                print(Student.search_student_by_ID(id))

            elif st_choice == 4:
                id = int(input("Enter student ID:"))

            elif st_choice == 5:
                id = int(input("Enter student ID to delete:"))
                Student.delete_student(id)
            else:
                break

    elif choice == 2:
        while True:
            course_menu()
            cr_choice = int(input("Enter 1-4:"))

            if cr_choice == 1:
                pass
            elif cr_choice == 2:
                pass
            elif cr_choice == 3:
                pass
            else:
                break

    elif choice == 3:
        while True:
            enrollment_menu()
            gr_choice = int(input("Enter 1-4:"))

            if gr_choice == 1:
                pass
            elif gr_choice == 2:
                pass
            elif gr_choice == 3:
                pass
            else:
                break

    elif choice == 4:
        while True:
            grade_menu()
            re_choice = int(input("Enter 1-4:"))

            if re_choice == 1:
                pass
            elif re_choice == 2:
                pass
            elif re_choice == 3:
                pass
            else:
                break

    elif choice == 5:
        while True:
            reports_menu()
            re_choice = int(input("Enter 1-4:"))

            if re_choice == 1:
                pass
            elif re_choice == 2:
                pass
            elif re_choice == 3:
                pass
            else:
                break
    else:
        break
