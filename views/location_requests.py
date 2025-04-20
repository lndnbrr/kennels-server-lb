LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations ():
    """Function returing the LOCATIONS list of dictionaries"""
    return LOCATIONS

def get_single_location (id):
    """Function returing a single location from the LOCATIONS list of dictionaries"""
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location
