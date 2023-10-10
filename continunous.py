import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-5,5,0.1)
y=np.cos(x*np.pi/2)
plt.plot(x,y)
plt.title("sin(πx/2)")
plt.show()