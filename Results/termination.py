import os
from collections import defaultdict

conditions =  [ 'time', 'iter', 'stall' ]
cases = { 'A': [''], 'B': [''], 'C': ['WithSynergies/', 'WithoutSynergies/']}
counters = dict()
counters['Global'] = { c : 0 for c in conditions }

for s in 'ABC':
    base = r'../Results/' + s + '/Replicas/'
    for c in cases[s]:
        case = s + ('s' if 'WithS' in c else '')
        counters[case] = { c : 0 for c in conditions }
        directory = base + c
        for filename in os.listdir(directory):
            if filename.startswith('r') and filename.endswith('.txt'):
                f = filename.split('_')
                source = f'{directory}{filename}'
                with open(source) as output:
                    for line in output:
                        if '#' not in line:
                            if 'end' in line:
                                line = line.split(';')
                                values = { 'time' : line[1],
                                           'iter' : line[2],
                                           'stall':  line[3] }
                                for criterion in values:
                                    fields = values[criterion].split('/')
                                    # sorry for the weird reporting with the iterations
                                    reached = float(fields[0]) + (1 if criterion == 'iter' else 0)
                                    limit = float(fields[1])
                                    if reached >= limit: # all that were met count
                                        counters[case][criterion] += 1
                                        counters['Global'][criterion] += 1

print('\\begin{tabular}{|l|r|r|r|}\n\\hline')
order = sorted(counters.keys())
print('Set & ' + ' & '.join(conditions) + ' \\\\\n')
for case in order:
    data = counters[case]
    values = ' & '.join([ str(data[c]) for c in conditions])
    print(f'{case} & {values} \\\\\n')
print('\\hline')
print('\\end{tabular}')
