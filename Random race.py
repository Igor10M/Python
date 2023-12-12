#random race
import random

class Vehicle:
    def __init__(self, pilot_name, max_speed, color):
        self.pilot_name = pilot_name
        self.max_speed = max_speed
        self.color = color
        self.is_broken = False
        self.distance = 0

    def move(self):
        if not self.is_broken:
            distance_moved = random.randint(0, self.max_speed) / 20
            self.distance += distance_moved

    def crash(self):
        if random.randint(1, 100) == 55:
            self.is_broken = True

class Race:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def start(self):
        while not any(vehicle.distance >= 100 for vehicle in self.vehicles if not vehicle.is_broken):
            for vehicle in self.vehicles:
                vehicle.move()
                vehicle.crash()
            if all(vehicle.is_broken for vehicle in self.vehicles):
                break

        winner = max(self.vehicles, key=lambda x: x.distance)
        if winner.is_broken:
            print("All vehicles crashed, no winner!")
        else:
            print(f"The winner is {winner.pilot_name} with a distance of {winner.distance}.")

vehicles = [
    Vehicle("Ash", 30, "Red"),
    Vehicle("Gary", 45, "Blue"),
    Vehicle("Misty", 40, "Green"),

]
race = Race(vehicles)


for i in range(3):
    print(f"Race {i + 1}:")

    for vehicle in vehicles:
        vehicle.is_broken = False
        vehicle.distance = 0

    race.start()
    print("")