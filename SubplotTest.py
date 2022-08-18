import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = np.linspace(0, 5, 10)
y1 = x1**2

fig2, axes2 = plt.subplots(figsize=(8, 4), nrows=1, ncols=3)
plt.tight_layout()
axes2[1].set_title('Plot 2')
axes2[1].set_xlabel('X')
axes2[1].set_ylabel('X^2')
axes2[1].plot(x1, y1)

plt.show()
