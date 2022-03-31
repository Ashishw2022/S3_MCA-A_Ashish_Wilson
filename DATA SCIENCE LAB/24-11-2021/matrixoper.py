import numpy
x=numpy.array([[2,4],[7,5]])
y=numpy.array([[5,6],[4,7]])

print("Matrix Addition")
print(numpy.add(x,y))

print("Matrix Subraction")
print(numpy.subtract(x,y))

print("Matrix multiplication")
print(numpy.multiply(x,y))


print("Matrix product")
print(numpy.dot(x,y))

print("Matrix square root")
print(numpy.sqrt(x))

print("Matrix divison")
print(numpy.divide(x,y))

print("Matrix sum of element")
print(numpy.sum(x))

print("Matrix sum of elements (x-axis)")
print(numpy.sum(x,axis=0))

print("Matrix Transpose of x")
print(x.T)
