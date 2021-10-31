
"""
Created on Fri Oct 29 13:40:14 2021

@author: rrfalkov
"""
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import xlrd, xlwt

exc_r = xlrd.open_workbook ('RR_215.xls')
sheet = exc_r.sheet_by_index(0)


x = np.array(sheet.col_values(0))
y = np.array(sheet.col_values(1))

def function_to_fit(x, a, b):
    return a*x + b

result = curve_fit(function_to_fit, x, y)
print(result)

err = 0.05 * x

plt.errorbar(x, y, fmt='bo', yerr=err)
a_opt, b_opt = result[0]
y_opt = a_opt*x + b_opt

plt.plot(x, y_opt, label='fitted line')
plt.grid()
plt.legend()
plt.plot(x, y, label='non-fitted line')
plt.plot(x, y,'r*')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('случайная зависимость')

