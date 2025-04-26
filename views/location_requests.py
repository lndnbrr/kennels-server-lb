import json
import sqlite3
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike",
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive",
    }
]


def get_all_locations ():
    '''Function that connects to database, performs an SQL query, 
    creates location instances, appends new instances to new locations 
    list of dictionaries, returns new locations list when called'''
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        loc_cursor = conn.cursor()
        loc_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        locations = []
        dataset = loc_cursor.fetchall()
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)

    return locations


def get_single_location(id):
    '''Function that connects to database, performs an SQL query based on 
    matching id, creates an location instance for that location and returns that new 
    instance when called with a specific id'''

    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        loc_cursor = conn.cursor()
        loc_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id=?
        """, (id,))

        data = loc_cursor.fetchone()
        location = Location(data['id'], data['name'], data['address'])

    return location.__dict__


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


def update_location (id, new_location):
    """Function updating a single location from the LOCATIONS list of dictionaries"""
    for index, location in enumerate(LOCATIONS):
        if location["id"]==id:
            LOCATIONS[index] = new_location
        break
