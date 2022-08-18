import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = np.linspace(0, 5, 10)
y1 = x1**2
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'red')
plt.title('Days Squared Chart')
plt.xlabel('Days')
plt.ylabel('Days Squared')
plt.subplot(1, 2, 2)
plt.plot(x1, y1, 'blue')
plt.title('Days Squared Chart')
plt.xlabel('Days')
plt.ylabel('Days Squared')

plt.show()
