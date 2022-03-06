#!/usr/bin/env python
# coding: utf-8

# ### Input angka kemudian mengganti angka dengan string

# In[2]:


bil_awal = int(input("Masukan bilangan awal: "))
bil_akhir = int(input("Masukan bilangan akhir: "))
list_bil = [i for i in range(bil_awal, bil_akhir +1 )]

for i in range (bil_awal, bil_akhir+1):
  if i%3==0 and i%5==0:
    print("Joko widodo") #Perkalian 3 dan 5, maka akan muncul Joko Widodo
  elif i%5==0:
    print("widodo")   #Perkalian 5, maka akan muncul Widodo
  elif i%3==0:
    print("Joko")  #Perkalian 3, maka akan muncul Joko
  else:
    print(i)

  i+=1


# ### Membuat segitiga kosong

# In[3]:


bantu=0
kosong=0
for i in reversed(range(10)):
    for j in range(i+1):
        print(' ', end='')
    for k in range(bantu+1):
        if k==0:
            print('*', end='')
        else:
            print(' ', end='')
    for l in range(bantu):
        if l==kosong:
            print('*', end='')
            kosong+=1
        else:
            print(' ', end='')
    bantu+=1
    print()
for i in range(11):
    print('* ', end='')


# In[ ]:




