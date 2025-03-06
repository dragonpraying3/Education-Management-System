def open_enrolments():
    enrolments = []
    try:
        with open("enrolments.txt", 'r') as tFile:
            for line in tFile:
                fields = line.rstrip().split(",")
                if len(fields) < 2:
                    print(f"Skipping invalid enrolment line: {line}")
                    continue
                enrolment = {
                    "Student ID": fields[0],
                    "Course ID": fields[1]
                }
                enrolments.append(enrolment)
    except FileNotFoundError:
        print("Warning: enrolments.txt not found. Creating an empty file.")
        with open("enrolments.txt", "w") as f:
            f.write("")
        return []
    return enrolments

def save_enrolments(enrolments):
    with open("enrolments.txt", "w") as f:
        for e in enrolments:
            f.write(f"{e['Student ID']},{e['Course ID']}\n")

def open_students():
    students = []
    try:
        with open("student.txt", 'r') as sFile:
            for line in sFile:
                fields = line.rstrip().split(",")
                if len(fields) < 2:
                    print(f"Skipping invalid student line: {line}")
                    continue
                student = {
                    "Student ID": fields[0],
                    "Name": fields[1]
                }
                students.append(student)
    except FileNotFoundError:
        print("Warning: student.txt not found. Creating an empty file.")
        with open("student.txt", "w") as f:
            f.write("")
        return []
    return students

def open_course():
    courses = []
    try:
        with open("course.txt", "r") as f:
            for line in f:
                parts = line.rstrip().split(",")
                if len(parts) < 7:
                    print("Warning: Incomplete course record found and skipped.")
                    continue
                course = {
                    "Course ID": parts[0].strip().upper(),
                    "Teacher ID": parts[1].strip().upper(),
                    "Course Name": parts[2].strip(),
                    "Instructor": parts[3].strip(),
                    "Assignment": parts[4].strip(),
                    "Lecture Notes": parts[5].strip(),
                    "Lesson Plan": parts[6].strip()
                }
                courses.append(course)
        return courses
    except FileNotFoundError:
        print("Warning: course.txt not found. Creating an empty file.")
        with open("course.txt", "w") as f:
            f.write("")
        return []

def course_exists(course_id):
    """
    Check whether the provided course_id exists in course.txt.
    This implementation reuses the open_course() function.
    Returns True if found, otherwise False.
    """
    courses = open_course()  # Reuse open_course() to get all course records
    for course in courses:
        if course["Course ID"].upper() == course_id.upper():
            return True
    return False

def student_enrol(enrolments):
    print("\n=== Student Enrolment ===")
    students = open_students()  # Get valid students from student.txt

    while True:
        student_id = input("Enter Student ID: ").strip().upper()
        student_name = input("Enter Student Name: ").strip()

        # Check if (ID, Name) pair exists in student.txt (name comparison case-insensitive)
        found = False
        for s in students:
            if s["Student ID"].upper() == student_id and s["Name"].lower() == student_name.lower():
                found = True
                break

        if not found:
            print("Error: This student (ID & Name) was not found in student.txt. Please try again.\n")
            continue

        course_id = input("Enter Course ID: ").strip().upper()
        if not course_id:
            print("Error: Course ID is required. Please try again.\n")
            continue

        # Check that the course exists in course.txt using course_exists() function
        if not course_exists(course_id):
            print("Error: The course does not exist in course.txt. Cannot enrol student in a non-existing course.\n")
            return

        # Check if the enrolment already exists
        exists = False
        for e in enrolments:
            if e["Student ID"].upper() == student_id and e["Course ID"].upper() == course_id:
                exists = True
                break
        if exists:
            print("Error: The enrolment already exists. Please try again.\n")
            continue

        new_enrolment = {
            "Student ID": student_id,
            "Course ID": course_id,
        }
        enrolments.append(new_enrolment)
        save_enrolments(enrolments)
        print("--------------------------------------------------")
        print("Student enrolment successful!\n")
        print(f"1. Student ID: {new_enrolment['Student ID']}")
        print(f"2. Course ID:{new_enrolment['Course ID']}")
        print("--------------------------------------------------")
        input("Press Enter to continue...")
        break

def remove_student():
    # Display current enrolments for reference
    try:
        with open('enrolments.txt', 'r') as wFile:
            content = wFile.read()
            print("Current Enrolments:")
            print(content)
    except FileNotFoundError:
        print("Warning: enrolments.txt not found.")

    enrolments = open_enrolments()

    if not enrolments:
        print("\nNo student enrolments found.")
        return

    print("\n=== Remove Student Enrolment ===")
    student_id = input("Enter Student ID to remove: ").strip().upper()
    course_id = input("Enter Course ID to remove: ").strip().upper()

    updated_enrolments = [e for e in enrolments if not (e["Student ID"].upper() == student_id and e["Course ID"].upper() == course_id)]

    if len(updated_enrolments) == len(enrolments):
        print("Error: No matching enrolment found for the given Student ID and Course ID.\n")
    else:
        save_enrolments(updated_enrolments)
        print(f"Enrolment for Student ID {student_id} in Course ID {course_id} removed successfully!\n")
        input("Press Enter to continue...")

def student_enrolment_menu():
    while True:
        enrolments = open_enrolments()

        print("\n------------------------------------------------------")
        print("---------------- Student Enrolment -------------------")
        print("------------------------------------------------------")
        print("1. Enrol Student")
        print("2. Remove Student")
        print("3. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")
            continue

        if opt == 1:
            student_enrol(enrolments)
        elif opt == 2:
            remove_student()
        elif opt == 3:
            print("Returning to teacher menu")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 3.")


# student_enrolment_menu()
