EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis",
        "years_employed": 4,
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Jacob Whinehouse",
        "years_employed": 2,
        "location_id": 2
    },
    {
        "id": 3,
        "name": "Steve Combs",
        "years_employed": 1,
        "location_id": 1
    }
]

def get_all_employees():
    """Function returing EMPLOYEES list of dictionaries"""
    return EMPLOYEES

def get_single_employee(id):
    """Function returing a single employee from the EMPLOYEES list of dictionaries"""
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
            return requested_employee

def create_employee(employee):
    """Function creating an employee to append to EMPLOYEES list of dictionaries"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    """Function deleting an employee from EMPLOYEES list of dictionaries"""
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
        if employee_index >= 0:
            EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """Function updating an employee from EMPLOYEES list of dictionaries"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
