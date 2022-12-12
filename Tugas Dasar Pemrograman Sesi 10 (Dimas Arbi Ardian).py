#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Tugas Nomor 1
#Menampilkan Nilai Maksimum List
print("1. Buatlah sebuah program dengan menggunakan list:")
print("a. Program yang menampilkan nilai maksimum dari sebuah list")
list = [456,700,200,1000,2000]
print(f"nilai dari list: ", list)
print(f"nilai maksimum dari list: ", max(list))
print("="*56)

print("b. Program yang menampilkan nilai minimum dari sebuah list")
print(f"nilai dari list: ", list)
print(f"nilai minimum dari list: ", min(list))
print("="*56)

print("c. Program yang menampilkan sebuah anggota baru di antara anggota list")
dimlist1 = ['a','e','i','u']
print(f"Original list: ", dimlist1)
dimlist1.insert(0, "o")
print(f"Memasukan huruf a pada list: ", dimlist1)
print("="*56)
print()

#Tugas Nomor 2
#Menampilkan Nilai Tuple
print("2. Buatlah sebuah program dengan menggunakan tuple:")
print("a. Program yang menampilkan isi dari sebuah tuple kemudian mengkorvesikan ke format string")
saya = ('g','a','n','t','e','n','g')
print(f"Tuple Original: ", saya)
for x in (saya):
    print(x, end='')
print()
print("="*56)

print("b. Program yang menampilkan nilai maksimum dari sebuah list")
tup1 = (0, 200, 1000, 2, 3, 9000, 10)
print(f"nilai dari tuple: ", tup1)
print(f"nilai maksimum dari tuple: ", max(tup1))
print("="*56)

print("c. Program yang menampilkan nilai minimum dari sebuah list")
print(f"nilai dari tuple: ", tup1)
print(f"nilai minimum dari tuple: ", min(tup1))
print("="*56)
print()

#Tugas Nomor 3
#Menampilkan Nilai Dictionary
print("3. Buatlah sebuah program dengan menggunakan tuple:")
print("Program yang menampilkan nilai minimum dari sebuah list")
dict1 = {90,50,70,60,80,1212,12,26}
print(f'nilai minimum dari dictionary:', min(dict1))
print("="*56)


# In[ ]:




