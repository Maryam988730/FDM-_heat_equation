#finite difference for 2D Heat Equation
import numpy as np
import matplotlib.pyplot as plt

#setting up the plate 
alpha_chip = 88  #thermal diffusivity 80 mm²/s)
alpha_plate = 111 #copper
n_nodes = 50
length = 30 #mm
time = 5 #s

#initailly set all alpha to plate
alpha = np.full((n_nodes, n_nodes), alpha_plate)

chip_rows =slice(15,35)
chip_cols =slice(15,35)

#set alpha for the chip
alpha[chip_rows, chip_cols] = alpha_chip


dx = length / n_nodes
dy = dx
dt = dx**2  / (4*alpha.max())  #satisfies the stability condition




#source term
#c1
c1_rows =slice(16,21)
c1_cols =slice(16,21)

c1_duty_period = 3
c1_duty_on = 0.9

Q_c1 = 30

#c2
c2_rows =slice(23,33)
c2_cols =slice(23,33)

c2_duty_period = 2
c2_duty_on = 1.4

Q_c2 = 60

#c3
c3_rows =slice(30,31)
c3_cols =slice(30,31)

c3_duty_period = 4
c3_duty_on = 0.6

Q_c3 = 20

def getQ(t, n_nodes):
    Q = np.full((n_nodes, n_nodes), 0.0)
    if (t % c1_duty_period) < c1_duty_on:
        Q[c1_rows, c1_cols] = Q_c1
    if (t % c2_duty_period) < c2_duty_on:
        Q[c2_rows, c2_cols] = Q_c2
    if (t % c3_duty_period) < c3_duty_on:
        Q[c3_rows, c3_cols] = Q_c3
    return Q
    





#BC and IC
# we are looking at a heated plate cooling down to room temp
u = np.ones((n_nodes, n_nodes)) * 20

#Dirichlet boundary conditions.
u[0,:] = 20
u[-1,:] = 20

u[:,0] = 20
u[:,-1] = 20


#plot
fig, ax = plt.subplots()
im = ax.imshow(u, cmap='viridis', vmin=0, vmax=100, origin='lower')

ax.set_title("Temperature Distribution in a Cooling Plate")
ax.set_xlabel("x-position (mm)")
ax.set_ylabel("y-position (mm)")

cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Temperature (°C)")



#simulate 
counter = 0
title = ax.set_title(f"Temperature Distribution\nTime = {counter:.2f} s")
while counter < time :
    Q= getQ(counter, n_nodes)
    #copy because we want to use temp from the previous time step, not the updates ones
    w = u.copy()
    for i in range(1, n_nodes -1):
        for j in range(1, n_nodes - 1):
            u[i,j] = w[i,j] + alpha[i,j] *dt* ((w[i+1, j] - 2*w[i, j] + w[i-1, j]) / dx**2 + (w[i, j+1] - 2*w[i, j] + w[i, j-1]) / dy**2) + Q[i,j]*dt

    counter += dt
    title.set_text(f"Temperature Distribution\nTime = {counter:.2f} s")

    #dynamic update
    im.set_data(u)
    plt.pause(0.01)
    print(counter, u.max())



#plot 
plt.show()

