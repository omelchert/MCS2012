set terminal postscript enhanced eps lw 2 24
set output './FIGS/wgtDistrib_type1.eps'

set label 100 "(c)" at graph -0.17,1. font "Times-Roman,32"

LW=1.5
PS=1.5
set style line 1 lw LW ps PS lt 1 pt 4
set style line 2 lw LW ps PS lt 1 pt 6
set style line 99 lw LW lt 1

set ylabel 'P_{T}({/Symbol w})' font 'Times-Italic'
set xlabel '{/Symbol w}' font 'Times-Italic'



f(x) = a*x**(-b)
a=2.
b=3.
fit [x=50:600] f(x) '../wgt_wgtType1_N10000_m2_nSamp100.logBinned' u (0.5*($1+$2)):3 via a

set xr [10:]
set yr [:]

set key samplen 1.
set key reverse Left

set format "10^{%L}"

set logs  
set label 1 "{/Symbol \265} {/Symbol w}^{-3}" at graph 0.6,0.5

p '../wgt_wgtType1_N10000_m2_nSamp100.logBinned' u (0.5*($1+$2)):3 w p ls 1 t '{/Symbol w}_{ij}=k_ik_j'\
, (x>8)?f(x):1/0 w l ls  99 notitle

