from menu import (
    main_menu,
    student_menu,
    course_menu,
    enrollment_menu,
    grade_menu,
    reports_menu,
)

from modules.student import Student
from modules.courses import Course
import modules.enrollment as Enrollment
import modules.grades as Grades
import modules.reports.course_reports as CourseReports
import modules.reports.dept_reports as DeptReports
import modules.reports.student_reports as StudentReports
import os

while True:
    os.system('clear')
    main_menu()
    choice = int(input("\033[33mEnter 1-6:\033[0m"))

    if choice == 1:
        while True:
            os.system('clear')
            student_menu()
            st_choice = int(input("\033[33mEnter 1-6:\033[0m"))

            if st_choice == 1:
                try:

                    name = input("\033[36mEnter name:\033[0m")
                    id = int(input("\033[36mEnter student id:\033[0m"))
                    email_address = input("\033[36mEnter email address:\033[0m")
                    age = int(input("\033[36mEnter student age:\033[0m"))
                    department = input("\033[36mEnter student department:\033[0m")

                    Student.add_student(id, name, age, email_address, department)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered, id and age should be numbers\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 2:
                for student in Student.get_all_students():
                    print(f"\033[32mID:\033[0m {student['id']} \033[32mwith Name:\033[0m {student['name']}")
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 3:
                try:

                    id = int(input("\033[36mEnter student ID:\033[0m"))
                    Student.search_student_by_ID(id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31minvalid input entered. id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 4:
                try:
                    id = int(input("\033[36mEnter student ID:\033[0m"))
                    name = input("\033[36mEnter student name:\033[0m")
                    age = int(input("\033[36mEnter age:\033[0m"))
                    email_address = input("\033[36mEnter email:\033[0m")
                    department = input("\033[36mEnter department:\033[0m")

                    Student.update_student(name, id, email_address, age, department)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered. id and age should be numbers\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 5:
                try:
                    id = int(input("\033[36mEnter student ID to delete:\033[0m"))
                    Student.delete_student(id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31minvalid input entered. id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 2:
        while True:
            os.system('clear')
            course_menu()
            cr_choice = int(input("\033[33mEnter 1-4:\033[0m"))

            if cr_choice == 1:
                try:
                    course_name = input("\033[36mEnter course name:\033[0m")
                    course_id = int(input("\033[36mEnter course ID:\033[0m"))
                    cr_hrs = int(input("\033[36mEnter credit hrs:\033[0m"))

                    Course.add_course(course_name, course_id, cr_hrs)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print(
                        "\n\033[31minvalid input entered. course id and credit hrs should be numbers\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif cr_choice == 2:
                for course in Course.view_all_courses():
                    print(
                        "\033[32mName:\033[0m",
                        course["name"],
                        "\033[32mID:\033[0m",
                        course["id"],
                        "\033[32mCredit hrs:\033[0m",
                        course["credit_hrs"],
                    )
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif cr_choice == 3:
                try:

                    course_id = int(input("\033[36mEnter course ID to delete:\033[0m"))
                    Course.delete_course(course_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered. course id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 3:
        while True:
            os.system('clear')
            enrollment_menu()
            en_choice = int(input("\033[33mEnter 1-4:\033[0m"))

            if en_choice == 1:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m"))
                    course_id = int(input("\033[36mEnter course ID:\033[0m"))

                    Enrollment.enroll_student_in_course(student_id, course_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered. course id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif en_choice == 2:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m"))
                    course_id = int(input("\033[36mEnter course ID:\033[0m"))

                    Enrollment.remove_enrollment_from_course(student_id, course_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print(
                        "\n\033[31minvalid input entered/ student id and course id should be numbers\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif en_choice == 3:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m"))

                    Enrollment.view_enrolled_courses(student_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered. student id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 4:
        while True:
            os.system('clear')
            grade_menu()
            gr_choice = int(input("\033[33mEnter 1-4:\033[0m"))

            if gr_choice == 1:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m"))
                    result = Grades.view_student_grades(student_id)
                    if result is not True:
                        input("\n\033[35mPress Enter to continue...\033[0m")
                        continue

                    course_name = input("\033[36mEnter course name to change grade:\033[0m")
                    grade = input("\033[36mEnter grade to assign:\033[0m")
                    Grades.assign_grade(student_id, course_name, grade)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered. student id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif gr_choice == 2:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m"))
                    result = Grades.view_student_grades(student_id)
                    if result is not True:
                        input("\n\033[35mPress Enter to continue...\033[0m")
                        continue

                    course_name = input("\033[36mEnter course name to change grade:\033[0m")
                    grade = input("\033[36mEnter updated grade:\033[0m")
                    Grades.update_grade(student_id, course_name, grade)
                    input("\n\033[35mPress Enter to continue...\033[0m")

                except ValueError:
                    print("\n\033[31minvalid input entered. student id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif gr_choice == 3:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m"))
                    Grades.view_student_grades(student_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31minvalid input entered. student id should be number\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            else:
                break

    elif choice == 5:
        while True:
            os.system('clear')
            reports_menu()
            re_choice = int(input("\033[33mEnter 1-4:\033[0m"))

            if re_choice == 1:
                print("\033[34m---Top Performing Student---\033[0m")
                StudentReports.top_performing_student()

                print("\n\033[34m---Avg Student Grade---\033[0m")
                StudentReports.avg_student_grade()

                print("\n\033[34m---Pass/Fail Students---\033[0m")
                StudentReports.pass_fail_students_count()
                
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif re_choice == 2:
                print("\n\033[34m---No. of Students in Each Department:---\033[0m")
                DeptReports.students_in_each_dept()
                
                input("\n\033[35mPress Enter to continue...\033[0m")
            
            elif re_choice == 3:
                print("\n\033[34m---No. of students in Each Enrolled Course:---\033[0m")
                CourseReports.students_in_each_course()
                
                input("\n\033[35mPress Enter to continue...\033[0m")
            
            else:
                break
    else:
        break