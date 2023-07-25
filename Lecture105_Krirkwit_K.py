class Vehicle:
    licenseCode = ""
    serialCode = ""
    def TurnOnAirConditioner(self):
        print("Turn on Air")

class Car(Vehicle):
    def TurnOnAirConditioner(self):
        print("Car Turn on Air")

class Pickup(Vehicle):
    def TurnOnAirConditioner(self):
        print("Pickup Turn on Air")

class Van(Vehicle):
    def TurnOnAirConditioner(self):
        print("Van Turn on Air")

class LuxuryCar(Vehicle):
    def TurnOnAirConditioner(self):
        print("Luxury car Turn on Air")


car1 = Car()
car1.TurnOnAirConditioner()

pickup1 = Pickup()
pickup1.TurnOnAirConditioner()

van1 = Van()
van1.TurnOnAirConditioner()

luxuryCar = LuxuryCar()
luxuryCar.TurnOnAirConditioner()