import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    fractal = np.zeros(c.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(z) < 1000  # Limiting the magnitude of z
        z[mask] = z[mask]**2 + c[mask]
        fractal += mask.astype(int)

    return fractal

# Custom colormap resembling fire-like hues
colors = [(0, 0, 0), (1, 0.5, 0), (1, 0, 0.2), (1, 0.8, 0), (1, 1, 1)]
cmap_name = 'fire'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors)

xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
width, height = 1000, 1000
max_iter = 100

mandelbrot = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(mandelbrot, extent=(xmin, xmax, ymin, ymax), cmap=custom_cmap, interpolation='nearest')
plt.colorbar(label='Iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
