reset
set terminal qt enhanced size 600,900
set multiplot layout 3,1 margins 0.1, 0.95, .065, .95 spacing 0, .025

set grid

set logscale y

ymin=5e-3
ymax=1e2

bass_en_proj = 382

set arrow 1 from bass_en_proj, ymin*5 to bass_en_proj, ymin dt 1 lw 2 

set yrange [ymin:ymax]
set xrange [370:480]

set format y "10^{%L}"
set ytics font ',10'

set key opaque

set title '90Zr+103Rh->193At*, BF=0.54' font ',12' 

# set arrow from 57.5,ymin to 57.5,ymax dt 2 lw 2 nohead
# set label 2 'E_{p}=5.2 AMeV' at 56,ymax*0.01 rotate font ',9'

set label 1 'xn' at graph 0.7, 0.9 font ',12'
set label 4 'B_{Bass}' at 384, 2*ymin font ',12'
# set arrow 2 from 395, 3e-4 to 385, 3e-4 

set xtics
set format x '' 
plot for [i=4:7] '90Zr_103Rh_193At_bf0.54.dat' index 0 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:7] '' index 1 using 1:i with l lw 2.5 lt i dt 3 title ''

# unset arrow 2
unset label 1
set label 2 'pxn' at graph 0.7, 0.9 font ',12'
unset title
set ylabel '{/Symbol s} [nb]' font ',12' offset -1,0
set format x '' 
plot for [i=4:7] '90Zr_103Rh_193At_bf0.54.dat' index 2 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=4:7] '' index 3 using 1:i with l lw 2.5 lt i dt 3 title ''

ymin = ymin*10
ymax = ymax*10
unset label 4
set label 4 'B_{Bass}' at 384, 2*ymin font ',12'
unset label 2
set label 3 '2pxn' at graph 0.7, 0.9 font ',12'
# unset title
unset arrow 1
set arrow 1 from bass_en_proj, ymin*5 to bass_en_proj, ymin dt 1 lw 2 
set yrange [ymin:ymax]
set xlabel 'E(90Zr) [MeV]' font ',12' offset 0,0
set format x '%h' 
set xtics font ',10'
set xtics
unset ylabel
plot for [i=4:7] '90Zr_103Rh_193At_bf0.54.dat' index 4 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=4:7] '' index 5 using 1:i with l lw 2.5 lt i dt 3 title ''

unset multiplot
