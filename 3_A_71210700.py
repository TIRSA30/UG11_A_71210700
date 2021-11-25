#Nomor 3

A = input("Masukan Kalimat: ")
B = int(input("Index Start: "))
C = int(input("Index Stop: "))

def hitung_hapus(A,B,C):
    m = len(A)
    n = len(A[B:C+1])
    total = (n/m) * 100

    return total

print(hitung_hapus(A,B,C))
