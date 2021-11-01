set term postscript eps font ",12" size 32, 24 color
set key off
set logscale x
set boxwidth 0.1 absolute
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
set xrange [0.5 : 1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
set yrange [54000.0:247500.00000000003]
plot "Parsed/r1_B4_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [49500.0:231000.00000000003]
plot "Parsed/r1_B4_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [121500.0:396000.00000000006]
plot "Parsed/r1_B4_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [94500.0:313500.0]
plot "Parsed/r1_B4_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [419850000.0:528000000.00000006]
plot "Parsed/r1_B4_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r1_B4_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 1, replica 2
set ylabel "Objective 1"
set yrange [54000.0:247500.00000000003]
plot "Parsed/r2_B4_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [49500.0:231000.00000000003]
plot "Parsed/r2_B4_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [121500.0:396000.00000000006]
plot "Parsed/r2_B4_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [94500.0:313500.0]
plot "Parsed/r2_B4_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [419850000.0:528000000.00000006]
plot "Parsed/r2_B4_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r2_B4_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 1, replica 3
set ylabel "Objective 1"
set yrange [54000.0:247500.00000000003]
plot "Parsed/r3_B4_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [49500.0:231000.00000000003]
plot "Parsed/r3_B4_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [121500.0:396000.00000000006]
plot "Parsed/r3_B4_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [94500.0:313500.0]
plot "Parsed/r3_B4_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [419850000.0:528000000.00000006]
plot "Parsed/r3_B4_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r3_B4_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 2, replica 1
set ylabel "Objective 1"
set yrange [72000.0:297000.0]
plot "Parsed/r1_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [40500.0:187000.00000000003]
plot "Parsed/r1_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [148500.0:429000.00000000006]
plot "Parsed/r1_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [40500.0:247500.00000000003]
plot "Parsed/r1_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [426600000.0:533500000.00000006]
plot "Parsed/r1_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r1_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 2, replica 2
set ylabel "Objective 1"
set yrange [72000.0:297000.0]
plot "Parsed/r2_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [40500.0:187000.00000000003]
plot "Parsed/r2_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [148500.0:429000.00000000006]
plot "Parsed/r2_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [40500.0:247500.00000000003]
plot "Parsed/r2_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [426600000.0:533500000.00000006]
plot "Parsed/r2_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r2_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 2, replica 3
set ylabel "Objective 1"
set yrange [72000.0:297000.0]
plot "Parsed/r3_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [40500.0:187000.00000000003]
plot "Parsed/r3_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [148500.0:429000.00000000006]
plot "Parsed/r3_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [40500.0:247500.00000000003]
plot "Parsed/r3_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [426600000.0:533500000.00000006]
plot "Parsed/r3_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r3_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 3, replica 1
set ylabel "Objective 1"
set yrange [18000.0:247500.00000000003]
plot "Parsed/r1_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [27000.0:253000.00000000003]
plot "Parsed/r1_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [40500.0:330000.0]
plot "Parsed/r1_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [13500.0:313500.0]
plot "Parsed/r1_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [421425000.0:534600000.00000006]
plot "Parsed/r1_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r1_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 3, replica 2
set ylabel "Objective 1"
set yrange [18000.0:247500.00000000003]
plot "Parsed/r2_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [27000.0:253000.00000000003]
plot "Parsed/r2_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [40500.0:330000.0]
plot "Parsed/r2_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [13500.0:313500.0]
plot "Parsed/r2_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [421425000.0:534600000.00000006]
plot "Parsed/r2_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r2_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set title "Instance 3, replica 3
set ylabel "Objective 1"
set yrange [18000.0:247500.00000000003]
plot "Parsed/r3_B4_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [27000.0:253000.00000000003]
plot "Parsed/r3_B4_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [40500.0:330000.0]
plot "Parsed/r3_B4_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [13500.0:313500.0]
plot "Parsed/r3_B4_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Budget"
set yrange [421425000.0:534600000.00000006]
plot "Parsed/r3_B4_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r3_B4_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
unset multiplot
set output "B9_20.eps"
set multiplot layout 9, 11
set xrange [0.5 : 1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
set yrange [9000.0:203500.00000000003]
plot "Parsed/r1_B9_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [9000.0:148500.0]
plot "Parsed/r1_B9_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [18000.0:181500.00000000003]
plot "Parsed/r1_B9_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [27000.0:72600.0]
plot "Parsed/r1_B9_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [1350.0:77550.0]
plot "Parsed/r1_B9_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [0.0:11550.000000000002]
plot "Parsed/r1_B9_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [113400.0:382800.00000000006]
plot "Parsed/r1_B9_20_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [0.0:178200.0]
plot "Parsed/r1_B9_20_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [0.0:204600.00000000003]
plot "Parsed/r1_B9_20_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [396900000.0:549450000.0]
plot "Parsed/r1_B9_20_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:12.100000000000001]
plot "Parsed/r1_B9_20_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 2
set ylabel "Objective 1"
set yrange [9000.0:203500.00000000003]
plot "Parsed/r2_B9_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [9000.0:148500.0]
plot "Parsed/r2_B9_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [18000.0:181500.00000000003]
plot "Parsed/r2_B9_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [27000.0:72600.0]
plot "Parsed/r2_B9_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [1350.0:77550.0]
plot "Parsed/r2_B9_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [0.0:11550.000000000002]
plot "Parsed/r2_B9_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [113400.0:382800.00000000006]
plot "Parsed/r2_B9_20_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [0.0:178200.0]
plot "Parsed/r2_B9_20_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [0.0:204600.00000000003]
plot "Parsed/r2_B9_20_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [396900000.0:549450000.0]
plot "Parsed/r2_B9_20_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:12.100000000000001]
plot "Parsed/r2_B9_20_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 3
set ylabel "Objective 1"
set yrange [9000.0:203500.00000000003]
plot "Parsed/r3_B9_20_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [9000.0:148500.0]
plot "Parsed/r3_B9_20_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [18000.0:181500.00000000003]
plot "Parsed/r3_B9_20_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [27000.0:72600.0]
plot "Parsed/r3_B9_20_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [1350.0:77550.0]
plot "Parsed/r3_B9_20_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [0.0:11550.000000000002]
plot "Parsed/r3_B9_20_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [113400.0:382800.00000000006]
plot "Parsed/r3_B9_20_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [0.0:178200.0]
plot "Parsed/r3_B9_20_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [0.0:204600.00000000003]
plot "Parsed/r3_B9_20_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [396900000.0:549450000.0]
plot "Parsed/r3_B9_20_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:12.100000000000001]
plot "Parsed/r3_B9_20_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 1
set ylabel "Objective 1"
set yrange [27000.0:187000.00000000003]
plot "Parsed/r1_B9_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [0.0:247500.00000000003]
plot "Parsed/r1_B9_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [0.0:170500.0]
plot "Parsed/r1_B9_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [4050.0:56100.00000000001]
plot "Parsed/r1_B9_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [13500.0:67650.0]
plot "Parsed/r1_B9_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [6750.0:28050.000000000004]
plot "Parsed/r1_B9_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [0.0:191400.00000000003]
plot "Parsed/r1_B9_20_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [97200.0:297000.0]
plot "Parsed/r1_B9_20_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [0.0:211200.00000000003]
plot "Parsed/r1_B9_20_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [394650000.0:550000000.0]
plot "Parsed/r1_B9_20_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:12.100000000000001]
plot "Parsed/r1_B9_20_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 2
set ylabel "Objective 1"
set yrange [27000.0:187000.00000000003]
plot "Parsed/r2_B9_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [0.0:247500.00000000003]
plot "Parsed/r2_B9_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [0.0:170500.0]
plot "Parsed/r2_B9_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [4050.0:56100.00000000001]
plot "Parsed/r2_B9_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [13500.0:67650.0]
plot "Parsed/r2_B9_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [6750.0:28050.000000000004]
plot "Parsed/r2_B9_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [0.0:191400.00000000003]
plot "Parsed/r2_B9_20_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [97200.0:297000.0]
plot "Parsed/r2_B9_20_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [0.0:211200.00000000003]
plot "Parsed/r2_B9_20_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [394650000.0:550000000.0]
plot "Parsed/r2_B9_20_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:12.100000000000001]
plot "Parsed/r2_B9_20_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 3
set ylabel "Objective 1"
set yrange [27000.0:187000.00000000003]
plot "Parsed/r3_B9_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [0.0:247500.00000000003]
plot "Parsed/r3_B9_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [0.0:170500.0]
plot "Parsed/r3_B9_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [4050.0:56100.00000000001]
plot "Parsed/r3_B9_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [13500.0:67650.0]
plot "Parsed/r3_B9_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [6750.0:28050.000000000004]
plot "Parsed/r3_B9_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [0.0:191400.00000000003]
plot "Parsed/r3_B9_20_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [97200.0:297000.0]
plot "Parsed/r3_B9_20_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [0.0:211200.00000000003]
plot "Parsed/r3_B9_20_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [394650000.0:550000000.0]
plot "Parsed/r3_B9_20_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:12.100000000000001]
plot "Parsed/r3_B9_20_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 1
set ylabel "Objective 1"
set yrange [54000.0:209000.00000000003]
plot "Parsed/r1_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [0.0:132000.0]
plot "Parsed/r1_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [0.0:137500.0]
plot "Parsed/r1_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [0.0:181500.00000000003]
plot "Parsed/r1_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [40500.0:280500.0]
plot "Parsed/r1_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [108000.0:297000.0]
plot "Parsed/r1_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [27000.0:270600.0]
plot "Parsed/r1_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [43200.0:217800.00000000003]
plot "Parsed/r1_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [10800.0:138600.0]
plot "Parsed/r1_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [398700000.0:525250000.00000006]
plot "Parsed/r1_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r1_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 2
set ylabel "Objective 1"
set yrange [54000.0:209000.00000000003]
plot "Parsed/r2_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [0.0:132000.0]
plot "Parsed/r2_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [0.0:137500.0]
plot "Parsed/r2_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [0.0:181500.00000000003]
plot "Parsed/r2_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [40500.0:280500.0]
plot "Parsed/r2_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [108000.0:297000.0]
plot "Parsed/r2_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [27000.0:270600.0]
plot "Parsed/r2_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [43200.0:217800.00000000003]
plot "Parsed/r2_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [10800.0:138600.0]
plot "Parsed/r2_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [398700000.0:525250000.00000006]
plot "Parsed/r2_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r2_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 3
set ylabel "Objective 1"
set yrange [54000.0:209000.00000000003]
plot "Parsed/r3_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [0.0:132000.0]
plot "Parsed/r3_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [0.0:137500.0]
plot "Parsed/r3_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [0.0:181500.00000000003]
plot "Parsed/r3_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [40500.0:280500.0]
plot "Parsed/r3_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [108000.0:297000.0]
plot "Parsed/r3_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [27000.0:270600.0]
plot "Parsed/r3_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [43200.0:217800.00000000003]
plot "Parsed/r3_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [10800.0:138600.0]
plot "Parsed/r3_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [398700000.0:525250000.00000006]
plot "Parsed/r3_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r3_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
unset multiplot
set output "B9_30.eps"
set multiplot layout 9, 11
set xrange [0.5 : 1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
set yrange [13500.0:231000.00000000003]
plot "Parsed/r1_B9_30_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [22500.0:209000.00000000003]
plot "Parsed/r1_B9_30_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [54000.0:247500.00000000003]
plot "Parsed/r1_B9_30_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [39150.0:107250.00000000001]
plot "Parsed/r1_B9_30_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [12150.0:103950.00000000001]
plot "Parsed/r1_B9_30_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [2700.0:49500.00000000001]
plot "Parsed/r1_B9_30_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [124200.0:495000.00000000006]
plot "Parsed/r1_B9_30_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [54000.0:356400.0]
plot "Parsed/r1_B9_30_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [10800.0:270600.0]
plot "Parsed/r1_B9_30_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [567450000.0:825000000.0000001]
plot "Parsed/r1_B9_30_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r1_B9_30_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 2
set ylabel "Objective 1"
set yrange [13500.0:231000.00000000003]
plot "Parsed/r2_B9_30_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [22500.0:209000.00000000003]
plot "Parsed/r2_B9_30_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [54000.0:247500.00000000003]
plot "Parsed/r2_B9_30_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [39150.0:107250.00000000001]
plot "Parsed/r2_B9_30_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [12150.0:103950.00000000001]
plot "Parsed/r2_B9_30_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [2700.0:49500.00000000001]
plot "Parsed/r2_B9_30_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [124200.0:495000.00000000006]
plot "Parsed/r2_B9_30_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [54000.0:356400.0]
plot "Parsed/r2_B9_30_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [10800.0:270600.0]
plot "Parsed/r2_B9_30_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [567450000.0:825000000.0000001]
plot "Parsed/r2_B9_30_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r2_B9_30_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 3
set ylabel "Objective 1"
set yrange [13500.0:231000.00000000003]
plot "Parsed/r3_B9_30_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [22500.0:209000.00000000003]
plot "Parsed/r3_B9_30_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [54000.0:247500.00000000003]
plot "Parsed/r3_B9_30_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [39150.0:107250.00000000001]
plot "Parsed/r3_B9_30_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [12150.0:103950.00000000001]
plot "Parsed/r3_B9_30_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [2700.0:49500.00000000001]
plot "Parsed/r3_B9_30_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [124200.0:495000.00000000006]
plot "Parsed/r3_B9_30_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [54000.0:356400.0]
plot "Parsed/r3_B9_30_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [10800.0:270600.0]
plot "Parsed/r3_B9_30_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [567450000.0:825000000.0000001]
plot "Parsed/r3_B9_30_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r3_B9_30_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 1
set ylabel "Objective 1"
set yrange [49500.0:341000.0]
plot "Parsed/r1_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [4500.0:286000.0]
plot "Parsed/r1_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [18000.0:253000.00000000003]
plot "Parsed/r1_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [4050.0:80850.0]
plot "Parsed/r1_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [27000.0:105600.00000000001]
plot "Parsed/r1_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [4050.0:33000.0]
plot "Parsed/r1_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [16200.0:231000.00000000003]
plot "Parsed/r1_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [86400.0:369600.00000000006]
plot "Parsed/r1_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [27000.0:323400.0]
plot "Parsed/r1_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [581850000.0:825000000.0000001]
plot "Parsed/r1_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r1_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 2
set ylabel "Objective 1"
set yrange [49500.0:341000.0]
plot "Parsed/r2_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [4500.0:286000.0]
plot "Parsed/r2_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [18000.0:253000.00000000003]
plot "Parsed/r2_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [4050.0:80850.0]
plot "Parsed/r2_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [27000.0:105600.00000000001]
plot "Parsed/r2_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [4050.0:33000.0]
plot "Parsed/r2_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [16200.0:231000.00000000003]
plot "Parsed/r2_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [86400.0:369600.00000000006]
plot "Parsed/r2_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [27000.0:323400.0]
plot "Parsed/r2_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [581850000.0:825000000.0000001]
plot "Parsed/r2_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r2_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 3
set ylabel "Objective 1"
set yrange [49500.0:341000.0]
plot "Parsed/r3_B9_30_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [4500.0:286000.0]
plot "Parsed/r3_B9_30_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [18000.0:253000.00000000003]
plot "Parsed/r3_B9_30_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [4050.0:80850.0]
plot "Parsed/r3_B9_30_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [27000.0:105600.00000000001]
plot "Parsed/r3_B9_30_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [4050.0:33000.0]
plot "Parsed/r3_B9_30_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [16200.0:231000.00000000003]
plot "Parsed/r3_B9_30_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [86400.0:369600.00000000006]
plot "Parsed/r3_B9_30_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [27000.0:323400.0]
plot "Parsed/r3_B9_30_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [581850000.0:825000000.0000001]
plot "Parsed/r3_B9_30_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r3_B9_30_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 1
set ylabel "Objective 1"
set yrange [63000.0:258500.00000000003]
plot "Parsed/r1_B9_30_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [22500.0:214500.00000000003]
plot "Parsed/r1_B9_30_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [4500.0:181500.00000000003]
plot "Parsed/r1_B9_30_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [67500.0:363000.00000000006]
plot "Parsed/r1_B9_30_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [67500.0:412500.00000000006]
plot "Parsed/r1_B9_30_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [81000.0:429000.00000000006]
plot "Parsed/r1_B9_30_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [32400.0:290400.0]
plot "Parsed/r1_B9_30_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [43200.0:356400.0]
plot "Parsed/r1_B9_30_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [48600.0:297000.0]
plot "Parsed/r1_B9_30_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [578250000.0:825000000.0000001]
plot "Parsed/r1_B9_30_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r1_B9_30_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 2
set ylabel "Objective 1"
set yrange [63000.0:258500.00000000003]
plot "Parsed/r2_B9_30_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [22500.0:214500.00000000003]
plot "Parsed/r2_B9_30_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [4500.0:181500.00000000003]
plot "Parsed/r2_B9_30_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [67500.0:363000.00000000006]
plot "Parsed/r2_B9_30_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [67500.0:412500.00000000006]
plot "Parsed/r2_B9_30_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [81000.0:429000.00000000006]
plot "Parsed/r2_B9_30_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [32400.0:290400.0]
plot "Parsed/r2_B9_30_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [43200.0:356400.0]
plot "Parsed/r2_B9_30_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [48600.0:297000.0]
plot "Parsed/r2_B9_30_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [578250000.0:825000000.0000001]
plot "Parsed/r2_B9_30_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r2_B9_30_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 3
set ylabel "Objective 1"
set yrange [63000.0:258500.00000000003]
plot "Parsed/r3_B9_30_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [22500.0:214500.00000000003]
plot "Parsed/r3_B9_30_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [4500.0:181500.00000000003]
plot "Parsed/r3_B9_30_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [67500.0:363000.00000000006]
plot "Parsed/r3_B9_30_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [67500.0:412500.00000000006]
plot "Parsed/r3_B9_30_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [81000.0:429000.00000000006]
plot "Parsed/r3_B9_30_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [32400.0:290400.0]
plot "Parsed/r3_B9_30_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [43200.0:356400.0]
plot "Parsed/r3_B9_30_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [48600.0:297000.0]
plot "Parsed/r3_B9_30_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [578250000.0:825000000.0000001]
plot "Parsed/r3_B9_30_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [13.5:19.8]
plot "Parsed/r3_B9_30_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
unset multiplot
set output "B9_100.eps"
set multiplot layout 15, 11
set xrange [0.5 : 1.5 * 64]
set title "Instance 1, replica 1
set ylabel "Objective 1"
set yrange [198000.0:577500.0]
plot "Parsed/r1_B9_100_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [634500.0:1177000.0]
plot "Parsed/r1_B9_100_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [270000.0:698500.0]
plot "Parsed/r1_B9_100_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [472500.0:1270500.0]
plot "Parsed/r1_B9_100_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [580500.0:1353000.0]
plot "Parsed/r1_B9_100_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [270000.0:825000.0000000001]
plot "Parsed/r1_B9_100_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [399600.0:996600.0000000001]
plot "Parsed/r1_B9_100_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [523800.0:1273800.0]
plot "Parsed/r1_B9_100_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [280800.0:838200.0000000001]
plot "Parsed/r1_B9_100_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [199147.5:275000.0]
plot "Parsed/r1_B9_100_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [52.2:77.0]
plot "Parsed/r1_B9_100_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 2
set ylabel "Objective 1"
set yrange [198000.0:577500.0]
plot "Parsed/r2_B9_100_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [634500.0:1177000.0]
plot "Parsed/r2_B9_100_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [270000.0:698500.0]
plot "Parsed/r2_B9_100_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [472500.0:1270500.0]
plot "Parsed/r2_B9_100_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [580500.0:1353000.0]
plot "Parsed/r2_B9_100_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [270000.0:825000.0000000001]
plot "Parsed/r2_B9_100_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [399600.0:996600.0000000001]
plot "Parsed/r2_B9_100_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [523800.0:1273800.0]
plot "Parsed/r2_B9_100_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [280800.0:838200.0000000001]
plot "Parsed/r2_B9_100_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [199147.5:275000.0]
plot "Parsed/r2_B9_100_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [52.2:77.0]
plot "Parsed/r2_B9_100_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 1, replica 3
set ylabel "Objective 1"
set yrange [198000.0:577500.0]
plot "Parsed/r3_B9_100_i1_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [634500.0:1177000.0]
plot "Parsed/r3_B9_100_i1_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [270000.0:698500.0]
plot "Parsed/r3_B9_100_i1_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [472500.0:1270500.0]
plot "Parsed/r3_B9_100_i1_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [580500.0:1353000.0]
plot "Parsed/r3_B9_100_i1_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [270000.0:825000.0000000001]
plot "Parsed/r3_B9_100_i1_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [399600.0:996600.0000000001]
plot "Parsed/r3_B9_100_i1_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [523800.0:1273800.0]
plot "Parsed/r3_B9_100_i1_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [280800.0:838200.0000000001]
plot "Parsed/r3_B9_100_i1_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [199147.5:275000.0]
plot "Parsed/r3_B9_100_i1_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [52.2:77.0]
plot "Parsed/r3_B9_100_i1_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 1
set ylabel "Objective 1"
set yrange [382500.0:891000.0000000001]
plot "Parsed/r1_B9_100_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [261000.0:676500.0]
plot "Parsed/r1_B9_100_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [310500.0:907500.0000000001]
plot "Parsed/r1_B9_100_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [648000.0:1435500.0]
plot "Parsed/r1_B9_100_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [648000.0:1303500.0]
plot "Parsed/r1_B9_100_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [418500.0:1039500.0000000001]
plot "Parsed/r1_B9_100_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [286200.0:831600.0000000001]
plot "Parsed/r1_B9_100_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [469800.0:1168200.0]
plot "Parsed/r1_B9_100_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [529200.0:1214400.0]
plot "Parsed/r1_B9_100_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [211477.5:275000.0]
plot "Parsed/r1_B9_100_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [56.7:77.0]
plot "Parsed/r1_B9_100_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 2
set ylabel "Objective 1"
set yrange [382500.0:891000.0000000001]
plot "Parsed/r2_B9_100_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [261000.0:676500.0]
plot "Parsed/r2_B9_100_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [310500.0:907500.0000000001]
plot "Parsed/r2_B9_100_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [648000.0:1435500.0]
plot "Parsed/r2_B9_100_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [648000.0:1303500.0]
plot "Parsed/r2_B9_100_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [418500.0:1039500.0000000001]
plot "Parsed/r2_B9_100_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [286200.0:831600.0000000001]
plot "Parsed/r2_B9_100_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [469800.0:1168200.0]
plot "Parsed/r2_B9_100_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [529200.0:1214400.0]
plot "Parsed/r2_B9_100_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [211477.5:275000.0]
plot "Parsed/r2_B9_100_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [56.7:77.0]
plot "Parsed/r2_B9_100_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 2, replica 3
set ylabel "Objective 1"
set yrange [382500.0:891000.0000000001]
plot "Parsed/r3_B9_100_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [261000.0:676500.0]
plot "Parsed/r3_B9_100_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [310500.0:907500.0000000001]
plot "Parsed/r3_B9_100_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [648000.0:1435500.0]
plot "Parsed/r3_B9_100_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [648000.0:1303500.0]
plot "Parsed/r3_B9_100_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [418500.0:1039500.0000000001]
plot "Parsed/r3_B9_100_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [286200.0:831600.0000000001]
plot "Parsed/r3_B9_100_i2_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [469800.0:1168200.0]
plot "Parsed/r3_B9_100_i2_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [529200.0:1214400.0]
plot "Parsed/r3_B9_100_i2_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [211477.5:275000.0]
plot "Parsed/r3_B9_100_i2_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [56.7:77.0]
plot "Parsed/r3_B9_100_i2_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 1
set ylabel "Objective 1"
set yrange [504000.0:1111000.0]
plot "Parsed/r1_B9_100_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [288000.0:753500.0000000001]
plot "Parsed/r1_B9_100_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [342000.0:891000.0000000001]
plot "Parsed/r1_B9_100_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [513000.0:1204500.0]
plot "Parsed/r1_B9_100_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [580500.0:1320000.0]
plot "Parsed/r1_B9_100_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [445500.0:1056000.0]
plot "Parsed/r1_B9_100_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [329400.0:897600.0000000001]
plot "Parsed/r1_B9_100_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [356400.0:950400.0000000001]
plot "Parsed/r1_B9_100_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [621000.0:1287000.0]
plot "Parsed/r1_B9_100_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [211342.5:275000.0]
plot "Parsed/r1_B9_100_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [57.6:77.0]
plot "Parsed/r1_B9_100_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 2
set ylabel "Objective 1"
set yrange [504000.0:1111000.0]
plot "Parsed/r2_B9_100_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [288000.0:753500.0000000001]
plot "Parsed/r2_B9_100_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [342000.0:891000.0000000001]
plot "Parsed/r2_B9_100_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [513000.0:1204500.0]
plot "Parsed/r2_B9_100_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [580500.0:1320000.0]
plot "Parsed/r2_B9_100_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [445500.0:1056000.0]
plot "Parsed/r2_B9_100_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [329400.0:897600.0000000001]
plot "Parsed/r2_B9_100_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [356400.0:950400.0000000001]
plot "Parsed/r2_B9_100_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [621000.0:1287000.0]
plot "Parsed/r2_B9_100_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [211342.5:275000.0]
plot "Parsed/r2_B9_100_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [57.6:77.0]
plot "Parsed/r2_B9_100_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 3, replica 3
set ylabel "Objective 1"
set yrange [504000.0:1111000.0]
plot "Parsed/r3_B9_100_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [288000.0:753500.0000000001]
plot "Parsed/r3_B9_100_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [342000.0:891000.0000000001]
plot "Parsed/r3_B9_100_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [513000.0:1204500.0]
plot "Parsed/r3_B9_100_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [580500.0:1320000.0]
plot "Parsed/r3_B9_100_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [445500.0:1056000.0]
plot "Parsed/r3_B9_100_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [329400.0:897600.0000000001]
plot "Parsed/r3_B9_100_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [356400.0:950400.0000000001]
plot "Parsed/r3_B9_100_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [621000.0:1287000.0]
plot "Parsed/r3_B9_100_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [211342.5:275000.0]
plot "Parsed/r3_B9_100_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [57.6:77.0]
plot "Parsed/r3_B9_100_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 4, replica 1
set ylabel "Objective 1"
set yrange [342000.0:808500.0000000001]
plot "Parsed/r1_B9_100_i4_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [324000.0:819500.0000000001]
plot "Parsed/r1_B9_100_i4_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [441000.0:957000.0000000001]
plot "Parsed/r1_B9_100_i4_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [526500.0:1237500.0]
plot "Parsed/r1_B9_100_i4_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [634500.0:1303500.0]
plot "Parsed/r1_B9_100_i4_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [405000.0:1188000.0]
plot "Parsed/r1_B9_100_i4_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [459000.0:1201200.0]
plot "Parsed/r1_B9_100_i4_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [297000.0:798600.0000000001]
plot "Parsed/r1_B9_100_i4_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [405000.0:1003200.0000000001]
plot "Parsed/r1_B9_100_i4_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [198045.0:275000.0]
plot "Parsed/r1_B9_100_i4_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [51.300000000000004:77.0]
plot "Parsed/r1_B9_100_i4_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 4, replica 2
set ylabel "Objective 1"
set yrange [342000.0:808500.0000000001]
plot "Parsed/r2_B9_100_i4_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [324000.0:819500.0000000001]
plot "Parsed/r2_B9_100_i4_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [441000.0:957000.0000000001]
plot "Parsed/r2_B9_100_i4_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [526500.0:1237500.0]
plot "Parsed/r2_B9_100_i4_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [634500.0:1303500.0]
plot "Parsed/r2_B9_100_i4_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [405000.0:1188000.0]
plot "Parsed/r2_B9_100_i4_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [459000.0:1201200.0]
plot "Parsed/r2_B9_100_i4_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [297000.0:798600.0000000001]
plot "Parsed/r2_B9_100_i4_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [405000.0:1003200.0000000001]
plot "Parsed/r2_B9_100_i4_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [198045.0:275000.0]
plot "Parsed/r2_B9_100_i4_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [51.300000000000004:77.0]
plot "Parsed/r2_B9_100_i4_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 4, replica 3
set ylabel "Objective 1"
set yrange [342000.0:808500.0000000001]
plot "Parsed/r3_B9_100_i4_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [324000.0:819500.0000000001]
plot "Parsed/r3_B9_100_i4_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [441000.0:957000.0000000001]
plot "Parsed/r3_B9_100_i4_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [526500.0:1237500.0]
plot "Parsed/r3_B9_100_i4_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [634500.0:1303500.0]
plot "Parsed/r3_B9_100_i4_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [405000.0:1188000.0]
plot "Parsed/r3_B9_100_i4_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [459000.0:1201200.0]
plot "Parsed/r3_B9_100_i4_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [297000.0:798600.0000000001]
plot "Parsed/r3_B9_100_i4_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [405000.0:1003200.0000000001]
plot "Parsed/r3_B9_100_i4_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [198045.0:275000.0]
plot "Parsed/r3_B9_100_i4_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [51.300000000000004:77.0]
plot "Parsed/r3_B9_100_i4_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 5, replica 1
set ylabel "Objective 1"
set yrange [216000.0:676500.0]
plot "Parsed/r1_B9_100_i5_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [283500.0:671000.0]
plot "Parsed/r1_B9_100_i5_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [450000.0:1023000.0000000001]
plot "Parsed/r1_B9_100_i5_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [567000.0:1287000.0]
plot "Parsed/r1_B9_100_i5_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [351000.0:1138500.0]
plot "Parsed/r1_B9_100_i5_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [621000.0:1270500.0]
plot "Parsed/r1_B9_100_i5_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [399600.0:1009800.0000000001]
plot "Parsed/r1_B9_100_i5_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [567000.0:1306800.0]
plot "Parsed/r1_B9_100_i5_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [372600.0:1069200.0]
plot "Parsed/r1_B9_100_i5_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [212400.0:275000.0]
plot "Parsed/r1_B9_100_i5_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [56.7:78.10000000000001]
plot "Parsed/r1_B9_100_i5_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 5, replica 2
set ylabel "Objective 1"
set yrange [216000.0:676500.0]
plot "Parsed/r2_B9_100_i5_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [283500.0:671000.0]
plot "Parsed/r2_B9_100_i5_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [450000.0:1023000.0000000001]
plot "Parsed/r2_B9_100_i5_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [567000.0:1287000.0]
plot "Parsed/r2_B9_100_i5_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [351000.0:1138500.0]
plot "Parsed/r2_B9_100_i5_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [621000.0:1270500.0]
plot "Parsed/r2_B9_100_i5_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [399600.0:1009800.0000000001]
plot "Parsed/r2_B9_100_i5_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [567000.0:1306800.0]
plot "Parsed/r2_B9_100_i5_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [372600.0:1069200.0]
plot "Parsed/r2_B9_100_i5_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [212400.0:275000.0]
plot "Parsed/r2_B9_100_i5_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [56.7:78.10000000000001]
plot "Parsed/r2_B9_100_i5_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
set title "Instance 5, replica 3
set ylabel "Objective 1"
set yrange [216000.0:676500.0]
plot "Parsed/r3_B9_100_i5_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set ylabel "Objective 2"
set yrange [283500.0:671000.0]
plot "Parsed/r3_B9_100_i5_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set ylabel "Objective 3"
set yrange [450000.0:1023000.0000000001]
plot "Parsed/r3_B9_100_i5_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set ylabel "Objective 4"
set yrange [567000.0:1287000.0]
plot "Parsed/r3_B9_100_i5_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set ylabel "Objective 5"
set yrange [351000.0:1138500.0]
plot "Parsed/r3_B9_100_i5_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set ylabel "Objective 6"
set yrange [621000.0:1270500.0]
plot "Parsed/r3_B9_100_i5_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set ylabel "Objective 7"
set yrange [399600.0:1009800.0000000001]
plot "Parsed/r3_B9_100_i5_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set ylabel "Objective 8"
set yrange [567000.0:1306800.0]
plot "Parsed/r3_B9_100_i5_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set ylabel "Objective 9"
set yrange [372600.0:1069200.0]
plot "Parsed/r3_B9_100_i5_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set ylabel "Budget"
set yrange [212400.0:275000.0]
plot "Parsed/r3_B9_100_i5_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set ylabel "Portfolio size"
set yrange [56.7:78.10000000000001]
plot "Parsed/r3_B9_100_i5_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
unset multiplot
