#!/usr/bin/env python
# coding: utf-8

# ### Menggabungkan 2 string tuple pada sebuah list

# In[1]:


warna = [('red','pink'), ('white','black'), ('orange','green')]

warna2 = [' '.join(temp) for temp in warna]

print('List tuple asal :')
print(warna)
print('Gabungan string tuple :')
print(warna2)


# ### Menggabungkan nilai dari 2 buah dict ke dalam sebuah list yang baru

# In[41]:


matkul = {"Mata Kuliah ": ["MTK","BIOLOGI","FISIKA","KIMIA"], "language": [77, 78, 84, 80]}
# Printing initial dict
print("List Asli : " , matkul)
print("Hasil Penggabungan :")
x = [key for key in matkul]
y = [value for value in matkul.values()]
for i in range(1):
    for j in range(4):
       
        print({f'{x[0]} : {y[0][j]}, {x[1]} : {y[1][j]}'},end=",")


# ### Jumlah nilai yang sama pada list sesuai urutan

# In[19]:


a = [1,2,3,4,5,6,7,8]
b = [2,2,3,1,2,6,7,9]
c = []

for i in range(len(a)):
    if a[i]==b[i]:
        c.append(a[i]) 
print(a)
print(b)
print("Jumlah angka yang sama sesuai urutan :", len(c))


# In[ ]:




