from datetime import timedelta
from instanceSetA import executeA
from instanceSetB import executeB
from instanceSetC import executeC
import os

limit = timedelta (seconds = 15) # maximum runtime for each individual execution
maxiter = 2**10 # maximum iterations
replicas = 30 # how many times each instance is solved
sep = ';' # output file column separator
prefixes = ['P', 'o', 'm'] 
filetypes = ['.dat', '.txt', '.txt'] 
execute = {'A': executeA, 'B': executeB, 'C': executeC}

for s in 'ABC':
    directory = r'../Instances/InstanceSet' + s + '/'
    output = f'../Results/InstanceSet{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    print('Reading instances from', directory)
    for filename in os.listdir(directory):
        print('Examining file', filename)        
        if filename.startswith(prefix) and filename.endswith(ending):
            print('Processing instance at', filename)
            for r in range(1, replicas + 1):
                print(f'Executing replica {r} for {filename} in {directory}')                
                with open(output + f'r{r}_' + filename, 'w') as target:
                    execute[s](directory + filename, limit, maxiter, target, sep)
