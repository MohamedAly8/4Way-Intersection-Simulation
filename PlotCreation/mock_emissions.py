import random
import matplotlib.pyplot as plt

# Constants
NUM_SIMULATIONS = 200
NUM_CARS_RANGE = range(1, 101,5)
CAR_TYPES = ['Manual', 'Self-Driven']
AVG_TRAVEL_TIME_RANGE = (10, 100)
EMISSIONS_PER_MIN_PER_CAR = {
    'Manual': 0.06,
    'Self-Driven': 0.02,
}

# Generate data
data_self = []
data_human = []

for num_cars in range(10, NUM_SIMULATIONS + 1, 2):

    # avg_travel_time = round(random.uniform(*AVG_TRAVEL_TIME_RANGE), 2)
    avg_travel_time = random.uniform(num_cars, num_cars * 1.1)

    emissions_per_min = EMISSIONS_PER_MIN_PER_CAR['Manual']
    emissions = random.uniform(emissions_per_min * avg_travel_time - 2, emissions_per_min * avg_travel_time + 2)

    while emissions < 0:
        # recalculate emissions 
        emissions = random.uniform(emissions_per_min * avg_travel_time * random.uniform(1, 3), emissions_per_min * avg_travel_time+ random.uniform(1, 3) )

    data_human.append((num_cars, avg_travel_time, emissions, 'Manual'))


for num_cars in range(10, NUM_SIMULATIONS + 1, 2):

    # avg_travel_time = round(random.uniform(*AVG_TRAVEL_TIME_RANGE), 2)
    avg_travel_time = random.uniform(num_cars, num_cars * 1.1)

    emissions_per_min = EMISSIONS_PER_MIN_PER_CAR['Self-Driven']
    
    emissions = random.uniform(emissions_per_min * avg_travel_time - random.uniform(1, 3) , emissions_per_min * avg_travel_time + random.uniform(1, 3))

    while emissions < 0:
        # recalculate emissions 
        emissions = random.uniform(emissions_per_min * avg_travel_time - 1, emissions_per_min * avg_travel_time + 1)
    
    print(emissions)


    data_self.append((num_cars, avg_travel_time, emissions, 'Self-Driven'))

# Plot data



plt.scatter([row[1] for row in data_human], [row[2] for row in data_human], color='red')
plt.scatter([row[1] for row in data_self], [row[2] for row in data_self], color='blue')


plt.xlabel('Number of Cars Passing Intersection in Simulation')
plt.ylabel('Average Emissions Produced Per Vehicle')
plt.title('Comparison of Emissions With Design Implementations vs Without')
plt.legend(['w/o Design', 'with Design Implemented'])
plt.show()