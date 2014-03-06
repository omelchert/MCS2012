set terminal postscript enhanced eps lw 2 24
set output './FIGS/degDistrib_type4.eps'

set label 100 "(b)" at graph -0.17,1. font "Times-Roman,32"

LW=1.5
PS=1.5
set style line 1 lw LW ps PS lt 1 pt 4
set style line 2 lw LW ps PS lt 1 pt 6
set style line 99 lw LW lt 1

set ylabel 'P_{T}(k)' font 'Times-Italic'
set xlabel 'k' font 'Times-Italic'

f(x) = a*x**(-b)
a=2.
b=2.5
fit [x=10:200] f(x) '../deg_wgtType4_N10000_m2_nSamp100.logBinned' u (0.5*($1+$2)):3 via a

set xr [2:]
set yr [:]

set key samplen 1.
set key reverse Left

set format "10^{%L}"

set logs  

set label 1 "{/Symbol \265} {/Times-Italic k}^{-2.5}" at graph 0.5,0.5

p '../deg_wgtType4_N10000_m2_nSamp100.logBinned' u (0.5*($1+$2)):3 w p ls 1 t '{/Symbol w}_{ij}=1/k_ik_j'\
, (x>8)?f(x):1/0 w l ls  99 notitle


