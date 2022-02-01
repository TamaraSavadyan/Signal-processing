import numpy as np
import math
import scipy.ndimage as ndi

from Signal import Signal

def convolve(signal1, signal2, isLinear=True):
    if isLinear:
        return np.convolve(signal1, signal2, 'full')
    else:
        h = ndi.convolve(signal1, signal2, mode='wrap')
        return np.roll(h, math.floor(h.size/2))
        

