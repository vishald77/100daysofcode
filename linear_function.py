from sympy import *
from sympy.plotting import plot3d


# x=symbols('x')
# # f=2*x+1
# f=x**2+1
# plot(f)

#3d plotting
x,y=symbols('x y')
f=2*x+3*y
plot3d(f)
