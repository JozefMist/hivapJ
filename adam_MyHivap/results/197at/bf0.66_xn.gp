reset 
set terminal qt enhanced size 800, 600

set title '56Fe+141Pr->197At*, BF=0.66' font ',12'

set logscale y
set format y "10^{%L}"

# set style line 100 lc rgb 'black' dt 3 lw 0.5
# set style line 101 lc rgb 'black' dt 4 lw 1
set grid

# set grid mytics

# set grid xtics lc rgb 'black' dt 3 lw 0.5


set xrange [230:290]
# set xrange [15:90]
set yrange [1E-6:5e-3]

set ylabel '{/Symbol s} [mb]' font ',12'
set xlabel '{E (56Fe) [MeV]' font ',12'

plot for [i=4:7] 'bf0.66_xn.dat' index 0 using 1:($i*10) with l lw 2 lt i title columnhead, '' index 1 using 1:($3*10) pt 5 lt 5 title columnhead, for [i=3:4] '' index 2 using 1:($i*10) pt 5 lt (i+3) title columnhead
