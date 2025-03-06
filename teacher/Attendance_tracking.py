def open_enrolments():
    enrolments = []
    try:
        with open("enrolments.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")
                if len(fields) < 2:
                    print(f"Skipping invalid enrolment line: {line}")
                    continue
                enrolment = {
                    "Student ID": fields[0].strip().upper(),
                    "Course ID": fields[1].strip().upper()
                }
                enrolments.append(enrolment)
    except FileNotFoundError:
        print("Warning: enrolments.txt not found. Creating an empty file.")
        with open("enrolments.txt", "w") as f:
            f.write("")
        return []
    return enrolments

def open_attendances():
    """
    Reads attendances.txt and returns a list of dictionaries.
    Each dictionary contains:
      - Student ID: the student's ID
      - Course ID: the course ID
      - Class Attendance: the class attendance record (e.g., "8/10")
      - Event Attendance: the event attendance record (e.g., "5/10")
      - Combined Attendance: the computed combined attendance (e.g., "13/20 (65.00%)")
    """
    attendances = []
    try:
        with open("attendances.txt", "r") as f:
            for line in f:
                parts = line.rstrip().split(",")
                if len(parts) >= 5:
                    record = {
                        "Student ID": parts[0].strip().upper(),
                        "Course ID": parts[1].strip().upper(),
                        "Class Attendance": parts[2].strip(),
                        "Event Attendance": parts[3].strip(),
                        "Combined Attendance": parts[4].strip()
                    }
                    attendances.append(record)
        return attendances
    except FileNotFoundError:
        print("Warning: attendances.txt not found. Creating an empty file.")
        return []

def save_attendances(attendances):
    with open("attendances.txt", "w") as f:
        for rec in attendances:
            f.write(f"{rec['Student ID']},{rec['Course ID']},{rec['Class Attendance']},"
                    f"{rec['Event Attendance']},{rec['Combined Attendance']}\n")

def upload_attendances():
    """
    Prompts the teacher to input a student's username and course ID.
    First, it checks that the student is enrolled in the course (using enrolments.txt).
    Then it prompts for class attendance and event attendance (in "attended/total" format),
    calculates the combined attendance, prints the record details, and appends the record to attendances.txt.
    """
    print("\n--- Upload Attendance ---")
    student_id = input("Enter Student ID: ").strip().upper()
    course_id = input("Enter Course ID: ").strip().upper()

    # Verify enrollment
    enrolments = open_enrolments()
    enrollment_found = False
    for e in enrolments:
        if e["Student ID"] == student_id and e["Course ID"] == course_id:
            enrollment_found = True
            break
    if not enrollment_found:
        print("Error: This student is not enrolled in the specified course. Cannot proceed.")
        return

    # Input attendance records
    class_attendance = input("Enter class attendance (e.g., 83/100): ").strip()
    event_attendance = input("Enter event attendance (e.g., 53/100): ").strip()

    # Helper function to parse attendance string
    def parse_attendance(att):
        parts = att.split("/")
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return int(parts[0]), int(parts[1])
        else:
            return None, None

    class_attended, class_total = parse_attendance(class_attendance)
    if class_attended is None:
        print("Invalid format for class attendance. Please use the format 'attended/total'.")
        return

    event_attended, event_total = parse_attendance(event_attendance)
    if event_attended is None:
        print("Invalid format for event attendance. Please use the format 'attended/total'.")
        return

    # Calculate combined attendance
    total_attended = class_attended + event_attended
    total_possible = class_total + event_total
    if total_possible > 0:
        percentage = (total_attended / total_possible) * 100
        combined_attendance = f"{total_attended}/{total_possible} ({percentage:.2f}%)"
    else:
        combined_attendance = "0/0 (0.00%)"

    # Append the new record to attendances.txt
    try:
        with open("attendances.txt", "a") as f:
            f.write(f"{student_id},{course_id},{class_attendance},{event_attendance},{combined_attendance}\n")
        print("Attendance record added successfully.")
    except Exception as e:
        print("Error saving attendance record:", e)
        return

    # Print the attendance report
    print("\n--- Attendance Report ---")
    print(f"Student Username: {student_id}")
    print(f"Course ID:        {course_id}")
    print(f"Class Attendance: {class_attendance}")
    print(f"Event Attendance: {event_attendance}")
    print(f"Combined:         {combined_attendance}")

def attendance_tracking_menu():
    """
    A simple menu for attendance tracking:
      1) Upload attendance (after verifying student enrollment)
      2) Exit
    """
    while True:
        print("\n----------- Attendance System Menu -----------")
        print("1) Upload attendance")
        print("2) Exit")
        choice = input("Please choose (1-2): ").strip()
        if choice == '1':
            upload_attendances()
        elif choice == '2':
            print("Program terminated.")
            break
        else:
            print("Invalid input, please choose 1 or 2.\n")

# Run the attendance tracking menu
# attendance_tracking_menu()
