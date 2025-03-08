def open_grades():
    grades = []
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")
                if len(fields) < 7:
                    print(f"Skipping invalid line: {line}")
                    continue
                record = {
                    "student_id": fields[0].strip().upper(),
                    "course_id": fields[1].strip().upper(),
                    "assignment_score": fields[2].strip(),
                    "exam_score": fields[3].strip(),
                    "gpa": fields[4].strip(),
                    "feedback": fields[5].strip(),
                    "performance": fields[6].strip()
                }
                grades.append(record)
        return grades
    except FileNotFoundError:
        print("Warning: 'grades.txt' not found. Creating an empty file.")
    return None

def open_attendances():
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
def generation_performances(grades):
    print("=== Performance Report (Grades) ===")
    student_id = input("Please enter the student ID to view grades (leave blank to view all): ").strip().upper()
    if not student_id:
        selected_records = grades
    else:
        selected_records = [record for record in grades if record["student_id"] == student_id]
    if not selected_records:
        print("No grade records found for the specified student or no records at all.")
        return
    for record in selected_records:
        print(f"student_id: {record['student_id']}")
        print(f"course_id: {record['course_id']}")
        print(f"assignment_score: {record['assignment_score']}")
        print(f"exam_score: {record['exam_score']}")
        print(f"gpa: {record['gpa']}")
        print(f"feedback: {record['feedback']}")
        print(f"performance: {record['performance']}")
        print("--------------------------------------------------")

def generation_participation(attendances):
    print("=== Participation Report (Attendances) ===")
    student_id = input("Please enter the student ID to view attendance (leave blank to view all): ").strip().upper()
    if not student_id:
        selected_records = attendances
    else:
        selected_records = [record for record in attendances if record["Student ID"] == student_id]
    if not selected_records:
        print("No attendance records found for the specified student or no records at all.")
        return
    for record in selected_records:
        print(f"Student ID: {record['Student ID']}")
        print(f"Event Attendance: {record['Event Attendance']}")
        print(f"Course 1: {record['Course 1']}")
        print(f"Course 1 Attendance: {record['Course 1 Attendance']}")
        print(f"Course 2: {record['Course 2']}")
        print(f"Course 2 Attendance: {record['Course 2 Attendance']}")
        print(f"Course 3: {record['Course 3']}")
        print(f"Course 3 Attendance: {record['Course 3 Attendance']}")
        print(f"Course 4: {record['Course 4']}")
        print(f"Course 4 Attendance: {record['Course 4 Attendance']}")
        print(f"Course 5: {record['Course 5']}")
        print(f"Course 5 Attendance: {record['Course 5 Attendance']}")
        print(f"Total Attendance: {record['Total Attendance']}")
        print("--------------------------------------------------")

def report_generation_menu():
    while True:
        grades = open_grades()
        attendances = open_attendances()

        print("\n------------------------------------------------------")
        print("---------------- Student Reports ---------------------")
        print("------------------------------------------------------")
        print("1. Generate Grades Report")
        print("2. Generate Attendance Report")
        print("3. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")
            continue

        if opt == 1:
            generation_performances(grades)
        elif opt == 2:
            generation_participation(attendances)
        elif opt == 3:
            print("Returning to teacher menu")
            break
        else:
            print("Invalid choice, please enter a number between 1-3.")

# report_generation_menu()
