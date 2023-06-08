# Force-Simulator
Summary:
Given a force law that is dependent upon position, velocity, both, or neither, it is possible to model the system's time evolution using differential equations. However, it is not always possible to analytically solve the equations. This program uses numerical methods to simulate the position and velocity of the particle over time.

Usage:
In order to use this program, specify the force law that you wish to study. You should specify the initial conditions such as the position and velocity of the mass. Specify the mass and define other parameters that you need to study the system (i.e. charge, coefficient of drag, mass of gravitational body, etc.) Then, run the program. The relevant computed position and velocity data over time is stored in arrays. Matplotlib os used to visualize the data.

Limitations: 
This program is not capable of simulating multi-particle systems. 

I needed a separate program for each N-dimensional system. Hence, there are different programs for the case of 1, 2, and 3 dimensional systems. Systems with more than 3 spatial dimensions can be simulated, but it is not clear what the physical meaning of the results would be. 

The error increases with each time step that is taken. This means that this program will only be within a reasonable level of accuracy for small amounts of time, in general. The rate at which the simulated behavior diverges from reality is dependent upon the force law that is provided.
