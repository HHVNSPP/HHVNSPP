set term postscript eps font ",20" size 16, 16 color
    set boxwidth 0.6 relative
    set style fill solid border -1
    set output "setBh.eps"
    set key off
    set ylabel "Number of uses"
set multiplot layout 4, 2
set xrange [0.1:13.9]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "20 projects, 4 objectives: shake"
plot "Parsed/h_B4_20_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "20 projects, 4 objectives: search"
plot "Parsed/h_B4_20_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "20 projects, 9 objectives: shake"
plot "Parsed/h_B9_20_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "20 projects, 9 objectives: search"
plot "Parsed/h_B9_20_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "30 projects, 9 objectives: shake"
plot "Parsed/h_B9_30_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "30 projects, 9 objectives: search"
plot "Parsed/h_B9_30_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "100 projects, 9 objectives: shake"
plot "Parsed/h_B9_100_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "100 projects, 9 objectives: search"
plot "Parsed/h_B9_100_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
