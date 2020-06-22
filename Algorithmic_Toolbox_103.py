import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(1, 100)
f = plt.figure(1)
plt.plot(n, 7 * n * n + 6 * n + 5)

f = plt.figure(2)
plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
plt.plot(n, 20 * n, label="20n")
plt.legend(loc='upper left')

n = np.linspace(1, 5)
f = plt.figure(3)
plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
plt.plot(n, 7 * n * n, label="7n^2")
plt.legend(loc='upper left')
plt.show()
f.show()
