import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import random



n_genyen=0
n_jwe=1000000 #kantite fwa ou jwe
pot1=1
pot2=2
pot3=3

#pot3 se li ki gen prim la

for i in range(0, n_jwe):
    chwa=random.choice([pot1,pot2,pot3])
    if chwa==pot1 :
        chwa=pot3
        n_genyen=n_genyen+1
    
    else:
        
        if chwa==pot2 :
            chwa=pot3
            n_genyen=n_genyen+1
        else:
            
        
            if chwa==pot3 :
                chwa=random.choice([pot1,pot2])

        
plt.pie([n_genyen,n_jwe-n_genyen],labels=['Genyen','Pedi'],autopct='%1.1f%%')#colors=['yellow','blue'])
plt.title("Posibilite Si Ou Decide Chanje")

#%matplotlib qt
