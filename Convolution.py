import numpy as np
from matplotlib import pyplot as plt
import math
import scipy.ndimage as ndi

x = np.array([0, 1.0, 0, 0])  # Последовательность x
y = np.array([0, 1.0, 2])  # Последовательность y
z = np.array([-1.0, 1, 0, 0])  # Последовательность z

h = np.convolve(x, y, 'full')  # Линейная свертка последовательностей x и y

# при mode='wrap' параметре расчитывается циклическая (а не линейная) свертка
h = ndi.convolve(x, z, mode='wrap')
# сдвиг последовательности h на половину ее длины
h = np.roll(h, math.floor(h.size/2))

def convolve(T, dt, f0):
    t = np.arange(0, T, dt) # Массив отсчетов по времени
    s = np.sin(2*np.pi*f0*t)



'''
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.xlim((-T, T))
plt.title('Sinus')
plt.xlabel('t, s')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(lags*dt, s_acf)
plt.xlim((-T, T))
plt.title('Autocorrelation')
plt.xlabel('lags, s')
plt.grid()

plt.show()
'''