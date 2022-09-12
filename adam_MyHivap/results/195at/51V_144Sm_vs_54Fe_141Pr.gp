reset 
set terminal qt enhanced size 800, 600

set title 'CN = 195At*: 54Fe+141Pr (4n) vs 51V+144Sm (3n), BF = 0.60' font ',12'

set logscale y
set format y "10^{%L}"

# set style line 100 lc rgb 'black' dt 3 lw 0.5
# set style line 101 lc rgb 'black' dt 4 lw 1

set grid

set xrange [220:280]
set yrange [1E-2:1E2]

set ylabel '{/Symbol s} [nb]' font ',12'
set xlabel '{E (proj) [MeV]' font ',12'

plot '51V_144Sm_vs_54Fe_141Pr.dat' index 0 using 1:($6*1E6) with l lw 2 lc rgb 'blue' title columnhead, '' index 0 using 1:($5*1E6) with l lw 1 dt 2 lc rgb 'blue' title columnhead, '' index 1 using 1:($3*1E6):($4*1E6) with yerrorbars pt 5 lc rgb 'blue' title columnhead, '' index 3 using 1:($5*1E6) with l lw 2 lc rgb 'red' title columnhead, '' index 3 using 1:($6*1E6) with l lw 1 dt 2 lc rgb 'red' title columnhead, '' index 4 using 1:($3*1E6) pt 5 lc rgb 'red' title columnhead
