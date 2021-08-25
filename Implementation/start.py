from datetime import timedelta
from instanceSetA import executeA
from instanceSetB import executeB
from instanceSetC import executeC
import os

limit = timedelta (seconds = 15) # maximum runtime for each individual execution
maxiter = 2**10 # maximum iterations
replicas = 30 # how many times each instance is solved
sep = ';' # output file column separator
prefixes = ['m', 'b', 'P'] # necesitamos notacion clara para las instancias
filetypes = ['.txt', '', '.dat'] # necesitamos ser consistentes 
execute = {'A': executeA, 'B': executeB, 'C': executeC}

for s in 'ABC':
    directory = r'../Instances/Set' + s + '/'
    output = f'../Results/Set{s}/'
    prefix = prefixes.pop(0)
    ending = filetypes.pop(0)
    print('Reading instances from', directory)
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith(ending):
            print('Processing instance at', filename)
            for r in range(1, replicas + 1):
                print('Executing replica', r)                
                with open(output + f'r{r}_' + filename, 'w') as target:
                    execute[s](directory + filename, limit, maxiter, target, sep)
