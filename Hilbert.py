import numpy as np
import math
from matplotlib import pyplot as plt
from scipy.fft import fft, rfft, ifft, irfft, fftfreq, rfftfreq
from scipy.signal import hilbert

def hilbertTransform(wavelet):
    
    wavelet = np.real(ifft(np.abs(fft(wavelet))))
    return np.imag(hilbert(wavelet))


