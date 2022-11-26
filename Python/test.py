from scipy.optimize import minimize

fun = lambda x: (x[0]-3)**2 + (x[1]-2)**2
constraints = ({'type':'ineq', 'fun':lambda x: -(x[0]**2 + x[1]**2 - 5)},
        {'type':'ineq', 'fun':lambda x: -(x[0] + 2*x[1] - 4)})

res = minimize(fun=fun, x0=[0,0], constraints=constraints)
print(res)