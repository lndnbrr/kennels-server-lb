class Customer:
    """Class that defines the template for how a customer should be structured in a dataset.
    Default params for email and password arer empty strings"""

    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
