reset
set terminal qt enhanced size 500,400
set bmargin 3

set key opaque

set logscale y

set title '51V+144Sm->195At*->192Po+p2n, BF comparison' font ',12'

ymin=5e-5
ymax=1e-1
set yrange [ymin:ymax]

set xrange [30:55]
set format y "10^{%L}"

set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set xlabel 'E^* [MeV]' font ',12' offset 0,0
set xtics font ',10'
set format x '%h'

set label '192Po (p2n)' font ',12' at 35,5e-2

plot for [i=0:4] '51V_144Sm_195At_barfac_comparison_192Po.dat' index i using 1:6 with l lw 2.5 lt (i+1) title columnhead, '' index 5 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'


unset multiplot
