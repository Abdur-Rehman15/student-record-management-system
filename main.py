import os
import sys
import time

from menu import (
    course_menu,
    enrollment_menu,
    grade_menu,
    main_menu,
    reports_menu,
    student_menu,
)

from modules.courses import Course
import modules.enrollment as Enrollment
import modules.grades as Grades
from modules.student import Student
import modules.reports.course_reports as CourseReports
import modules.reports.dept_reports as DeptReports
import modules.reports.student_reports as StudentReports


def animated_intro():
    """Displays a modern cyber-terminal intro sequence with dynamically generated borders."""
    os.system("clear" if os.name != "nt" else "cls")
    print("\n" * 3)

    # 1. Scanning Effect
    status_text = " » INITIALIZING SECURE SHELL CONNECTION..."
    for char in status_text:
        sys.stdout.write(f"\033[90m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.01)  # Snappier intro
    time.sleep(0.3)
    print(" \033[92m[OK]\033[0m")

    # 2. Setup Dimensions and Dynamic Border
    title = "STUDENT RECORD MANAGEMENT SYSTEM"
    padding_each_side = 10
    inner_width = len(title) + (padding_each_side * 2)

    print("\n" + " " * 15 + "\033[36m┌" + "─" * inner_width + "┐\033[0m")
    sys.stdout.write(" " * 15 + "\033[36m│\033[0m" + " " * padding_each_side)
    sys.stdout.flush()

    for char in title:
        sys.stdout.write(f"\033[1;33m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.03)

    sys.stdout.write(" " * padding_each_side + "\033[36m│\033[0m\n")
    print(" " * 15 + "\033[36m└" + "─" * inner_width + "┘\033[0m")
    time.sleep(0.3)

    # 3. Spinning Loader
    print("\n" + " " * 28 + "\033[90mLoading database core...\033[0m")
    spin_symbols = ["◐", "◓", "◑", "◒"]
    for i in range(8):
        sys.stdout.write(f"\r" + " " * 38 + f"\033[35m{spin_symbols[i % 4]}\033[0m")
        sys.stdout.flush()
        time.sleep(0.08)

    sys.stdout.write(f"\r" + " " * 32 + "\033[1;92mACCESS GRANTED\033[0m\n")
    time.sleep(0.6)


def animated_clear_and_header(subtitle):
    """Clears screen and sweeps a smooth neon progress/separator line over the submenu context."""
    os.system("clear" if os.name != "nt" else "cls")

    # Clean header banner
    print(f"\033[1;90m[ SYSTEM // \033[1;36m{subtitle.upper()}\033[1;90m ]\033[0m")

    # Sleek sliding line animation
    width = 45
    for i in range(width + 1):
        line = "━" * i
        spaces = " " * (width - i)
        sys.stdout.write(f"\r\033[36m{line}\033[90m{spaces}┫\033[0m")
        sys.stdout.flush()
        time.sleep(0.006)
    print("\n")


# Execute Intro Sequence once at system startup
animated_intro()

while True:
    animated_clear_and_header("Main Dashboard")
    main_menu()

    try:
        while True:
            choice = int(input("\n\033[33mEnter 1-6:\033[0m "))
            if 1 <= choice <= 6:  # FIXED: Now catches all numbers between 1 and 6 inclusive
                break
            else:
                print("\033[31mPlease enter a number from 1 to 6.\033[0m")

    except ValueError:
        print("invalid choice entered")
        input("\n\033[35mPress Enter to continue...\033[0m")
        continue

    if choice == 1:
        while True:
            animated_clear_and_header("Students Directory")
            student_menu()
            try:
                while True:
                    st_choice = int(input("\n\033[33mEnter 1-6:\033[0m "))
                    if 1 <= st_choice <= 6:  # FIXED
                        break
                    else:
                        print("\033[31mPlease enter a number from 1 to 6.\033[0m")

            except ValueError:
                print("invalid choice entered")
                input("\n\033[35mPress Enter to continue...\033[0m")
                continue

            if st_choice == 1:
                try:
                    print("\033[90m┌─[ Register New Student ]────────────┐\033[0m")
                    name = input(" \033[36mEnter name:\033[0m ")
                    id = int(input(" \033[36mEnter student id:\033[0m "))
                    email_address = input(" \033[36mEnter email address:\033[0m ")
                    age = int(input(" \033[36mEnter student age:\033[0m "))
                    department = input(" \033[36mEnter student department:\033[0m ")
                    print("\033[90m└─────────────────────────────────────┘\033[0m")

                    Student.add_student(id, name, age, email_address, department)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print(
                        "\n\033[31m[ERROR] Invalid input entered; ID and age must be numbers.\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 2:
                print("\033[90m┌─[ System Database Query ]───────────┐\033[0m")
                for student in Student.get_all_students():
                    print(
                        f"  \033[32m• ID:\033[0m {student['id']:<6} │ \033[32mName:\033[0m {student['name']}"
                    )
                print("\033[90m└─────────────────────────────────────┘\033[0m")
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 3:
                try:
                    id = int(input("\033[36mEnter student ID:\033[0m "))
                    Student.search_student_by_ID(id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print(
                        "\n\033[31m[ERROR] Invalid input entered. ID must be a number.\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 4:
                try:
                    id = int(input("\033[36mEnter student ID to modify:\033[0m "))
                    name = input("\033[36mEnter updated name:\033[0m ")
                    age = int(input("\033[36mEnter updated age:\033[0m "))
                    email_address = input("\033[36mEnter updated email:\033[0m ")
                    department = input("\033[36mEnter updated department:\033[0m ")

                    Student.update_student(name, id, email_address, age, department)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print(
                        "\n\033[31m[ERROR] Invalid input entered. ID and age must be numbers.\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif st_choice == 5:
                try:
                    id = int(input("\033[31mEnter student ID to purge:\033[0m "))
                    Student.delete_student(id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print(
                        "\n\033[31m[ERROR] Invalid input entered. ID must be a number.\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 2:
        while True:
            animated_clear_and_header("Courses")
            course_menu()
            try:
                while True:
                    cr_choice = int(input("\n\033[33mEnter 1-4:\033[0m "))
                    if 1 <= cr_choice <= 4:  # FIXED
                        break
                    else:
                        print("\033[31mPlease enter a number from 1 to 4.\033[0m")
            except ValueError:
                print("invalid choice entered")
                input("\n\033[35mPress Enter to continue...\033[0m")
                continue

            if cr_choice == 1:
                try:
                    course_name = input("\033[36mEnter course name:\033[0m ")
                    course_id = int(input("\033[36mEnter course ID:\033[0m "))
                    cr_hrs = int(input("\033[36mEnter credit hours:\033[0m "))

                    Course.add_course(course_name, course_id, cr_hrs)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print(
                        "\n\033[31m[ERROR] Course ID and credit hours must be numerical values.\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif cr_choice == 2:
                print("\033[90m┌─[ Available Curriculum ]────────────┐\033[0m")
                for course in Course.view_all_courses():
                    print(
                        f"  \033[32m• ID:\033[0m {course['id']:<5} │ \033[32mCredits:\033[0m {course['credit_hrs']} │ \033[32mTitle:\033[0m {course['name']}"
                    )
                print("\033[90m└─────────────────────────────────────┘\033[0m")
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif cr_choice == 3:
                try:
                    course_id = int(input("\033[31mEnter course ID to purge:\033[0m "))
                    Course.delete_course(course_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31m[ERROR] Course ID must be a number.\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 3:
        while True:
            animated_clear_and_header("Enrollments")
            enrollment_menu()
            try:
                while True:
                    en_choice = int(input("\n\033[33mEnter 1-4:\033[0m "))
                    if 1 <= en_choice <= 4:  # FIXED
                        break
                    else:
                        print("\033[31mPlease enter a number from 1 to 4.\033[0m")
            except ValueError:
                print("invalid choice entered")
                input("\n\033[35mPress Enter to continue...\033[0m")
                continue

            if en_choice == 1:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m "))
                    course_id = int(input("\033[36mEnter course ID:\033[0m "))

                    Enrollment.enroll_student_in_course(student_id, course_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31m[ERROR] System keys must be numerical.\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif en_choice == 2:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m "))
                    course_id = int(input("\033[36mEnter course ID:\033[0m "))

                    Enrollment.remove_enrollment_from_course(student_id, course_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print(
                        "\n\033[31m[ERROR] Student ID and Course ID must be numerical values.\033[0m"
                    )
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif en_choice == 3:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m "))
                    Enrollment.view_enrolled_courses(student_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31m[ERROR] Student ID must be a number.\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 4:
        while True:
            animated_clear_and_header("Student Grades")
            grade_menu()
            try:
                while True:
                    gr_choice = int(input("\n\033[33mEnter 1-4:\033[0m "))
                    if 1 <= gr_choice <= 4:  # FIXED
                        break
                    else:
                        print("\033[31mPlease enter a number from 1 to 4.\033[0m")
            except ValueError:
                print("invalid choice entered")
                input("\n\033[35mPress Enter to continue...\033[0m")
                continue

            if gr_choice == 1:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m "))
                    result = Grades.view_student_grades(student_id)
                    if result is not True:
                        input("\n\033[35mPress Enter to continue...\033[0m")
                        continue

                    course_name = input(
                        "\033[36mEnter course name to assign grade:\033[0m "
                    )
                    grade = input("\033[36mEnter grade to assign:\033[0m ")
                    Grades.assign_grade(student_id, course_name, grade)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31m[ERROR] Student ID must be a number.\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif gr_choice == 2:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m "))
                    result = Grades.view_student_grades(student_id)
                    if result is not True:
                        input("\n\033[35mPress Enter to continue...\033[0m")
                        continue

                    course_name = input(
                        "\033[36mEnter course name to update grade:\033[0m "
                    )
                    grade = input("\033[36mEnter updated grade:\033[0m ")
                    Grades.update_grade(student_id, course_name, grade)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31m[ERROR] Student ID must be a number.\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")

            elif gr_choice == 3:
                try:
                    student_id = int(input("\033[36mEnter student ID:\033[0m "))
                    Grades.view_student_grades(student_id)
                    input("\n\033[35mPress Enter to continue...\033[0m")
                except ValueError:
                    print("\n\033[31m[ERROR] Student ID must be a number.\033[0m")
                    input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break

    elif choice == 5:
        while True:
            animated_clear_and_header("Reports")
            reports_menu()
            try:
                while True:
                    re_choice = int(input("\n\033[33mEnter 1-4:\033[0m "))
                    if 1 <= re_choice <= 4:  # FIXED
                        break
                    else:
                        print("\033[31mPlease enter a number from 1 to 4.\033[0m")
            except ValueError:
                print("invalid choice entered")
                input("\n\033[35mPress Enter to continue...\033[0m")
                continue

            if re_choice == 1:
                print("\033[34m┏━[ Performance Metrics Evaluation ]━━┓\033[0m")
                StudentReports.top_performing_student()
                print("\n\033[34m├─ Average Grade Distributions\033[0m")
                StudentReports.avg_student_grade()
                print("\n\033[34m├─ Final Outcome Counts\033[0m")
                StudentReports.pass_fail_students_count()
                print("\033[34m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif re_choice == 2:
                print("\n\033[34m┏━[ Demographics By Department ]━━━━━━┓\033[0m")
                DeptReports.students_in_each_dept()
                print("\033[34m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
                input("\n\033[35mPress Enter to continue...\033[0m")

            elif re_choice == 3:
                print("\n\033[34m┏━[ Enrollment Density Metrics ]━━━━━━┓\033[0m")
                CourseReports.students_in_each_course()
                print("\033[34m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
                input("\n\033[35mPress Enter to continue...\033[0m")
            else:
                break
    else:
        print("\033[1;31mTerminating Session Safely... Goodbye.\033[0m")
        break