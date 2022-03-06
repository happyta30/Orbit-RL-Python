#!/usr/bin/env python
# coding: utf-8

# ### Menghitung Jumlah Paragraf Pada File Text

# In[1]:


file = open("berita.txt", "r")
berita = file.read()

Counter = 0

paragraf = berita.split("\n")
  
for i in paragraf:
    if i:
        Counter += 1
      
print(berita)

print("\nJumlah Paragraf :", Counter)


# ### Meng-Copy isi dari satu file ke file lainnya

# In[2]:


# import module
import shutil
  
# use copyfile()
try :
    shutil.copyfile('berita.txt','news.txt')
    print('successfully copy!!!'"\n")
except : 
    print ('failed to copy')

file = open("berita.txt", "r")
txt = open('news.txt', 'r')
print('FILE BERITA :'"\n", file.read())
print("\n"'FILE NEWS :'"\n", txt.read())
    


# ### Mencari Paragraf dengan jumlah kata terbanyak disebuah text file

# In[6]:


file = open("berita.txt", "r")

frequent_word = ""
frequency = 0 
words = []
 
# Traversing file line by line
for line in file:
     
    # splits each line into
    # words and removing spaces
    # and punctuations from the input
    line_word = line.lower().replace(',','').replace('.','').split(" "); 
     
    # Adding them to list words
    for w in line_word: 
        words.append(w); 
         
# Finding the max occurred word
for i in range(0, len(words)): 
     
    # Declaring count
    count = 1; 
     
    # Count each word in the file 
    for j in range(i+1, len(words)): 
        if(words[i] == words[j]) : 
            count = count + 1; 
 
    # If the count value is more
    # than highest frequency then
    if(count > frequency): 
        frequency = count; 
        frequent_word = words[i]; 


print("Kata yang banyak muncul : " , frequent_word)
print("Jumlah: " , str(frequency))
file.close();


# In[ ]:





# In[ ]:




