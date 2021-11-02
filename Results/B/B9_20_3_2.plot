set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 1"
set yrange [54000.0:209000.00000000003]
plot "Parsed/r2_B9_20_i3_1.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c0 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c0
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 2"
set yrange [0.0:132000.0]
plot "Parsed/r2_B9_20_i3_2.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c1 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c1
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 3"
set yrange [0.0:137500.0]
plot "Parsed/r2_B9_20_i3_3.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c2 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c2
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 4"
set yrange [0.0:181500.00000000003]
plot "Parsed/r2_B9_20_i3_4.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c3 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c3
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 5"
set yrange [40500.0:280500.0]
plot "Parsed/r2_B9_20_i3_5.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c4 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c4
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 6"
set yrange [108000.0:297000.0]
plot "Parsed/r2_B9_20_i3_6.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c5 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c5
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 7"
set yrange [27000.0:270600.0]
plot "Parsed/r2_B9_20_i3_7.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c6 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c6
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 8"
set yrange [43200.0:217800.00000000003]
plot "Parsed/r2_B9_20_i3_8.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c7 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c7
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Objective 9"
set yrange [10800.0:138600.0]
plot "Parsed/r2_B9_20_i3_9.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c8 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c8
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Budget"
set yrange [398700000.0:525250000.00000006]
plot "Parsed/r2_B9_20_i3_10.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c9 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c9
set term postscript eps font ",12" size 2, 11 color
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
set output "B9_20_3_2.eps"
set xrange [0.5 : 1.5 * 64]
set ylabel "Portfolio size"
set yrange [9.0:11.0]
plot "Parsed/r2_B9_20_i3_11.txt" u 1:3:2:6:5 with candlesticks lt -1 lw 2 lc rgb c10 whiskerbars, \
"" u 1:4:4:4:4 with candlesticks lt -1 lw 3 lc rgb c10
