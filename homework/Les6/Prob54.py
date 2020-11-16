import time


class Cars:
    name = None
    speed = None
    colour = None
    is_police = False

    def __init__(self, name, speed, colour, is_police=False):
        self.name = name
        self.speed = speed
        self.colour = colour
        self.is_police = is_police

    def go(self):
        return "The car has departed"

    def stop(self):
        return "The car has stopped"

    def turn(self, direction):
        return "the car turned to " + direction


class TownCar(Cars):
    def __init__(self, name, speed, colour, is_police):
        super().__init__(name, speed, colour, is_police)

    def show_speed(self):
        print(f'The speed of {self.name} is {self.speed}')

        if self.speed > 60:
            print('slow down cowboy you are going too fast')


class SportCar(Cars):
    def __init__(self, name, speed, colour, is_police):
        super().__init__(name, speed, colour, is_police)


class WorkCar(Cars):
    def __init__(self, name, speed, colour, is_police):
        super().__init__(name, speed, colour, is_police)

    def show_speed(self):
        print(f'The speed of {self.name} was {self.speed} mph.')

        if self.speed > 40:
            print('I know that inside you are racer but you better hold ya horses pal')


class PoliceCar(Cars):
    def __init__(self, name, speed, colour, is_police):
        super().__init__(name, speed, colour, is_police)

    def police(self):
        if self.is_police:
            print('weep weep')
            time.sleep(3)
            print('weep weep, stop your vehicle now')
        else:
            print('its undercover')


FordGT = SportCar('Ford', 200,  'Red', False)
Chrysler = TownCar('Chrysler', 59,  'Grey', False)
FordF150 = WorkCar('FordPickUp', 109,  'Yellow', False)
DodgeCharger = PoliceCar('Dodge', 180, 'Black&White', True)

# I call only couple, tried to have some fun
print(f'{FordF150.colour} {FordF150.name} starting racing on the highway, after couple dangerous manouvers '
      f'{FordF150.turn("Downtown")}. {DodgeCharger.colour} {DodgeCharger.name} stopped by at the lights.')
print(f'{FordF150.show_speed()}, said the guy in the Charger catching up with the truck. Truck Kid smiled at him and '
      f'pushed the thortle with furious anger.')
print(f'After just a second he heard sirens from behind.{DodgeCharger.police()}')
