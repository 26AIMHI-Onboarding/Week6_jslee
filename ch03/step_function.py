# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype=int)

# -5.0부터 5.0까지 0.1 간격의 넘파이 배열 생성
X = np.arange(-5.0, 5.0, 0.1)

# 위에서 정의한 step_function을 호출하여 Y값을 계산하세요.
Y = step_function(X)

# 그래프를 그립니다.
plt.plot(X, Y)
# y축의 범위를 0과 1이 명확히 보이도록 설정
plt.ylim(-0.1, 1.1) 
plt.show()