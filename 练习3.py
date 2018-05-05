import numpy as np
from scipy.optimize import leastsq
xi=np.array([0,1,2,3,-1,-2,-3])
yi=np.array([-1.21,1.9,3.2,10.3,2.2,3.71,8.7])


def func(p,x):
    a,b,c=p
    return a*x**2+b*x+c
def err(p,x,y,s):
    print (s)
    return func(p,x)-y
p0=[1,2,1]

s='leastsq 调用次数才能收敛'
Para=leastsq(err,p0,args=(xi,yi,s))
a,b,c=Para[0]
print('a=',a,'\n','b=',b,'\n','c=',c)
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(xi,yi,color='red',label='sample point',linewidth=3)
x=np.linspace(-5,5,1000)
y=a*x**2+b*x+c
plt.scatter(x,y,color='orange',label='Fit line',linewidth=0.5)
plt.legend()
plt.show()