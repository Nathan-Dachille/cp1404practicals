"""Project Management Exercise for Prac_07.
ESTIMATED TIME: 45
ACTUAL TIME: 2:00
"""

import csv
import datetime
from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Display Menu and Call appropriate function."""
    project_filename = input("Enter the project filename to load: ")
    projects = load_projects(project_filename)
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
            update_project(projects)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(project_filename):
    """Load projects to a list from a file."""
    projects = []
    with open(project_filename, 'r', newline='', encoding='utf-8') as in_file:
        in_file.readline()
        reader = csv.reader(in_file, delimiter='\t')
        for row in reader:
            date = datetime.datetime.strptime(row[1], "%d/%m/%Y").date()
            project = Project(row[0], date, int(row[2]), float(row[3]), int(row[4]))
            projects.append(project)
    return projects


def save_projects(project_filename, projects):
    """Load projects to a file from a list of projects."""
    with open(project_filename, 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        header = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
        writer.writerow(header)
        for project in projects:
            row = [project.name, project.start_date, project.priority,
                   project.cost_estimate, project.completion_percentage]
            writer.writerow(row)


def display_projects(projects):
    """Display projects and whether they are complete."""
    incomplete_projects = [project for project in projects if not project.is_completed()]
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed Projects:")
    completed_projects = [project for project in projects if project.is_completed()]
    for project in completed_projects:
        print(f"  {project}")


def filter_by_date(projects, date_string):
    """Display projects that start after a certain date."""
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.start_date > date:
            print(project)


def add_project(projects):
    """Add a valid project from user input."""
    print("Let's add a new project")
    name = input("Name: ")
    is_valid_date = False
    is_valid_priority = False
    is_valid_cost = False
    is_valid_completion = False
    while not is_valid_date:
        try:
            date_string = input("Start date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%mm/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Enter valid date.")
    while not is_valid_priority:
        try:
            priority = int(input("Priority: "))
            if priority >= 1:
                is_valid_priority = True
            else:
                print("Enter valid priority.")
        except TypeError:
            print("Enter valid priority.")
    while not is_valid_cost:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            if cost_estimate >= 0:
                is_valid_cost = True
            else:
                print("Enter valid cost estimate.")
        except TypeError:
            print("Enter valid cost estimate.")
    while not is_valid_completion:
        try:
            completion_percentage = int(input("Percent complete: "))
            if 0 < completion_percentage <= 100:
                is_valid_completion = True
            else:
                print("Enter valid completion percent.")
        except TypeError:
            print("Enter valid completion percent.")
    projects.append(Project(name, date, cost_estimate, completion_percentage))


def update_project(projects):
    """Update the priority and/or the completion percentage of a project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    is_valid_option = False
    is_valid_priority = False
    is_valid_completion = False
    while not is_valid_option:
        try:
            index = int(input("Project choice: "))
            if 0 < index <= len(projects) - 1:
                is_valid_option = True
            else:
                print("Enter valid choice.")
        except TypeError:
            print("Enter valid choice.")
    while not is_valid_priority:
        try:
            priority = input("New Priority: ")
            if priority == '':
                is_valid_priority = True
                break
            priority = int(priority)
            if priority >= 1:
                is_valid_priority = True
            else:
                print("Enter valid priority.")
        except TypeError:
            print("Enter valid priority.")
    while not is_valid_completion:
        try:
            completion_percentage = int(input("New Percentage: "))
            if 0 < completion_percentage <= 100:
                is_valid_completion = True
            else:
                print("Enter valid percentage")
        except TypeError:
            print("Enter valid percentage")
    if isinstance(priority, int):
        projects[index].priority = priority
    if isinstance(completion_percentage, int):
        projects[index].completion_percentage = completion_percentage


if __name__ == '__main__':
    main()
