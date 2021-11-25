#Test Case 1, 2, 3:
print("======== Calculator sederhana ========")

print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")

a = int(input("Masukan pilihan:"))
x = int(input("Masukan bilangan 1: "))
y = int(input("Masukan bilanga 2: "))

def calculator(a):
    if(a == 1):
        print("Hasilnya: ",tambah(x,y))
    elif(a == 2):
        print("Hasilnya: ",kurang(x,y))
    elif(a == 3):
        print("Hasilnya: ",kali(x,y))
    elif(a == 4):
        print("Hasilnya: ",bagi(x,y))
    elif(a == 5):
        print("Hasilnya: ",pangkat(x,y))
    else:
        print("Hasilnya: Maaf input operasi antar 1-5")

def tambah(x,y):
    tambah = x+y
    return tambah
def kurang(x,y):
    kurang = x-y
    return kurang
def kali(x,y):
    kali = x*y
    return kali
def bagi(x,y):
    kurang = x/y
    return bagi
def pangkat(x,y):
    pangkat = x**y
    return pangkat

calculator(a)
