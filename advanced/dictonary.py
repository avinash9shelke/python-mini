employees = {
    "E001": {"name": "Avinash Shelke", "role": "Staff Software Engineer", "location": "Pune"},
    "E002": {"name": "Sanchita Kulkarni", "role": "Engineering Manager", "location": "Mumbai"},
    "E003": {"name": "Mokshada Wadhwani", "role": "Director of Engineering", "location": "Bangalore"}
}


# Function to display all employees
def display_employees():
    for emp_id, details in employees.items():
        print(f"{emp_id}: {details['name']} - {details['role']} ({details['location']})")


# Function to add a new employee
def add_employee(emp_id, name, role, location):
    if emp_id in employees:
        print(f"Employee ID {emp_id} already exists.")
    else:
        employees[emp_id] = {"name": name, "role": role, "location": location}
        print(f"Added {name} to the directory.")


#Function to update an employee's role
def update_role(emp_id, new_role):
    if emp_id in employees:
        employees[emp_id]["role"] = new_role
        print(f"Updated role for {employees[emp_id]['name']} to {new_role}.")
    else:
        print(f"Employee ID {emp_id} not found.")


#Function to remove an employee
def remove_employee(emp_id):
    if emp_id in employees:
        removed = employees.pop(emp_id)
        print(f"Removed {removed['name']} from the directory.")
    else:
        print(f"Employee ID {emp_id} not found.")


# Example usage
display_employees()
add_employee("E004", "Ravi Deshmukh", "QA Engineer", "Hyderabad")
update_role("E001", "Principal Engineer")
remove_employee("E002")


