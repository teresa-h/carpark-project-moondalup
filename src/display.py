class Display:

    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
