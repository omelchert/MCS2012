set terminal postscript enhanced eps lw 1 18
set output "runTimes.eps"

set origin 0.,0.
set size 1.,1.1
set multiplot

set lmargin 10
set rmargin 2 
set tmargin 0
set bmargin 4

## probability mass function
	set origin 0.,0.
	set size 0.5,0.5
	set key samplen 1.
	set label 1 "(a)" at graph -0.32,1. font "Times-Roman"
	set logsc
	set format "10^{%L}"
	set xr [100:10000000]
	set yr [10**(-4):10]; set ytics (10**(-4),10**(-3),10**(-2),10**(-1),1,10)

	set ylabel "execution time (sec) &{sec}" font "Helvetica,18"
	set xlabel "{/Times-Italic N}" font "Helvetica,18"
        set key at graph 0.95,0.3

	p "./runTimes.dat" u 1:2 w lp pt 7 t "{/Times-Italic t}_{par}"\
	, "./runTimes.dat" u 1:3 w lp pt 9 t "{/Times-Italic t}_{seq}"\


## distribution function
	set origin 0.5,0.
	set size 0.5,0.5
	unset label 1
	set label 2 "(b)" at graph -0.36,1. font "Times-Roman"

	set logsc
	set format y "%g"
	set xr [100:10000000]
	set yr [0.08:2]
        set ytics (0.1,0.2,0.4,0.8,1.6)

	set ylabel "{/Times-Italic t}_{seq}/{/Times-Italic t}_{par}" font "Helvetica,18"
	set xlabel "{/Times-Italic N}" font "Helvetica,18"

	p "./runTimes.dat" u 1:4 w lp pt 7 notitle

unset multiplot
