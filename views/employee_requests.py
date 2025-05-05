import json
import sqlite3
from models import Employee, Location


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
    '''Function that connects to database, performs a SELECT SQL query, 
    creates employee instances, appends new instances to new employees 
    list of dictionaries, returns new employees list when called'''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        empl_cursor = conn.cursor()

        empl_cursor.execute("""
        SELECT 
            e.id,
            e.name,
            e.years_employed,
            e.location_id,
            l.name loc_name,
            l.address
        FROM employee e
        JOIN location l
            ON l.id = e.location_id
        """)

        employees = []

        dataset = empl_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['years_employed'], row['location_id'])

            location = Location(row['id'], row['loc_name'],
                                row['address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees


def get_single_employee(id):
    '''Function that connects to database, performs a SELECT SQL query based on 
    matching id, creates an employee instance for that employee and returns that new 
    instance when called with a specific id'''

    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        emp_cursor = conn.cursor()
        emp_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.years_employed,
            e.location_id
        FROM employee e
        WHERE e.id=?
        """,(id, ))

        data = emp_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['years_employed'], data['location_id'])

    return employee.__dict__


def create_employee(employee):
    """Function creating an employee to append to EMPLOYEES list of dictionaries"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_employee(id):
    """Function deleting an employee from EMPLOYEES list of dictionaries"""

    with sqlite3.connect("./kennel.sqlite3") as conn:
        emp_cursor = conn.cursor()

        emp_cursor.execute('''
        DELETE FROM employee
        WHERE id = ?
        ''', (id, ))


def update_employee (id, employee_updates):
    '''Function that connects to database, performs an UPDATE SQL query based on matching id, 
    grabs changes based on employee_updates and replaces the values'''
    with sqlite3.connect ("./kennel.sqlite3") as conn:
        new_emp_cursor = conn.cursor()

        new_emp_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                years_employed = ?,
                location_id = ?
        WHERE id = ?
        """, (employee_updates['name'], employee_updates['years_employed'],
              employee_updates['location_id'], id, ))

        rows_affected = new_emp_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def get_employee_by_location(location_id):
    '''Function that connects to database, performs a SELECT SQL query with the 
    condition that the location_id matches the param location_id, 
    creates employee instances, appends new instances to new employees 
    list of dictionaries, returns new employees list when called'''
    with sqlite3.connect('./kennel.sqlite3') as conn:

        conn.row_factory = sqlite3.Row
        em_lo_cursor = conn.cursor()

        em_lo_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.years_employed,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, (location_id,))

        employees = []
        dataset = em_lo_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['years_employed'], row['location_id'])

            employees.append(employee.__dict__)
    return employees
        