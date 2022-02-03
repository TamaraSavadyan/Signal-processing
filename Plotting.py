from matplotlib import pyplot as plt

from Signal import Signal

class Plot(Signal):

    def plotSignal(self, row, col, index, title='', xLabel='', yLabel=''):
        
        plt.figure(figsize=(10,10))
        plt.subplot(row, col, index)
        plt.plot(self.t, self.wavelet)
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.grid()

        plt.show()