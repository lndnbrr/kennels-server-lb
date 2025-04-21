CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "name": "Tyler Braxwort"
    },
    {
        "id": 3,
        "name": "Lucy Jenkins"
    },
    {
        "id": 4,
        "name": "Richard Scott"
    }
]

def get_all_customers():
    """Function returing CUSTOMERS list of dictionaries"""
    return CUSTOMERS

def get_single_customer(id):
    """Function returing a single customer from the CUSTOMERS list of dictionaries"""

    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

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
