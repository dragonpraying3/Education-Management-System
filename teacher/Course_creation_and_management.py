def open_teacher():
    """
    Load teacher data from teachers.txt.
    Each line: Teacher ID, Day, Instructor, Available time
    """
    teachers = []
    try:
        with open("teachers.txt", "r") as f:
            for line in f:
                parts = line.rstrip().split(",")
                if len(parts) < 4:
                    print("Warning: Incomplete teacher record found and skipped.")
                    continue
                teacher = {
                    "Teacher ID": parts[0].strip().upper(),
                    "Day": parts[1].strip(),
                    "Instructor": parts[2].strip(),
                    "Available time": parts[3].strip()
                }
                teachers.append(teacher)
        return teachers
    except FileNotFoundError:
        print("Warning: teachers.txt not found.")
        return None  # Return an empty list if file not found

def open_course():
    """
    Load course data from course.txt.
    Each line: Course ID, Teacher ID, Course Name, Instructor, Assignment, Lecture Notes, Lesson Plan
    """
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
        return None  # Return an empty list if file not found

def save_course(courses):
    """
    Save course data to course.txt using the following fields:
    Course ID, Teacher ID, Course Name, Instructor, Assignment, Lecture Notes, Lesson Plan
    """
    with open("course.txt", "w") as f:
        for course in courses:
            f.write(f"{course['Course ID']},{course['Teacher ID']},{course['Course Name']},"
                    f"{course['Instructor']},{course['Assignment']},{course['Lecture Notes']},"
                    f"{course['Lesson Plan']}\n")

def teacher_create_course():
    """
    Allows a teacher to create a course.
    1. Enter Teacher ID to verify; if the teacher record exists, continue; otherwise exit.
    2. Enter a new Course ID (and check for duplicates), Course Name, Assignment, Lecture Notes, and Lesson Plan.
       The Instructor field is automatically taken from the teacher record, and Teacher ID is recorded.
    3. Save the new course record to course.txt and print all current course information.
    """
    teacher_id = input("Please enter Teacher ID: ").strip().upper()
    teachers = open_teacher()
    teacher_found = None
    for t in teachers:
        if t["Teacher ID"] == teacher_id:
            teacher_found = t
            break
    if not teacher_found:
        print("Teacher ID does not exist; cannot create course.")
        return

    print("Teacher verified. Welcome,", teacher_found["Instructor"])

    courses = open_course()
    if courses is None:
        return
    course_id = input("Please enter new Course ID: ").strip().upper()
    if any(c["Course ID"] == course_id for c in courses):
        print("Error: Course ID already exists. Please try again.")
        return

    course_name = input("Please enter Course Name: ").strip()
    assignment = input("Please enter Assignment information: ").strip()
    lecture_notes = input("Please enter Lecture Notes: ").strip()
    lesson_plan = input("Please enter Lesson Plan: ").strip()

    if not (course_id and course_name and assignment and lecture_notes and lesson_plan):
        print("Error: All fields are required. Please try again.")
        return

    new_course = {
        "Course ID": course_id,
        "Teacher ID": teacher_id,
        "Course Name": course_name,
        "Instructor": teacher_found["Instructor"],
        "Assignment": assignment,
        "Lecture Notes": lecture_notes,
        "Lesson Plan": lesson_plan
    }
    courses.append(new_course)
    save_course(courses)
    print("--------------------------------------------------")
    print("Course created successfully! Current courses:")
    print(f"1. Course ID: {new_course['Course ID']}")
    print(f"   Teacher ID:    {new_course['Teacher ID']}")
    print(f"   Course Name:   {new_course['Course Name']}")
    print(f"   Instructor:    {new_course['Instructor']}")
    print(f"   Assignment:    {new_course['Assignment']}")
    print(f"   Lecture Notes: {new_course['Lecture Notes']}")
    print(f"   Lesson Plan:   {new_course['Lesson Plan']}")
    print("--------------------------------------------------")

