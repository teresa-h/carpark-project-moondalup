from car_park import CarPark
from display import Display
from sensor import Sensor
import unittest


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Smith Street", 150)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Smith Street")
        self.assertEqual(self.car_park.capacity, 150)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 150)

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


if __name__ == "__main__":
    unittest.main()

