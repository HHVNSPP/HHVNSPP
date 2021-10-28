set term postscript eps font ",20" size 12, 6 color
set output "setA.eps"
set multiplot layout 3, 5
set xlabel "# of projects"
set ylabel "Total benefit"
set key outside Right
set pointsize 1
set key off
set xrange [45:105]
set xtics 50, 10
set yrange [150:550]
set ytics 200, 100
set title "A 1" font ",30"
x=67
y=352
set arrow 1 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A1_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A1_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A1_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 1
unset arrow 1

set title "A 2" font ",30"
x=75
y=411
set arrow 2 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A2_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A2_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A2_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 2
unset arrow 2

set title "A 3" font ",30"
x=68
y=378
set arrow 3 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A3_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A3_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A3_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 3
unset arrow 3

set title "A 4" font ",30"
x=74
y=448
set arrow 4 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A4_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A4_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A4_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 4
unset arrow 4

set title "A 5" font ",30"
x=79
y=459
set arrow 5 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A5_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A5_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A5_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 5
unset arrow 5

set title "A 6" font ",30"
x=74
y=404
set arrow 6 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A6_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A6_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A6_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 6
unset arrow 6

set title "A 7" font ",30"
x=76
y=416
set arrow 7 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A7_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A7_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A7_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 7
unset arrow 7

set title "A 8" font ",30"
x=68
y=397
set arrow 8 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A8_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A8_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A8_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 8
unset arrow 8

set title "A 9" font ",30"
x=74
y=472
set arrow 9 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A9_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A9_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A9_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 9
unset arrow 9

set title "A 10" font ",30"
x=76
y=460
set arrow 10 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A10_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A10_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A10_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 10
unset arrow 10

set title "A 11" font ",30"
x=76
y=386
set arrow 11 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A11_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A11_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A11_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 11
unset arrow 11

set title "A 12" font ",30"
x=78
y=482
set arrow 12 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A12_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A12_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A12_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 12
unset arrow 12

set title "A 13" font ",30"
x=79
y=426
set arrow 13 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A13_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A13_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A13_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 13
unset arrow 13

set title "A 14" font ",30"
x=81
y=469
set arrow 14 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A14_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A14_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A14_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 14
unset arrow 14

set title "A 15" font ",30"
x=80
y=388
set arrow 15 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb "#999999"
plot "Parsed/A15_r1.txt" using 1:2 with points pt 7 lc rgb "#0000ff", y with lines lt -1 lw 3 lc rgb "#999999", \
     "Parsed/A15_r2.txt" using 1:2 with points pt 5 lc rgb "#ff0000", \
     "Parsed/A15_r3.txt" using 1:2 with points pt 7 lc rgb "#00ff00"
show arrow 15
unset arrow 15

unset multiplot
