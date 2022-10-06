import numpy as np
from sympy import symbols, integrate, sinc

x = symbols('x')

print(integrate((sinc(x))**2,(x,-np.inf,np.inf)))