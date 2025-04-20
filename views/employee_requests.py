EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Jacob Whinehouse"
    },
    {
        "id": 3,
        "name": "Steve Combs"
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
