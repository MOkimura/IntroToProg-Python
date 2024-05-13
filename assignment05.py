# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Michael Okimura, 05/13/2024, Created Script
# ------------------------------------------------------------------------------------------ #

from sys import exit
import csv

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
column_names: str  # Column headers for the dictionary table.
file_rows: list  # Rows of data stored in the csv file.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
def file_read():
    try:
        with open(FILE_NAME, "r") as file:
            column_names = ("Student First Name", "Student Last Name", "Course Name")
            file_rows = csv.DictReader(file, fieldnames=column_names)
            for row in file_rows:
                students.append(row)
    except FileNotFoundError:
        print("ERROR: Unable to load database!")


# Menu choice 1
def user_data_input():
    try:
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        if not student_first_name or not student_last_name or not course_name:
            raise ValueError()
        else:
            new_data = {
                "Student First Name": student_first_name,
                "Student Last Name": student_last_name,
                "Course Name": course_name
            }
            students.append(new_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
    except ValueError:
        print("ERROR: Cannot enter blank information!\n")
        user_data_input()

# Menu choice 2
def show_current_data():
    print("-"*50)
    for student in students:
        print(f"{student["Student First Name"]} {student["Student Last Name"]} {student["Course Name"]}")
    print("-"*50)

# Menu choice 3
def save_data():
    column_names = ("Student First Name", "Student Last Name", "Course Name")
    with open(FILE_NAME, "w") as file:
        try:
            file_rows = csv.DictWriter(file, fieldnames=column_names)
            file_rows.writerows(students)
            print("New user(s) info added!")
        except KeyError:
            print("ERROR: Unable to locate Key")

# Menu choice 4
def exit_program():
    print("Program Ended")
    exit()

# Invalid menu selection
def invalid_menu_selection():
    print("Please only choose option 1, 2, 3, or 4")

# Start of program execution
if __name__ == "__main__":
    file_read()

    # Present and Process the data
    while (True):
        print(MENU)
        menu_choice = input("What would you like to do: ")
        match menu_choice:

            # Input user data
            case "1":
                user_data_input()
                
            # Present the current data
            case "2":
                show_current_data()

            # Save the data to a file
            case "3":
                save_data()
                
            # Stop the program
            case "4":
                exit_program()

            # If any input other than the menu option is selected
            case _:
                invalid_menu_selection()   