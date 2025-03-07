def open_attendances():
    """
    Reads 'attendances.txt' and returns a list of dictionaries,
    each containing 13 fields:
      1)  Student ID
      2)  Event Attendance,
      3)  Course 1, 4) Course 1 Attendance,
      5)  Course 2, 6) Course 2 Attendance,
      7)  Course 3, 8) Course 3 Attendance,
      9)  Course 4, 10) Course 4 Attendance,
      11) Course 5, 12) Course 5 Attendance,
      13) Total Attendance
    """
    attendances = []
    try:
        with open("attendances.txt", "r") as record:
            for line in record:
                fields = line.rstrip().split(',')
                while len(fields) < 13:
                    fields.append("")
                detail = {
                    'Student ID': fields[0],
                    'Event Attendance': fields[1],
                    'Course 1': fields[2],
                    'Course 1 Attendance': fields[3],
                    'Course 2': fields[4],
                    'Course 2 Attendance': fields[5],
                    'Course 3': fields[6],
                    'Course 3 Attendance': fields[7],
                    'Course 4': fields[8],
                    'Course 4 Attendance': fields[9],
                    'Course 5': fields[10],
                    'Course 5 Attendance': fields[11],
                    'Total Attendance': fields[12]
                }
                attendances.append(detail)
        return attendances
    except FileNotFoundError:
        print("Error: attendances.txt not found.")
        return None


def parse_attendance(att_str):
    """
    Helper function:
    Converts a string 'attended/total' into a tuple (attended, total).
    Returns (0, 0) if the format is invalid or empty.
    """
    try:
        attended, total = att_str.split("/")
        return int(attended), int(total)
    except:
        return 0, 0


def recalc_total_attendance(record):
    """
    Recalculate the 'Total Attendance' field for a record,
    by summing:
      - Event Attendance
      - Course 1~5 Attendance
    and storing the result as 'attended/total'.
    If the total is zero, leave the field blank.
    """
    total_attended = 0
    total_possible = 0

    # Event Attendance
    if record['Event Attendance']:
        ea, et = parse_attendance(record['Event Attendance'])
        total_attended += ea
        total_possible += et

    # Courses 1 to 5 Attendance
    for i in range(1, 6):
        att_str = record[f'Course {i} Attendance']
        if att_str:
            ca, ct = parse_attendance(att_str)
            total_attended += ca
            total_possible += ct

    if total_possible == 0:
        record['Total Attendance'] = ""
    else:
        record['Total Attendance'] = f"{total_attended}/{total_possible}"


def upload_or_update_attendance():
    """
    Prompts the teacher to enter a student's attendance record.
    If the student already has a record, it checks if the course code already exists.
      - If the course exists, only its attendance is updated.
      - If not, it adds the course in the first available empty slot.
    Additionally, if the teacher doesn't want to update the Event Attendance, they can press Enter to skip it.
    The record is written to 'attendances.txt' as one line with 13 comma-separated fields.
    """
    print("\n--- Upload/Update Attendance ---")
    student_id = input("Enter Student ID: ").strip().upper()

    # Prompt for event attendance with an option to skip updating it.
    event_att = input("Enter Event Attendance (e.g., 1/4) [press Enter to skip]: ").strip()

    course_code = input("Enter Course Code (e.g., ISCC001): ").strip().upper()
    course_att = input("Enter Course Attendance (e.g., 21/25): ").strip()

    # Read existing attendance records
    attendances = open_attendances()
    if attendances is None:
        return

    # Search for an existing record for the student
    record = None
    for att in attendances:
        if att['Student ID'] == student_id:
            record = att
            break

    # If no record exists, create a new blank record
    if record is None:
        record = {
            'Student ID': student_id,
            'Event Attendance': '',
            'Course 1': '',
            'Course 1 Attendance': '',
            'Course 2': '',
            'Course 2 Attendance': '',
            'Course 3': '',
            'Course 3 Attendance': '',
            'Course 4': '',
            'Course 4 Attendance': '',
            'Course 5': '',
            'Course 5 Attendance': '',
            'Total Attendance': ''
        }
        attendances.append(record)

    # Update Event Attendance only if the teacher provided an input
    if event_att:
        record['Event Attendance'] = event_att

    # Check if the course code already exists in the record
    course_found = False
    for i in range(1, 6):
        if record[f'Course {i}'].upper() == course_code:
            # Update the attendance for the existing course
            record[f'Course {i} Attendance'] = course_att
            course_found = True
            break

    # If the course is not already present, find the first empty course slot
    if not course_found:
        assigned = False
        for i in range(1, 6):
            if not record[f'Course {i}']:
                record[f'Course {i}'] = course_code
                record[f'Course {i} Attendance'] = course_att
                assigned = True
                break
        if not assigned:
            print("Warning: This student already has 5 courses filled. No more courses can be added.")
            # Additional logic can be added here to decide whether to overwrite an existing course.

    # Recalculate the total attendance for the record
    recalc_total_attendance(record)

    # Write all updated attendance records back to attendances.txt (overwrite the file)
    with open("attendances.txt", "w") as f:
        for att in attendances:
            line = ",".join([
                att['Student ID'],
                att['Event Attendance'],
                att['Course 1'],
                att['Course 1 Attendance'],
                att['Course 2'],
                att['Course 2 Attendance'],
                att['Course 3'],
                att['Course 3 Attendance'],
                att['Course 4'],
                att['Course 4 Attendance'],
                att['Course 5'],
                att['Course 5 Attendance'],
                att['Total Attendance']
            ])
            f.write(line + "\n")

    print("\n--- Attendance Record Updated Successfully ---")
    print(f"Student ID:        {record['Student ID']}")
    print(f"Event Attendance:  {record['Event Attendance']}")
    print(f"Course Code:       {course_code}")
    print(f"Course Attendance: {course_att}")
    print(f"Total Attendance:  {record['Total Attendance']}")


def attendance_tracking_menu():
    """
    A simple menu for attendance tracking.
    Options:
      1) Upload/Update Attendance
      2) Exit
    """
    while True:
        print("\n----------- Attendance System Menu -----------")
        print("1) Upload/Update Attendance")
        print("2) Exit")
        choice = input("Please choose (1-2): ").strip()
        if choice == "1":
            upload_or_update_attendance()
        elif choice == "2":
            print("Program terminated.")
            break
        else:
            print("Invalid input, please choose 1 or 2.\n")


# attendance_tracking_menu()
