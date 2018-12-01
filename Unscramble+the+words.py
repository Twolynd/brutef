
# coding: utf-8

# In[2]:

"""
Way to sort words if you have a wordlist.

"""
import numpy as np
words=input()
words=words.split(' ')
file=open('wordlist.txt','r')
data = file.readlines()
c=0
Num=[]
pind=[]
for k in range(len(words)):
    pal=[]
    for m in range(len(data)):
        P=list(words[k])
        wl=list(data[m])
        if '\n' in wl: wl.remove('\n')
        if len(P)==len(wl):
            for n in range(len(P)):
                for o in range(len(wl)):
                    if P[n]==wl[o]:                        
                        wl[o]='--'
                        break
        pal.append(wl)
    pind=(len(P))
    

    Index=0
    for i in pal:
        Index+=1
        if i==['--']*pind:
            c=Index
    Num.append(data[c-1])
    
    del(pal)
for i in range(len(Num)):
    print(Num[i])


# In[ ]:



