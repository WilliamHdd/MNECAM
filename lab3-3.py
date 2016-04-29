from sympy import *
import numpy as np 

def exo3_1():
   
    x = symbols('x')
    result = ((((x+3)*2)-4)-(2*x))+3
    print(result)

exo3_1()

def exo3_2():
    V0, t, g = symbols('V0 t g ')
    
    expr = (V0*t) -(0.5*g*(t**2))
    speed = diff(expr, t)
    acc = diff(speed, t)
    print(expr)
    print(speed)
    print(acc)
    
                

exo3_2()
