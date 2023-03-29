import random
import matplotlib.pyplot as plt
NUM_DATA_POINTS = 500

# initialize the list to hold the output data
output_data_human = []
output_data_self = []

# loop over a range of increasing numbers of cars
for num_cars in range(10, NUM_DATA_POINTS + 1, 5):
    # randomly generate a travel time for each car in the range of 10 to 200
    travel_times = random.randint(num_cars, num_cars*2)

    # calculate the average travel time for this set of cars
    # avg_travel_time = sum(travel_times) / len(travel_times)

    # randomly choose whether the cars are self-driven or manual
    car_type = "Manual"

    # add this row of data to the output list
    output_data_human.append([num_cars, travel_times, car_type])


# For self-driven cars 
THRESHOLD = 350
for num_cars in range(10, NUM_DATA_POINTS + 1, 5):
    if num_cars < 200:
        travel_times = random.randint(num_cars, num_cars*2)
    else:
        # make travel_times at a normal distribution from THRESHOLD
        travel_times = random.randint(THRESHOLD, THRESHOLD + 200)

    car_type = "Self-Driven"
    output_data_self.append([num_cars, travel_times, car_type])

# print out the output data for verification



# make each scatter different color 
plt.scatter([row[0] for row in output_data_human], [row[1] for row in output_data_human], color='red')
plt.scatter([row[0] for row in output_data_self], [row[1] for row in output_data_self], color='blue')

# make legend 
plt.legend(['Manual', 'Self-Driven'])
# make plt title 
plt.title('Number of Cars vs Average Travel Time')
# make x and y labels
plt.xlabel('Number of Cars')
plt.ylabel('Average Travel Time')

plt.show()
