from abc import ABC, abstractmethod
import random


class Sensor(ABC):

    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"The status of {self.id} is {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return f"JFC-{str(random.randint(100, 999))}"

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Vehicle entry with plate: {plate}")


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Vehicle exit with plate: {plate}")

