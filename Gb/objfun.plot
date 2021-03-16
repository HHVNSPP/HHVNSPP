set term postscript eps font ",30" size 12, 9 color
dx=50
set datafile separator ","
set key outside Right
set pointsize 1.2
set xrange [-200:5200]
set xtics 0, 500
set yrange [100000:400000]
set ytics 100000,100000
set xlabel "Runtime (seconds)"
set ylabel "Objective"
c1='#ff4500'
c2='#009999'
c3='#a020f0'
c4='#1e90ff'
c5='#006400'
c6='#4b0082'
c7='#a0522d'
c8='#ff0000'
c9='#0000dd'
set output "objfuna.eps"
#set title '20 projects with 4 objectives' font ",40"
set multiplot layout 3, 1
set title 'B 20-4 1'
plot 'obj/2plt_b_20obj4_1_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b_20obj4_1_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b_20obj4_1_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b_20obj4_1_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4
set title 'B 20-4 2'
plot 'obj/2plt_b_20obj4_2_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b_20obj4_2_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b_20obj4_2_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b_20obj4_2_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4
set title 'B 20-4 3'
plot 'obj/2plt_b_20obj4_3_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b_20obj4_3_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b_20obj4_3_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b_20obj4_3_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4
unset multiplot

set output "objfunb.eps"
#set title '20 projects with 9 objectives'
set multiplot layout 3, 1
set xrange [-200:5700]
set xtics 0, 500
set title 'B 20-9 1'
plot 'obj/2plt_b20obj9_1_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b20obj9_1_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b20obj9_1_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b20obj9_1_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b20obj9_1_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b20obj9_1_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b20obj9_1_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b20obj9_1_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b20obj9_1_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 20-9 2 DATA MISSING'
plot 1
set title 'B 20-9 3 DATA MISSING'
plot 1
unset multiplot

set key off
set output "objfunc.eps"
#set title '30 projects with 9 objectives'
set yrange [-50000:550000]
set ytics 0,200000
set xrange [-500:16500]
set xtics 0, 2500
set multiplot layout 3, 1
set title 'B 30-9 1'
plot 'obj/2plt_b30obj9_1_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b30obj9_1_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b30obj9_1_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b30obj9_1_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b30obj9_1_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b30obj9_1_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b30obj9_1_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b30obj9_1_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b30obj9_1_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 30-9 2'
plot 'obj/2plt_b30obj9_2_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b30obj9_2_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b30obj9_2_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b30obj9_2_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b30obj9_2_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b30obj9_2_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b30obj9_2_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b30obj9_2_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b30obj9_2_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 30-9 3'
plot 'obj/2plt_b30obj9_3_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b30obj9_3_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2 ,\
     'obj/2plt_b30obj9_3_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b30obj9_3_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b30obj9_3_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b30obj9_3_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b30obj9_3_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b30obj9_3_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b30obj9_3_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
unset multiplot

set term postscript eps font ",30" size 12, 15 color
set output "objfund.eps"
#set title '100 projects with 9 objectives'
set multiplot layout 5, 1
set xrange [-800:11800]
set xtics 0, 2000
set yrange [100000:1500000]
set ytics 100000,500000
set title 'B 100-9 1'
plot 'obj/2plt_b100obj9_1_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b100obj9_1_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b100obj9_1_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b100obj9_1_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b100obj9_1_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b100obj9_1_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b100obj9_1_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b100obj9_1_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b100obj9_1_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 100-9 2'
plot 'obj/2plt_b100obj9_2_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b100obj9_2_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b100obj9_2_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b100obj9_2_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b100obj9_2_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b100obj9_2_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b100obj9_2_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b100obj9_2_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b100obj9_2_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 100-9 3'
plot 'obj/2plt_b100obj9_3_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b100obj9_3_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b100obj9_3_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b100obj9_3_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b100obj9_3_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b100obj9_3_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b100obj9_3_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b100obj9_3_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b100obj9_3_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 100-9 4'
plot 'obj/2plt_b100obj9_4_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b100obj9_4_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2,\
     'obj/2plt_b100obj9_4_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b100obj9_4_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b100obj9_4_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b100obj9_4_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b100obj9_4_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b100obj9_4_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b100obj9_4_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
set title 'B 100-9 5'
plot 'obj/2plt_b100obj9_5_o1.csv' u ($1 + 0 * dx):3 every ::1 t "Obj. 1" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c1, \
     'obj/2plt_b100obj9_5_o2.csv' u ($1 + 1 * dx):3 every ::1 t "Obj. 2" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c2, \
     'obj/2plt_b100obj9_5_o3.csv' u ($1 + 2 * dx):3 every ::1 t "Obj. 3" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c3, \
     'obj/2plt_b100obj9_5_o4.csv' u ($1 + 3 * dx):3 every ::1 t "Obj. 4" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c4, \
     'obj/2plt_b100obj9_5_o5.csv' u ($1 + 4 * dx):3 every ::1 t "Obj. 5" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c5, \
     'obj/2plt_b100obj9_5_o6.csv' u ($1 + 5 * dx):3 every ::1 t "Obj. 6" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c6, \
     'obj/2plt_b100obj9_5_o7.csv' u ($1 + 6 * dx):3 every ::1 t "Obj. 7" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c7, \
     'obj/2plt_b100obj9_5_o8.csv' u ($1 + 7 * dx):3 every ::1 t "Obj. 8" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c8, \
     'obj/2plt_b100obj9_5_o9.csv' u ($1 + 8 * dx):3 every ::1 t "Obj. 9" with linespoints pt 7 dt 2 lt -1 lw 3 lc rgb c9
unset multiplot

