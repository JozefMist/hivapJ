reset
set terminal qt enhanced size 500,400
set bmargin 3

set key opaque

set logscale y

set title '56Fe+141Pr->195At+2n, BF comparison' font ',12'

ymin=1e-6
ymax=1e-2
set yrange [ymin:ymax]

set xrange [20:55]
set format y "10^{%L}"

set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set xlabel 'E^* [MeV]' font ',12' offset 0,0
set xtics font ',10'
set format x '%h'

plot for [i=0:4] '2n_56Fe141Pr_BF_comparison.dat' index i using 1:6 with l lw 2.5 lt (i+1) title columnhead, '' index 5 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'

unset multiplot
