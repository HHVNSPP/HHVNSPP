python3 setB.py > setB.plot
for file in `ls -1 *.plot`;
do
    gnuplot $file
done
