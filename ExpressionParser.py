import re
import tokenize

import sympy

class ExpressionParser:
    #r"^\s*[+-]?\s*(\d+\s*\.?\s*\d*|\d*\s*\.?\s*\d+)\s*$"
    double_regex = r'^\s*[-]?\s*('
    #(minus)? num/x oper num/x oper...
    @staticmethod
    def simplify(expression: str):

        simplified = ''
        expression = expression.replace('^', '**')

        try:
            if ('x' in expression and '=' in expression):
                eq1, eq2 = expression.split('=')
                total_eq = eq1+'- ('+ eq2 + ')'
                simplified = sympy.simplify(total_eq)
                #x = sympy.Symbol('x')
                #print(total_eq_simplified)
                #eq = sympy.Eq(eq1, eq2)
                #simplified = sympy.solve(total_eq_simplified, x)
            elif ('x' in expression):
                simplified = sympy.simplify(expression)
            else:
                simplified = eval(expression)
            #simplified = eval(simplified)
        except (SyntaxError, tokenize.TokenError, sympy.core.SympifyError):
            simplified = 'Error'
        return simplified


if __name__ == '__main__':
    expression = ''
    while(expression!='e'):
        expression = input()

        print(ExpressionParser.simplify(expression))



