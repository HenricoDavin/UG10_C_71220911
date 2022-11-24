a= str (input("Masukkan daftar pesanan : "))
b= print("Daftar pesanan : ", [a])
c= str(input("Masukkan pesanan yang ingin ditambahkan : "))

list = a

if c in list:
    print (c.upper(), "sudah berada dalam daftar pesanan")
else:
    print ("Hasil penambahan pada daftar pesanan : ", [a.upper(),c.upper()])
