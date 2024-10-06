import numpy as np
import matplotlib.pyplot as plt

def julia_set(xmin, xmax, ymin, ymax, width, height, c_real, c_imag, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    fractal = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 1000  # Limiting the magnitude of Z
        Z[mask] = Z[mask]**2 + complex(c_real, c_imag)
        fractal += mask.astype(int)

    return fractal

xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
width, height = 1000, 1000
c_real, c_imag = -0.7, 0.27015
max_iter = 255

julia = julia_set(xmin, xmax, ymin, ymax, width, height, c_real, c_imag, max_iter)

plt.imshow(julia, extent=(xmin, xmax, ymin, ymax), cmap='inferno', interpolation='nearest')
plt.colorbar(label='Iterations')
plt.title('Julia Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()


