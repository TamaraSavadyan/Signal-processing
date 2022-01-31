import numpy as np
from matplotlib import pyplot as plt

class Signal():
    def __init__(self, f0, dt, waveletType=None, b=0, noise=False):
        self.f0 = f0
        self.dt = dt
        self.waveletType = waveletType
        self.t = np.arange(0, 1/self.f0, self.dt)
        self.b = b
        self.noise = noise
        self.wavelet = 0

    def setTypeOfSignal(self):
        self.waveletType = self.waveletType.lower()
        if self.waveletType == 'ricker':
            self.wavelet = (1 - 2*(self.f0/2*self.t)**2) * \
                np.exp(-(self.f0/2*self.t)**2)

        elif self.waveletType == 'gelfand':
            self.wavelet = np.exp(-self.b*self.t**2) * np.sin(self.f0*self.t)

        elif self.waveletType == 'berlage':
            n = 2
            self.wavelet = self.t**n * \
                np.exp(-self.b*self.t) * np.sin(self.f0*self.t)

        elif self.waveletType == 'bubble':
            self.wavelet = np.exp(-self.f0/np.pi*self.t)**2 * \
                np.sin(self.f0*self.t)

        elif self.waveletType == 'damped_sine':
            self.wavelet = np.exp(-self.b*self.t) * np.sin(self.f0*self.t)

        elif self.waveletType == 'damped_cosine':
            self.wavelet = np.exp(-self.b*self.t) * np.cos(self.f0*self.t)

        elif self.waveletType == 'sine':
            self.wavelet = np.sin(2*np.pi*self.f0*self.t)

        elif self.waveletType == 'cosine':
            self.wavelet = np.cos(2*np.pi*self.f0*self.t)

        else:
            self.wavelet = np.random.rand(self.t)

        if self.noise:
            self.wavelet += np.random.rand(self.t.size)


