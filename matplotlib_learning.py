import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y1 = np.random.rand(50)
y2 = np.random.rand(50)

figure, axes = plt.subplots(2, 2)


axes[0][0].scatter(x, y1,
                   marker = 's',
                   c = 'fuchsia')
axes[0][0].set_title('marker, c')
axes[0][0].set_facecolor('lightblue')


colors_1 = np.random.rand(50)
axes[0][1].scatter(x, y1,
                   marker = '*',
                   c = colors_1,
                   s = 700)
axes[0][1].set_title('marker, c, s')
axes[0][1].set_facecolor('lightgreen')


size = 1000*np.random.rand(50)
axes[1][0].scatter(x, y2,
                   marker = 'o',
                   c = 'lightcoral',
                   s = size,
                   linewidths = 2,
                   edgecolors = 'darkred')
axes[1][0].set_title('marker, linewidths, edgecolors, c, s')
axes[1][0].set_facecolor('lightgray')


size = 1000*np.random.rand(50)
colors_2 = np.random.rand(50)
axes[1][1].scatter(x, y2,
                   marker = 'o',
                   c = colors_2,
                   s = size,
                   edgecolors = 'blue',
                   alpha = 0.4)
axes[1][1].set_title('marker, linewidths, edgecolors, alpha, c, s')


figure.set_facecolor('pink')


figure.set_size_inches((12,12))

plt.show()

