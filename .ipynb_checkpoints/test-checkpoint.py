# Source - https://stackoverflow.com/a/64368662
# Posted by JohanC
# Retrieved 2026-08-24, License - CC BY-SA 4.0

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.linspace(0, 6 * np.pi, 200)
line1, = ax.plot(x, np.sin(x))
line2, = ax.plot(x, np.cos(x) / 100)

def animate(i):
    line1.set_ydata(np.sin(x + i / 10.0))  # update the first part
    if i % 10 == 0:
        j = i / 10
        line2.set_ydata(np.cos(x) * j / 20)  # update the second part, only every 5 steps
    return line1, line2,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=100)
plt.show()
