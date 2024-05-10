import numpy as np

class Crout:
    def __init__(self, A, b):
        self.A = A
        self.b = b
    
    def hitung(self):
        # Ini sama seperti pada implementasi di code LU Gauss
        n = len(self.A)
        L = np.zeros((n, n))
        U = np.zeros((n, n))

        for i in range(n):
            L[i, i] = 1

            for j in range(i, n):
                L[j, i] = self.A[j, i] - np.dot(L[j, :i], U[:i, i])
            
            for j in range(i, n):
                U[i, j] = (self.A[i, j] - np.dot(L[i, :i], U[:i, j])) / L[i, i]

        # Menghitung hasil dari persamaan, dimana hasilnya akan hasilkan ditampung pada variable x
        y = np.linalg.solve(L, self.b)
        x = np.linalg.solve(U, y)

        return x