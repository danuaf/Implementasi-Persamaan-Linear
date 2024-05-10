from Metnum.MatrixBalikan import MatrixBalikan
from Metnum.LUGauss import LUGauss
from Metnum.Crout import Crout
from Dump.header import header as hd
import numpy as np

if __name__ == "__main__":
    hd.int1()
    hd.int2()
    opsi = int(input("Opsi Nomor: "))

    # ===============Menangkap Input dari User========================

    # Digunakan untuk input ordo matrik
    n = int(input("Masukkan ukuran matriks (n): "))

    # Digunaka untuk memasukan element matrix dengna menggunakan iterasi sesuai ordo yang dimasukan
    print("Masukkan elemen-elemen matriks A:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"A[{i+1}, {j+1}]: "))

    # Digunakan untuk memasukan element vektor satu persatu menggunakan iterasi juga
    print("Masukkan elemen-elemen vektor b:")
    b = np.zeros(n)
    for i in range(n):
        b[i] = float(input(f"b[{i+1}]: "))

    # Pengkondisian untuk opsi penyelesaian sesuai yang dipilih pengguna
    if opsi == 1:
        metode = MatrixBalikan(A, b)
        hasil = metode.hitung()
        print(f"Hasil dengan menggunakan metode matrix balikan adalah : {hasil}")
    elif opsi == 2:
        metode = LUGauss(A, b)
        hasil = metode.hitung()
        print(f"Hasil dengan menggunakan metode LU Gauss adalah : {hasil}")
    elif opsi == 3:
        metode = Crout(A, b)
        hasil = metode.hitung()
        print(f"Hasil dengan menggunakan metode Crout adalah : {hasil}")
    elif opsi == 4:
        metode1 = MatrixBalikan(A, b)
        hasil1 = metode1.hitung()
        metode2 = LUGauss(A, b)
        hasil2 = metode2.hitung()
        metode3 = Crout(A, b)
        hasil3 = metode3.hitung()
        print(f"Hasil dengan menggunakan metode matrix balikan adalah : {hasil1}")
        print(f"Hasil dengan menggunakan metode LU Gauss adalah : {hasil2}")
        print(f"Hasil dengan menggunakan metode Crout adalah : {hasil3}")
    else:
        print("Maaf, opsi yang anda pilih salah. Terimakasih telah menggunakan program ini")