import numpy as np

arr1 = np.array([2, 3, 4])

print(arr1)
print(arr1.dtype)
print('--------------')

arr2 = np.array([1, 2.2, 3.3])
print(arr2)
print(arr2.dtype)
print(arr1 + arr2)
print('--------------')

print(arr1 * 10)
print('--------------')

data = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(data)
print(arr3)
print(arr3.dtype)
print(arr3[0],arr3[1])
print('--------------')

# 创建多维矩阵
print(np.zeros((3, 5)))
print(np.ones((3, 5)))
print(np.empty((2, 3, 4)))
print('--------------')

arr4 = np.arange(10)
print(arr4)
print(arr4[5:8])
# 赋值
arr4[5:8] = 10
print(arr4)

# 赋值不改变原有值 副本
arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4)
