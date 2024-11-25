import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x0 = 0
x1 = np.pi
x_interval = 0.01

X = np.arange(x0,x1,x_interval)
Y = X**2 * np.cos(X)+ 3*np.sin(2*X)

plt.plot(X,Y,color='yellow',label=r'$X^2 * np.cos(X)+ 3*np.sin(2*X)')
plt.fill_between(X,Y,color='red',alpha=0.4)
integration = lambda x:x**2 * np.cos(x)+ 3*np.sin(2*x)
integral, _ = integrate.quad(integration,x0,x1)
print("integral value:")
print(integral)
plt.xlabel('s')
plt.ylabel('F(x)')
plt.title('plot of F(x)= X^2 * np.cos(X)+ 3*np.sin(2*X)')
plt.show()
