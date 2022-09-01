reset
set terminal qt enhanced size 600,900
set multiplot layout 3,1 margins 0.1, 0.95, .065, .95 spacing 0, .025

set grid

set logscale y

ymin=3e-7
ymax=1e-3

bass_en_proj = 382

set arrow 1 from bass_en_proj, ymin to bass_en_proj, ymax dt 2 lw 2 nohead

set yrange [ymin:ymax]
set xrange [350:490]

set format y "10^{%L}"
set ytics font ',10'

set key opaque

set title '90Zr+103Rh->193At*, BF=0.55' font ',12' 

# set arrow from 57.5,ymin to 57.5,ymax dt 2 lw 2 nohead
# set label 2 'E_{p}=5.2 AMeV' at 56,ymax*0.01 rotate font ',9'

set label 1 'xn' at graph 0.7, 0.9 font ',12'
set label 4 'Bass barrier' at 400, 3e-4 font ',12'
set arrow 2 from 395, 3e-4 to 385, 3e-4 

set xtics
set format x '' 
plot for [i=4:8] '90Zr_103Rh_193At_bf0.55.dat' index 0 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:8] '' index 1 using 1:i with l lw 2.5 lt i dt 3 title ''

unset arrow 2
unset label 4
unset label 1
set label 2 'pxn' at graph 0.7, 0.9 font ',12'
unset title
set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set format x '' 
plot for [i=4:8] '90Zr_103Rh_193At_bf0.55.dat' index 2 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=4:8] '' index 3 using 1:i with l lw 2.5 lt i dt 3 title ''

unset label 4
unset label 2
set label 3 '2pxn' at graph 0.7, 0.9 font ',12'
unset title
ymin = ymin*10
# ymax = ymax*10
unset arrow 1
set arrow 1 from bass_en_proj, ymin to bass_en_proj, ymax dt 2 lw 2 nohead
set yrange [ymin:ymax]
set xlabel 'E(90Zr) [MeV]' font ',12' offset 0,0
set format x '%h' 
set xtics font ',10'
set xtics
unset ylabel
plot for [i=4:8] '90Zr_103Rh_193At_bf0.55.dat' index 4 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=4:8] '' index 5 using 1:i with l lw 2.5 lt i dt 3 title ''

unset multiplot
