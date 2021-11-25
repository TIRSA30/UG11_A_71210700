#Nomor 2

def ambil_huruf(kalimat,index = 0):
    panjang_kalimat = len(kalimat)
    if panjang_kalimat%2 == 0:
        index_tengah = (panjang_kalimat / 2)
    else:
        index_tengah = panjang_kalimat//2
    hasil = kalimat[int(index_tengah)+index]

    return hasil
print(ambil_huruf("abcdefg",1))
print(ambil_huruf("abcdefg",2))
print(ambil_huruf("abcd"))
