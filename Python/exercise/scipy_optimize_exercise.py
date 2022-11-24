import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog, minimize, curve_fit


# linear programing
c = np.array([-2, -3, 5])
A_ub = np.array([[-2, 5, -1], [1, 3, 1]])
B_ub = np.array([-10, 12])
A_eq = np.array([[1, 1, 1]])
B_eq = np.array([7])
x1 = (0, 7)
x2 = (0, 7)
x3 = (0, 7)
res = linprog(c, A_ub, B_ub, A_eq, B_eq, bounds=(x1, x2, x3))
print(res.x)

# nonlinear problems
fun = lambda x: x[0]**2 + x[1]**2 + x[2]**2 + 8
constraints = ({'type':'ineq', 'fun':lambda x: x[0]**2 - x[1] + x[2]**3},
        {'type':'ineq', 'fun':lambda x: -(x[0] + x[1] + x[2]**2 - 20)},
        {'type': 'eq', 'fun':lambda x: -(x[0] + x[1]**2 - 2)},
        {'type': 'eq', 'fun':lambda x: x[1] + 2*x[2]**2 - 3})
bounds = ((0,None), (0, None), (0, None))
res = minimize(fun=fun, x0=[0,0,0], constraints=constraints, bounds=bounds)
print(res.x)

# curve_fit
fun = lambda x, A, B, C: A*x*x + B*x + C
x = np.linspace(0, 10, 100)
y = x**2
y_noise = y + np.random.normal(loc=0, scale=5, size=x.size)
popt, pcov = curve_fit(fun, x, y_noise)
print(popt)
fig ,ax = plt.subplots()
ax.plot(x, y, color='red')
ax.plot(x, fun(x, *popt), color='green')
ax.legend(['real', 'predict'])
plt.show()