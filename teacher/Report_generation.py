def open_grades():
    grades = []
    try:
        with open("grades.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")

                # Make sure there are at least 2 fields
                if len(fields) < 2:
                    print(f"Skipping invalid line: {line}")
                    continue

                # Create the grade entry from the first two fields
                grade_entry = {
                    "Student ID": fields[0],
                    "Grade": fields[1]
                }
                grades.append(grade_entry)
    except FileNotFoundError:
        print("Warning: grades.txt not found. Creating an empty file.")
        # Create an empty file if it doesn't exist (without using pass)
        with open("grades.txt", "w") as empty_file:
            empty_file.write("")  # effectively does nothing, just ensures file is created

    # Return the list of grade dictionaries
    return grades

def open_attendances():
    attendances = []
    try:
        with open("attendances.txt", "r") as file:
            for line in file:
                # Remove whitespace and split by comma
                fields = line.strip().split(",")
                # Ensure we have two fields: Student ID and Attendance
                attendance_entry = {"Student ID": fields[0], "Attendance": fields[1]}
                attendances.append(attendance_entry)
    except FileNotFoundError:
        # Return empty list if file not found
        print("Warning: attendances.txt not found. Creating an empty file.")
    return None

def save_attendances(attendances):
    with open("attendances.txt", "w") as file:
        for entry in attendances:
            file.write(f"{entry['Student ID']},{entry['Attendance']}\n")


def generation_performances(grades):
    print("=== Performance Report (Grades) ===")
    try:
        with open('grades.txt', 'r') as file:
            for line in file:
                fields = line.strip().split(",")

                # Check that we have at least 7 fields
                if len(fields) < 7:
                    print(f"Skipping invalid line: {line}")
                    continue

                tp_number = fields[0]
                course_id = fields[1]
                assignment_score = fields[2]
                exam_score = fields[3]
                gpa = fields[4]
                feedback = fields[5]
                performance = fields[6]

                # Format the output as desired
                print(f"TP Number: {tp_number}")
                print(f"Course ID: {course_id}")
                print(f"Assignment Score: {assignment_score}")
                print(f"Exam Score: {exam_score}")
                print(f"GPA: {gpa}")
                print(f"Feedback: {feedback}")
                print(f"Performance: {performance}")
                print("--------------------------------------------------")
    except FileNotFoundError:
        print("Error: grades.txt not found.")

def generation_participation(attendances):
        print("=== Participation Report (Attendances) ===")
        try:
            with open("attendances.txt", "r") as file:
                for line in file:
                    fields = line.strip().split(",")

                    # Ensure there are at least 2 fields: TP Number and Attendance
                    if len(fields) < 2:
                        print(f"Skipping invalid line: {line}")
                        continue

                    tp_number = fields[0]
                    attendance = fields[1]

                    # Format the output as desired
                    print(f"TP Number: {tp_number}")
                    print(f"Attendance: {attendance}")
                    print("--------------------------------------------------")
        except FileNotFoundError:
            print("Error: attendances.txt not found.")


def Report_Generation_Menu():
    while True:
        grades = open_grades()
        attendances = open_attendances()

        print("\n------------------------------------------------------")
        print("----------------Student Enrolment----------------------")
        print("------------------------------------------------------")
        print("1. generation grades")
        print("2. generation attendances")
        print("3. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Only integer 1- is allowed.")
            continue

        if opt == 1:
            generation_performances(grades)

        elif opt == 2:
            generation_participation(attendances)


        elif opt == 3:
            print("Returning to teacher manu")
            break

        else:
            print("Invalid choice, please enter a number between 1-3 .")

