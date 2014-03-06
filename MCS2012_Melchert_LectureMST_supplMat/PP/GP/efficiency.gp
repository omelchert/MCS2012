set terminal postscript enhanced eps lw 2 24
set output './FIGS/efficiency.eps'

set label 100 "(e)" at graph -0.2,1. font "Times-Roman,32"

LW=1.5
PS=1.5
set style line 1 lw LW ps PS lt 1 pt 4
set style line 2 lw LW ps PS lt 1 pt 6

set ylabel '{/Symbol a} = {/Symbol w}_{T}/{/Symbol w}_G'
set xlabel 'N'

set xr [50:10000]
set yr [0.05:0.4]

set key samplen 1.
set key reverse Left

set format x "10^{%L}"
set ytics (0.05,0.1,0.2,0.4)

set logs 

p '../efficiency_wgtType4_m2_nSamp100.dat' u 1:2 w lp ls 1 t '{/Symbol w}_{ij}=1/k_ik_j'\
, '../efficiency_wgtType1_m2_nSamp100.dat' u 1:2 w lp ls 2 t '{/Symbol w}_{ij}=k_ik_j'

