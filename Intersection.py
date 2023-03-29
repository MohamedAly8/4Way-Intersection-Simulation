import random
import matplotlib.pyplot as plt
from sys import *
from Car import *
from EmissionsCalculator import *
from queue import Queue
import time
from multiprocessing import Process
import threading


#Constants
N = "North"
E = "East"
S = "South"
W = "West"

class Intersection:

    def __init__(self, lane_size=3, carArrivalFrequency=None):

        

        self.north_queue = Queue()
        self.south_queue = Queue()
        self.east_queue = Queue()
        self.west_queue = Queue()


        self.north_progress = []
        self.south_progress = []
        self.east_progress= []
        self.west_progress= []
        self.car_in_system = 0
        self.cars_passed = 0
        self.car_counter = 0
        self.light = "NS"
        self.light_duration = 5 # seconds
        self.last_switch_time = time.time()
        self.lane_size = lane_size
        self.accident_count = 0
        self.accidents = [] # Cause , Severity

        self.emissions = []

        self.lock = threading.Lock()

        self.carArrivalFrequency = carArrivalFrequency
         

    def spawn_car(self):
            
        car = Car(self.car_counter, time.time())
        
        self.car_in_system += 1
        if car.direction == N:
            self.north_queue.put(car)
        elif car.direction == S:
            self.south_queue.put(car)
        elif car.direction == E:
            self.east_queue.put(car)
        elif car.direction == W:
            self.west_queue.put(car)
        else:
            print("Error: Car direction not valid")
        
        self.car_counter += 1
        self.currentCar = car

        print(self.emissions)

    def car_passed(self):
        self.car_in_system -= 1
        self.cars_passed += 1
    
    def switch_light(self):

        

        current_time = time.time()

        # Dynamic light change based on queue sizes
        # current_time - self.last_switch_time > self.light_duration 
        if (self.light == "NS" and self.east_queue.qsize() + self.west_queue.qsize() > 5) or (
                self.light == "EW" and self.north_queue.qsize() + self.south_queue.qsize() > 5):

            if self.light == "NS":
                self.light = "EW"
                
                # ACCIDENT PROBLEM

                if len(self.north_progress) > 0 or len(self.south_progress) > 0:
                    accident_lightswitch += 1
                    print("Accident at lightswitch")
                    
                    [car_passed() for _ in len(self.north_progress)]
                    [car_passed() for _ in len(self.south_progress)]
                    self.north_passed = []
                    self.south_passed = []


                
            else:
                self.light = "NS"
                

                # ACCIDENT PROBLEM

                if len(self.east_progress) > 0 or len(self.west_progress) > 0:
                    accident_lightswitch += 1
                    print("Accident at lightswitch")
                    [car_passed() for _ in len(self.east_progress)]
                    [car_passed() for _ in len(self.west_progress)]
                    self.east_passed = []
                    self.west_passed = []


            print("Light Green for:", self.light)
            self.last_switch_time = current_time


    def pass_N_cars(self):
        with self.lock:
            for _ in range(min(3, self.north_queue.qsize())):
                        car = self.north_queue.get()
                        if time.time() >= car.clear_time:
                            self.car_passed()
                        else:
                            self.north_progress.append(car)
                    
                        time_diff = time.time() - car.get_arrival_time()
                        self.emissions.append(self.get_car_emmisions(car, time_diff))


                        for car in self.north_progress:
                            if car.get_clear_time() >= time.time():
                                self.north_progress.remove(car)
                                self.car_passed()



    def pass_S_cars(self):
        with self.lock:
            for _ in range(min(3, self.south_queue.qsize())):
                        car = self.south_queue.get()
                        if time.time() >= car.clear_time:
                            self.car_passed()
                        else:
                            self.south_progress.append(car)
                    
                        time_diff = time.time() - car.get_arrival_time()
                        self.emissions.append(self.get_car_emmisions(car, time_diff))

                        for car in self.south_progress:
                            if car.get_clear_time() >= time.time():
                                self.south_progress.remove(car)
                                self.car_passed()

    def pass_E_cars(self):
        for _ in range(min(3, self.east_queue.qsize())):
                    car = self.east_queue.get()
                    if time.time() >= car.clear_time:
                        self.car_passed()
                    else:
                        self.east_progress.append(car)
                
                    time_diff = time.time() - car.get_arrival_time()
                    self.emissions.append(self.get_car_emmisions(car, time_diff))

                    for car in self.east_progress:
                        if car.get_clear_time() >= time.time():
                            self.east_progress.remove(car)
                            self.car_passed()

    def pass_W_cars(self):
        for _ in range(min(3, self.west_queue.qsize())):
                    car = self.west_queue.get()
                    if time.time() >= car.clear_time:
                        self.car_passed()
                        
                    else:
                        self.west_progress.append(car)
                
                    time_diff = time.time() - car.get_arrival_time()
                    self.emissions.append(self.get_car_emmisions(car, time_diff))

                    for car in self.west_progress:
                        if car.get_clear_time() >= time.time():
                            self.west_progress.remove(car)
                            self.car_passed()
                            

    def get_car_emmisions(self, car, total_time):
        ec = EmissionsCalculator(car, total_time)
        return round(ec.calculate(),2)


    def increment_accident(self):
        self.accident_count += 1

    def run_intersection(self):
        start_time = time.time()
        # loop_time = start_time + 5 # How often data is shown (5 seconds)

        if not self.carArrivalFrequency:
            next_car_spawn_time = start_time + random.random()
        else:
            next_car_spawn_time = start_time + 1/self.carArrivalFrequency


        currlight = self.light
        while currlight == self.light:

            
            # spawn car every 1 second 
            if time.time() >= next_car_spawn_time:
                self.spawn_car()
                next_car_spawn_time += random.random()
                print("Car spawned", self.currentCar.get_direction(), "Bound")
                

                # Check if driver overspeeding or wreckless 
                if self.currentCar.speed > 75:
                    print("Overspeeding driver")
                    if random.random() < 0.5 or self.currentCar.get_isWreckless():
                        
                        if self.currentCar.get_isWreckless():
                            print("Wreckless driver")
                        print("ACCIDENT!! ")

                        angle_severity = 0
                        accident_direction = self.currentCar.get_direction()

                        if accident_direction == N or accident_direction == S:
                            if len(self.east_progress) != 0 or len(self.west_progress) != 0:
                                print("T BONE")
                                angle_severity = 1
                        if accident_direction == E or accident_direction == W:
                            if len(self.north_progress) != 0 or len(self.south_progress) != 0:
                                print("T BONE")
                                angle_severity = 1

                        accident_severity = int(self.currentCar.speed/10) + (1 if self.currentCar.get_isWreckless() else 0) + angle_severity

                        self.increment_accident()

            if self.light == "NS":
                # Process Northbound/Southbound cars
                t1 = threading.Thread(target=self.pass_N_cars())
                t2 = threading.Thread(target=self.pass_S_cars())
               
                t1.start()
                t2.start()
                t1.join()
                t2.join()

            else:
                # Process East/West bound cars
                t1 = threading.Thread(target=self.pass_E_cars())
                t2 = threading.Thread(target=self.pass_W_cars())
        
                t1.start()
                t2.start()
                t1.join()
                t2.join()



            # Switch light every 5 seconds        
            self.switch_light()


        print(f"Total number of cars passed: {self.cars_passed}")
        #Cars waiting N
        print(f"Total number of cars waiting North: {self.north_queue.qsize()}")
        #Cars waiting S
        print(f"Total number of cars waiting South: {self.south_queue.qsize()}")
        #Cars waiting E
        print(f"Total number of cars waiting East: {self.east_queue.qsize()}")
        #Cars waiting W
        print(f"Total number of cars waiting West: {self.west_queue.qsize()}")

        print(f"Total Accidents: {self.accident_count}")

        print(f"Total Emissions: {sum(self.emissions)}")


def initialize_intersection(lane_size=3):
    intersection = Intersection(lane_size=lane_size, carArrivalFrequency=100)
    return intersection

def run_simulation(intersection):
    # start_time = time.time()
    # end = start_time + duration

    for _ in range(10):
        intersection.run_intersection()

    return intersection


if __name__ == '__main__':

    intersection = initialize_intersection()
    intersection = run_simulation(intersection)