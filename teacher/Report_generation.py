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
        with open("grades.txt", "w") as f:
            f.write("")
        return []

def open_attendances():
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
        with open("attendances.txt", "w") as f:
            f.write("")
        return []

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
        print(f"Course ID: {record['Course ID']}")
        print(f"Class Attendance: {record['Class Attendance']}")
        print(f"Event Attendance: {record['Event Attendance']}")
        print(f"Combined Attendance: {record['Combined Attendance']}")
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
