import numpy as np
import matplotlib.pyplot as plt

#parameter yang digunakan
n = 1000000
t = np.logspace(np.log10(10),np.log10(500),n)

#silahkan merubah parameter ini
A = [ 3, 6, 1.5, 1.5 ]
d = [ .004, .001, .002, .0015 ]
f = [ 3, 1, 2, 2.5 ]

#membuat pasangan x dan y
x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t)
y = A[2]*np.sin(t*f[2])*np.exp(-d[2]*t) + A[3]*np.sin(t*f[3])*np.exp(-d[3]*t)

#menampilkan plotnya
plt.plot(x,y,'k',linewidth=.1)
plt.axis('off')
plt.show()