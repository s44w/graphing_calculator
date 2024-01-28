import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy

class Grid:
    def __init__(self):
        #draw axes
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        x = numpy.arange(-5, 5, 1)
        y = numpy.arange(-5, 5, 1)

        plt.plot(x,y)
        plt.grid(color = 'grey', linestyle = '--')
        plt.show()


if __name__ == '__main__':
    grid = Grid()