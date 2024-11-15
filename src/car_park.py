from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location="Unknown", capacity=200, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park at {self.location}, has {self.capacity} bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        if len(self.plates) > self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 32,
            "time": 1430
        }
        for display in self.displays:
            display.update(data)

