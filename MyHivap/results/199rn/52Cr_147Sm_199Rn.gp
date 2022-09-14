reset
set terminal qt enhanced size 600,650
set multiplot layout 3,1 margins 0.13, 0.98, .075, .96 spacing 0, .005

set logscale y

ymin=1.2e-7
ymax=0.95e-2

set yrange [ymin:ymax]
set xrange [20:82]

set format y "10^{%L}"
set ytics font ',13'

set key opaque

stats '52Cr_147Sm_199Rn.dat'
max_col = STATS_columns 

set title '52Cr+147Sm->199Rn*, BARFAC=0.67' font ',15' offset 0,-1

array(n) = word("30.8 33.1 38.8 41.1 53.2 59.3" , n)

do for [i=1:6]{
set arrow i from array(i), ymin to array(i), ymax dt 3 lw 1 nohead 
}

set arrow 7  from 37.9,ymin to 37.9,ymax dt 2 lw 1.5 nohead
#xn channels
set xtics
set format x '' 
set key font ',11'
set label 1 'xn' at graph 0.05,0.9 font ',12'
plot for [i=3:max_col] '52Cr_147Sm_199Rn.dat' index 0 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:max_col] '' index 1 using 1:i with l lw 2.5 lt i dt 3 title '', for [i=2:(max_col-1)] 'exp_52Cr_147Sm_199Rn.dat' index 0 using 1:(column(2*i)):(column(2*i+1)) with yerrorbars pt 7 ps 1.2 lt (i+1) lw 0 title '' #columnhead(2*i)

#pxn channels
unset title
set ylabel '{/Symbol s} [mb]' font ',15' offset -3.5,0
set format x '' 
unset label 1
set label 1 'pxn' at graph 0.05,0.9 font ',12'
plot for [i=3:max_col] '52Cr_147Sm_199Rn.dat' index 2 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:max_col] '' index 3 using 1:i with l lw 2.5 lt i dt 3 title '', for [i=2:(max_col-1)] 'exp_52Cr_147Sm_199Rn.dat' index 1 using 1:(column(2*i)):(column(2*i+1)) with yerrorbars pt 7 ps 1.2 lt (i+1) lw 0 title '' #columnhead(2*i)

#2pxn channels
unset title
ymin = ymin*10
ymax = ymax*10

do for [i=1:6]{
unset arrow i
set arrow i from array(i), ymin to array(i), ymax dt 3 lw 1 nohead 
}
unset arrow 0
set arrow 7  from 37.9,ymin to 37.9,ymax dt 2 lw 1.5 nohead
set yrange [ymin:ymax]
set xlabel 'E* [MeV]' font ',15' offset 0,0
set format x '%h' 
set xtics font ',13'
set xtics
unset ylabel
unset label 1
set label '2pxn' at graph 0.05,0.9 font ',12'
plot for [i=2:max_col] '52Cr_147Sm_199Rn.dat' index 4 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:max_col] '' index 5 using 1:i with l lw 1.5 lt i dt 3 title '',  for [i=2:(max_col-1)] 'exp_52Cr_147Sm_199Rn.dat' index 2 using 1:(column(2*i)):(column(2*i+1)) with yerrorbars pt 7 ps 1.2 lt (i+1) lw 0 title '' #columnhead(2*i)

unset multiplot
