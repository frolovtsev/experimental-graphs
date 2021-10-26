import matplotlib.pyplot as plt
import numpy as np
import openpyxl as xl


book = xl.open("list for mnk.xlsx", read_only=True)
sheet = book.active
x = []
y = []
y_error = []
for row in range(2, sheet.max_row+1):
    x.append(sheet[row][0].value)
    y.append(sheet[row][1].value)
    y_error.append(sheet[row][2].value)

x = np.array(x)
y = np.array(y)
y_error = np.array(y_error)


# Метод 1
mnk = np.polyfit(x, y, 1)
print("Коэффициенты, полученные первым методом: a = ", mnk[0], ', b = ', mnk[1])

# Метод 2
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print("Коэффициенты, полученные вторым методом: a = ", m, ', b = ', c)

# Строим график
plt.scatter(x, y)
plt.errorbar(x, y, yerr = y_error, fmt=".b" )
plt.plot(x, m * x + c, 'r')
plt.xlabel(sheet[1][0].value)
plt.ylabel(sheet[1][1].value)
plt.grid()
help(plt.errorbar)

plt.suptitle('Зависимость силы тока от напряжения по закону трёх вторых')
plt.savefig('grafic.png')
plt.show()
