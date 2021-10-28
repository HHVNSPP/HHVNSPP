set term postscript eps font ",12" size 32, 24 color
set key off
set logscale x
set boxwidth 0.5 relative
set style fill solid border -1
set xtics 1, 2
set xlabel "Iteration"
c0="#dddddd"
c1="#ff4500"
c2="#009999"
c3="#a020f0"
c4="#1e90ff"
c5="#006400"
c6="#4b0082"
c7="#a0522d"
c8="#ff0000"
c9="#0000dd"
c10="#33dd00"
set output "B4_20.eps"
set multiplot layout 9, 6
set xrange [0.5:1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B4_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B4_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B4_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B4_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r1_B4_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r1_B4_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 1, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B4_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B4_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B4_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B4_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r2_B4_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r2_B4_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 1, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B4_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B4_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B4_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B4_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r3_B4_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r3_B4_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 2, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r1_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r1_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 2, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r2_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r2_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 2, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r3_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r3_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 3, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r1_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r1_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 3, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r2_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r2_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 3, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
plot "Parsed/r3_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
plot "Parsed/r3_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
unset multiplot
set output "B9_20.eps"
set multiplot layout 9, 11
set xrange [0.5:1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_20_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_20_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_20_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_20_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_20_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_20_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_20_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_20_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_20_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_20_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_20_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_20_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_20_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_20_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_20_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_20_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_20_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_20_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_20_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_20_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_20_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_20_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_20_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_20_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_20_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_20_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_20_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_20_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_20_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_20_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
unset multiplot
set output "B9_30.eps"
set multiplot layout 9, 11
set xrange [0.5:1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_30_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_30_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_30_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_30_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_30_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_30_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_30_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_30_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_30_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_30_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_30_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_30_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_30_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_30_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_30_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_30_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_30_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_30_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_30_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_30_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_30_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_30_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_30_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_30_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_30_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_30_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_30_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_30_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_30_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_30_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_30_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_30_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_30_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_30_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_30_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_30_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_30_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_30_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_30_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_30_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_30_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_30_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_30_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_30_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_30_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_30_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_30_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_30_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_30_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_30_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_30_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_30_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_30_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_30_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_30_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_30_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_30_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_30_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_30_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_30_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_30_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_30_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_30_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_30_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_30_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_30_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
unset multiplot
set output "B9_100.eps"
set multiplot layout 15, 11
set xrange [0.5:1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_100_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_100_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_100_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_100_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_100_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_100_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_100_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_100_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_100_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_100_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_100_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_100_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_100_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_100_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_100_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_100_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_100_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_100_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_100_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_100_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_100_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_100_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_100_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_100_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_100_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_100_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_100_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_100_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_100_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_100_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_100_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_100_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_100_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_100_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_100_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_100_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_100_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_100_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_100_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_100_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_100_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_100_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_100_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_100_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_100_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_100_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_100_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_100_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_100_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_100_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_100_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_100_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_100_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_100_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_100_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_100_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_100_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_100_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_100_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_100_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_100_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_100_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_100_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_100_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_100_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_100_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_100_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_100_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_100_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_100_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_100_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_100_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_100_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_100_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_100_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_100_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_100_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_100_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_100_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_100_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_100_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_100_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_100_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_100_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_100_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_100_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_100_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_100_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_100_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_100_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_100_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_100_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_100_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_100_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_100_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_100_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_100_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_100_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_100_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 4, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_100_i4_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_100_i4_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_100_i4_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_100_i4_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_100_i4_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_100_i4_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_100_i4_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_100_i4_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_100_i4_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_100_i4_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_100_i4_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 4, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_100_i4_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_100_i4_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_100_i4_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_100_i4_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_100_i4_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_100_i4_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_100_i4_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_100_i4_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_100_i4_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_100_i4_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_100_i4_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 4, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_100_i4_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_100_i4_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_100_i4_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_100_i4_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_100_i4_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_100_i4_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_100_i4_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_100_i4_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_100_i4_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_100_i4_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_100_i4_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 5, replica 1
set ylabel "Objective 1"
plot "Parsed/r1_B9_100_i5_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r1_B9_100_i5_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r1_B9_100_i5_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r1_B9_100_i5_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r1_B9_100_i5_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r1_B9_100_i5_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r1_B9_100_i5_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r1_B9_100_i5_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r1_B9_100_i5_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r1_B9_100_i5_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r1_B9_100_i5_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 5, replica 2
set ylabel "Objective 1"
plot "Parsed/r2_B9_100_i5_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r2_B9_100_i5_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r2_B9_100_i5_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r2_B9_100_i5_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r2_B9_100_i5_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r2_B9_100_i5_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r2_B9_100_i5_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r2_B9_100_i5_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r2_B9_100_i5_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r2_B9_100_i5_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r2_B9_100_i5_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 5, replica 3
set ylabel "Objective 1"
plot "Parsed/r3_B9_100_i5_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
plot "Parsed/r3_B9_100_i5_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
plot "Parsed/r3_B9_100_i5_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
plot "Parsed/r3_B9_100_i5_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
plot "Parsed/r3_B9_100_i5_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
plot "Parsed/r3_B9_100_i5_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
plot "Parsed/r3_B9_100_i5_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
plot "Parsed/r3_B9_100_i5_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
plot "Parsed/r3_B9_100_i5_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
plot "Parsed/r3_B9_100_i5_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
plot "Parsed/r3_B9_100_i5_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
unset multiplot
