import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x0 = 0
x1 = 2
x_interval = 0.01

X = np.arange(x0,x1,x_interval)
Y = np.exp(-X**2)

plt.plot(X,Y,color='yellow',label=r'$e(-x^2)')
plt.fill_between(X,Y,color='red',alpha=0.4)
integration = lambda x: np.exp(-x**2)
integral, _ = integrate.quad(integration,x0,x1)
print("integral value:")
print(integral)
plt.xlabel('s')
plt.ylabel('F(x)')
plt.title('plot of F(x)= 2x*e^(sin(x)) + cos(e^x)')
plt.show()
