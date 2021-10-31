import matplotlib.pyplot as plt
import numpy as np

mnk = np.genfromtxt ('МНК.txt')

i = 0
x = np.array([])
y = np.array([])
error = np.array([])
while i <= np.shape(mnk)[0]-1:
    x=np.append(x, mnk[i][0])
    y=np.append(y, mnk[i][1])
    error=np.append(error,mnk[i][2])
    i+=1
plt.title ("Обработка МНК")
plt.scatter(x, y, s=8)
plt.errorbar(x,y,error, fmt=".")
A = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, y, rcond=None)[0]
plt.plot(x, x*a+b)
plt.xlabel('Сила тока в контуре I, А')
plt.ylabel('Момент силы M, Нм')
plt.show()