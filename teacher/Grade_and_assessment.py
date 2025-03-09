def open_enrolments():
    enrolments = []
    try:
        with open("enrolments.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")
                if len(fields) < 2:
                    print("Skipping invalid enrolment line:", line.strip())
                    continue
                enrolment = {
                    "Student ID": fields[0].strip().upper(),
                    "Course ID": fields[1].strip().upper()
                }
                enrolments.append(enrolment)
        return enrolments
    except FileNotFoundError:
        print("Warning: enrolments.txt not found.")
    return None

def display_enrolments():
    """
    Reads and displays the current enrolment records.
    """
    enrolments = open_enrolments()
    if enrolments is None or len(enrolments) == 0:
        print("No enrolment records found.")
        return
    print("\n=== Current Enrolment Records ===")
    for rec in enrolments:
        print("Student ID:", rec["Student ID"], "| Course ID:", rec["Course ID"])
    print("---------------------------------\n")

def verify_enrollment(student_id, course_id):
    """
    Checks if the (student_id, course_id) pair exists in enrolments.txt.
    Returns True if found, otherwise False.
    """
    enrolments = open_enrolments()
    if enrolments is None:
        return False
    for e in enrolments:
        if e["Student ID"] == student_id and e["Course ID"] == course_id:
            return True
    return False

def open_grades():
    grades = []
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")
                if len(fields) < 7:
                    print("Skipping invalid line:", line.strip())
                    continue
                record = {
                    "student ID": fields[0].strip().upper(),
                    "course ID": fields[1].strip().upper(),
                    "assignment score": fields[2].strip(),
                    "exam score": fields[3].strip(),
                    "gpa": fields[4].strip(),
                    "feedback": fields[5].strip(),
                }
                grades.append(record)
        return grades
    except FileNotFoundError:
        print("Warning: 'grades.txt' not found.")
    return None

def save_grades(data):
    with open("grades.txt", "w") as f:
        for record in data:
            line = ",".join([
                record.get("student ID", "").strip().upper(),
                record.get("course ID", "").strip().upper(),
                record.get("assignment score", "").strip(),
                record.get("exam score", "").strip(),
                record.get("gpa", "").strip(),
                record.get("feedback", "").strip(),
            ])
            f.write(line + "\n")

def Grading_assignment_score():
    # Display current enrolments first.
    display_enrolments()
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student ID"] == student_id and record["course ID"] == course_id:
            found = True
            try:
                score = float(input("Enter assignment score (0-100): "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                return
            if not 0 <= score <= 100:
                print("Score must be between 0 and 100!")
                return
            record["assignment score"] = str(score)
            save_grades(data)
            print("Assignment score saved successfully.")
            print("You entered assignment score: {:.2f}%".format(score))
            break
    if not found:
        print("Record not found. Please check student ID and course ID.")

def Grading_exam_score():
    display_enrolments()
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student ID"] == student_id and record["course ID"] == course_id:
            found = True
            try:
                score = float(input("Enter exam score (0-100): "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                return
            if not 0 <= score <= 100:
                print("Score must be between 0 and 100!")
                return
            record["exam score"] = str(score)
            save_grades(data)
            print("Exam score saved.")
            print("You entered exam score: {:.2f}%".format(score))
            break
    if not found:
        print("Record not found. Please check student ID and course ID.")

def Grading_gpa():
    display_enrolments()
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student ID"] == student_id and record["course ID"] == course_id:
            found = True
            try:
                assignment = float(record.get("assignment score", 0))
                exam = float(record.get("exam score", 0))
            except ValueError:
                print("Existing score data is invalid!")
                return
            avg = (assignment + exam) / 2
            if avg >= 80:
                gpa = "4.0"
            elif avg >= 75:
                gpa = "3.7"
            elif avg >= 70:
                gpa = "3.3"
            elif avg >= 65:
                gpa = "3.0"
            elif avg >= 60:
                gpa = "2.7"
            elif avg >= 55:
                gpa = "2.3"
            elif avg >= 50:
                gpa = "2.0"
            else:
                gpa = "Fail"
            record["gpa"] = gpa
            save_grades(data)
            print("GPA calculated:", gpa)
            print("Calculated using assignment score: {} and exam score: {}".format(assignment, exam))
            input("Press Enter to continue...")
            break
    if not found:
        print("Record not found. Please check student ID and course ID.")

def Give_feedback():
    display_enrolments()
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student ID"] == student_id and record["course ID"] == course_id:
            found = True
            feedback = input("Enter feedback evaluation: ")
            record["feedback"] = feedback
            save_grades(data)
            print("Feedback evaluation saved.")
            print("You entered feedback:", feedback)
            break
    if not found:
        print("Record not found. Please check student ID and course ID.")

def Grade_and_Assessment_Menu():
    while True:
        print("\n------------------------------------------------------")
        print("--------- Grade and Assessment Menu ---------")
        print("------------------------------------------------------")
        print("1. Grade Assignment Score")
        print("2. Grade Exam Score")
        print("3. Calculate GPA")
        print("4. Give Feedback")
        print("5. Exit")
        print("------------------------------------------------------")
        try:
            opt = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Only integers 1-5 are allowed.")
            continue
        if opt == 1:
            Grading_assignment_score()
        elif opt == 2:
            Grading_exam_score()
        elif opt == 3:
            Grading_gpa()
        elif opt == 4:
            Give_feedback()
        elif opt == 5:
            print("Returning to teacher menu...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

# Run the Grade and Assessment Menu
# Grade_and_Assessment_Menu()
