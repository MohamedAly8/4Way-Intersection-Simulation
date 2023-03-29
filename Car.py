import random

MANUAL_SELFDRIVEN_RATIO = 0.3
vehiclesTypes = ["Manual", "SelfDriven"]
N = "North"
E = "East"
S = "South"
W = "West"

class Car:
    def __init__(self, name, arrival_time):
        self.name = name
        self.arrival_time = arrival_time
        self.depart_time = 0
        self.vehicleType = random.choices(vehiclesTypes, weights=[1-MANUAL_SELFDRIVEN_RATIO, MANUAL_SELFDRIVEN_RATIO])[0]

        if self.vehicleType == "Manual":     
            self.clear_time = 10
        else:
            self.clear_time = 6

        # Is the driver not reactive / DUI / Unstable
        self.isWreckless = random.random() < 0.01

        #Randomly generate speed distributed around 60 km/h, max: 100km/h
        self.speed = int(random.normalvariate(60, 10))
        self.speed = max(40, min(self.speed, 100))

        self.direction = random.choices([N, E, S, W])[0]
        #Randomly generate turn direction
        self.turn_direction = random.choices(["Left", "Right", "Straight"], weights=[0.20, 0.20, 0.6])[0]
        

    def get_name(self):
        return self.name


    def get_arrival_time(self):
        return self.arrival_time
    
    def get_depart_time(self):
        return self.depart_time

    def set_depart_time(self, time):
        self.depart_time = time


    def get_clear_time(self):
        return self.clear_time

    def set_clear_time(self, clear_time):
        self.clear_time = clear_time
    
    def get_speed(self):
        return self.speed

    def get_isWreckless(self):
        return self.isWreckless

    def get_direction(self):
        return self.direction

    def get_turn_direction(self):
        return self.turn_direction

    def get_vehicleType(self):
        return self.vehicleType