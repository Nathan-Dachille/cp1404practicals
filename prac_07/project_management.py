"""Project Management Exercise for Prac_07.
ESTIMATED TIME: 45
ACTUAL TIME:
"""

import csv
from project import Project
import datetime

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            project_filename = input("Enter the project filename to load: ")
            load_projects(project_filename)
        elif choice == "S":
            # SAVE
            pass
        elif choice == "D":
            # Display
            pass
        elif choice == "F":
            # Filter
            pass
        elif choice == "A":
            # Add
            pass
        elif choice == "U":
            # Update
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def load_projects(project_filename):
    projects = []
    with open(project_filename, 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file, delimiter='\t')
        for row in reader:
            date = datetime.datetime.strptime(row[1], "%d/%m/%Y").date()
            project = Project(row[0], date, int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)

