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
