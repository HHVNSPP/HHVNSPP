# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:06:22 2020

@author: Madys
"""
import numpy as np
import random
projects=[]

sin=1 #si se quieren sinergias 1, si no 0
num_proj=100
num_obj=3
num_inst=4
budget=num_proj*1000

def beneficios(obj): 
   if obj==4:
       matriz=[0,0,0,0]
       a1=[[0,0,1,1],[1,0,1,0],[0,1,0,1],[1,1,0,0],[0.5,0.5,0.5,0.5],[0.8,0.7,0.5,0],[0,0.7,0.8,0.5]]
       a2=random.choice(a1)
       for j in range(4):
          matriz[j]=round(random.randint(10,15)*10*a2[j])
       return matriz
   if obj==3:
       matriz=[0,0,0]
       a1=[[0,1,1],[1,0,1],[0,1,0],[1,1,0],[1,0.5,0.5],[0.8,0.7,0.5],[0.7,0.5,0.8]]
       a2=random.choice(a1)
       for j in range(4):
          matriz[j]=round(random.randint(10,15)*10*a2[j])
       return matriz


if sin==0:
    name="m3_obj_"
else:
    name="m3_sin_4obj_"
    
for inst in range(num_inst):
    if sin==0:
        nsyn=0
    else:
        nsyn=random.randint(round(num_proj/20),round(num_proj/15))
    file1 = open(name+str(num_proj)+"_"+str(inst+1) +".txt", "w") 
    file1.write(str(num_proj)+"\n")
    file1.write(str(budget)+"\n")
    file1.write("2 3 4\n")
    file1.write(str(nsyn)+"\n")
    for i in range(nsyn):
        npr=random.randint(2,8)
        mina=random.randint(2,npr)
        maxa=random.randint(mina,npr)
        text=str(i)+ " 1 " +str(npr) +" " + str(random.randint(10,30)*10) + " "+ str(mina)+" "+ str(maxa)+"\n"
        file1.write(text)
        output = list(range(num_proj))
        random.shuffle(output)
        a=""
        for i in range(npr):
            if i < npr-1:
                a=a+str(output[i])+" "
            else:
                a=a+str(output[i])+"\n"
        file1.write(a)
    for i in range(num_proj):    
        minimo=random.randint(10,30)*100
        maximo=round(minimo*random.randint(11,15)/10)
        ben=beneficios()        
#        file1.write(str(minimo)+" ;"+ str(maximo)+" ;"+ str(random.randint(1,3))+" ;"+str(random.randint(1,2))+" ;"+ str(ben[0])+" ;"+str(ben[1])+" ;"+str(ben[2])+" ;"+str(ben[3])+"\n")
        file1.write(str(minimo)+" "+ str(maximo)+" "+ str(random.randint(1,3))+" "+str(random.randint(1,2))+" "+ str(ben[0])+" "+str(ben[1])+" "+str(ben[2])+" "+str(ben[3])+" \n")
    file1.close()   
