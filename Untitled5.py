#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import matplotlib.pyplot as plt
import openpyxl
book = openpyxl.open(r'C:\Users\Liaisan\Desktop\data.xlsx', read_only=True)
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

sum_x = 0;
for i in range(n): 
    sum_x = sum_x + x[i]
sum_y = 0;
for i in range(n):
    sum_y = sum_y + y[i]
sum_xx = 0;
for i in range(n): 
    sum_xx = sum_xx + x[i]**2
sum_xy = 0;
for i in range(n): 
    sum_xy = sum_xy + y[i]*x[i]
sum_yy = 0;
for i in range(n): 
    sum_yy = sum_yy + y[i]**2
    
B = (sum_y*sum_xx - sum_x*sum_xy) / (n * sum_xx - sum_x**2)
K = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
min0 = x.min()
max0 = x.max()
x0 = np.array([min0,max0])
y0 = np.array([min0*K + B,max0*K + B])

plt.xlabel(nameX)
plt.ylabel(nameY)
plt.grid()

plt.scatter(x, y)
plt.plot(x0, y0, color = 'pink')
plt.errorbar(x, y, yerr=Yerr,fmt='o')

plt.show()

Sum_y2 = 0;
for i in range(n): 
    Sum_y2 = Sum_y2 + (y[i] - B - K*x[i])**2
Sum_y2 = Sum_y2/(n-2)
SB = (Sum_y2*sum_xx/(n*sum_xx - sum_x**2))**0.5
SK = (Sum_y2*n/(n*sum_xx - sum_x**2))**0.5

print('y  =  kx + b')
print( 'b  = ', B)
print( 'Sb = ', SB)
print( 'k  = ', K)
print('Sk = ', SK)


# In[ ]:





# In[ ]:




