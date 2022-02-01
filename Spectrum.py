import numpy as np
from scipy.fft import fft

from Signal import Signal

class Spectrum(Signal):

    def fourierTransform(self):
        S_ampl = np.abs(fft(self.wavelet))
        S_freq = np.angle(fft(self.wavelet))
        f = np.arange(0, 1/self.dt, 1/self.t.size/self.dt)

        return S_ampl, S_freq, f

