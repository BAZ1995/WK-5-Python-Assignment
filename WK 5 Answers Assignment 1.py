# Base Class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, and I protect {self.city} using my {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with Inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h while using {self.power}!")

class StrengthHero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.strength_level = strength_level

    def use_power(self):
        print(f"{self.name} smashes obstacles with {self.strength_level} strength and {self.power}!")

# Creating Objects
hero1 = FlyingHero("SkySwift", "Wind Manipulation", "SkyCity", 300)
hero2 = StrengthHero("TitanFist", "Earthquake Punch", "RockTown", "Ultra")

# Using the methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
