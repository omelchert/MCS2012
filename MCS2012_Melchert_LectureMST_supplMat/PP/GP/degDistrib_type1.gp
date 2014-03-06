set terminal postscript enhanced eps lw 2 24
set output './FIGS/degDistrib_type1.eps'

set label 100 "(a)" at graph -0.17,1. font "Times-Roman,32"

LW=1.5
PS=1.5
set style line 1 lw LW ps PS lt 1 pt 4
set style line 2 lw LW ps PS lt 1 pt 6

set ylabel 'P_{T}(k)' font 'Times-Italic'
set xlabel 'k' font 'Times-Italic'

set xr [:10]
set yr [:]

set key samplen 1.
set key reverse Left

set format y "10^{%L}"

set logs y 

p '../deg_wgtType1_N10000_m2_nSamp100.pmf' u 1:3 w p ls 1 t '{/Symbol w}_{ij}=k_ik_j'


