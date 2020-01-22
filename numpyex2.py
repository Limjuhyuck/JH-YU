import numpy as np

# 배열 합치기
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1,array2])

print(array3)
print(array3.shape) #크기출력

#numpy는 배열의 형태를 자유자재로 변경 가능
array4 = np.array([1,2,3,4])     #1차원 배열
array5 = array4.reshape((2,2))   #2차원 배열

print(array4)
print(array5)

# Numpy 배열 세로 축으로 합치기
array6 = np.arange(4).reshape(1,4) #0부터 4까지의 1차원 배열
array7 = np.arange(8).reshape(2,4) #0부터 8까지의 2차원 배열

print(array6)
print(array7)

#axis=0을 붙이면 배열이 세로로 합쳐진다. 옆에 붙는 것이 아니라 세로로.
array8 = np.concatenate([array6,array7],axis=0)
print(array8)

# 배열 나누기 (axis=0 -> 행, axis=1 -> 열)
array = np.arange(8).reshape(2,4)
left, right = np.split(array, [2],axis=1) #2열을 기준으로 나누기
print(left.shape)
print(right.shape)
print(array)
print(left)
print(right)