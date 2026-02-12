# coding: utf-8
import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    
    # NAND 게이트가 작동하도록 적절한 가중치와 편향을 설정하세요.
    # 힌트: AND 게이트의 부호를 반전시켜보세요. (교재 p.53)
    w = np.array([-0.5, -0.5]) 
    b = 0.7
    
    # 퍼셉트론의 연산 식을 완성하세요 (입력값과 가중치의 곱의 합 + 편향)
    tmp = np.sum(w*x)+b
    
    # 활성화 함수(임계값을 넘으면 1, 아니면 0)를 구현하세요
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))