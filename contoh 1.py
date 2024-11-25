import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x0 = 0
x1 = 1
x_interval = 0.01

X = np.arange(x0,x1,x_interval)
Y = 2 * X * np.exp(np.sin(X)) + np.cos(np.exp(X))

plt.plot(X,Y)

integration = lambda x: 2 * x * np.exp(np.sin(x)) + np.cos(np.exp(x))
integral, _ = integrate.quad(integration,x0,x1)
print("integral value:")
print(integral)
plt.xlabel('s')
plt.ylabel('F(x)')
plt.title('plot of F(x)= 2x*e^(sin(x)) + cos(e^x)')
plt.show()
