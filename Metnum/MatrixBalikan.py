import numpy as np

class MatrixBalikan:
    def __init__(self, A, b):
        self.A = A
        self.b = b
    
    def hitung(self):
        # Menghitung determinan matrix A
        determinanA = np.linalg.det(self.A)

        # Cek apakah Matrix A memiliki determinant
        if determinanA != 0:
            # Hitung matriks balikan A
            inversA = np.linalg.inv(self.A)

            # Hitung solusi x
            x = np.dot(inversA, self.b)

            return x

        else:
            return "Matriks A tidak memiliki invers"