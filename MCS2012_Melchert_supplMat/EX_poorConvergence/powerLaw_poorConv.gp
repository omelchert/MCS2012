set terminal postscript enhanced eps lw 1 18
set output "powerLaw_poorConv.eps"

set origin 0.,0.
set size 1.,1.0
set multiplot

set lmargin 10
set rmargin 2 
set tmargin 0
set bmargin 4

## probability mass function
	set origin 0.,0.
	set size 0.5,0.5
	set key samplen 1.
	set yr [4:8]; set ytics (4,5,6,7,8)
	set xr [0:100000]; set xtics ("0" 0, "5{\264}10^4" 50000, "10^5" 100000)
	set xlabel "N" font "Times-Italic"
	set ylabel "av" font "Times-Roman"
	set label 1 "(a)" at graph -0.28,1. font "Times-Roman"

	p "powerLaw_poorConv_N100000.dat" u 1:2:3 w yerrorlines pt 7 ps 0.75 notitle\

## distribution function
	set origin 0.5,0.
	set size 0.5,0.5
	set yr [30:70]; set ytics(30,40,50,60,70)
	set ylabel "sDev" font "Times-Roman"
	unset label 1
	set label 2 "(b)" at graph -0.32,1. font "Times-Roman"

	p "powerLaw_poorConv_N100000.dat" u 1:4 w lp pt 7 ps 0.75 notitle

	set origin 0.58,0.215
	set size 0.38,0.26
	unset label 2
	set yr [4.5:5.5]; set ytics (4.5,5,5.5,6) font "Helvetica,15"
	set ylabel "aDev" offset 4.,0. font "Times-Roman"
	unset xlabel
	set xtics ("0" 0, "5{\264}10^4" 50000, "10^5" 100000) font "Helvetica,15"
	#unset xtics
	p "powerLaw_poorConv_N100000.dat" u 1:5 w lp pt 7 ps 0.75 notitle


unset multiplot
