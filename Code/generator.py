# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:06:22 2020

GENERATOR FOR THE INSTANCE SET C

@author: Madys
"""
import random

projects = []
num_proj = 512
num_obj = 4
num_inst = 4
budget = num_proj * 1000
name = "m_o"

def benefits(obj): 
   if obj == 4:
       matrix = [0,0,0,0]
       a1=[[0,0,1,1],[1,0,1,0],[0,1,0,1],[1,1,0,0],[0.5,0.5,0.5,0.5],[0.8,0.7,0.5,0],[0,0.7,0.8,0.5]]
       a2=random.choice(a1)
       for j in range(4):
          matrix[j]=round(random.randint(10,15)*10*a2[j])
       return matrix
   if obj==3:
       matrix=[0,0,0]
       a1=[[0,1,1],[1,0,1],[0,1,0],[1,1,0],[1,0.5,0.5],[0.8,0.7,0.5],[0.7,0.5,0.8]]
       a2=random.choice(a1)
       for j in range(4):
          matrix[j]=round(random.randint(10,15)*10*a2[j])
       return matrix
    
for inst in range(num_inst):
    nsyn = random.randint(round(num_proj/20),round(num_proj/15))
    file = open(name+str(num_proj)+"_"+str(inst+1) +".txt", "w")    
    file.write(str(num_proj)+"\n")
    file.write(str(budget)+"\n")
    file.write("2 3 4\n")
    file.write(str(nsyn)+"\n")
    
    file_ns = open(name+str(num_proj)+"_"+str(inst+1) +"ns.txt", "w")    
    file_ns.write(str(num_proj)+"\n")
    file_ns.write(str(budget)+"\n")
    file_ns.write("2 3 4\n")
    file_ns.write('0'+"\n")
    
    for i in range(nsyn):
        npr=random.randint(2,8)
        mina=random.randint(2,npr)
        maxa=random.randint(mina,npr)
        text=str(i)+ " 1 " +str(npr) +" " + str(random.randint(10,30)*10) + " "+ str(mina)+" "+ str(maxa)+"\n"
        file.write(text)
        output = list(range(num_proj))
        random.shuffle(output)
        a=""
        for i in range(npr):
            if i < npr-1:
                a=a+str(output[i])+" "
            else:
                a=a+str(output[i])+"\n"
        file.write(a)
    for i in range(num_proj):    
        low=random.randint(10,30)*100
        high=round(low*random.randint(11,15)/10)
        ben=benefits(num_obj)        
        cat1=str(random.randint(1,3))
        cat2= str(random.randint(1,2))
        file.write(str(low)+" "+ str(high)+" "+ cat1 +" "+ cat2 +" "+ str(ben[0])+" "+str(ben[1])+" "+str(ben[2])+" "+str(ben[3])+" \n")
        file_ns.write(str(low)+" "+ str(high)+" "+ cat1 +" "+ cat2+" "+ str(ben[0])+" "+str(ben[1])+" "+str(ben[2])+" "+str(ben[3])+" \n")
    file.close()   
    file_ns.close()  
