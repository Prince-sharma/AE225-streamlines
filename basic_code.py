import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
n=1000
x_axis = np.linspace(-100,100,n)
soln=np.zeros((n,2))
U=1
k=0.1
C=0.1
num=10
psi=np.linspace(-10,10,20)
for j in range(num):
    for i in range(n):
        def func(z):
            x=z[0]
            y=z[1]
            F=np.zeros((2))
            F[0]= U*y - k*np.log(np.sqrt(x*x + y*y)) - C*y/(x*x + y*y) + psi[j]
            F[1]=x-x_axis[i]
            return F
        zGuess=np.array([0.1,1])
        z=fsolve(func, zGuess)
        soln[i:,0]=z[0]
        soln[i:,1]=z[1]
    plt.plot(soln[:,0], soln[:,1], 'b')
plt.ylim(-10,10)
plt.xlim(-25,25)
plt.show()
