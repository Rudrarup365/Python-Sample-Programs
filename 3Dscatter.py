import matplotlib.pyplot as plt
import numpy as np

# Create a figure and a 3D axes object
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Generate some sample data
x = np.random.rand(100) * 10
y = np.random.rand(100) * 10
z = np.random.rand(100) * 10

# Plot the data as a 3D scatter plot
ax.scatter(x, y, z)

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set a title for the plot
ax.set_title('Simple 3D Scatter Plot')

# Display the plot
plt.show()