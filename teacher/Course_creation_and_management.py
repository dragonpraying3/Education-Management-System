def open_teacher():
    """Load teacher data from teachers.txt.
       Each line: Course ID,Day,Instructor,Available time
    """
    teachers = []
    try:
        with open("teachers.txt", "r") as instructor:
            for column in instructor:
                column = column.rstrip().split(",")
                # Ensure we have 4 fields
                item = {
                    "Teacher ID": column[0],
                    "Day": column[1],
                    "Instructor": column[2],
                    "Available time": column[3]
                  }
                teachers.append(item)
        return teachers
    except FileNotFoundError:
        print("Warning: teachers.txt not found. Creating an empty file.")
    return None # Return an empty list if file not found

def save_teacher(teachers):
    """Save teacher data back to teachers.txt.
       Each line: Course ID,Day,Instructor,Available time
    """
    with open("teachers.txt", "w") as f:
        for t in teachers:
            f.write(f"{t['Teacher ID']},"
                    f"{t['Day']},"
                    f"{t['Instructor']},"
                    f"{t['Available time']}\n")

def open_course():
    courses = []
    try:
        with open("course.txt", 'r') as tFile:
            for line in tFile:
                line = line.rstrip().split(",")
            # Ensure we have at least 6 fields
                course = {
                    "Course ID": line[0],
                    "Course Name": line[1],
                    "Instructor": line[2],
                    "Assignment": line[3],
                    "Lecture Notes": line[4],
                    "Lesson Plan": line[5]
                }
                courses.append(course)
            return courses
    except FileNotFoundError:
        print("Warning: course.txt not found. Creating an empty file.")
    return None

def save_course(courses):
    """Save course data to course.txt using the same capitalized keys."""
    with open("course.txt", "w") as f:
        for course in courses:
            f.write(f"{course['Course ID']},"
                    f"{course['Course Name']},"
                    f"{course['Instructor']},"
                    f"{course['Assignment']},"
                    f"{course['Lecture Notes']},"
                    f"{course['Lesson Plan']}\n")

def Create_course(courses):
    """Create a new course using the same keys as open_course/save_course."""
    print("\n=== Create course ===")
    while True:
        course_id = input("Enter Course ID: ").strip().upper()
        course_name = input("Enter Course Name: ").strip().upper()
        instructor = input("Enter Instructor: ").strip()
        assignment = input("Enter Assignment: ").strip()
        lecture_notes = input("Enter Lecture Notes: ").strip()
        lesson_plan = input("Enter Lesson Plan: ").strip()

        if (not course_id or not course_name or not instructor
                or not assignment or not lecture_notes or not lesson_plan):
            print("Error: All fields are required. Please try again.\n")
        else:
            new_course = {
                "Course ID": course_id,
                "Course Name": course_name,
                "Instructor": instructor,
                "Assignment": assignment,
                "Lecture Notes": lecture_notes,
                "Lesson Plan": lesson_plan
            }
            courses.append(new_course)
            save_course(courses)
            print("Course created successfully!\n")
            input("Press space to continue")
            break


