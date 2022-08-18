import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = np.linspace(0, 5, 10)
y1 = x1**2

fig1 = plt.figure(figsize=(5, 4), dpi=100)
axes1 = fig1.add_axes([0.1, 0.1, 0.9, 0.9])
axes1.set_xlabel('Days')
axes1.set_ylabel('Days Squared')
axes1.set_title('Days Squared Chart')
axes1.plot(x1, y1, label='x/x^2')
axes1.plot(y1, x1, label='x^2/x')
axes1.legend(loc=0)

axes2 = fig1.add_axes([0.45, 0.45, 0.4, 0.3])
axes2.set_xlabel('Days')
axes2.set_ylabel('Days Squared')
axes2.set_title('Days Squared Chart')
axes2.plot(x1, y1, 'red')
axes2.text(0, 40, 'Message')
plt.show()
