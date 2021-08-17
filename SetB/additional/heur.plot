set term postscript eps font ",8" size 3, 4 color
set boxwidth 0.6 relative
set style fill solid border -1
set key off
set ytics 0, 1000
set output 'heurShake.eps'
set xlabel 'Heuristic'
set ylabel 'Number of uses'
set xtics ('SwapRnd' 1, 'SwapQuarter' 2, 'SwapThird' 3, 'SwapHalf' 4, 'ShakeArea' 5, 'ShakeRegion' 6, 'Swap1' 7, 'DrawHighBgt' 8, 'AddRnd' 9, 'AddLowBgt' 10, 'DrawRnd' 11, 'DrawHighBgt' 12, 'DrawRPutLessBgt' 13, 'AddMaxBgt' 14, 'SwapArea' 15, 'IncrBgtArea' 16, 'DecrBgtArea' 17, 'SwapReg' 18, 'IncrBgtReg' 19, 'DecrBgtReg' 20)

set multiplot layout 4, 1

set title 'B 20 4 Shake'
set yrange [-500:2500]
set ytics 0, 500
set xrange [0.5:6.5]
plot 'heur_b20_4.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc rgb variable

set title 'B 20 9 Shake'
set yrange [55:95]
set ytics 60, 10
set xrange [0.5:6.5]
plot 'heur_b20_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

set title 'B 30 9 Shake'
set xrange [0.5:6.5]
set yrange [25:45]
set ytics 30, 5
plot 'heur_b30_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

set title 'B 100 9 Shake'
set xrange [0.5:6.5]
set yrange [15:105]
set ytics 20, 20
plot 'heur_b100_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

unset multiplot
set term postscript eps font ",8" size 8, 4 color
set output 'heurLocal.eps'
set multiplot layout 4, 1

set title 'B 20 4 Local search'
set yrange [2800:6200]
set ytics 3000, 1000
set xrange [6.5:20.5]
plot 'heur_b20_4.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc rgb variable

set title 'B 20 9 Local search'
set xrange [6.5:20.5]
set yrange [350:1050]
set ytics 400, 100
plot 'heur_b20_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

set title 'B 30 9 Local search'
set xrange [6.5:20.5]
set yrange [180:620]
set ytics 200, 100
plot 'heur_b30_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

set title 'B 100 9 Local search'
set xrange [6.5:20.5]
set yrange [250:1750]
set ytics 500, 500
plot 'heur_b100_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable