import math
import numpy as np
import matplotlib.pyplot as plt

def von_Neumann_rejection(arr, N):
    x_count_list = [0 for i in range(len(arr))]
    for k in range(N):
        x = np.random.rand() * (len(arr) - 1)
        y = np.random.rand() * max(arr)
        x_near = round(x) # 四捨五入
        if arr[int(x_near)] >= y:
            x_count_list[int(x_near)] += 1

    return x_count_list

def normalize(arr):
    return arr / np.linalg.norm(arr)

if __name__ == '__main__':

    # x: [x_min, x_max], y:[0, y_max]
    N = 10000000
    fs = 100 # 配列の長さ
    pi = math.pi
    x  = np.linspace(-4*pi, 4*pi, fs)

    f = np.sin(x) + np.cos(x) + 100 # 元の関数
    f_count_list = von_Neumann_rejection(f, N) # 乱数のカウント

    plt.plot(normalize(f)) # 元の関数を正規化
    plt.plot(normalize(f_count_list)) # 乱数のカウントを正規化
    plt.show()
