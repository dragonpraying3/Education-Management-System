def open_grades():
    grades=[]
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                line = line.rstrip().split(",")
                detail={
                    "student id" : line[0],
                    "course id" : line[1],
                    "assignment grades": line[2],
                    "exam grades" : line[3],
                    "gpa" : line[4],
                    "feedback" : line[5],
                    "performance" : line[6]
                }
                grades.append(detail)
            return grades
    except FileNotFoundError:
        print("Warning: 'grades.txt' not found. ")
    return None  # return an empty list is file is missing

def save_grades(data):
    with open("grades.txt", "w") as f:
        for record in data:
            f.write(",".join([
                record.get("username", "").strip().upper(),
                record.get("course_id", "").strip().upper(),
                record.get("assignment_score", "").strip(),
                record.get("exam_score", "").strip(),
                record.get("gpa", "").strip(),
                record.get("performance", "").strip()
            ]) + "\n")

def Grading_assignment_score():
    username = input("Enter username: ").strip().upper()
    course_id = input("Enter course id: ").strip().upper()

    data = open_grades()

    if not data:
        print("No data found in file.")
        return

    found = False
    for record in data:
        # Compare stripped values to avoid whitespace issues
        if record["username"].strip() == username and record["course_id"].strip() == course_id:
            found = True
            try:
                score = float(input("Enter assignment score (0-100): "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                return
            if score < 0 or score > 100:
                print("Score must be between 0 and 100!")
                return

            # Correct key: "assignment_score"
            record["assignment_score"] = str(score)
            save_grades(data)
            print("Assignment score saved successfully.")
            break

    if not found:
        print("Record not found. Please check username and course ID.")

def Grading_exam_score():
    username = input("Enter username: ").strip().upper()
    course_id = input("Enter course id: ").strip().upper()
    data = open_grades()

    if not data:
        print("No data found in file.")
        return

    found = False
    for record in data:
        if record["username"].strip() == username and record["course_id"].strip() == course_id:
            found = True
            try:
                score = float(input("Enter exam score (0-100): "))
            except ValueError:
                print("Invalid input!")
                return
            if score < 0 or score > 100:
                print("Score must be between 0 and 100!")
                return

            record["exam_score"] = str(score)
            save_grades(data)
            print("Exam score saved.")
            break

    if not found:
        print("Record not found.")

def Grading_gpa():
    username = input("Enter username: ").strip().upper()
    course_id = input("Enter course id: ").strip().upper()
    data = open_grades()

    if not data:
        print("No data found in file.")
        return

    found = False
    for record in data:
        if record["username"].strip() == username and record["course_id"].strip() == course_id:
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
            input("Press space to continue")
            break

    if not found:
        print("Record not found.")

def Give_feedback():
    username = input("Enter username: ").strip().upper()
    course_id = input("Enter course id: ").strip().upper()
    data = open_grades()

    if not data:
        print("No data found in file.")
        return

    found = False
    for record in data:
        if record["username"].strip() == username and record["course_id"].strip() == course_id:
            found = True
            feedback = input("Enter feedback evaluation: ")
            record["performance"] = feedback  # or "feedback" if you prefer
            save_grades(data)
            print("Feedback evaluation saved.")
            break

    if not found:
        print("Record not found.")

def Grade_and_Assessment_Menu():
    while True:
        print("\n------------------------------------------------------")
        print("---------Grade and Assessment----------")
        print("------------------------------------------------------")
        print("1. Grading Assignment score")
        print("2. Grading Exam score ")
        print("3. Grading GPA")
        print("4. Give feedback")
        print("5. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Only integer 1-5 is allowed.")
            continue

        if opt == 1:
            Grading_exam_score()
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
            print("Invalid choice, please enter a number between 1-5.")

