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
            projects = load_projects(project_filename)
        elif choice == "S":
            project_filename = input("Enter the project filename to save: ")
            save_projects(project_filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            filter_by_date(projects, date_string)
        elif choice == "A":
            add_project(projects)
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
    return projects


def save_projects(project_filename, projects):
    with open(project_filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        header = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
        writer.writerow(header)
        for project in projects:
            row = [project.name, project.start_date, project.priority,
                   project.cost_estimate, project.completion_percentage]
            writer.writerow(row)


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed Projects:")
    completed_projects = [project for project in projects if project.is_completed()]
    for project in completed_projects:
        print(f"  {project}")


def filter_by_date(projects, date_string):
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > date:
            print(project)


def add_project(projects):
    print("Let's add a new project")
    (name, date, cost, completion) = get_valid_project(None)
    projects.append(Project(name, date, cost, completion))


def get_valid_project(new: None):
    name = input(f"{new}Name: ")
    is_valid_date = False
    is_valid_priority = False
    is_valid_cost = False
    is_valid_completion = False
    while not is_valid_date:
        try:
            date_string = input(f"{new}Start date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%mim/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Enter valid date.")
    while not is_valid_priority:
        try:
            priority = int(input(f"{new}Priority: "))
            if priority >= 1:
                is_valid_priority = True
        except TypeError:
            print("Enter valid priority.")
    while not is_valid_cost:
        try:
            cost_estimate = float(input(f"{new}Cost estimate: $"))
            if cost_estimate >= 0:
                is_valid_cost = True
        except TypeError:
            print("Enter valid cost.")
    while not is_valid_completion:
        try:
            completion_percent = int(input(f"{new}Percent complete: "))
            if 0 < completion_percent <= 100:
                is_valid_completion = True
        except TypeError:
            print("Enter valid completion percent.")
    return name, date, priority, completion_percent


if __name__ == '__main__':
    main()
