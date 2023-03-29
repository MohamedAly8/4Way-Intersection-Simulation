import random
import matplotlib.pyplot as plt
import numpy as np

# Constants
NUM_POINTS = 100
REACTION_TIME_RANGE = np.linspace(0.5, 2, NUM_POINTS)
FLOW_OF_TRAFFIC = 80 / (REACTION_TIME_RANGE ** 2) * np.exp(-0.001 * REACTION_TIME_RANGE)
NOISE_STD_DEV = 30


# Add random noise to the flow of traffic data
flow_of_traffic_with_noise = FLOW_OF_TRAFFIC + np.random.normal(scale=NOISE_STD_DEV, size=NUM_POINTS)



# Plot data
fig, ax = plt.subplots()
ax.scatter(REACTION_TIME_RANGE, flow_of_traffic_with_noise, label='Data Points')

ax.set_xlabel('Reaction Time (s)')
ax.set_ylabel('Flow of Traffic (Cars / minute)')
ax.set_title('Reaction Time vs. Flow of Traffic')
ax.legend(['Human Driven Vehicles'])
plt.show()