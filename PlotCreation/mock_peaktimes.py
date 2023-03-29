import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
NUM_POINTS = 100
EAST_TRAFFIC_RANGE = np.linspace(0, 100, NUM_POINTS)
FLOW_WITH_SWITCHING = 220 / (1 + np.exp(-0.2*(EAST_TRAFFIC_RANGE-60)))   # Sigmoid curve peaking at 50%
FLOW_NO_SWITCHING = np.zeros(NUM_POINTS)

for i in range(NUM_POINTS):
    if i < 50:
        FLOW_NO_SWITCHING[i] = FLOW_WITH_SWITCHING[i] # Sigmoid curve peaking at 60%
    else:
        FLOW_NO_SWITCHING[i] = 150 / (1 + np.exp(-0.08*(EAST_TRAFFIC_RANGE[i]-50)))
    
# Add deviation to np arrays


# remove negative values 
for i in range(NUM_POINTS):
    if FLOW_WITH_SWITCHING[i] < 0:
        FLOW_WITH_SWITCHING[i] = 0
    if FLOW_NO_SWITCHING[i] < 0:
        FLOW_NO_SWITCHING[i] = 0

# first 5% of the graph 
for i in range(0,5):
    FLOW_NO_SWITCHING[i] = random.uniform(0, 20)
    FLOW_WITH_SWITCHING[i] = random.uniform(0, 20)

# next 10%
for i in range(5,15):
    FLOW_NO_SWITCHING[i] = random.uniform(20, 50)
    FLOW_WITH_SWITCHING[i] = random.uniform(20, 50)

# next 20%
for i in range(15,35):
    FLOW_NO_SWITCHING[i] = random.uniform(55, 80)
    FLOW_WITH_SWITCHING[i] = random.uniform(45, 70)


# next 20%
for i in range(35,55):
    FLOW_NO_SWITCHING[i] = random.uniform(90, 115)
    FLOW_WITH_SWITCHING[i] = random.uniform(80, 90)

# next 10%
for i in range(55,65):
   
    FLOW_WITH_SWITCHING[i] = random.uniform(120, 130) + 50
    FLOW_NO_SWITCHING[i] = random.uniform(100, 120) 



NOISE_STD_DEV = 10
FLOW_WITH_SWITCHING += np.random.normal(scale=NOISE_STD_DEV, size=NUM_POINTS)
FLOW_NO_SWITCHING += np.random.normal(scale=NOISE_STD_DEV, size=NUM_POINTS) 


for i in range(NUM_POINTS):
    if FLOW_WITH_SWITCHING[i] < 0:
        FLOW_WITH_SWITCHING[i] = random.uniform(0, 20)
    if FLOW_NO_SWITCHING[i] < 0:
        FLOW_NO_SWITCHING[i] = random.uniform(0, 20)


# Plot data
fig, ax = plt.subplots()
ax.scatter(EAST_TRAFFIC_RANGE, FLOW_NO_SWITCHING, label='No Lane Switching')
ax.scatter(EAST_TRAFFIC_RANGE, FLOW_WITH_SWITCHING, label='With Lane Switching')

ax.set_xlabel('% of Traffic Heading East')
ax.set_ylabel('Number of Cars Passed [Eastbound] (Vehicles/Minute)')
ax.set_title('Traffic Flow with and without Lane Switching')
ax.legend()

# Add verical line in graph at x axis = 55 with text
plt.text(50, 125, 'Lane Switches Eastbound', rotation=90)
plt.axvline(x=55, color='r', linestyle='--')
plt.show()
