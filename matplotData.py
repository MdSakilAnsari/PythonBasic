
import matplotlib.pyplot as plt
Time=[1,2,3,4,5]
Distance=[10,20,15,25,30]
plt.plot(Time,Distance,linestyle='dotted')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.scatter('Time','Distance')
plt.show()