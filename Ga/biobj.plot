set term postscript eps font ",20" size 12, 6 color
set output "biobj.eps"
set multiplot layout 3, 5
set xlabel "# of projects"
set ylabel "Benefit"
set datafile separator ","
set key outside Right
set pointsize 1.2
set key off
set xrange [59:86]
set xtics 60, 5
set yrange [260:540]
set ytics 300, 100

set title "A 1" font ",30"
x=67
set arrow 1 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_1.csv' using 1:2 with points pt 7 lc rgb "#009999", 352 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 1
unset arrow 1
set title "A 2"
x=75
set arrow 2 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_2.csv' using 2:1 with points pt 7 lc rgb "#009999", 411 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 2
unset arrow 2
set title "A 3"
x=68
set arrow 3 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_3.csv' using 1:2 with points pt 7 lc rgb "#009999", 378 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 3
unset arrow 3
set title "A 4"
x=74
set arrow 4 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_4.csv' using 1:2 with points pt 7 lc rgb "#009999", 448 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 4
unset arrow 4
set title "A 5"
x=79
set arrow 5 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_5.csv' using 1:2 with points pt 7 lc rgb "#009999", 459 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 5
unset arrow 5
set title "A 6"
x=74
set arrow 6 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_6.csv' using 1:2 with points pt 7 lc rgb "#009999", 404 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 6
unset arrow 6
set title "A 7"
x=76
set arrow 7 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_7.csv' using 1:2 with points pt 7 lc rgb "#009999", 416 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 7
unset arrow 7
set title "A 8"
x=68
set arrow 8 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_8.csv' using 1:2 with points pt 7 lc rgb "#009999", 397 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 8
unset arrow 8
set title "A 9"
x=74
set arrow 9 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_9.csv' using 1:2 with points pt 7 lc rgb "#009999", 472 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 9
unset arrow 9
set title "A 10"
x=76
set arrow 10 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_10.csv' using 1:2 with points pt 7 lc rgb "#009999", 460 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 10
unset arrow 10
set title "A 11"
x=76
set arrow 11 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_11.csv' using 1:2 with points pt 7 lc rgb "#009999", 386 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 11
unset arrow 11
set title "A 12"
x=78
set arrow 12 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_12.csv' using 1:2 with points pt 7 lc rgb "#009999", 482 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 12
unset arrow 12
set title "A 13"
x=79
set arrow 13 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_13.csv' using 1:2 with points pt 7 lc rgb "#009999", 426 with lines lt -1 lw 3 lc rgb '#ff0000'
show arrow 13
unset arrow 13
set title "A 14"
x=81
set arrow 14 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_14.csv' using 1:2 with points pt 7 lc rgb "#009999", 469 with lines lt -1 lw 3 lc rgb '#ff0000'
set datafile separator ";"
show arrow 14
unset arrow 14
set title "A 15"
x=80
set arrow 15 from x, graph 0 to x, graph 1 nohead lt -1 lw 3 lc rgb '#ff0000'
plot '100a_15.csv' using 2:3  with points pt 7 lc rgb "#009999", 388 with lines lt -1 lw 3 lc rgb '#ff0000'
unset multiplot