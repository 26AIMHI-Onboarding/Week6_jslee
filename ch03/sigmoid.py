# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# -5.0부터 5.0까지 0.1 간격의 넘파이 배열 생성
X = np.arange(-5.0, 5.0, 0.1)

# 위에서 정의한 sigmoid 함수를 호출하여 Y값을 계산하세요.
Y = sigmoid(X)

plt.plot(X, Y)
# y축의 범위를 0과 1 사이가 잘 보이도록 설정
plt.ylim(-0.1, 1.1) 
plt.show()