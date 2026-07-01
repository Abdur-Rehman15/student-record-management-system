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

while True:
    main_menu()
    choice = int(input("Enter 1-6:"))

    if choice == 1:
        while True:
            student_menu()
            st_choice = int(input("Enter 1-6:"))

            if st_choice == 1:
                try:

                    name = input("Enter name:")
                    id = int(input("Enter student id:"))
                    email_address = input("Enter email address:")
                    age = int(input("Enter student age:"))
                    department = input("Enter student department:")

                    Student.add_student(id, name, age, email_address, department)

                except ValueError:
                    print("\ninvalid input entered, id and age should be numbers")

            elif st_choice == 2:
                for student in Student.get_all_students():
                    print(f"ID: {student['id']} with Name: {student['name']}")

            elif st_choice == 3:
                try:

                    id = int(input("Enter student ID:"))
                    Student.search_student_by_ID(id)
                except ValueError:
                    print("\ninvalid input entered. id should be number")

            elif st_choice == 4:
                try:
                    id = int(input("Enter student ID:"))
                    name = input("Enter student name:")
                    age = int(input("Enter age:"))
                    email_address = input("Enter email:")
                    department = input("Enter department:")

                    Student.update_student(name, id, email_address, age, department)

                except ValueError:
                    print("\ninvalid input entered. id and age should be numbers")

            elif st_choice == 5:
                try:
                    id = int(input("Enter student ID to delete:"))
                    Student.delete_student(id)
                except ValueError:
                    print("\ninvalid input entered. id should be number")
            else:
                break

    elif choice == 2:
        while True:
            course_menu()
            cr_choice = int(input("Enter 1-4:"))

            if cr_choice == 1:
                try:
                    course_name = input("Enter course name:")
                    course_id = int(input("Enter course ID:"))
                    cr_hrs = int(input("Enter credit hrs:"))

                    Course.add_course(course_name, course_id, cr_hrs)

                except ValueError:
                    print(
                        "\ninvalid input entered. course id and credit hrs should be numbers"
                    )

            elif cr_choice == 2:
                for course in Course.view_all_courses():
                    print(
                        "Name:",
                        course["name"],
                        "ID:",
                        course["id"],
                        "Credit hrs:",
                        course["credit_hrs"],
                    )

            elif cr_choice == 3:
                try:

                    course_id = int(input("Enter course ID to delete:"))
                    Course.delete_course(course_id)

                except ValueError:
                    print("\ninvalid input entered. course id should be number")
            else:
                break

    elif choice == 3:
        while True:
            enrollment_menu()
            en_choice = int(input("Enter 1-4:"))

            if en_choice == 1:
                try:
                    student_id = int(input("Enter student ID:"))
                    course_id = int(input("Enter course ID:"))

                    Enrollment.enroll_student_in_course(student_id, course_id)

                except ValueError:
                    print("\ninvalid input entered. course id should be number")

            elif en_choice == 2:
                try:
                    student_id = int(input("Enter student ID:"))
                    course_id = int(input("Enter course ID:"))

                    Enrollment.remove_enrollment_from_course(student_id, course_id)

                except ValueError:
                    print(
                        "\ninvalid input entered/ student id and course id should be numbers"
                    )

            elif en_choice == 3:
                try:
                    student_id = int(input("Enter student ID:"))

                    Enrollment.view_enrolled_courses(student_id)

                except ValueError:
                    print("\ninvalid input entered. student id should be number")
            else:
                break

    elif choice == 4:
        while True:
            grade_menu()
            gr_choice = int(input("Enter 1-4:"))

            if gr_choice == 1:
                try:
                    student_id = int(input("Enter student ID:"))
                    result = Grades.view_student_grades(student_id)
                    if result is not True:
                        continue

                    course_name = input("Enter course name to change grade:")
                    grade = input("Enter grade to assign:")
                    Grades.assign_grade(student_id, course_name, grade)

                except ValueError:
                    print("\ninvalid input entered. student id should be number")

            elif gr_choice == 2:
                try:
                    student_id = int(input("Enter student ID:"))
                    result = Grades.view_student_grades(student_id)
                    if result is not True:
                        continue

                    course_name = input("Enter course name to change grade:")
                    grade = input("Enter updated grade:")
                    Grades.update_grade(student_id, course_name, grade)

                except ValueError:
                    print("\ninvalid input entered. student id should be number")

            elif gr_choice == 3:
                try:
                    student_id = int(input("Enter student ID:"))
                    Grades.view_student_grades(student_id)
                except ValueError:
                    print("\ninvalid input entered. student id should be number")

            else:
                break

    elif choice == 5:
        while True:
            reports_menu()
            re_choice = int(input("Enter 1-4:"))

            if re_choice == 1:
                print("---Top Performing Student---")
                StudentReports.top_performing_student()

                print("\n---Avg Student Grade---")
                StudentReports.avg_student_grade()

                print("\n---Pass/Fail Students---")
                StudentReports.pass_fail_students_count()

            elif re_choice == 2:
                print("\n---No. of Students in Each Department:---")
                DeptReports.students_in_each_dept()

            elif re_choice == 3:
                print("\n---No. of students in Each Enrolled Course:---")
                CourseReports.students_in_each_course()
            else:
                break
    else:
        break
