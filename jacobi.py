import numpy as np
'''
a = np.array([1.59, -0.4, -0.54])
b = np.array([-0.4, 1.7, 0.4])
c = np.array([-0.54, 0.4, 0.54])

y = np.append(a,b)
y = np.append(y,c)
y = y.reshape(3,3)
forca = np.array([0, 150, -100])
forca = forca.reshape(3,1)
'''
def obe_j(ite, tol, k, f):
    x = np.zeros(len(k[0]))

    counter = 0 
    while counter < ite:
        temp_l = []
        x_temp = x.copy()
        for i in range(len(f)):
            temp_l.append(np.multiply(x, k[i]))


        for j in range(len(x)):
            r = 0
            for l in range(len(temp_l)):
                if j == l:
                    r += 0
                    continue
                r += temp_l[j][l]
            x[j] = (f[j]-r)/k[j][j]


        for m in range(len(x)):
            if (abs(x[m]-x_temp[m]) < tol) and abs(x[m]-x_temp[m]) != 0:
                return x
            
        counter += 1

    return x
