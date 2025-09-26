import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initial data for the plot
x_data, y_data, z_data = [], [], []
line, = ax.plot(x_data, y_data, z_data, 'b-') # 'b-' for blue line

# Function to update the plot
def update(frame):
    # Generate new data for each frame (e.g., a spiral)
    t = frame * 0.1
    x = np.sin(t)
    y = np.cos(t)
    z = t
    
    x_data.append(x)
    y_data.append(y)
    z_data.append(z)

    line.set_data(x_data, y_data) # Update x and y data
    line.set_3d_properties(z_data) # Update z data

    # Set axis limits to keep the plot visible as data grows
    ax.set_xlim(min(x_data) - 0.1, max(x_data) + 0.1)
    ax.set_ylim(min(y_data) - 0.1, max(y_data) + 0.1)
    ax.set_zlim(min(z_data) - 0.1, max(z_data) + 0.1)
    
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Live 3D Graph')

plt.show()