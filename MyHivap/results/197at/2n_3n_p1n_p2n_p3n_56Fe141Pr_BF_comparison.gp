reset
set terminal qt enhanced size 800,1000

set multiplot layout 3,2

set bmargin 3

set key opaque

set logscale y

ymin=5e-6
ymax=1e-1
xmin=20
xmax=65

set format y "10^{%L}"

set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set xlabel 'E^* [MeV]' font ',12' offset 0,0
set xtics font ',10'
set format x '%h'



set yrange [ymin:ymax]

set xrange [20:55]
set title '56Fe+141Pr->194At+3n, BF comparison' font ',12'
plot for [i=0:3] '2n_3n_p1n_p2n_p3n_56Fe141Pr_BF_comparison.dat' index 4*i using 1:5 with l lw 2.5 lt (i+1) title columnhead, '' index 14 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'

set xrange [20:45]
set title '56Fe+141Pr->195At+2n, BF comparison' font ',12'
plot for [i=0:3] '2n_3n_p1n_p2n_p3n_56Fe141Pr_BF_comparison.dat' index 4*i using 1:6 with l lw 2.5 lt (i+1) title columnhead, '' index 15 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'

set yrange [ymin:ymax]
set xrange [30:70]
set title '56Fe+141Pr->193Po+p3n, BF comparison' font ',12'
plot for [i=0:3] '2n_3n_p1n_p2n_p3n_56Fe141Pr_BF_comparison.dat' index (4*i+1) using 1:5 with l lw 2.5 lt (i+1) title columnhead, '' index 16 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'

set yrange [ymin*10:ymax*10]
set xrange [20:55]
set title '56Fe+141Pr->194Po+p2n, BF comparison' font ',12'
plot for [i=0:3] '2n_3n_p1n_p2n_p3n_56Fe141Pr_BF_comparison.dat' index (4*i+1) using 1:6 with l lw 2.5 lt (i+1) title columnhead, '' index 17 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'

set yrange [ymin*10:ymax*10]
set xrange [20:55]
set title '56Fe+141Pr->195Po+p1n, BF comparison' font ',12'
plot for [i=0:3] '2n_3n_p1n_p2n_p3n_56Fe141Pr_BF_comparison.dat' index (4*i+1) using 1:7 with l lw 2.5 lt (i+1) title columnhead, '' index 18 using 1:2:3 with errorbars pt 5 lc rgb 'black' title 'Exp. value'

unset multiplot
