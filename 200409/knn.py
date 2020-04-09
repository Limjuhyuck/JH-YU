import cv2
import numpy as np
import matplotlib.pyplot as plt
# 난수 생성자를 이용하여 랜덤으로 빨간색 군과 파란색 군 생성
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)

# 각각 라벨링
responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# 빨간색 군들을 표시
red = trainData[responses.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

# 파란색 군들을 표시
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

# 새로운 요소 표시
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

# kNN을 이용하여 분류
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

# 결과
print("result: ", results)
print("neighbours: ", neighbours)
print("distance: ", dist)

plt.show()

