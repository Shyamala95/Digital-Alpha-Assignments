import numpy as np
array2d=np.ndarray((3,5),dtype=int)
print("Dimension : ", array2d.shape)
array2d.fill(2)
print(array2d)
array3d = array2d.reshape(2,2,2)
print(array3d)
array3d+=5
print("After adding 5 :", array3d)
print(array3d)

array3d -= 2
print("After subtracting 5 :", array3d)
print(array3d)

array3d *= 2
print("After multiplying 5 :", array3d)
print(array3d)

