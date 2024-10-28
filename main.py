import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# User input
m = float(input("Enter the load weight (in kg): "))
k = float(input("Enter the spring constant (in N/m): "))
c = float(input("Enter the medium resistance coefficient (in kg/s): "))

# Initial conditions
x0 = 1.0  # Initial offset (in meters)
v0 = 0.0  # Initial speed (in m/s)
y0 = [x0, v0]  # Vector of initial conditions

# Modeling time
t_max = 20  # Maximum time (in seconds)
dt = 0.01  # Time step
t = np.arange(0, t_max, dt)  # Time array

# Function for solving differential equation
def model(y, t, m, k, c):
    x, v = y
    dxdt = v
    dvdt = -(c/m)*v - (k/m)*x
    return [dxdt, dvdt]

# Solution of differential equation
sol = odeint(model, y0, t, args=(m, k, c))

# Extract results
x = sol[:, 0]  # Position
v = sol[:, 1]  # Speed

# Calculate energies
KE = 0.5 * m * v**2  # Kinetic energy
PE = 0.5 * k * x**2  # Potential energy of a spring
TE = KE + PE         # Total mechanical energy

# Plot graphs
plt.figure(figsize=(12, 6))

plt.plot(t, KE, label='Kinetic energy (KE)')
plt.plot(t, PE, label='Potential energy (PE)')
plt.plot(t, TE, label='Total mechanical energy (TME)')

plt.title("Energy transformations during oscillation of a load on a spring")
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.legend()
plt.grid(True)
plt.show()