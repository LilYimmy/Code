#Brandon Yim Linear Algebra program
import numpy as np
print("This is a cross multiplyer for vectors")
x = list(map(int, input("Input the values here and have a space between every number ").split()))
print("The first vector is ",x)
y = list(map(int, input("Input the values of the second vector ").split()))
print("The second vector is ", y)
final = np.cross(x,y)
print("The two multiplied vectors equal ", final)
