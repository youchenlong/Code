import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, curve_fit


"""
=================================
minimize
=================================
"""
def func(x):
    return x[0]**2 + x[1]**2 + x[2]**2 + 8

cons = ({'type':'ineq', 'fun':lambda x: x[0]**2 - x[1] + x[2]**3},
        {'type':'ineq', 'fun':lambda x: -(x[0] + x[1] + x[2]**2 - 20)},
        {'type': 'eq', 'fun':lambda x: -(x[0] + x[1]**2 - 2)},
        {'type': 'eq', 'fun':lambda x: x[1] + 2*x[2]**2 - 3})

bnds = ((0,None), (0, None), (0, None))

res = minimize(fun=func, x0=[0,0,0], constraints=cons, bounds=bnds)
print(res.x)


"""
=================================
curve_fit
=================================
"""
def func(x, A, B, C):
    return A*x*x + B*x + C
x = np.linspace(0, 10, 100)
y = x**2
y_noise = y + np.random.normal(loc=0, scale=5, size=x.size)
popt, pcov = curve_fit(func, x, y_noise)
print(popt)
fig ,ax = plt.subplots()
ax.plot(x, y, color='red')
ax.plot(x, func(x, *popt), color='green')
ax.legend(['real', 'predict'])
plt.show()