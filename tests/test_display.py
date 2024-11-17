import unittest
from display import Display
from car_park import CarPark


class TestDisplay(unittest.TestCase):
    """
    Unit test that tests the Display class
    """
    def setUp(self):
        """
        Sets up an instance of a car park and an instance of a display.
        """
        self.car_park = CarPark("123 Smith Street", 150)
        self.display = Display(1, CarPark(...), "Welcome to the car park", True)

    def test_display_initialized_with_all_attributes(self):
        """
        Tests whether the display is initialized with all the attributes.
        """
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertIsInstance(self.display.car_park, CarPark)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)

    def test_update(self):
        """
        Tests whether the update method works.
        """
        self.display.update({"message": "Thank you for parking here"})
        self.assertEqual(self.display.message, "Thank you for parking here")
