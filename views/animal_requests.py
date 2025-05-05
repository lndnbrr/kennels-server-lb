import json
import sqlite3
from models import Animal, Location, Customer

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "breed": "Dog",
        "location_id": 1,
        "customer_id": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "breed": "Dog",
        "location_id": 1,
        "customer_id": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "breed": "Cat",
        "location_id": 2,
        "customer_id": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    '''Function that connects to database, performs a SELECT SQL query, 
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
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer,
            c.address cus_address,
            c.email,
            c.password
        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            on c.id = a.customer_id
        """)

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            location = Location(row['id'], row['location_name'],
                                row['location_address'])

            customer = Customer(row['id'], row['customer'],
                                row['cus_address'],
                                row['email'],
                                row['password'])

            animal.location = location.__dict__
            animal.customer = customer.__dict__

            animals.append(animal.__dict__)

    return animals


def get_single_animal(id):
    '''Function that connects to database, performs a SELECT SQL query based on 
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


def create_animal(new_animal):
    """Function creating a single animal to append to ANIMALS list of dictionaries"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'],
              # locationId matches with frontend, while location_id matches with backend.
              new_animal['locationId'],
              # customerId matches with frontend, while customer_id matches with backend.
              new_animal['customerId'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_animal['id'] = id


    return new_animal


    # # Get the id value of the last animal in the list
    # max_id = ANIMALS[-1]["id"]

    # # Add 1 to whatever that number is
    # new_id = max_id + 1

    # # Add an `id` property to the animal dictionary
    # animal["id"] = new_id

    # # Add the animal dictionary to the list
    # ANIMALS.append(animal)

    # # Return the dictionary with `id` property added
    # return animal


def delete_animal(id):
    '''Function that connects to database and performs a DELETE SQL query based on matching id'''

    with sqlite3.connect("./kennel.sqlite3") as conn:
        an_cursor = conn.cursor()

        an_cursor.execute('''
        DELETE FROM animal
        WHERE id = ?
        ''', (id, ))


def update_animal(id, new_animal):
    '''Function that connects to database, performs an UPDATE SQL query based on matching id, 
    grabs changes based on new_animal and replaces the values'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_animal_by_location(location_id):
    '''Function that connects to database, performs a SELECT SQL query with the 
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
    '''Function that connects to database, performs a SELECT SQL query with the 
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
