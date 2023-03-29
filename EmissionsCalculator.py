from Car import *

class EmissionsCalculator:
    def __init__(self, car: Car, duration: float):
        self.car = car
        self.duration = duration
        self.manualCarFactor = 1.2
        self.selfDrivingFactor = 0.8

    def calculate(self):
        # Calculate the emissions based on the car's type and driving habits
        vehicle_type = self.car.get_vehicleType()
        speed = self.car.get_speed()
        is_wreckless = self.car.get_isWreckless()
        clear_time = self.car.get_clear_time()

        if vehicle_type == "Manual":
            factor = self.manualCarFactor
        else:
            factor = self.selfDrivingFactor

        if is_wreckless:
            # A wreckless driver emits more pollutants
            pollutant_factor = 1.5
        else:
            pollutant_factor = 1.0

        # Calculate the total amount of emissions
        total_emissions = speed * clear_time * factor * pollutant_factor / (self.duration * 1000)

        return total_emissions


