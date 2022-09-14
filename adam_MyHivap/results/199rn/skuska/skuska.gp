reset
set terminal qt enhanced size 700,700

set logscale y

ymin=1.2e-8
ymax=9e-1

set yrange [ymin:ymax]
set xrange [20:80]

set format y "10^{%L}"
set ytics font ',10'

set key opaque

plot for [i=1:6] 'exp.dat' using 1:(column(2*i)):(column(2*i+1)) with yerrorbars pt 5 lt (i+2) lw 0 title columnhead(2*i)
#plot for [i=1:6] 'exp.dat' using 1:2*i with p pt 5 lt 2*i title columnhead(2*i)
