from Metnum.LUGauss import LUGauss
from Metnum.MatrixBalikan import MatrixBalikan
from Metnum.Crout import Crout

import numpy as np


A = np.array([[2, 1, -1], [3, 2, 1], [1, 1, 1]])
b = np.array([4, 5, 6])


metode1 = MatrixBalikan(A, b)
hasil1 = metode1.hitung()
print(f"Hasil dengan menggunakan metode matrix balikan adalah : {hasil1}")
# metode2 = LUGauss(A, b)
# hasil2 = LUGauss.hitung()
# metode3 = Crout(A, b)
# hasil3 = Crout.hitung()
# print(f"Hasil dengan menggunakan metode LU Gauss adalah : {hasil2}")
# print(f"Hasil dengan menggunakan metode Crout adalah : {hasil3}")