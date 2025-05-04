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
    '''Function that connects to database, performs a SELECT SQL query, 
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
    '''Function that connects to database, performs a SELECT SQL query based on 
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
    '''Function that connects to database and performs a DELETE SQL query based on matching id'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        del_loc_cursor = conn.cursor()

        del_loc_cursor.execute("""
        DELETE FROM Location
        WHERE id = ?
        """, (id, ))


def update_location (id, location_updates):
    '''Function that connects to database, performs an UPDATE SQL query based on matching id, 
    grabs changes based on location_updates and replaces the values'''
    with sqlite3.connect ("./kennel.sqlite3") as conn:
        new_loc_cursor = conn.cursor()

        new_loc_cursor.execute("""
        UPDATE Location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (location_updates['name'],location_updates['address'], id, ))

        rows_checked = new_loc_cursor.rowcount

    if rows_checked == 0:
        return False
    else:
        return True
