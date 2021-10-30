# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:33:02 2021

@author: Сергей
"""
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
book = openpyxl.open('D:\Pyton\exersizes\data2.xlsx', read_only=True)
sheet = book.active

x = []
y = []
xx = []
yy = []
YYerr = []
nameX = sheet[1][0].value
nameY = sheet[1][1].value
for row in range(2,sheet.max_row+1):
    xx.append(sheet[row][0].value)
    yy.append(sheet[row][1].value)
    YYerr.append(sheet[row][2].value)
x = np.array(xx)
y = np.array(yy)
Yerr = np.array(YYerr)
n = sheet.max_row-1

sx = 0;
for i in range(n): 
    sx = sx + x[i]
sy = 0;
for i in range(n):
    sy = sy + y[i]
sxx = 0;
for i in range(n): 
    sxx = sxx + x[i]*x[i]
sxy = 0;
for i in range(n): 
    sxy = sxy + y[i]*x[i]
syy = 0;
for i in range(n): 
    syy = syy + y[i]*y[i]
    
A = (sy*sxx - sx*sxy) / (n * sxx - sx * sx)
B = (n * sxy - sx * sy) / (n * sxx - sx * sx)
min0 = x.min()
max0 = x.max()
x0 = np.array([min0,max0])
y0 = np.array([min0*B + A,max0*B + A])


plt.xlabel(nameX)
plt.ylabel(nameY)
plt.grid()

plt.scatter(x, y)
plt.plot(x0, y0, color = 'brown')
plt.errorbar(x, y, yerr=Yerr,fmt='o')

plt.show()



Sy2 = 0;
for i in range(n): 
    Sy2 = Sy2 + (y[i] - A - B*x[i]) * (y[i] - A - B*x[i])
Sy2 = Sy2/(n-2)
SA = (Sy2*sxx/(n*sxx - sx*sx))**0.5
SB = (Sy2*n/(n*sxx - sx*sx))**0.5

print('y  =  a + bx')
print( 'a  = ', A)
print( 'Sa = ', SA)
print( 'b  = ', B)
print('Sb = ', SB)
