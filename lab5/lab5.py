import numpy as np
import matplotlib.pyplot as plt

x = np.array([234, 114, 169, 137, 170, 127])    #mileage
y = np.array([21.9, 24.5, 25.5, 22.8, 21.9, 24.8])     #price
n = len(x)
x_ = np.sum(x)/n
x_array = np.full(n, x_)
y_ = np.sum(y)/n


b1 = ((((np.sum(np.multiply(x, y)))) / n) - (x_ * y_)) / (np.sum(np.subtract(np.power(x, 2), np.power(x_, 2)) / n))
b0 = y_ - (b1 * x_)


pred = b0 + np.multiply(x,b1)
print(pred)
plt.figure()
plt.scatter (x, y)
plt.plot(x, pred)
plt.show()