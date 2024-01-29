import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.axes as axes
import sympy
import numpy as np

from ExpressionParser import ExpressionParser

class Grid:
    def __init__(self):
        #draw axes
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

        plt.grid(color='grey', linestyle='--')
        #plt.show()


    def draw_function(self, func: sympy.Expr):
        xvals = np.linspace(-5, 5, 40)
        x = sympy.Symbol('x')

        func_lambdified = sympy.lambdify(x, func, "numpy")
        yvals = func_lambdified(xvals)

        plt.plot(xvals, yvals)
        plt.xlim(5)
        plt.ylim(5)

        left_border = min(yvals)
        right_border = max(yvals)
        plt.xticks(np.arange(int(min(left_border, -1*right_border)), int(right_border+1) + 1, 1.0))
        plt.yticks(np.arange(int(min(left_border, -1*right_border)), int(right_border+1) + 1, 1.0))

        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()




if __name__ == '__main__':
    expression = input()
    func = ExpressionParser.simplify(expression)
    grid = Grid()
    grid.draw_function(func)