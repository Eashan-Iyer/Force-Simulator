# Extension to the case of 2-dimensional space, or 4-dimensional phase-space

import numpy as np

simulationtime=20
simulationstep=0.001

x0=[0, 0]
v0=[5, 10]

position=np.array(x0)
velocity=np.array(v0)

m=np.array([10])

momentum=m*velocity


# Here, you define the force law that you wish to study. In this case, 2D projectile motion with a linear drag force is being simulated.

b=1

def force(t, pos, vel):
  return [-b*velocities[int(t/simulationstep)][0], -b*velocities[int(t/simulationstep)][1]-9.8]

velocities=[velocity]
positions=[position]

for i in range (int(simulationtime/simulationstep)):
  impulse=np.array(simulationstep)*force(simulationstep*i, positions[-1], velocities[-1])
  delv=impulse/m
  velocities.append(velocities[-1]+delv)
  positions.append(positions[-1]+simulationstep*velocities[-1])
  
# Visualizing the results of the data
  
xpos=np.array([])
ypos=np.array([])
for pos in positions:
  np.append(xpos, pos[0])
  np.append(xpos, pos[1])

x_pos=list(pos[0] for pos in positions)
y_pos=list(pos[1] for pos in positions)

plt.plot(x_pos, y_pos)
plt.xlabel("X position")
plt.ylabel("Y position")

print(x_pos, y_pos)

plt.show()
