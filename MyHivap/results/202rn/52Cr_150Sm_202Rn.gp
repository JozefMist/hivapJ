reset
set terminal qt enhanced size 600,800
set multiplot layout 3,1 margins 0.1, 0.97, .085, .93 spacing 0, .025
set logscale y

ymin=1e-5
ymax=1e0

set yrange [ymin:1e-1]

set xrange [25:65]
set format y "10^{%L}"

set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set ytics font ',10'

set format x '%h' 
set xtics font ',10'

set arrow from 38.2,ymin to 38.2,1e-1 dt 2 lw 1.5 nohead
set arrow from 44,ymin to 44,1e-1 dt 2 lw 1.5 nohead
set arrow from 50,ymin to 50,1e-1 dt 2 lw 1.5 nohead

unset xlabel
set xtics
set format x ''

set key opaque

plot for [i=3:7] '52Cr_150Sm_202Rn.dat' index 0 using 1:i with l lw 2.5 lt i title columnhead(i)

set arrow from 38.2,ymin to 38.2,ymax dt 2 lw 1.5 nohead
set arrow from 44,ymin to 44,ymax dt 2 lw 1.5 nohead
set arrow from 50,ymin to 50,ymax dt 2 lw 1.5 nohead

set yrange [:1e0]
unset xlabel
set xtics

plot for [i=3:7] '52Cr_150Sm_202Rn.dat' index 1 using 1:i with l lw 2.5 lt i title columnhead(i) 

set xlabel 'E* [MeV]' font ',12' offset 0,0
set xtics
set format x '%h'

plot for [i=3:7] '52Cr_150Sm_202Rn.dat' index 2  using 1:i with l lw 2.5 lt i title columnhead

unset multiplot
