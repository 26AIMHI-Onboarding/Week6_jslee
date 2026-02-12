# coding: utf-8
import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 각 층의 행렬 연산 후 적절한 활성화 함수를 적용하세요. (교재 p.100)
    
    # 1층 연산 및 시그모이드 함수 적용
    a1 = np.dot(x,w1)+b1
    z1 = sigmoid(a1)
    
    # 2층 연산 및 시그모이드 함수 적용
    a2 = np.dot(z1,w2)+b2
    z2 = sigmoid(a2)
    
    # 3층(출력층) 연산 및 소프트맥스 함수 적용
    # 분류 문제에서는 마지막 출력층에 softmax를 사용합니다.
    a3 = np.dot(z2,w3)+b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network()

batch_size = 100 # 한 번에 묶어서 처리할 데이터의 양
accuracy_cnt = 0

# 배치 크기만큼 건너뛰며 데이터를 처리하세요. (교재 p.104)
for i in range(0, len(x), batch_size):
    # 1. 입력 데이터에서 배치 크기만큼 슬라이싱합니다.
    x_batch = x[i:i+batch_size]
    
    # 2. 배치 데이터를 한꺼번에 예측합니다.
    y_batch = predict(network, x_batch)
    
    # 3. 각 행(axis=1)에서 가장 확률이 높은 인덱스를 찾습니다.
    p = np.argmax(y_batch, axis=1)
    
    # 4. 예측 결과와 실제 정답(t)을 비교하여 맞힌 개수를 합산합니다.
    accuracy_cnt += np.sum(p==t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))