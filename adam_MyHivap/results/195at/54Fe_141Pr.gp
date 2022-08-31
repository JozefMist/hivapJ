reset 
set terminal qt enhanced size 600, 400

set title '54Fe+141Pr->195At*, BF=0.59' font ',12'

set logscale y
set format y "10^{%L}"

# set style line 100 lc rgb 'black' dt 3 lw 0.5
# set style line 101 lc rgb 'black' dt 4 lw 1

set grid

set xrange [230:290]
set yrange [1E-10:]

set ylabel '{/Symbol s} [mb]' font ',12'
set xlabel '{E (54Fe) [MeV]' font ',12'

plot for [i=4:7] '54Fe_141Pr.dat' index 0 using 1:i with l lw 2 lt (i) title columnhead, '' index 1 using 1:3 pt 5 lt 5 title columnhead
