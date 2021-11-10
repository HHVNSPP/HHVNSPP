set term postscript eps font ",16" size 12, 96 color
set boxwidth 0.6 relative
set style fill solid border -1
set output "usage_details.eps"
set key off
set ylabel "Number of uses"
set multiplot layout 24, 2
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Global"
plot "Usage/Global_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Global"
plot "Usage/Global_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set A instance P100R5A2S5 with synergies"
plot "Usage/Set_A_instance_P100R5A2S5_with_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set A instance P100R5A2S5 with synergies"
plot "Usage/Set_A_instance_P100R5A2S5_with_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n30i1 without synergies"
plot "Usage/Set_B_instance_k9n30i1_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n30i1 without synergies"
plot "Usage/Set_B_instance_k9n30i1_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n30i3 without synergies"
plot "Usage/Set_B_instance_k9n30i3_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n30i3 without synergies"
plot "Usage/Set_B_instance_k9n30i3_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n30i2 without synergies"
plot "Usage/Set_B_instance_k9n30i2_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n30i2 without synergies"
plot "Usage/Set_B_instance_k9n30i2_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k4n20i1 without synergies"
plot "Usage/Set_B_instance_k4n20i1_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k4n20i1 without synergies"
plot "Usage/Set_B_instance_k4n20i1_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k4n20i2 without synergies"
plot "Usage/Set_B_instance_k4n20i2_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k4n20i2 without synergies"
plot "Usage/Set_B_instance_k4n20i2_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k4n20i3 without synergies"
plot "Usage/Set_B_instance_k4n20i3_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k4n20i3 without synergies"
plot "Usage/Set_B_instance_k4n20i3_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n20i2 without synergies"
plot "Usage/Set_B_instance_k9n20i2_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n20i2 without synergies"
plot "Usage/Set_B_instance_k9n20i2_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n20i3 without synergies"
plot "Usage/Set_B_instance_k9n20i3_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n20i3 without synergies"
plot "Usage/Set_B_instance_k9n20i3_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i4 without synergies"
plot "Usage/Set_B_instance_k9n100i4_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i4 without synergies"
plot "Usage/Set_B_instance_k9n100i4_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n20i1 without synergies"
plot "Usage/Set_B_instance_k9n20i1_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n20i1 without synergies"
plot "Usage/Set_B_instance_k9n20i1_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i5 without synergies"
plot "Usage/Set_B_instance_k9n100i5_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i5 without synergies"
plot "Usage/Set_B_instance_k9n100i5_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i1 without synergies"
plot "Usage/Set_B_instance_k9n100i1_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i1 without synergies"
plot "Usage/Set_B_instance_k9n100i1_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i2 without synergies"
plot "Usage/Set_B_instance_k9n100i2_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i2 without synergies"
plot "Usage/Set_B_instance_k9n100i2_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i3 without synergies"
plot "Usage/Set_B_instance_k9n100i3_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set B instance k9n100i3 without synergies"
plot "Usage/Set_B_instance_k9n100i3_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C512 with synergies"
plot "Usage/Set_C_instance_C512_with_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C512 with synergies"
plot "Usage/Set_C_instance_C512_with_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C256 with synergies"
plot "Usage/Set_C_instance_C256_with_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C256 with synergies"
plot "Usage/Set_C_instance_C256_with_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C128 with synergies"
plot "Usage/Set_C_instance_C128_with_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C128 with synergies"
plot "Usage/Set_C_instance_C128_with_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C64 with synergies"
plot "Usage/Set_C_instance_C64_with_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C64 with synergies"
plot "Usage/Set_C_instance_C64_with_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C256 without synergies"
plot "Usage/Set_C_instance_C256_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C256 without synergies"
plot "Usage/Set_C_instance_C256_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C64 without synergies"
plot "Usage/Set_C_instance_C64_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C64 without synergies"
plot "Usage/Set_C_instance_C64_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C128 without synergies"
plot "Usage/Set_C_instance_C128_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C128 without synergies"
plot "Usage/Set_C_instance_C128_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
set title "Set C instance C512 without synergies"
plot "Usage/Set_C_instance_C512_without_synergies_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
set title "Set C instance C512 without synergies"
plot "Usage/Set_C_instance_C512_without_synergies_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
unset multiplot
set term postscript eps font ",24" size 12, 12 color
set boxwidth 0.6 relative
set style fill solid border -1
set output "usage.eps"
set key off
set ylabel "Number of uses"
set multiplot layout 2, 1
set title "Global heuristic usage in the shake stage"
set xrange [0.1:13.9]
set yrange [-5.5:60.50000000000001]
set xtics ("incrMax" 1,"incrMin" 2,"incrRnd" 3,"liftIncr" 4,"liftRnd" 5,"rndMax" 6,"rndMin" 7,"rndRnd" 8,"swapGroup" 9,"swapHalf" 10,"swapQuarter" 11,"swapRandom" 12,"swapThird" 13) rotate by 90 right offset 0,-1
plot "Usage/global_shake.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#ffff00" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
set title "Global heuristic usage in the search stage"
set xrange [0.1:33.9]
set yrange [-46.7:513.7]
set xtics ("deflGrMax" 1,"deflGrMin" 2,"deflGrRnd" 3,"exchGrMax" 4,"exchGrMin" 5,"exchGrRnd" 6,"exclHigh" 7,"exclLow" 8,"exclRnd" 9,"fundAtMax" 10,"fundAtMin" 11,"fundAtRnd" 12,"inclHighMax" 13,"inclHighMin" 14,"inclHighRnd" 15,"inclLowMax" 16,"inclLowMin" 17,"inclLowRnd" 18,"inclRndMax" 19,"inclRndMin" 20,"inclRndRnd" 21,"incrMax" 22,"incrMin" 23,"incrRnd" 24,"inflGrMax" 25,"inflGrMin" 26,"inflGrRnd" 27,"liftIncr" 28,"liftRnd" 29,"rndMax" 30,"rndMin" 31,"rndRnd" 32,"swapOne" 33) rotate by 90 right offset 0,-1
plot "Usage/global_search.txt" using 1:3:2:6:5 notitle with candlesticks lt -1 lw 2 lc "#00ffff" whiskerbars, \
"" using 1:4:4:4:4 notitle with candlesticks lt -1 lw 3 lc rgb "#000000"
