reset 
set terminal qt enhanced size 600, 400

set title '51V+144Sm->195At*, BF=0.62' font ',12'

set logscale y
set format y "10^{%L}"

# set style line 100 lc rgb 'black' dt 3 lw 0.5
# set style line 101 lc rgb 'black' dt 4 lw 1

set grid

set xrange [210:270]
set yrange [1E-10:]

set ylabel '{/Symbol s} [mb]' font ',12'
set xlabel '{E (51V) [MeV]' font ',12'

plot for [i=5:8] '51V_144Sm.dat' index 0 using 1:i with l lw 2 lt (i) title columnhead, '' index 1 using 1:3 pt 5 lt 3 title columnhead, '' index 2 using 1:3 pt 3 lt 3 title columnhead, '' index 3 using 1:3 pt 2 lt 7 title columnhead
