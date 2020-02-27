# 1 단계 : 노이즈 제거
# 2 단계 : Gradient 값이 높은 부분 찾기
# 3 단계 : 최대값이 아닌 픽셀 값은 0으로 만들기
# 4 단계 : Hyteresis Thresholding
import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny():
    img = cv2.imread('son.jpg', cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200) #Canny(imgname, 한계값, 한계값)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)

    titles = ['origin', 'edge1', 'edge2', 'edge3']
    images = [img, edge1, edge2, edge3]

    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

    cv2.waitKey(0)
    cv2.destoryAllWindows()

canny()
