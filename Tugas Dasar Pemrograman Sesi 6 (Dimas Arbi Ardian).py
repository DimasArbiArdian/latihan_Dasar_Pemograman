#!/usr/bin/env python
# coding: utf-8

# In[9]:


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


# In[ ]:


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


# In[ ]:




