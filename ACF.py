import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import correlate, correlation_lags

from Signal import Signal

class ACF(Signal):

    def acf(self):

        s_acf = correlate(self.wavelet, self.wavelet,'full') # Массив элементов АКФ
        lags = correlation_lags(self.wavelet.size, self.wavelet.size, "full") # Массив индексов АКФ

        plt.figure(figsize=(10,10))
        plt.subplot(2,1,1)
        plt.plot(self.t, self.wavelet)
        plt.xlim((-1/self.f0, 1/self.f0))
        plt.title('Sinus')
        plt.xlabel('t, s')
        plt.grid()

        plt.subplot(2,1,2) 
        plt.plot(lags*self.dt, s_acf) #В plot передается массив сдвигов в секундах, а не в у.е.
        plt.xlim((-1/self.f0, 1/self.f0))
        plt.title('Autocorrelation')
        plt.xlabel('lags, s')
        plt.grid()

        plt.show()
    

s = ACF(50, 0.001, 'sine', noise=True)
s.setTypeOfSignal()

if __name__ == "__main__":
    s.acf()