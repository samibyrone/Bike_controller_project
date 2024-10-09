import unittest

from Automatic_Bike.automatic_bike import AutomaticBike

class TestAutomaticBike(unittest.TestCase):

    def test_for_automaticBike_to_be_off(self):
        automatic_bike = AutomaticBike()
        self.assertFalse(automatic_bike.turnOff())

    def test_for_automaticBike_to_be_turn_on(self):
        automatic_bike = AutomaticBike()
        bike = automatic_bike.turnOn()
        self.assertEqual(automatic_bike.turnOn(), bike)

    def test_for_automaticBike_can_accelerate(self):
        automatic_bike = AutomaticBike()
        bike = automatic_bike.turnOn()
        self.assertEqual(automatic_bike.turnOn(), bike)
        speed = 1
        speed = automatic_bike.set_acceleration(speed)
        self.assertEqual(automatic_bike.set_acceleration(6), speed)

    def test_for_automaticBike_can_increase_acceleration_to_gear_one(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 15
        automatic_bike.automatic_bike_speed_increase_to_gear_one(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_increase_to_gear_one(15), 16)

    def test_for_automaticBike_can_increase_acceleration_to_gear_two(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 24
        automatic_bike.automatic_bike_speed_increase_to_gear_two(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_increase_to_gear_two(24), 26)

    def test_for_automaticBike_can_increase_acceleration_to_gear_three(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 35
        automatic_bike.automatic_bike_speed_increase_to_gear_three(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_increase_to_gear_three(35), 38)

    def test_for_automaticBike_can_decrease_acceleration_to_gear_four(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 44
        automatic_bike.automatic_bike_speed_increase_to_gear_four(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_increase_to_gear_four(44), 48)

    def test_for_automaticBike_can_decrease_acceleration_to_gear_one(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 15
        automatic_bike.automatic_bike_speed_decrease_to_gear_one(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_decrease_to_gear_one(15), 14)

    def test_for_automaticBike_can_decrease_acceleration_to_gear_two(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 24
        automatic_bike.automatic_bike_speed_decrease_to_gear_two(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_decrease_to_gear_two(24), 22)

    def test_for_automaticBike_can_decrease_acceleration_to_gear_three(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 35
        automatic_bike.automatic_bike_speed_decrease_to_gear_three(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_decrease_to_gear_three(35), 32)

    def test_for_automaticBike_can_decrease_acceleration_by_gear_four(self):
        automatic_bike = AutomaticBike()
        automatic_bike.turnOn()
        speed = 44
        automatic_bike.automatic_bike_speed_decrease_to_gear_four(speed)
        self.assertEqual(automatic_bike.automatic_bike_speed_decrease_to_gear_four(44), 40)