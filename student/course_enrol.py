# student
def open_course():
    courses = []  # create an empty list to store student data
    with open("course.txt", 'r') as tFile:
        for line in tFile:
            line = line.rstrip().split(",")  # split each line become a list and remove whitespace
            while len(line) < 9:
                line.append("")
            # store each list in a dictionary
            course = {
                "Course ID": line[0],
                "Course Name": line[1],
                "Instructor": line[2],
                "Assignment": line[3],
                "Lecture Notes": line[4],
                "Announcement": line[5],
                "Overall Attendance": line[6],
                "Lesson Plan": line[7]
            }
            courses.append(course)  # add student dictionary to the list
    return courses

def open_students():
    students=[] #create an empty list to store student data
    with open("students.txt", 'r') as tFile:
        for line in tFile:
            line=line.rstrip().split(",") #split each line become a list and remove whitespace
            #set the limit of the append block inside the list
            while len(line)<9:
                line.append("")
            #store each list in a dictionary
            student = {
                "Student ID": line[0],
                "Name": line[1],
                "Email": line[2],
                "Contact": line[3],
                "Emergency Contact": line[4],
                "Gender":line[5],
                "Student Status":line[6],
                "Tuition Fees":line[7],
                "Payment":line[8]
            }
            students.append(student) #add student dictionary to the list
    return students #return the list containing student dictionary

def open_enrolments():
    enrolments = []  # create an empty list to store student data
    with open("enrolments.txt", 'r') as tFile:
        for line in tFile:
            line = line.rstrip().split(",")  # split each line become a list and remove whitespace
            while len(line) < 3:
                line.append("")
            # store each list in a dictionary
            enrolment = {
                "Student ID": line[0],
                "Course ID": line[1]
            }
            enrolments.append(enrolment) # add student dictionary to the list
    return enrolments

def update_enrolments(enrolled):
    with open("enrolments.txt", "w") as file:
        for enrol in enrolled:
            file.write(",".join([
                enrol["Student ID"],
                enrol["Course ID"],
            ]) + "\n")

def course_enrolment_menu():
    while True:
        print("\n-------------------------------------")
        print("--------Course Enrolment Menu--------")
        print("-------------------------------------")
        print("1. Browse Available Courses")
        print("2. Enrol in a Course")
        print("3. View Enrolled Course")
        print("4. Exit")
        print("------------------------------------")

        opt = int(input("Enter your choice (1/2/3): "))
        try:
            if opt == 1:
                browse_course()
            elif opt == 2:
                enrol_in_course()
            elif opt == 3:
                view_enrol_course()
            elif opt == 4:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please only Enter (1/2/3)")

def browse_course():

    courses = open_course()
    print("")
    title = "Available Courses"
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)

    for course in courses:
        print(f"Course ID: {course["Course ID"]} Course Name: {course["Course Name"]}")
        print("=" * width)
    input("Enter to continue...")

def enrol_in_course():
    students = open_students()
    courses = open_course()
    enrolled = open_enrolments()

    tp_number = input("\nEnter your TP number: ").upper()

    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break  # stop when found student id
    if student_found:
        browse_course()
        print("student ID founded")

        course_id = input("Enter the Course ID you want to enrol in: ").upper()
        course_found = None
        for course in courses:
            if course["Course ID"] == course_id:
                course_found = course
                break # stop when course id found

        if course_found:
            for enrol in enrolled:
                if enrol["Student ID"] == tp_number and enrol["Course ID"] == course_id:
                    input(f"Student {tp_number} is already enrolled in {course_id}.")
                    return

            enrolled.append({"Student ID": tp_number, "Course ID": course_id})
            update_enrolments(enrolled)

            input(f"Student {tp_number} enrolled in {course_id} successfully!")

        else:
            print("Course ID not found")
    else:
        print("Student ID not found")

def view_enrol_course():
    students = open_students()
    enrolments = open_enrolments()
    tp_number = input("\nEnter your TP number: ").upper()

    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break  # stop when found student id

    if student_found:
        enrolled_course = []
        for enrolment in enrolments:
            if enrolment["Student ID"] == tp_number:
                enrolled_course.append(enrolment["Course ID"])

        if enrolled_course:
            print(f"\nCourses enrolled by {tp_number}:")
            for course_id in enrolled_course:
                print(f"  - {course_id}")

        else:
            print(f"Student {tp_number} is not enrolled in any courses.")
    else:
        print("Student ID not found.")
    input("\npress enter to continue...")


#course_enrolment_menu()