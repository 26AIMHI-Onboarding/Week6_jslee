import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    # 넘파이 배열을 PIL용 이미지 객체로 변환
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# 1. MNIST 데이터를 불러오세요. (교재 p.99)
# flatten=True는 1차원 배열로, normalize=False는 0~255 값을 유지합니다.
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 5

# 2. 이미지의 형상을 확인하고, 다시 28x28 크기로 변형하세요. (교재 p.100)
print(img.shape)  # flatten=True 이므로 (784,)가 출력됨
img = img.reshape(28, 28)
print(img.shape)  

img_show(img)