import numpy as np

class Signal():
    def __init__(self, f0, dt, waveletType='', b=0, noise=False):
        self.f0 = f0
        self.dt = dt
        self.waveletType = waveletType
        self.b = b
        self.noise = noise
        self.t = 10*np.arange(-1/self.f0, 1/self.f0, self.dt)


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

        elif self.waveletType == 'dampedsine':
            self.wavelet = np.exp(-self.b*self.t) * np.sin(self.f0*self.t)

        elif self.waveletType == 'dampedcosine':
            self.wavelet = np.exp(-self.b*self.t) * np.cos(self.f0*self.t)

        elif self.waveletType == 'sine':
            self.wavelet = np.sin(2*np.pi*self.f0*self.t)

        elif self.waveletType == 'cosine':
            self.wavelet = np.cos(2*np.pi*self.f0*self.t)

        else:
            self.wavelet = np.random.rand(self.t.size)

        if self.noise:
            self.wavelet += np.random.rand(self.t.size)


