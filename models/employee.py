class Employee:
    """Class that defines the template for how an employee should be structured in a dataset"""

    def __init__(self, id, name, years_employed, location_id):
        self.id = id
        self.name = name
        self.years_employed = years_employed
        self.location_id = location_id
