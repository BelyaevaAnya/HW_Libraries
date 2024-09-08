import numpy as np
import matplotlib.pyplot as plt
import scipy

# np.arange
# np.savez
# del
# whos
# np.load
# np.block
# np.newaxis
# np.savetxt
# np.loadtxt

#SavingSharing NumPy arrays
x = np.arange(10)
y = x ** 2
print(x)
print(y)
np.savez("./NumpyFiles/x_y-squared.npz", x_axis=x, y_axis=y)
del x, y
load_xy = np.load("./NumpyFiles/x_y-squared.npz")
print(load_xy.files)
x = load_xy["x_axis"]
y = load_xy["y_axis"]
print(x)
print(y)
array_out = np.block([x[:, np.newaxis], y[:, np.newaxis]])
print("the output array has shape ", array_out.shape, " with values:")
print(array_out)
np.savetxt("./NumpyFiles/x_y-squared_1.csv", X=array_out, header="x, y", delimiter=",")
del x, y
load_xy = np.loadtxt("./NumpyFiles/x_y-squared_1.csv", delimiter=",")
print(load_xy.shape)
x = load_xy[:, 0]
y = load_xy[:, 1]
print(x)
print(y)


import numpy as np

list = [1, 2, 3, 4]
sample_array = np.array(list)
print("List in python : ", list)
print("Numpy Array in python :",
      sample_array)
print(type(list))
print(type(sample_array))


list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
sample_array = np.array([list_1,
                         list_2,
                         list_3])
print("Numpy multi dimensional array in python\n",
      sample_array)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
sample_array = np.array([list_1,
                         list_2,
                         list_3])
print("Numpy array :")
print(sample_array)
print("Shape of the array :",
      sample_array.shape)

sample_array = np.array([[0, 4, 2],
                       [3, 4, 5],
                       [23, 4, 5],
                       [2, 34, 5],
                       [5, 6, 7]])

print("shape of the array :",
      sample_array.shape)

sample_array_1 = np.array([[0, 4, 2]])
sample_array_2 = np.array([0.2, 0.4, 2.4])
print("Data type of the array 1 :",
      sample_array_1.dtype)
print("Data type of array 2 :",
      sample_array_2.dtype)

arr = np.array([3,4,5,5])
print("Array :",arr)

iterable = (a*a for a in range(8))
arr = np.fromiter(iterable, float)
print("fromiter() array :",arr)

var = "KakPoniat'ChtoSluchilos'"
arr = np.fromiter(var, dtype = 'U2')
print("fromiter() array :",
      arr)

print(np.arange(1, 20 , 2,
          dtype = np.float32))

print(np.linspace(3.5, 10, 3))

print(np.linspace(3.5, 10, 3,
            dtype = np.int32))

print(np.empty([4, 3],
         dtype = np.int32,
         order = 'f'))

print(np.ones([4, 3],
        dtype = np.int32,
        order = 'f'))

print(np.zeros([4, 3],
         dtype = np.int32,
         order = 'f'))