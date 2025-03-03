import Course_creation_and_management
import Student_enrolment
import Grade_and_assessment
import Attendance_tracking
import Report_generation

def main_menu():
    while True:
        # ... Print your main menu header ...

        print("Main Menu:")
        print("1. Course creation and management")
        print("2. Student_enrolment")
        print("3. Grade_and_assessment")
        print("4. Attendance_tracking")
        print("5. Report_generation")
        print("6. Exit")

        try:
            selection = int(input("Please enter your choice (1-6): "))
            if selection == 1:
                # Go to the sub-menu in Course_creation_and_management
                Course_creation_and_management.Course_creation_and_Management_Menu()
            elif selection == 2:
                Student_enrolment.Student_Enrolment_Menu()
            elif selection == 3:
                Grade_and_assessment.Grade_and_Assessment_Menu()
            elif selection == 4:
                Attendance_tracking.Attendance_Tracking_Menu()
            elif selection == 5:
                Report_generation.Report_Generation_Menu()
            elif selection == 6:
                print("Thank you for visiting the system.\nExiting Teacher Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input! Only integers 1–6 are allowed.\nPlease try again.")

main_menu()




