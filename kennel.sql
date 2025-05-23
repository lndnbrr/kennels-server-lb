CREATE TABLE `Location` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
);

CREATE TABLE `Customer` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);


CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
  `years_employed` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);



  INSERT INTO `Location` VALUES (null, 'Nashville North', "64 Washington Heights");
  INSERT INTO `Location` VALUES (null, 'Nashville South', "101 Penn Ave");


  INSERT INTO `Customer` VALUES (null, "Mo Silvera", "201 Created St", "mo@silvera.com", "password");
  INSERT INTO `Customer` VALUES (null, "Bryan Nilsen", "500 Internal Error Blvd", "bryan@nilsen.com", "password");
  INSERT INTO `Customer` VALUES (null, "Jenna Solis", "301 Redirect Ave", "jenna@solis.com", "password");
  INSERT INTO `Customer` VALUES (null, "Emily Lemmon", "454 Mulberry Way", "emily@lemmon.com", "password");


  INSERT INTO `Employee` VALUES (null, "Madi Peper", "35498 Madison Ave", 1, 2);
  INSERT INTO `Employee` VALUES (null, "Kristen Norris", "100 Main St", 1, 3);
  INSERT INTO `Employee` VALUES (null, "Meg Ducharme", "404 Unknown Ct", 2, 1);
  INSERT INTO `Employee` VALUES (null, "Hannah Hall", "204 Empty Ave", 1, 4);
  INSERT INTO `Employee` VALUES (null, "Leah Hoefling", "200 Success Way", 2, 1);


  INSERT INTO `Animal` VALUES (null, "Snickers", "Recreation", "Dalmation", 4, 1);
  INSERT INTO `Animal` VALUES (null, "Jax", "Treatment", "Beagle", 1, 1);
  INSERT INTO `Animal` VALUES (null, "Falafel", "Treatment", "Siamese", 4, 2);
  INSERT INTO `Animal` VALUES (null, "Doodles", "Kennel", "Poodle", 3, 1);
  INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);
  INSERT INTO `Animal` VALUES (null, "Cleo", "Kennel", "Poodle", 2, 2);
  INSERT INTO `Animal` VALUES (null, "Popcorn", "Kennel", "Beagle", 3, 2);
  INSERT INTO `Animal` VALUES (null, "Curly", "Treatment", "Poodle", 4, 2);


-- Get only the animal rows where the `id` field value is 3
SELECT
    a.id,
    a.name,
    a.breed,
    a.status,
    a.location_id,
    a.customer_id
FROM animal a
WHERE a.id = 3

-- Get only the customer rows where the `id` field value is 2
SELECT
    c.id,
    c.name,
    c.address,
    c.email,
    c.password
FROM customer c
WHERE c.id = 2

-- Get only the employee rows where the `id` field value is 4
SELECT 
    e.id,
    e.name,
    e.years_employed,
    e.location_id
FROM employee e
WHERE e.id = 4

-- Get only the location rows where the `id` field value is 1
SELECT
    l.id,
    l.name,
    l.address
FROM location l
WHERE l.id = 1

-- Remove only the employee rows where the `id` field value is 3
DELETE FROM `Employee`
WHERE id = 3


-- Update only the animal rows where the `id` field value is 8
UPDATE `Animal`
SET breed = 'Terrier'
WHERE id = 8

-- Get all animal rows and show the corresponding location based on matching location_id
SELECT
    a.id,
    a.name,
    a.breed,
    a.status,
    a.location_id,
    a.customer_id,
    l.name location_name,
    l.address location_address
FROM Animal a
JOIN Location l
    ON l.id = a.location_id

-- Get all animal rows and show the corresponding customer based on matching customer_id
SELECT
    a.id,
    a.name,
    a.breed,
    a.status,
    a.location_id,
    a.customer_id,
    c.name customer,
    c.address cus_address,
    c.email,
    c.password
FROM Animal a
JOIN Customer c
    ON c.id = a.customer_id

-- Get all employee rows and show the corresponding location based on matching location_id
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

-- Get all customer rows that have an animal with matching customer_id
-- and show the location that have a matching location_id of the animal
-- and order so that we can see the animals owned by customer
SELECT
    c.id cus_id,
    c.name customer,
    a.name animal,
    l.name storefront
FROM Customer c
JOIN Animal a
    ON c.id = a.customer_id
JOIN Location l
    ON l.id = a.location_id
ORDER BY c.id

-- check if new Animal datapoint appears after POST request
SELECT * FROM Animal ORDER BY id DESC;
