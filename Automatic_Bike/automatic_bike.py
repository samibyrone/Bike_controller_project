class AutomaticBike:

    def __init__(self,):
        self._isOn = False
        self.gear_level = 0
        self.accelerate = 1


    def get_isOn(self):
        return self._isOn

    def turnOn(self):
        self._isOn = True

    def turnOff(self):
        self._isOn = False

    def set_acceleration(self, accelerate):
        self.accelerate = accelerate

    def get_acceleration(self):
        return self.accelerate

    def automatic_bike_speed_increase_to_gear_one(self, current_speed):
        if 0 <= current_speed <= 20:
            self.gear_level = 1
            self.accelerate = 1
            current_speed += self.accelerate
        return current_speed

    def automatic_bike_speed_increase_to_gear_two(self, current_speed):
        if 20 < current_speed <= 30:
            self.gear_level = 2
            self.accelerate = 2
            current_speed += self.accelerate
        return current_speed

    def automatic_bike_speed_increase_to_gear_three(self, current_speed):
        if 30 < current_speed <= 40:
            self.gear_level = 3
            self.accelerate = 3
            current_speed += self.accelerate
        return current_speed

    def automatic_bike_speed_increase_to_gear_four(self, current_speed):
        if 40 < current_speed <= 50:
            self.gear_level = 4
            self.accelerate = 4
            current_speed += self.accelerate
        return current_speed

    def automatic_bike_speed_decrease_to_gear_one(self, current_speed):
        if 0 <= current_speed <= 20:
            self.gear_level = 1
            self.accelerate = 1
            current_speed -= self.accelerate
        return current_speed

    def automatic_bike_speed_decrease_to_gear_two(self, current_speed):
        if 20 < current_speed <= 30:
            self.gear_level = 2
            self.accelerate = 2
            current_speed -= self.accelerate
        return current_speed

    def automatic_bike_speed_decrease_to_gear_three(self, current_speed):
        if 30 < current_speed <= 40:
            self.gear_level = 3
            self.accelerate = 3
            current_speed -= self.accelerate
        return current_speed

    def automatic_bike_speed_decrease_to_gear_four(self, current_speed):
        if 40 < current_speed <= 50:
            self.gear_level = 4
            self.accelerate = 4
            current_speed -= self.accelerate
        return current_speed