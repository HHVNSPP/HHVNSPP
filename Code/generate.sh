replicas=3
objectives=4
synergies=5
areas=3
regions=2
budget=1.5 
for p in {6..9}; do
    n=$((2**p))
    echo Generating instances with $n projects
    python3 generator.py $replicas $objectives $n $synergies $areas $regions $budget
done
mv C*.txt ../Data/C/
