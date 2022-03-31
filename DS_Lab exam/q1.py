import numpy as np
A=np.array([[2,4],[4,2]])
B=np.array([[3,4],[6,7]])
C=np.array([[5,6],[7,8]])
print("Matrix A \n",A,"\nMatrix B \n",B,"\nMatrix C \n",C)
ab=np.dot(A,B)
bb=np.power(B,2)
mb=np.multiply(bb,4)
dc=np.divide(C,4)
total=ab+mb-dc
print("\n Total\n",total)
