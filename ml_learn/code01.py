import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = 0.8 * x - 5
y2 = x**2 + 4*x -15
plt.plot(x, y2)
plt.show()