def update_course():
    """
    Update an existing course's Instructor, Assignment, Lecture Notes, or Lesson Plan.
    """
    course_id = input("\nPlease enter the Course ID to update: ").strip().upper()
    courses = open_course()
    if courses is None:
        return

    course_found = None
    for course in courses:
        if course["Course ID"] == course_id:
            course_found = course
            break

    if course_found is None:
        print("Course not found. Returning to menu.")
        return

    while True:
        print("\n--------------------------------------")
        print("--------- Current Course Info --------")
        print("--------------------------------------")
        print(f"Course ID:       {course_found['Course ID']}")
        print(f"Teacher ID:      {course_found['Teacher ID']}")
        print(f"Course Name:     {course_found['Course Name']}")
        print(f"Instructor:      {course_found['Instructor']}")
        print(f"Assignment:      {course_found['Assignment']}")
        print(f"Lecture Notes:   {course_found['Lecture Notes']}")
        print(f"Lesson Plan:     {course_found['Lesson Plan']}")
        print("--------------------------------------")
        input("Press Enter to continue...")

        print("\nSelect the field to update:")
        print("1. Instructor")
        print("2. Assignment")
        print("3. Lecture Notes")
        print("4. Lesson Plan")
        print("5. Return to main menu")

        try:
            choice = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print(f"Old Instructor: {course_found['Instructor']}")
            course_found['Instructor'] = input("New Instructor: ").strip()
            save_course(courses)
            print("Instructor updated successfully!\n")
        elif choice == 2:
            print(f"Old Assignment: {course_found['Assignment']}")
            course_found['Assignment'] = input("New Assignment: ").strip()
            save_course(courses)
            print("Assignment updated successfully!\n")
        elif choice == 3:
            print(f"Old Lecture Notes: {course_found['Lecture Notes']}")
            course_found['Lecture Notes'] = input("New Lecture Notes: ").strip()
            save_course(courses)
            print("Lecture Notes updated successfully!\n")
        elif choice == 4:
            print(f"Old Lesson Plan: {course_found['Lesson Plan']}")
            course_found['Lesson Plan'] = input("New Lesson Plan: ").strip()
            save_course(courses)
            print("Lesson Plan updated successfully!\n")
        elif choice == 5:
            print("Returning to main menu.\n")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

def view_course(courses):
    """Print all course records."""
    print("\n=== Course List ===")
    if not courses:
        print("No course records available.")
    else:
        counter = 1
        for course in courses:
            print(f"{counter}. Course ID: {course['Course ID']}")
            print(f"   Teacher ID:    {course['Teacher ID']}")
            print(f"   Course Name:   {course['Course Name']}")
            print(f"   Instructor:    {course['Instructor']}")
            print(f"   Assignment:    {course['Assignment']}")
            print(f"   Lecture Notes: {course['Lecture Notes']}")
            print(f"   Lesson Plan:   {course['Lesson Plan']}")
            print("--------------------------------------------------")
            counter += 1

def schedule():
    """Let the user choose a teacher record and update its Available Time."""
    teachers = open_teacher()
    if teachers is None:
        return

    print("\n--- Teacher Records ---")
    counter = 1
    for teacher in teachers:
        print(f"{counter}. Teacher ID: {teacher['Teacher ID']} - Instructor: {teacher['Instructor']} - Available Time: {teacher['Available time']}")
        counter += 1

    try:
        choice = int(input("Select the teacher (by number) to update Available Time: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice < 1 or choice > len(teachers):
        print("Invalid selection, number out of range.")
        return

    selected_teacher = teachers[choice - 1]
    new_time = input("Enter new Available Time: ").strip()
    if new_time:
        selected_teacher["Available time"] = new_time
        print("Available Time updated successfully!")
        with open("teachers.txt", "w") as f:
            for teacher in teachers:
                f.write(f"{teacher['Teacher ID']},{teacher['Day']},{teacher['Instructor']},{teacher['Available time']}\n")
    else:
        print("No new Available Time entered.")

def course_creation_and_management_menu():
    """Main menu for course creation and management."""
    while True:
        courses = open_course()
        print("\n------------------------------------------------------")
        print("--------- Course Creation and Management Menu --------")
        print("------------------------------------------------------")
        print("1. Create course (after teacher verification)")
        print("2. Update course")
        print("3. View all courses")
        print("4. Schedule")
        print("5. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if opt == 1:
            teacher_create_course()
        elif opt == 2:
            update_course()
        elif opt == 3:
            view_course(courses)
        elif opt == 4:
            schedule()
        elif opt == 5:
            print("Exiting course management menu.")
            break
        else:
            print("Invalid selection, please enter a number between 1 and 5.")

# Run the main menu
# course_management_menu()
