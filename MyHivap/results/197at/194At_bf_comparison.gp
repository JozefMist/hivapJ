reset
set terminal qt enhanced size 800,600
set bmargin 3

set key opaque
set grid

set logscale y

set title '56Fe+141Pr->194At+3n, BF comparison' font ',12'

ymin=1e-5
ymax=5e-3
set yrange [ymin:ymax]

set xrange [230:280]
set format y "10^{%L}"

set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set xlabel 'E(56Fe) [MeV]' font ',12' offset 0,0
set xtics font ',10'
set format x '%h'

plot for [i=0:4] '194At_bf_comparison.dat' index i using 1:6 with l lw 2.5 lt (i+1) title columnhead, '' index 5 using 1:3:4 with yerrorbars pt 5 lc rgb 'black' title columnhead

