import json
import sqlite3
from models import Animal

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "breed": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "breed": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "breed": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    '''Function that connects to database, performs an SQL query, 
    creates animal instances, appends new instances to new animals 
    list of dictionaries, returns new animals list when called'''
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """)

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    return animals


def get_single_animal(id):
    '''Function that connects to database, performs an SQL query based on 
    matching id, creates an animal instance for that animal and returns that new 
    instance when called with a specific id'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

    return animal.__dict__


def create_animal(animal):
    """Function creating a single animal to append to ANIMALS list of dictionaries"""
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    '''Function that connects to database and performs a DELETE SQL query based on matching id'''

    with sqlite3.connect("./kennel.sqlite3") as conn:
        an_cursor = conn.cursor()

        an_cursor.execute('''
        DELETE FROM animal
        WHERE id = ?
        ''', (id, ))


def update_animal(id, new_animal):
    """Function updating a single animal from ANIMALS list of dictionaries"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break

def get_animal_by_location(location_id):
    '''Function that connects to database, performs an SQL query with the 
    condition that the location_id matches the param location_id, 
    creates animal instances, appends new instances to new animals 
    list of dictionaries, returns new animals list when called'''
    with sqlite3.connect('./kennel.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        an_lo_cursor = conn.cursor()

        an_lo_cursor.execute("""
        SELECT 
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.location_id=?          
        """, (location_id,))

        animals = []
        dataset = an_lo_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return animals

def get_animals_by_status(status):
    '''Function that connects to database, performs an SQL query with the 
    condition that the status matches the param status, 
    creates animal instances, appends new instances to new animals 
    list of dictionaries, returns new animals list when called'''
    with sqlite3.connect('./kennel.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        an_st_cursor = conn.cursor()
        an_st_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = an_st_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)
    return animals
