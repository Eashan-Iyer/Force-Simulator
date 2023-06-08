import numpy as np

# Defining the time and the numerical step size
simulationtime=10
simulationstep=0.001

x0=[1]
v0=[10]

position=np.array(x0)
velocity=np.array(v0)

m=np.array([10])

momentum=m*velocity

# Defining the force as a function of the velocity

# Combination of drag and gravitational forces

def force(t):
  return -9.8-10*velocities[int(t/simulationstep)]

velocities=[float(velocity)]
positions=[float(position)]

# Computing in array of positions and velocities indexed over time

for i in range (int(simulationtime/simulationstep)):
  impulse=force(i*simulationstep)*simulationstep
  delv=impulse/m
  velocities.append(velocities[-1]+delv)
  positions.append(positions[-1]+simulationstep*velocities[-1])
import matplotlib.pyplot as plt

time=np.linspace(0, simulationtime, num=int(simulationtime/simulationstep)+1)

# Visualizing the results of the simulation

plt.plot(time, velocities)
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.show()

plt.plot(time, positions)
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()

plt.plot(positions, m*velocities)
plt.xlabel("Position")
plt.ylabel("Momentum")
plt.show()
