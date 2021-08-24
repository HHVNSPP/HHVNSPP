import random
matrix=[]
num_proj=150
num_obj=1
num_inst=1
budget=num_proj*800
inst=0
name="alb_"
to_select=[" 1 0 0 0 0"," 0 1 0 0 0"," 0 0 1 0 0"," 0 0 0 1 0", " 0 0 0 0 1"] 

for i in range(num_proj):    
    bgt=random.randint(100,130)*10
    ben=random.randint(100,150)
    bgt_max=int(random.randint(125,135)/100*bgt ) 
    area=random.choice([1,2,3,4,5])
    region=random.choice([1,2,3,4,5])
    matrix.append([str(i+1),str(bgt),str(bgt_max),area,region, str(ben)])


file1 = open(name+str(num_proj)+"_"+str(inst+1) +".dat", "w")                            
file1.write("data;\n")
file1.write("set A:= 1 2 3 4 5;\n")
file1.write("set R:= 1 2 3 4 5;\n")
file1.write("param P :="+str(budget)+";\n")  
file1.write("param nproj :="+str(num_proj)+";\n")  
file1.write("\n")  
file1.write("param: Cmin Cmax benf :=\n")  
for i in matrix: 
   file1.write(i[0]+" "+i[1]+" "+i[2]+ " "+i[5]+"\n")
file1.write(";\n") 
file1.write("\n")  
file1.write("param costoA: 1  2  3  4  5:=\n")      
for i in matrix:   
    file1.write(i[0]+to_select[i[3]-1]+"\n")
file1.write(";\n") 
file1.write("\n")  
file1.write("param costoR: 1  2  3  4  5:=\n") 
for i in matrix:        
    file1.write(i[0]+to_select[i[4]-1]+"\n")
file1.write(";\n") 
file1.close()   


