import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

num_points = 50
x, y = np.random.rand(2, num_points)*10
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points) * 1000

fig, ax = plt.subplots()

scat = ax.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap="viridis")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def animate(i):
    new_x = x + np.random.rand(num_points)*0.1
    new_y = y + np.random.rand(num_points)*0.1
    scat.set_offsets(np.c_[new_x, new_y])
    return scat,

anim = animation.FuncAnimation(fig, animate, frames=100, interval=1000, blit=True)

plt.show()
