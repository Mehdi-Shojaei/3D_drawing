import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(20, 10))  # increase figure size

# Add the 3D subplot
ax = fig.add_subplot(121, projection='3d')
x = df['septa th']
y = df['inspace th']
z = df['height']
c = df['SIF']

# Define percentiles based on SIF values
low_percentile = np.percentile(c, 80)
high_percentile = np.percentile(c, 90)

# Define colors based on SIF value and percentiles
colors = np.where(c < low_percentile, 'blue', np.where(c < high_percentile, 'purple', 'red'))

# Define marker sizes based on SIF value and percentiles
sizes = np.where(c < low_percentile, 25, np.where(c < high_percentile, 50, 100))

# Define alpha (transparency) based on SIF value and percentiles
alphas = np.where(c < low_percentile, 0.6, np.where(c < high_percentile, 0.8, 0.9))

# Plot the surface
surf = ax.scatter(x, y, z, c=colors, cmap='coolwarm', s=sizes, alpha=alphas)

# Set color of red dots to be more reddish
surf.set_cmap('Reds')

# Set axis labels with larger fonts and bold weights
ax.set_xlabel('Septa Thickness (mm)', fontsize=13, fontweight='bold', labelpad=12)
ax.set_ylabel('Interspace Distance (mm)', fontsize=13, fontweight='bold', labelpad=12)
ax.set_zlabel('Height (mm)', fontsize=13, fontweight='bold', labelpad=12)
ax.set_title('Cu Grids', fontsize=16, fontweight='bold')

# Get indices of points above the high percentile
idx = np.where(c > high_percentile)[0]

# Plot lines from points towards each axis
for i in idx:
    ax.plot([x[i], x[i]], [y[i], y[i]], [0, z[i]], color='green', linestyle='--', linewidth=1.0)
    ax.plot([x[i], x[i]], [0, y[i]], [z[i], z[i]], color='green', linestyle='--', linewidth=1.0)
    ax.plot([0, x[i]], [y[i], y[i]], [z[i], z[i]], color='green', linestyle='--', linewidth=1.0)

# Add a subplot for the legend
ax_legend = fig.add_subplot(122)
ax_legend.set_xlim([-1, 1])
ax_legend.set_ylim([-1, 1])
ax_legend.set_axis_off()

# Define the labels and colors with larger font sizes and bold weights
labels = ['Low percentile SIF', 'Mid percentile SIF', 'High percentile SIF']
colors = ['blue', 'purple', 'red']
fontdict = {'fontsize': 14, 'fontweight': 'bold'}

# Plot the legend dots and labels
for i in range(len(labels)):
    ax_legend.scatter(-0.95, i*0.22, color=colors[i], s=90)
    ax_legend.text(-0.9, i*0.22, labels[i], fontsize=15, fontweight='bold')


plt.savefig('Where ever you want!', dpi=300)
plt.show()
