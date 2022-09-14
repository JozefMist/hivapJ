reset
set terminal qt enhanced size 700,500
# set multiplot layout 3,1 margins 0.11, 0.9, .085, .93 spacing 0, .025
set lmargin 10

set logscale y

ymin=1e-8
ymax=1e-3

set yrange [ymin:ymax]
set xrange [390:450]

set format y "10^{%L}"
set ytics font ',13'

set key opaque

set title '90Zr+103Rh->193At*, BF=0.67' font ',15' 

# set xtics
# set format x '' 
# plot for [i=3:7] '93Nb_100Ru_193At_lab_en.dat' index 0 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:6] '' index 1 using 1:i with l lw 2.5 lt i dt 3 title ''

# unset title
# set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
# set format x '' 
# plot for [i=3:7] '93Nb_100Ru_193At_lab_en.dat' index 2 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:6] '' index 3 using 1:i with l lw 2.5 lt i dt 3 title ''

# unset title
# set yrange [ymin*10:ymax*10]

set arrow 1 from 424,ymin to 424,ymax dt 3 lw 2 nohead
set arrow 2 from 410,ymin to 410, ymax dt 1 lw 2 nohead
# set 
set xlabel 'E_{lab} [MeV]' font ',14' offset 0,0
set ylabel '{/Symbol s} [mb]' font ',14' offset -2.9,0
set format x '%h' 
set xtics font ',13'
set xtics 5
set object rectangle from 410,ymin to 424,ymax fillcolor rgb 'blue' fillstyle transparent solid 0.2 noborder
# unset ylabel
set key font ',13'
plot for [i=5:7] '93Nb_100Ru_193At_lab_en.dat' using 1:i with l lw 2.5 lt i title columnhead(i)
#, for [i=3:6] '' index 5 using 1:i with l lw 2.5 lt i dt 3 title ''

# unset multiplot
