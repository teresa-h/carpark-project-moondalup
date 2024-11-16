import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("200 Sunny Street", 100)
        self.entry_sensor = EntrySensor(123, True, self.car_park)
        self.exit_sensor = ExitSensor(456, True, self.car_park)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertEqual(self.entry_sensor.id, 123)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_entry_sensor_update_car_park(self):
        self.car_park.add_car("XYZ-666")
        self.assertEqual(self.car_park.plates, ["XYZ-666"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.exit_sensor.id, 456)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_exit_sensor_update_car_park(self):
        self.car_park.add_car("GHD-888")
        self.car_park.remove_car("GHD-888")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)
