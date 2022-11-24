print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")

a =input("Masukan angka pertama: ")
b =input("Masukan angka kedua: ")
c =input ("Pilihan Anda: ")


if c ==("1"):
    print (int(a) + int(b))

elif c ==("2"):
    print (int(a) - int(b))

elif c ==("3"):
    print (int(a) * int(b))
elif c ==("4"):
    print (float(a) / float(b))

