import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.axes as axes
import sympy
import matplotlib.axes as axes
import numpy

from ExpressionParser import ExpressionParser

class Grid:
    def __init__(self):
        #draw axes
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.grid(color='grey', linestyle='--')
        #plt.show()

    def draw_function(self, func: sympy.Expr):
        xvals = numpy.linspace(-5, 5, 20)  # 20 points from -5 to 5 in ndarray
        x = sympy.Symbol('x')

        yvals = [func.subs(x, xval) for xval in xvals]  # evaluate f for each point in xvals

        #plt.plot(xvals, yvals)

        #fig, ax = plt.subplots()
        plt.plot(xvals, yvals)
        #loc = ticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
        #plt.plot.set_major_locator(loc)
        #plt.MultipleLocator(base=2.0)
        #plt.xticks(numpy.arange(-5, 5, 1))
        #plt.yticks(numpy.arange(-5, 5, 1))
        #plt.xscale('linear')
        #plt.yscale('linear')
        plt.show()




if __name__ == '__main__':
    expression = input()
    func = ExpressionParser.simplify(expression)
    grid = Grid()
    grid.draw_function(func)