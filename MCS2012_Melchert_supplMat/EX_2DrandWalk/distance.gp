set terminal postscript enhanced eps lw 1 18
set output "distance.eps"

set size 0.5,0.5
set yr [0:0.1]; set ytics (0.,0.02,0.04,0.06,0.08,0.1)
set xr [0:40]; set xtics (0,10,20,30,40)
set ylabel "p_X(R_N)" font "Times-Italic"
set xlabel "R_N" font "Times-Italic"
set label 1 "(b)" at graph -0.42,1. font "Times-Roman"

f(x)= x*exp( -(x-mu)**2/(2*s*s)  )/(s*s)
mu = 0.
s  = 8.
fit [x=:] f(x) "2dRW_N100_n100000.pdf" u (0.5*($1+$2)):3 via s

p "2dRW_N100_n100000.pdf" u (0.5*($1+$2)):3 w histeps notitle\
, f(x) w l notitle

