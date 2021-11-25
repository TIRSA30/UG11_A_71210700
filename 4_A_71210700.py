#Nomor 4

def ambildanbalik(kalimat,mulai,akhir,data):
    if(data):
        A = kalimat[mulai-1:akhir]
        return(A[::-1])
    elif(not data):
        return(kalimat[mulai-1:akhir])
    else:
        print("Maaf, salah input")

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))
