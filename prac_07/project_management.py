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
        print(f"\t{project}")
    print("Completed Projects:")
    completed_projects = [project for project in projects if project.is_completed()]
    for project in completed_projects:
        print(f"\t{project}")


if __name__ == '__main__':
    main()
