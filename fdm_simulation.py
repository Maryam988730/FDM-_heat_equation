#finite difference for 2D Heat Equation
import numpy as np
import matplotlib.pyplot as plt

#setting up the plate 
a = 88  #thermal diffusivity
n_nodes = 50
length = 30 #mm
time = 5 #s

dx = length / n_nodes
dy = dx
dt = dx**2  / (4*a)  #satisfies the stability condition

#BC and IC
# we are looking at a heated plate cooling down to room temp
u = np.ones((n_nodes, n_nodes)) * 100

#Dirichlet boundary conditions.
u[0,:] = 20
u[-1,:] = 20

u[:,0] = 20
u[:,-1] = 20

#simulate 
counter = 0
while counter < time :
    #copy because we want to use temp from the previous time step, not the updates ones
    w = u.copy()
    for i in range(1, n_nodes -1):
        for j in range(1, n_nodes - 1):
            u[i,j] = w[i,j] + a*dt* ((w[i+1, j] - 2*w[i, j] + w[i-1, j]) / dx**2 + (w[i, j+1] - 2*w[i, j] + w[i, j-1]) / dy**2)

    counter += dt


