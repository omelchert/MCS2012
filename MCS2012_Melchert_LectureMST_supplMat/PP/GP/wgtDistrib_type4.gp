set terminal postscript enhanced eps lw 2 24
set output './FIGS/wgtDistrib_type4.eps'

set label 100 "(d)" at graph -0.17,1. font "Times-Roman,32"

LW=1.5
PS=1.5
set style line 1 lw LW ps PS lt 1 pt 4
set style line 2 lw LW ps PS lt 1 pt 6
set style line 99 lw LW lt 1

set ylabel 'P_{T}({/Symbol w})' font 'Times-Italic'
set xlabel '{/Symbol w}' font 'Times-Italic'



set xr [:0.6]
set yr [0.4:6]

set ytics (0.5,1.,2.,4.,8)
set key samplen 1.
set key reverse Left


set logs y 

p '../wgt_wgtType4_N10000_m2_nSamp100.linBinning' u (0.5*($1+$2)):3 w p ls 1 t '{/Symbol w}_{ij}=1/(k_ik_j)'\

