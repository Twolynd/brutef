
# coding: utf-8

# In[ ]:

"""
Simulation of a generator of passwords.

Number of people = n
length of password = lp

cf is the sample, you can always excluit a specific number of letters.

The only advantage this code has over of the others is the size of the file, i've added a Comparation function just for excluiting
useless passwords "aaaaaa" for example.

The problem here is very similar to the classic brute force, you can choice a sample of people (n) where you can ask for their passwords for a specific lenght, then you can ask yourself for the probability of guess a password. In this frame the probability of find the  password is proportional to 10^(lenght of cf), so you have to do those simulations to reach the goal.


"""



from random import choice
import random
from statistics import mean
def imp(a):
    c=''
    for i in a:
        c=c+i
    return c

def comp(a):
    p=[]
    for i in range(len(a)):
        x=random.randint(0,len(a)-1)
        if a[x]!=a[x-1]:
            p.append(1)
        else:
            p.append(0)
    return mean(p)

cf=["a","b","c","d","e","l","f","m","n","o","r","p","g","s","u","t","i"]

weight=[]
letme=[]
lp=8
pd=[]
n=10000
for i in range(n):
    pas=[]
    for k in range(lp):
        pas.append(choice(cf))
    xs=comp(pas)

    weight.append(xs)
    if weight[i]>0.99:
        pd.append(imp(pas))

f = open('passwords.txt','a')
for i in pd:
    f.write('\n' + i)
f.close()

