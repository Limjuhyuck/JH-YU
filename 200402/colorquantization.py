import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg')

Z = img.reshape((-1, 3))
Z = np.float32(Z)

# criteria = 반복을 종료할 조건 (type, max_iter, epsilon)
# EPS (epsilon)-> 주어지는 정확도에 도달하면 반복 중단
# MAX_ITER (max iteration)-> 지정된 횟수만큼 반복하고 중단
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 7
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imshow('res2', res2)
cv2.waitKey(0)

cv2.destroyAllWindows()


# titles = ['image','colorquantization']
# images = [img, res2]
#
# for i in range(2):
#     plt.subplot(1, 2, i+1), plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
#
# plt.show()
