import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, ifft

from Signal import Signal

class ZeroPhase(Signal):
    
    def zeroPhaseTransform(self):
        x0 = ifft(np.abs(fft(self.wavelet)))

        x0_ = np.roll(x0, (self.wavelet.size-1)//2)
        ti_ = np.arange(-((self.wavelet.size-1)//2), self.wavelet.size//2+1, 1)

        return ti_, x0_ 