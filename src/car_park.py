from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    """
    A class to represent a carpark.

    Attributes:

    location : str
        where the car park is located
    capacity: int
        the capacity of the car park
    plates : str
        the plates that have entered the car park
    sensors: str
        the sensors that have been registered with this car park
    displays: str
        the displays that have been registered with this car park
    log file: str
        where the plates are getting logged when entering and exiting
    config file : str
        where the configurations can be stored
    """
    def __init__(self,
                 location="Unknown",
                 capacity=200,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file=Path("log.txt"),
                 config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.config_file.touch(exist_ok=True)

    def __str__(self):
        """
        :return: a string of with carpark's location and the capacity of bays
        """
        return f"Car park at {self.location}, has {self.capacity} bays."

    def register(self, component):
        """
        Registers a sensor or display and returns type error if component is neither
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        """
        Appends a car plate to the plates list of the carpark.
        Update the displays once it has appended.
        Logs the entered action with the car plates

        :param plate: string
        """
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """
          Removes a car plate from the car park.
          Update the displays once it has been removed.
          Logs the exited action with the car plates

          :param plate: string
          """
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        """
        Key, value pairs of data of available bays, temperature and time that updates.
        """
        data = {
            "available_bays": self.available_bays,
            "temperature": 32,
            "time": 1430
        }
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        """
        Logs car plates entering and exiting with a time stamp into a file.

        :param plate: str
            plate of car
        :param action: str
            whether car is entering or exiting

        """
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with open("config.json", "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
            return cls(config["location"], config["capacity"], log_file=config["log_file"])
