import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    # 학습된 가중치 매개변수를 읽어옵니다. 
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 각 층의 행렬 연산 후 적절한 활성화 함수를 적용하세요. (교재 p.100)
    
    # 1층 연산 및 시그모이드 함수 적용
    a1 = np.dot(x,W1)+b1
    z1 = sigmoid(a1)
    
    # 2층 연산 및 시그모이드 함수 적용
    a2 = np.dot(z1,W2)+b2
    z2 = sigmoid(a2)
    
    # 3층(출력층) 연산 및 소프트맥스 함수 적용
    # 분류 문제에서는 마지막 출력층에 softmax를 사용합니다.
    a3 = np.dot(z2,W3)+b3
    y = softmax(a3)

    return y


# 1. 데이터셋과 네트워크 초기화
x, t = get_data()
network = init_network()
accuracy_cnt = 0

# 2. 이미지를 한 장씩 꺼내 정확도를 측정합니다.
for i in range(len(x)):
    y = predict(network, x[i])
    
    # 출력된 10개의 확률 값 중 가장 큰 인덱스를 예측값으로 선택
    p = np.argmax(y)
    
    if p == t[i]:
        accuracy_cnt += 1

# 3. 전체 데이터 중 맞힌 개수의 비율을 출력합니다.
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))