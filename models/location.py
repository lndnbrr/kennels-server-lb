class Location:
    """Class that defines the template for how a location should be structured in a dataset"""

    def __init__(self, id, name, address, top_selling_pet):
        self.id = id
        self.name = name
        self.address = address
        self.top_selling_pet = top_selling_pet