def Update_course():
    """Update an existing course's Instructor, Assignment, Lecture Notes, or Lesson Plan."""
    course_id = input("\nEnter your Course ID: ").strip().upper()
    courses = open_course()

    course_found = None
    for course in courses:
        if course["Course ID"].upper() == course_id.upper():
            course_found = course
            break

    if course_found is None:
        print("Course not found. Returning to menu.")
        return

    while True:
        print("\n--------------------------------------")
        print("---------Current Course----------")
        print("--------------------------------------")
        print(f"Course ID:       {course_found['Course ID']}")
        print(f"Course Name:     {course_found['Course Name']}")
        print(f"Instructor:      {course_found['Instructor']}")
        print(f"Assignment:      {course_found['Assignment']}")
        print(f"Lecture Notes:   {course_found['Lecture Notes']}")
        print(f"Lesson Plan:     {course_found['Lesson Plan']}")
        print("--------------------------------------")
        input("Press Enter to continue...")

        print("\nWhich field do you want to update?")
        print("1. Instructor")
        print("2. Assignment")
        print("3. Lecture Notes")
        print("4. Lesson Plan")
        print("5. Exit to main menu")

        try:
            choice = int(input("Select the choice you want to update: "))
        except ValueError:
            print("Invalid input. Please enter a number 1-5.")
            continue

        if choice == 1:
            print(f"Old Instructor: {course_found['Instructor']}")
            course_found['Instructor'] = input("New Instructor: ").strip()
            save_course(courses)
            print("Instructor updated!\n")

        elif choice == 2:
            print(f"Old Assignment: {course_found['Assignment']}")
            course_found['Assignment'] = input("New Assignment: ").strip()
            save_course(courses)
            print("Assignment updated!\n")

        elif choice == 3:
            print(f"Old Lecture Notes: {course_found['Lecture Notes']}")
            course_found['Lecture Notes'] = input("New Lecture Notes: ").strip()
            save_course(courses)
            print("Lecture notes updated!\n")

        elif choice == 4:
            print(f"Old Lesson Plan: {course_found['Lesson Plan']}")
            course_found['Lesson Plan'] = input("New Lesson Plan: ").strip()
            save_course(courses)
            print("Lesson plan updated!\n")

        elif choice == 5:
            print("Returning to menu.\n")
            break


        else:
            print("Invalid choice. No changes made.\n")
            input("")

def Schedule():
    """Let the user select a course from teacher records and update its Available Time."""
    teachers = open_teacher()  # Load existing teacher records

    if not teachers:
        print("\nNo teacher records found (teachers.txt is empty).")
        return

    # Display teacher records with a manual counter
    print("\n--- Teacher Courses ---")
    counter = 1
    for teacher in teachers:
        print(str(counter) + ". Teacher ID: " + teacher["Teacher ID"] +
              " - Instructor: " + teacher["Instructor"] +
              " - Available Time: " + teacher["Available time"])
        counter += 1

    # Ask the user to choose a course by its list number
    try:
        choice = int(input("Select the number of the course to update available time: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice < 1 or choice > len(teachers):
        print("Invalid choice. Number out of range.")
        input("")
        return

    # Get the selected teacher record
    selected_teacher = teachers[choice - 1]

    # Input new available time
    new_time = input("Enter new available time: ").strip()
    if new_time:
        selected_teacher["Available time"] = new_time
        print("Available time updated!")
        save_teacher(teachers)
    else:
        print("No new time entered.")


def View_course(courses):
    """Generate a schedule listing each course's details."""
    print("\n=== Course Schedule ===")
    if not courses:
        print("No courses available.")
    else:
        counter = 1
        for course in courses:
            # Use the EXACT keys from open_course()
            print(f"{counter}. Course Name: {course['Course Name']}")
            print(f"   Instructor:      {course['Instructor']}")
            print(f"   Assignment:      {course['Assignment']}")
            print(f"   Lecture Notes:   {course['Lecture Notes']}")
            print(f"   Lesson Plan:     {course['Lesson Plan']}")
            # If you also want 'Available time', you must store it in course.txt
            # or merge data from teachers.txt
            print("   ------------------")
            counter += 1


def Course_creation_and_Management_Menu():
    """Main menu for course creation and management."""
    while True:
        # Load courses each time we display the menu (so we see updates).
        courses = open_course()

        print("\n------------------------------------------------------")
        print("---------Course Creation and Management Menu----------")
        print("------------------------------------------------------")
        print("1. Create course")
        print("2. Update course")
        print("3. View Course")
        print("4. Schedule")
        print("5. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Only integer 1-5 is allowed.")
            continue

        if opt == 1:
            Create_course(courses)

        elif opt == 2:
            Update_course()

        elif opt == 3:
            View_course(courses)

        elif opt == 4:
            # Generate schedule from the (possibly updated) courses
            Schedule()

        elif opt == 5:
            print("Returning to teacher menu")
            break

        else:
            print("Invalid choice, please enter a number between 1-5.")

# Course_creation_Dnd_Management_Menu()
