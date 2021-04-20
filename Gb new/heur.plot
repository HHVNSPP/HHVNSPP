set term postscript eps font ",8" color

set size 2.2, 1
set boxwidth 0.6 relative
set style fill solid border -1
set key off
set ytics 0, 1000
set output 'heur.eps'
set multiplot 
set xlabel 'Heuristic'
set ylabel 'Number of uses'
set xtics ('SwapRandom' 1, 'SwapQuarter' 2, 'SwapThird' 3, 'SwapHalf' 4, 'ShakeArea' 5, 'ShakeRegion' 6, 'Swap1' 7, 'DrawHightBgt' 8, 'AddRandom' 9, 'AddLowBgt' 10, 'DrawRandom' 11, 'DrawHightBgt' 12, 'DrawRandomPutLessBgt' 13, 'AddMaxBgt' 14, 'SwapArea' 15, 'IncreseBgtArea' 16, 'DecreaseBgtArea' 17, 'SwapRegion' 18, 'IncreseBgtRegion' 19, 'DecreaseBgtRegion' 20)

set title 'B 20 4 Shake'
set origin 0, 0.75
set size 0.6, 0.25
set yrange [-500:2500]
set ytics 0, 500
set xrange [0.5:6.5]
plot 'heur_b20_4.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc rgb variable
set title 'B 20 4 Local search'
set origin 0.6, 0.75
set size 1.6, 0.25
set yrange [2800:6200]
set ytics 3000, 1000
set xrange [6.5:20.5]
plot 'heur_b20_4.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc rgb variable

set title 'B 20 9 Shake'
set origin 0, 0.5
set size 0.6, 0.25
set yrange [55:95]
set ytics 60, 10
set xrange [0.5:6.5]
plot 'heur_b20_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable
set title 'B 20 9 Local search'
set origin 0.6, 0.5
set size 1.6, 0.25
set xrange [6.5:20.5]
set yrange [350:1050]
set ytics 400, 100
plot 'heur_b20_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

set title 'B 30 9 Shake'
set origin 0, 0.25
set size 0.6, 0.25
set xrange [0.5:6.5]
set yrange [25:45]
set ytics 30, 5
plot 'heur_b30_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable
set title 'B 30 9 Local search'
set origin 0.6, 0.25
set size 1.6, 0.25
set xrange [6.5:20.5]
set yrange [180:620]
set ytics 200, 100
plot 'heur_b30_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable

set title 'B 100 9 Shake'
set origin 0, 0
set size 0.6, 0.25
set xrange [0.5:6.5]
set yrange [15:105]
set ytics 20, 20
plot 'heur_b100_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable
set title 'B 100 9 Local search'
set origin 0.6, 0
set size 1.6, 0.25
set xrange [6.5:20.5]
set yrange [250:1750]
set ytics 500, 500
plot 'heur_b100_9.txt' using 1:2:3:4:5:($1 < 7 ? 1 : 2) with candlesticks lt -1 lw 2 lc variable whiskerbars, \
     '' using 1:6:6:6:6:($1 < 7 ? 1 : 2) notitle with candlesticks lt -1 lw 3 lc variable