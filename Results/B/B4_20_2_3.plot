set term postscript eps font ",12" size 2, 6 color
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
set output "B4_20_2_3.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 1"
set yrange [72000.0:297000.0]
plot "Parsed/r3_B4_20_i2_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set term postscript eps font ",12" size 2, 6 color
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
set output "B4_20_2_3.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 2"
set yrange [40500.0:187000.00000000003]
plot "Parsed/r3_B4_20_i2_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set term postscript eps font ",12" size 2, 6 color
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
set output "B4_20_2_3.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 3"
set yrange [148500.0:429000.00000000006]
plot "Parsed/r3_B4_20_i2_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set term postscript eps font ",12" size 2, 6 color
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
set output "B4_20_2_3.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 4"
set yrange [40500.0:247500.00000000003]
plot "Parsed/r3_B4_20_i2_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set term postscript eps font ",12" size 2, 6 color
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
set output "B4_20_2_3.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Budget"
set yrange [426600000.0:533500000.00000006]
plot "Parsed/r3_B4_20_i2_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set term postscript eps font ",12" size 2, 6 color
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
set output "B4_20_2_3.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r3_B4_20_i2_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
