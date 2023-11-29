import math
#! Dx =  ∆X = Xf - Xo
#! Dy =  ∆Y = Yf - Yo

#@ Displacement is a vector quantity.

"""
Velocity = d/t, or Vx =  ∆X/ ∆T | Vy =  ∆Y/ ∆T
Speed is a scalar quantity, while veloctiy is a vector
acceleration =  ∆v/∆t,

V = Xf - Xo / t, 
A = Vf - Vo / t

Projectile Motion can be calculated using this:

X(t) = X0 + V0 × cos(θ) × t
Y(t) = Y0 + V0 × sin(θ) × t - 1/2 × g × t^2

X(t) & Y(t) are horizontal and vertical positions at time t,
X0 & Y0 are inital positions
V0 is the initial velocity
θ is the launch angle,
g is the acceleration due to gravity

"""
import matplotlib.pyplot as plt
import math


def projectile_motion_simulation(initial_position, initial_velocity, launch_angle, delta_t, num_time_steps):
    # Obtain inital positions
    x_0, y_0 = initial_position
    v_0 = initial_velocity
    theta = launch_angle

    # Here, we convert the theta to radians (https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:trig/x2ec2f6f830c9fb89:radians/v/introduction-to-radians#:~:text=A%20radian%20is%20an%20angle,the%20radius%20of%20the%20circle.)
    theta_rad = math.radians(theta)

    # We setup the inital Horizontal & Vertical Components of velocity
    v_x_0 = v_0 * math.cos(theta_rad)
    v_y_0 = v_0 * math.sin(theta_rad)

    # Acceleration due to gravity on earth. This is different from planet to planet
    g = 9.8  # m/s^2

    # We make arrays to store the results we get.
    x_array = [x_0]
    y_array = [y_0]
    v_x_array = [v_x_0]
    v_y_array = [v_y_0]

    # Euler's method to simulate a loop.
    for _ in range(1, num_time_steps):
        x_new = x_array[-1] + v_x_array[-1] * delta_t
        y_new = y_array[-1] + v_y_array[-1] * delta_t
        v_x_new = v_x_array[-1]
        v_y_new = v_y_array[-1] - g * delta_t

        x_array.append(x_new)
        y_array.append(y_new)
        v_x_array.append(v_x_new)
        v_y_array.append(v_y_new)

    return x_array, y_array

def plot_trajectory(x_array, y_array):
    # Plot the trajectory
    plt.figure()
    plt.plot(x_array, y_array, label='Projectile Motion')
    plt.title('Projectile Motion Simulation')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.legend()
    plt.show()


inital_x = float(input("Inital X: "))
inital_y = float(input("Inital Y: "))

initial_position = (inital_x, inital_y)  # Initial position (x, y)
initial_velocity =  float(input("Inital Velocity: ")) # Initial velocity (m/s)
launch_angle =  float(input("Lauch Angle: ")) # Launch angle (degrees)
delta_t = float(input("Delta Time: "))  # Time step for simulation (s)
total_time = float(input("Time for simulation: "))  # Total simulation time (s)

# Calc number of steps by total / delta
num_time_steps = int(total_time / delta_t)

# Run the simulation
x_result, y_result = projectile_motion_simulation(initial_position, initial_velocity, launch_angle, delta_t, num_time_steps)

# Plot the trajectory
plot_trajectory(x_result, y_result)
