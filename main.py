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
            st_choice = int(input("Enter 1-5:"))

            if st_choice == 1:
                name = input("Enter name:")
                id = int(input("Enter student id:"))
                email_address = input("Enter email address:")
                age = int(input("Enter student age:"))
                department = input("Enter student department:")

                Student.add_student(id, name, age, email_address, department)

            elif st_choice == 2:
                print(Student.get_all_students())

            elif st_choice == 3:
                id = int(input("Enter student ID:"))
                print(Student.search_student_by_ID(id))

            elif st_choice == 4:
                id = int(input("Enter student ID:"))
                name = input("Enter student name:")
                age = int(input("Enter age:"))
                email_address = input("Enter email:")
                department = input("Enter department:")

                print(Student.update_student(name, id, email_address, age, department))

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
                course_name = input("Enter course name:")
                course_id = int(input("Enter course ID:"))
                cr_hrs = int(input("Enter credit hrs:"))

                print(Course.add_course(course_name, course_id, cr_hrs))

            elif cr_choice == 2:
                print(Course.view_all_courses())

            elif cr_choice == 3:
                course_id = int(input("Enter course ID to delete:"))
                print(Course.delete_course(id))
            else:
                break

    elif choice == 3:
        while True:
            enrollment_menu()
            en_choice = int(input("Enter 1-4:"))

            if en_choice == 1:
                student_id = int(input("Enter student ID:"))
                course_id = int(input("Enter course ID:"))

                print(Enrollment.enroll_student_in_course(student_id, course_id))

            elif en_choice == 2:
                student_id = int(input("Enter student ID:"))
                course_id = int(input("Enter course ID:"))

                print(Enrollment.remove_enrollment_from_course(student_id, course_id))

            elif en_choice == 3:
                student_id = int(input("Enter student ID:"))

                print(Enrollment.view_enrolled_courses(student_id))
            else:
                break

    elif choice == 4:
        while True:
            grade_menu()
            gr_choice = int(input("Enter 1-4:"))

            if gr_choice == 1:
                student_id = int(input("Enter student ID:"))
                print(Grades.view_student_grades(student_id))
                course_name = input("Enter course name to change grade:")
                grade = input("Enter grade to assign:")
                print(Grades.assign_grade(student_id, course_name, grade))

            elif gr_choice == 2:
                student_id = int(input("Enter student ID:"))
                grades = Grades.view_student_grades(student_id)
                if grades is not None:
                    print(grades)
                    course_name = input("Enter course name to change grade:")
                    grade = input("Enter updated grade:")
                    print(Grades.update_grade(student_id, course_name, grade))
                else:
                    print('no student found for this ID')

            elif gr_choice == 3:
                student_id = int(input("Enter student ID:"))
                print(Grades.view_student_grades(student_id))

            else:
                break

    elif choice == 5:
        while True:
            reports_menu()
            re_choice = int(input("Enter 1-4:"))

            if re_choice == 1:
                print("---Top Performing Student---")
                print(StudentReports.top_performing_student())

                print("\n---Avg Student Grade---")
                print(StudentReports.avg_student_grade())

                print("\n---Pass/Fail Students---")
                print(StudentReports.pass_fail_students_count())

            elif re_choice == 2:
                print("No. of Students in Each Department:")
                print(DeptReports.students_in_each_dept())

            elif re_choice == 3:
                print("No. of students in Each Enrolled Course:")
                print(CourseReports.students_in_each_course())
            else:
                break
    else:
        break
