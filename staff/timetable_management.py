from datetime import datetime

def convert_time(time): #convert time format for easy comparison
    return datetime.strptime(time,'%H:%M')
SCHEDULE_PATH=r"C:\Users\User\PycharmProjects\Assignment\git\chloride33-\assets\schedule.txt"
def open_timetable():
    schedule=[]
    try:
        with open(SCHEDULE_PATH,'r')as hFile:
            for row in hFile:
                row=row.rstrip().split(",")
                item={
                    "Course ID":row[0],
                    "Day":row[1],
                    "Time Slot":row[2],
                    "Instructor":row[3],
                    "Venue":row[4]
                }
                schedule.append(item)
            return schedule
    except FileNotFoundError:
        raise FileNotFoundError("Error: schedule.txt not found.")

def open_teacher():
    teachers=[]
    try:
        with open("assets/teachers.txt",'r')as instructor:
            for column in instructor:
                column=column.rstrip().split(",")
                item={
                    "Course ID":column[0],
                    "Day": column[1],
                    "Instructor":column[2],
                    "Office Hours":column[3]
                }
                teachers.append(item)
            return teachers
    except FileNotFoundError:
        raise FileNotFoundError("Error: teachers.txt not found. Returning empty list")

def update_timetable():
    schedule=open_timetable()
    print()
    print("-"*60,"Current Timetable","-"*60)
    index=1
    with open("./assets/schedule.txt",'w')as hFile:
        for item in schedule:
            hFile.write(",".join(item.values())+"\n")
            print(f"{index}. Course ID:{item['Course ID']}\t\tDay:{item['Day']}\t\tTime Slot:{item['Time Slot']}\t\tInstructor:{item['Instructor']}\t\tVenue:{item['Venue']}")
            print("-"*150)
            index+=1

def update_teachers():
    teachers=open_teacher()
    print()
    print("-" * 40, "Instructors Official Hours", "-" * 40)
    with open("assets/teachers.txt", 'w') as instructor:
        for item in teachers:
            instructor.write(",".join(item.values()) + "\n")
            print(f"Course ID:{item['Course ID']}\t\tDay:{item['Day']}\t\tInstructor:{item['Instructor']}\t\tOffice Hours:{item['Office Hours']}")
            print("-" * 100)

def edit_schedule():
    schedule=open_timetable()
    teachers=open_teacher()
    while True:
        print("-"*40,"Action Menu","-"*40)
        print("1. Scheduling Class")
        print("2. Rescheduling Class")
        print("3. Exit")

        try:
            option=int(input("Enter your option:"))
            if option==1:
                update_timetable()
                bil=int(input("Enter line number need to schedule:"))
                if 1<= bil<=len(schedule):
                    real_bil = bil - 1
                    if schedule[real_bil]['Time Slot'] == " ":
                        scheduling=input("Enter the time slot of the class schedule in 24 hours method (eg. 12.00-14.00):")
                        schedule[real_bil]['Time Slot']=scheduling

                        with open("./assets/schedule.txt", 'w') as hFile:
                            for item in schedule:  # write the entire schedule back to the schedule.txt
                                hFile.write(",".join(item.values()) + "\n")

                    else:
                        print("The schedule selected already have time slot. Please select Rescheduling Class if wanted.\n")
                        continue
                else:
                    print("The line number was not in the timetable.")
                update_timetable()
            elif option==2:
                update_timetable()
                print("")
                update_teachers()
                bil = int(input("Enter line number of the timetable need to reschedule:"))
                if 1 <= bil <= len(schedule):
                    real_bil = bil - 1
                    selected_class=schedule[real_bil]
                    instructor_name=selected_class['Instructor']
                    class_day=selected_class['Day']

                    found=False
                    for teacher in teachers:
                        if teacher['Instructor']==instructor_name and teacher['Day']==class_day:
                            time_start,time_end=teacher['Office Hours'].split("-")
                            new_start, new_end = input("Enter new time (HH:MM-HH:MM): ").split("-")

                            if convert_time(time_start)<=convert_time(new_start)<=convert_time(time_end) and convert_time(time_start)<=convert_time(new_end)<=convert_time(time_end):
                                schedule[real_bil]['Time Slot']=f"{new_start}-{new_end}"
                                print("Reschedule successful!")


                                with open("./assets/schedule.txt", 'w') as hFile:
                                    for item in schedule:  # write the entire schedule back to the schedule.txt
                                        hFile.write(",".join(item.values()) + "\n")
                                update_timetable()
                                found=True
                                break
                            else:
                                print("Error:New time slot is outside the instructor's available hours.")
                                break
                        else:
                            print("The instructor not found.\n")
                    if not found:
                        print("The line number enter is not in the list.")
                else:
                    print("The line number was not in the timetable.")
            elif option==3:
                print("Exiting the page...")
                break
            else:
                print("Please enter number 1-3 only.")
        except ValueError:
            print("Invalid option. Please enter only integer.")

def timetable_menu():
    while True:
        print("")
        title = "Timetable Management Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View Class Schedule")
        print("2. Edit Schedule In Timetable")
        print("3. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                update_timetable()
            elif choose==2:
                edit_schedule()
            elif choose==3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

# timetable_menu()
