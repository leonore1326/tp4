#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:15:21 2020

@author: leonore
"""


from math import floor
import numpy as np
import random
import time
import matplotlib.pyplot as plt

def tri_par_insertion(Liste):
    n=len(Liste)
    i=1
    for i in range (n):
        x=Liste[i]
        j=i
        while j>=0 and Liste[j-1]>x:
            Liste[j]=Liste[j-1]
            j=j-1
        Liste[j]=x
    
    return(Liste)

def faire_un_tas(Liste, debut, fin):
    racine=debut
    while 2*racine<fin:
        enfant=racine*2+1
        sw=racine
        if Liste[enfant]>Liste[racine]:
            sw=enfant
        if enfant+1<fin and Liste[enfant+1]>Liste[sw]:
            sw=enfant+1
        if sw==racine:
            return(Liste)
        else:
            temporaire=Liste[sw]
            Liste[sw]=Liste[racine]
            Liste[racine]=temporaire 
            racine=sw
    return(Liste)

def faire_un_gros_tas(Liste,fin):
    n=len(Liste)
    for debut in reversed(range(floor(n/2))):
        Liste=faire_un_tas(Liste, debut, fin)
    return(Liste)
        

def tri_par_tas(Liste):
    Liste=faire_un_gros_tas(Liste,len(Liste))
    for fin in reversed(range(len(Liste))):
        temp=Liste[fin]
        Liste[fin]=Liste[0]
        Liste[0]=temp  
        Liste=faire_un_tas(Liste, 0, fin-1)
        
    return(Liste)

def recherche_sequentielle(L,n):
    for k in range(len(L)):
        if L[k]==n:
            #print(n,'est bien dans la liste, première occurrence à l indexe', k)
            return(True)
    return(False)

def recherche_dichotome(L,n):
    #T=tri_par_tas(L)
    a=0
    b=len(L)-1
    c=floor((b-a)/2)
    while (n!=L[c]) and (b-a)>1:
        if n>L[c]:
            a=c
            c=a+floor((b-a)/2)
        elif n<L[c]:
            b=c
            c=a+floor((b-a)/2)
    if n==L[c]:
        return(True)
    else:
        return(False)
            
### complexité du tri

temps_insertion=[]
temps_tas=[]
abcsisse=[]
for k in range (3,13):
    abcsisse.append(k)
    L=np.random.randint(1000,size=2**k)
    a=time.time()
    L1=tri_par_insertion(L)
    b=time.time()
    temps_insertion.append(b-a)
    a=time.time()
    L2=tri_par_insertion(L)
    b=time.time()
    temps_tas.append(b-a)
plt.figure('Comparaison du temps des algos de tri en fonction de la puissance de 2 de la longueur de la liste')
plt.plot(abcsisse, temps_insertion,label='insertion')
plt.plot(abcsisse, temps_tas,label='tas')
plt.legend()
# plt.figure("Pour l'aglo de tas seulement")
# plt.plot(abcsisse, temps_tas,label='tas')
# plt.legend()
plt.show(block=False)
    
### complexité de la recherche dans liste triée

temps_sequentiel=[]
temps_dichtome=[]
abcsisse=[]
for k in range (3,10):
    s_seq=0
    s_dich=0
    abcsisse.append(k)
    
    for n in range (1000) :       
        L=np.random.randint(1000,size=2**k)
        L=tri_par_tas(L)
        J=random.randint(0,2**k)
        a=time.time()
        boul=recherche_sequentielle(L, J)
        b=time.time()
        s_seq+=b-a
        c=time.time()
        boul1=recherche_dichotome(L, J)
        d=time.time()
        s_dich+=d-c
        
    temps_sequentiel.append(s_seq/1000)
    temps_dichtome.append(s_dich/1000)
    
plt.figure('Comparaison du temps des algos de recherche en fonction de la puissance de 2 de la longueur (moyenne sur 1000)')
plt.plot(abcsisse, temps_sequentiel,label='sequentiel')
plt.plot(abcsisse, temps_dichtome,label='dichotomie')
plt.legend()
plt.show(block=False)
    
### complexité de tri avec la fonction Python L.sort() et le tri par tas

temps_python=[]
temps_tas=[]
abcsisse=[]
for k in range (3,13):
    abcsisse.append(k)
    L=np.random.randint(1000,size=2**k)
    a=time.time()
    L1=L.sort()
    b=time.time()
    temps_python.append(b-a)
    a=time.time()
    L2=tri_par_insertion(L)
    b=time.time()
    temps_tas.append(b-a)
plt.figure('Comparaison du temps des algos de tri en fonction de la puissance de 2 de la longueur de la liste')
plt.plot(abcsisse, temps_python,label='fonctionL.sort()')
plt.plot(abcsisse, temps_tas,label='tas')
plt.legend()

plt.show(block=False)
    
