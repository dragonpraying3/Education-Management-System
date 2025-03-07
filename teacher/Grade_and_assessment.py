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
        return enrolments
    except FileNotFoundError:
        print("Warning: enrolments.txt not found.")
    return None

def verify_enrollment(student_id, course_id):
    enrolments = open_enrolments()
    if enrolments is None:
        return
    for e in enrolments:
        print(f"Comparing stored: {e['Student ID']} with input: {student_id}")
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

def save_grades(data):
    with open("grades.txt", "w") as f:
        for record in data:
            line = ",".join([
                record.get("student_id", "").strip().upper(),
                record.get("course_id", "").strip().upper(),
                record.get("assignment_score", "").strip(),
                record.get("exam_score", "").strip(),
                record.get("gpa", "").strip(),
                record.get("feedback", "").strip(),
                record.get("performance", "").strip()
            ])
            f.write(line + "\n")

def Grading_assignment_score():
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    # Verify enrollment
    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            found = True
            try:
                score = float(input("Enter assignment score (0-100): "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                return
            if score < 0 or score > 100:
                print("Score must be between 0 and 100!")
                return

            record["assignment_score"] = str(score)
            save_grades(data)
            print("Assignment score saved successfully.")
            print(f"You entered assignment score: {score}")
            break

    if not found:
        print("Record not found. Please check student ID and course ID.")

def Grading_exam_score():
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    # Verify enrollment
    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return
    found = False
    for record in data:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            found = True
            try:
                score = float(input("Enter exam score (0-100): "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                return
            if score < 0 or score > 100:
                print("Score must be between 0 and 100!")
                return

            record["exam_score"] = str(score)
            save_grades(data)
            print("Exam score saved.")
            print(f"You entered exam score: {score}")
            break

    if not found:
        print("Record not found.")

def Grading_gpa():
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    # Verify enrollment
    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            found = True
            try:
                assignment = float(record.get("assignment_score", 0))
                exam = float(record.get("exam_score", 0))
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
            print(f"Calculated using assignment score: {assignment} and exam score: {exam}")
            input("Press Enter to continue...")
            break

    if not found:
        print("Record not found.")

def Give_feedback():
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    # Verify enrollment
    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    found = False
    for record in data:
        if record["student_id"] == student_id and record["course_id"] == course_id:
            found = True
            feedback = input("Enter feedback evaluation: ")
            record["feedback"] = feedback
            save_grades(data)
            print("Feedback evaluation saved.")
            print(f"You entered feedback: {feedback}")
            break

    if not found:
        print("Record not found.")

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
            print("Invalid input! Only integer 1-5 is allowed.")
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
