# latihan_Dasar_Pemograman
Nama: Dimas Arbi Ardian
NIM: 20220040165
Kelas: TI J 2022
Prodi: Teknik Informatika


# Cara Pertama
print("===== Program Nilai Kelulusan =====")
nilai = int(input("Inputkan nilai akhir: "))
if (nilai >= 90) and (nilai <=100):
 grade = "A (Dengan Pujian)"
elif (nilai >= 80) and (nilai <=89):
 grade = "B (Sangat Memuaskan)"
elif (nilai >= 70) and (nilai <=79):
 grade = "C (Memuaskan)"
elif (nilai >= 60) and (nilai <=69):
 grade = "D (Tidak Memuaskan)"
elif (nilai >= 0) and (nilai <=59):
 grade = "E (Tidak LULUS)"
else:
    while nilai % 3 != 1 or nilai > 100:
        nilai = int(input('Masukkan lagi: '))
    print ("Benar")

print ("Hasil akhir","Grade Anda: ", grade)


# Cara Kedua
print("===== Program Nilai Kelulusan =====")
while True:
    try:
        nilai = int(input("Inputkan nilai akhir: "))
    except ValueError:
        print("Inputan harus berupa number")
    else:
        if (nilai >= 90) and (nilai <=100):
            print("")
            print("A")
            print("Dengan Pujian")
        elif (nilai >= 80) and (nilai <=89):
            print("")
            print("B")
            print("Sangat Memuaskan")
        elif (nilai >= 70) and (nilai <=79):
            print("")
            print("C")
            print("Memuaskan")
        elif (nilai >= 60) and (nilai <=69):
            print("")
            print("D")
            print("Tidak Memuaskan")
        elif (nilai >= 0) and (nilai <=59):
            print("")
            print("E")
            print("Tidak LULUS")
        else:
            "Invalid Input"
# Tugas Sesi 7
def Luas_Segitiga():
    print("🔺Hitung Luas Segitiga🔻")
    alas = int(input('Masukan alasnya: '))
    tinggi = int(input('Masukan tingginya: '))
    Luas = 1/2 * (alas * tinggi)
    print("Luas Segitiga Adalah: ", Luas, ("cm2"))

def Luas_Persegi_Panjang():
    print('⬛Hitung Luas Persegi Panjang⬜')
    panjang = float(input('Masukan tingginya: '))
    lebar = float(input('Masukan lebarnya: '))
    Luas = (panjang * lebar)
    print("Luas Persegi Panjang Adalah: ", Luas, ("cm2"))

def Bilangan_Ganjil_Genap():
    print('🚗Menentukan Bilangan Ganjil dan Genap🚓')
    x = int(input('Masukkan Angka: '))
    print('adalah bilangan', 'genap' if (x % 2 == 0) else 'ganjil')

while True:
    try:
        userInput = int(input(
            "MENU : \n1. Luas Segitiga\n2. Luas Persegi Panjang\n3. Menentukan Angka Ganjil Genap\n4. Quit\nPilih Nomer: "))
    except ValueError:
        print("Inputan harus berupa number")
    else:
        if (userInput == 1):
            Luas_Segitiga()
        elif (userInput == 2):
            Luas_Persegi_Panjang()
        elif (userInput == 3):
            Bilangan_Ganjil_Genap()
        else:
            break
