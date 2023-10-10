import matplotlib.pyplot as plt
import numpy as py
def impluse(x):
    if x==0:
        return 1
    else:
        return 0
x= range(-11,10)
y=[impluse(i) for i in x]
plt.plot(x,y,marker='o')
plt.title("impluse")
plt.show()