import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0, 5.0, 0.1)

# 위에서 정의한 relu 함수를 호출하여 y값을 계산하세요.
y = relu(x)

plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()