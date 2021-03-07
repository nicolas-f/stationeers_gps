import matplotlib.pyplot as plt
import numpy as np
import math

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# x = np.arange(100)
# y = []
# for vx in x:
#     y.append((1/math.log10(vx + 1.52595396)) - 0.44836111)
# ax.plot(x, y)  # Plot some data on the axes.
# plt.show()


fig, ax = plt.subplots()  # Create a figure containing a single axes.
totalmoles = 0
target_moles = 248
debit = 0.1
tick_mole = 0.5
cur_tick = 0
x = []
y = []
while True:
    cur_tick += 1
    x.append(cur_tick)
    totalmoles += tick_mole
    debit = max(0.05, (1 - totalmoles / target_moles) * 15)
    tick_mole = debit * 5
    y.append(totalmoles)
    if totalmoles >= target_moles:
        break
print(cur_tick)
print(totalmoles)
ax.plot(x, y)  # Plot some data on the axes.
plt.show()