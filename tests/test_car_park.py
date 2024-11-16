from car_park import CarPark
from display import Display
from sensor import Sensor
from pathlib import Path
import unittest


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Smith Street", 150, log_file="log.txt", config_file="config.json")

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Smith Street")
        self.assertEqual(self.car_park.capacity, 150)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 150)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))
        self.assertEqual(self.car_park.config_file, Path("config.json"))

    def test_add_car(self):
        self.car_park.add_car("NMTAFE-001")
        self.assertEqual(self.car_park.plates, ["NMTAFE-001"])
        self.assertEqual(self.car_park.available_bays, 149)

    def test_remove_car(self):
        self.car_park.add_car("NMTAFE-001")
        self.car_park.remove_car("NMTAFE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 150)

    def test_overfill_the_car_park(self):
        for i in range(150):
            self.car_park.add_car(f"NMTAFE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("NMTAFE-150")
        self.assertEqual(self.car_park.available_bays, 0)

        self.car_park.remove_car("NMTAFE-150")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        self.car_park = CarPark("99 Baker Street", 50)
        component = "Apple"
        with self.assertRaises(TypeError):
            self.car_park.register(component)

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def tearDown(self):
        Path("new_log.txt").unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100,
                              self.car_park.log_file)
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100,
                              self.car_park.log_file)  
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line


if __name__ == "__main__":
    unittest.main()

