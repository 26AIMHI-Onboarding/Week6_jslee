import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1/(1+np.exp(-x))


def step_function(x):
    return np.array(x>0, dtype=int)

x = np.arange(-5.0, 5.0, 0.1)

## 시그모이드 함수 결과 계산
y1 = sigmoid(x)

## 계단 함수 결과 계산
y2 = step_function(x)

plt.plot(x, y1)
plt.plot(x, y2, 'k--')
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()