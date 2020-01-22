import numpy as np

list_data = [1, 2, 3]
array = np.array(list_data)

print(array.size)
print(array.dtype)
print(array[2])

# # 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 4*4의 배열을 만들며 0으로 초기화 되어있고 각각 실수형 데이터 타입을 가진다.
array2 = np.zeros((4, 4), dtype = float)
print(array2)
# 4*4의 배열을 만들며 0으로 초기화 되어있고 각각 문자열 데이터 타입을 가진다.
array3 = np.ones((4, 4), dtype=str)
print(array3)

# 0 부터 9까지 랜덤하게 초기화 된 배열 만들기 np.random.randint(x,y,(a,b)) x부터 y-1까지 axb 행렬 만든다.

array4 = np.random.randint(0, 10, (3,3))
print(array4)

# 평균이 0이고, 표준 편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0,1,(3,3))
print(array5)