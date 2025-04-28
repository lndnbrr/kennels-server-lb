import json
import sqlite3
from models import Customer 


CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "address": "24 Bryant Street Oakland, CA",
        "email": "RyTry@yahoo.com",
        "password": "pintolenTlzz20fo"
    },
    {
        "id": 2,
        "name": "Tyler Braxwort",
        "address": "314 Pi Dr Hell, MI",
        "email": "TBrax@yahoo.com",
        "password": "Ih8M@H!!!"
    },
    {
        "id": 3,
        "name": "Lucy Jenkins",
        "address": "2034 Smoky Ln Nashville, TN",
        "email": "oljenkins@hotmail.com",
        "password": "LEROYYYYYJENKINSSSSS"
    },
    {
        "id": 4,
        "name": "Richard Scott",
        "address": "13 Office Rd Scranton, PA",
        "email": "rickovermike@gmail.com",
        "password": "&dundEwinner1994!"
    }
]


def get_all_customers():
    '''Function that connects to database, performs an SQL query, 
    creates customer instances, appends new instances to new customers 
    list of dictionaries, returns new customers list when called'''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        cus_cursor = conn.cursor()
        cus_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        customers = []
        dataset = cus_cursor.fetchall()
        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'],
                                row['email'], row['password'])
            customers.append(customer.__dict__)

    return customers


def get_single_customer(id):
    '''Function that connects to database, performs an SQL query based on 
    matching id, creates an customer instance for that customer and returns that new 
    instance when called with a specific id'''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        cus_cursor = conn.cursor()

        cus_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id=?
        """,(id,))

        data = cus_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'],
                                 data['email'], data['password'])

    return customer.__dict__


def create_customer(customer):
    """Function creating a single customer to append to CUSTOMERS list of dictionaries"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer


def delete_customer(id):
    """Function deleting a customer from CUSTOMERS list of dictionaries"""
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
        if customer_index >= 0:
            CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """Function updating a customer from CUSTOMERS list of dictionaries"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer


# TODO: you will get an error about the address on customer.
# Look through the customer model and requests to see if you can solve the issue.

def get_customer_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers
