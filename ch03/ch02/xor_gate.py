from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1, x2):
    """
    XOR 게이트 구현 (교재 p.59)
    NAND, OR, AND 게이트를 적절히 조합하여 비선형 영역을 분리하세요.
    """
    # 1. 0층에서 1층으로 가는 신호 전달 (NAND와 OR 활용)
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    
    # 2. 1층에서 2층으로 가는 최종 신호 전달 (AND 활용)
    y = AND(s1, s2)
    
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))