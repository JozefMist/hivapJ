reset
set terminal qt enhanced size 500,300

set logscale y

ymin=1e-8
ymax=1e-2

set yrange [ymin:ymax]
set xrange [35:75]

set format y "10^{%L}"
set ytics font ',10'

set format x '%h' 
set xtics font ',10'
set xtics

set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set xlabel 'E* [MeV]' font ',12' offset 0,0

set key opaque

set arrow from 57.5,ymin to 57.5,ymax dt 2 lw 2 nohead
set label 2 'E_{p}=5.2 AMeV' at 56,ymax*0.01 rotate font ',9'

plot for [i=2:5] '46Ti_144Sm_190Po_pxn.dat' index 0 using 1:i with l lw 2.5 lt i dt 3 title '', for [i=2:5] '' index 1 using 1:i with l lw 2.5 lt i title columnhead(i)
