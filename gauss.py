import numpy as np

def sistema(ite, tol, a, b):
    n = len(a)
    x = np.zeros(n)
    x_old = np.zeros(n)
    erro = 0
    i = 0
    while i < ite and erro < tol:
        for l in range(0,n):
            s=0
            for c in range(0, n):
                s-=(a[l,c])*(x[c])
            s += x[l]*a[l,l]
            x[l]=(b[l]+s)/(a[l,l])
        erro = max(np.divide(np.subtract(x, x_old), x+1))
        x_old = x
        i += 1
    print(i)
    print(x)

a = np.array([[1.59*(10**8),-0.40*(10**8), -0.54*(10**8)],[-0.40*(10**8),1.70*(10**8), 0.40*(10**8)],[-0.54*(10**8), 0.40*(10**8), 0.54*(10**8)]])
f = np.array([0.0,150.0,-100.0])

sistema(5000, 0.0001, a, f)