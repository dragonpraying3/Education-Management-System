def open_attendances():
    """
    Reads attendances.txt and returns a dictionary where:
    - Key: 'username'
    - Value: 'attendance'
    """
    attendances = []
    try:
        with open("attendances.txt", 'r') as vFile:
            for line in vFile:
                line = line.rstrip().split(",")  # remove whitespace and split each line become a list
                # store each list in a dictionary with index label
                program = {
                    "Username": line[0],
                    "Attendances": line[1],
                }
                attendances.append(program)  # add each event program to the events list
            return attendances
    except FileNotFoundError:
        print("Warning: 'attendances.txt' not found. ")
    return None  # return an empty list is file is missing

def save_attendances(attendances):
    with open("attendances.txt", "w") as f:
        for e in attendances:
            f.write(f"{e['Username']},"
                    f"{e['Attendances']}\n")

def upload_attendances():
    attendances = open_attendances()

    # Prompt for a new username until it is unique
    while True:
        username = input("Enter a new student username: ").strip().upper()
        # Check if user already exists
        user_exists = any(record["Username"] == username for record in attendances)
        if user_exists:
            print("Error: That username already exists. Please try again.")
        else:
            break

    # Prompt for attendance until the format is correct
    while True:
        status = input("Enter attendance (e.g., 12/100): ").strip()
        parts = status.split('/')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            break
        else:
            print("Invalid attendance format. Please enter in the format 12/100.")

    # Add the new record to the list
    attendances.append({"username": username, "attendance": status})

    # Write the updated list to the file
    with open("attendances.txt", "w") as vFile:
        for rec in attendances:
            vFile.write(f"{rec['username']},{rec['attendance']}\n")

    print("Attendance record updated successfully.")
    print(f"New record added: {username} - {status}")

def Attendance_Tracking_Menu():
    """
    A simple menu loop:
    1) Check attendance by entering a username
    2) Exit
    """
    while True:
        print("\n----------- Attendance System Menu -----------")
        print("1) upload_attendances")
        print("2) Exit")

        choice = input("Please choose (1-2): ").strip()
        if choice == '1':
            upload_attendances()
        elif choice == '2':
            print("Program terminated.")
            break
        else:
            print("Invalid input, please choose 1 or 2.\n")

Attendance_Tracking_Menu()

