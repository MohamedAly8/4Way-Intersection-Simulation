def numCars_vs_Time():
    x = []
    y = []
    for i in range(5,1000,10):
        print(i)
        x.append(i)
        sim = Simulation(i,"Manual")
        sim.run()
        y.append(sum(sim.data)/len(sim.data))
    plt.scatter(x,y,color='blue',label = "Manual")
    plt.legend(loc='upper right')
    plt.xlabel("Number of Car")
    plt.ylabel("Average Travel time(s)")

def Human_vs_Self():
    x = []
    y = []
    for i in range(5,1000,10):
        print(i)
        x.append(i)
        sim = Simulation(i,"Self-Driving")
        sim.run()
        y.append(sum(sim.data)/len(sim.data))
    plt.scatter(x,y,color='red',label="Self_Driven")
    plt.legend(loc='upper right')
    plt.show()
