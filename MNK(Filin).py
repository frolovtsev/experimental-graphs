import numpy as np
import matplotlib.pyplot as plt
import openpyxl

wookbook = openpyxl.load_workbook("Data.xlsx")
worksheet = wookbook.active

x = np.array([[i.value for i in m] for m in worksheet['A2':'A5']])
y = np.array([[i.value for i in m] for m in worksheet['B2':'B5']])
yerr = np.array([[i.value for i in m] for m in worksheet['C2':'C5']])

x = x.flatten()
y = y.flatten()
yerr = yerr.flatten()

A = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, y, rcond=None)[0]
print('Уравнение: x = A * y + B' '\n' 'Коэффициенты:' '\n' "Slope: A =",a, '\n' 'Intercept: B =',b)


plt.plot(x, (a * x + b), color="red", linewidth = 1.5, label='Зависимость')
plt.scatter(x, y, s=8, color="skyblue", marker="s", label='Экспериментальные данные')
plt.errorbar(x, y, yerr, fmt=".", elinewidth=0.7)

plt.xlim([290, 360])
plt.ylim([0.55, 0.75])
plt.legend()
plt.xlabel('Напряжение на диоде U, V')
plt.ylabel('Температура диода, k')
plt.suptitle('Зависимость напряжения на диоде U,от температуры диода')
plt.grid() 
plt.show() 