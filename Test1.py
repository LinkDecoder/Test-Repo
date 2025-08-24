import sympy, sys
import numpy as np
class Family:
    lastname = 'kim'
    def __init__(self):
        self.firstname= 'youname'

if __name__ == '__main__':
    A = np.array([[1,2],[3,4]],dtype=np.complex128)
    B = np.linalg.inv(A)
    print(A, ' \n', B)

    print(A.size)
    print(A.shape)
    print(np.matmul(A,B))

