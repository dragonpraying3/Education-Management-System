def open_enrolments():
    enrolments = []  # create an empty list to store student data
    with open("enrolments.txt", 'r') as tFile:
        for line in tFile:
            line = line.rstrip().split(",")  # split each line become a list and remove whitespace
            # store each list in a dictionary
            enrolment = {
                "Student ID": line[0],
                "Course ID": line[1]
            }
            enrolments.append(enrolment) # add student dictionary to the list
    return enrolments

def save_enrolments(enrolments):
    with open("enrolments.txt", "w") as f:
        for e in enrolments:
            f.write(f"{e['Student ID']},"
                    f"{e['Course ID']}\n")

def open_students():
    students = []  # create an empty list to store student data
    with open("student.txt", 'r') as sFile:
        for line in sFile:
            line = line.rstrip().split(",")  # split each line and remove whitespace
            student = {
                "Student ID": line[0],
                "Name": line[1]
            }
            students.append(student)
    return students


def Student_Enrol(enrolments):
    print("\n=== Student Enrolment ===")
    students = open_students()  # Get valid students from student.txt

    while True:
        student_id = input("Enter Student ID: ").strip()
        student_name = input("Enter Student Name: ").strip()

        # Check if (ID, Name) pair exists in student.txt
        found = False
        for s in students:
            # Compare ID exactly and compare names (case-insensitive if desired)
            if s["Student ID"] == student_id and s["Name"] == student_name:
                found = True
                break

        if not found:
            print("Error: This student (ID & Name) was not found in student.txt. Please try again.\n")
            continue

        course_id = input("Enter Course ID: ").strip()
        if not course_id:
            print("Error: Course ID is required. Please try again.\n")
            continue

        # If student is found and course_id is valid, add new enrolment
        new_enrolment = {
            "Student ID": student_id,
            "Course ID": course_id,
        }
        enrolments.append(new_enrolment)
        save_enrolments(enrolments)
        print("Student enrolment successful!\n")
        input("Press Enter to continue...")
        break

def Remove_Student():
    with open('enrolments.txt', 'r') as wFile:
        content = wFile.read()
        print(content)

    enrolments = open_enrolments()

    if not enrolments:
        print("\nNo student enrolments found.")
        return

    print("\n=== Remove Student Enrolment ===")
    student_id = input("Enter Student ID to remove: ").strip().upper()
    course_id = input("Enter Course ID to remove: ").strip().upper()

    # Check if the student and course exist in the enrolments
    updated_enrolments = [e for e in enrolments if not (e["Student ID"] == student_id and e["Course ID"] == course_id)]

    if len(updated_enrolments) == len(enrolments):
        print("Error: No matching enrolment found for the given Student ID and Course ID.\n")
    else:
        save_enrolments(updated_enrolments)
        print(f"Enrolment for Student ID {student_id} in Course ID {course_id} removed successfully!\n")
        input("")

def Student_Enrolment_Menu():
    while True:
        enrolments= open_enrolments()

        print("\n------------------------------------------------------")
        print("----------------Student Enrolment----------------------")
        print("------------------------------------------------------")
        print("1. Enrol Student")
        print("2. Remove Student")
        print("3. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Only integer 1- is allowed.")
            continue

        if opt == 1:
            Student_Enrol(enrolments)

        elif opt == 2:
            Remove_Student()

        elif opt == 3:
            print("Returning to teacher manu")
            break

        else:
            print("Invalid choice, please enter a number between 1-3 .")
