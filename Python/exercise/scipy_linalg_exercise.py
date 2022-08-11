import numpy as np
from scipy import linalg

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
linalg.det(a)
linalg.inv(a)
linalg.eigvals(a)
linalg.eig(a)
linalg.lu(a)
linalg.qr(a)
linalg.svd(a)