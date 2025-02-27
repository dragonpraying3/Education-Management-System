import upd_info
import course_enrol
import material_access
import grade_tracking

def student_menu():
    while True:
        print("\n-------------------------------")
        print("---------Student Menu----------")
        print("-------------------------------")
        print("1. Update Personal Information")
        print("2. Course Enrolment")
        print("3. Course Material Access")
        print("4. Grades Tracking")
        print("5. Feedback Submission")
        print("6. Exit")
        print("-------------------------------")

        opt = int(input("\nYour choice: "))

        if opt == 1:
            upd_info.information_menu()
        elif opt == 2:
            course_enrol.course_enrolment_menu()
        elif opt == 3:
            material_access.course_material_access()
        elif opt == 4:
            grade_tracking.grades_menu()
        elif opt == 6:
            print("Exiting")
            break


student_menu()
