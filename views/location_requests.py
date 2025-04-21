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


def create_location(location):
    """Function creating a single location to append to LOCATIONS list of dictionaries"""
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location


def delete_location(id):
    """Function deleting a single location from the LOCATIONS list of dictionaries"""
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
        if location_index >= 0:
            LOCATIONS.pop(location_index)
