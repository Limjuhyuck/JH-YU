# 이미지에서 잡음 제거
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('noise.jpg')

dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()

# 영상에서 잡음 제거
cap = cv2.VideoCapture('movie.mp4')

img = [cap.read()[1] for i in range(5)]

gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]

gray = [np.float64(i) for i in gray]

noise = np.random.randn(*gray[1].shape) * 10

noisy = [i + noise for i in gray]

noisy = [np.uint8(np.clip(i, 0, 255)) for i in noisy]

dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)

plt.subplot(131), plt.imshow(gray[2], 'gray') # 원본
plt.subplot(132), plt.imshow(noisy[2], 'gray') # 이미지에 noise 더한 것
plt.subplot(133), plt.imshow(dst, 'gray') # noise 제거
plt.show()



