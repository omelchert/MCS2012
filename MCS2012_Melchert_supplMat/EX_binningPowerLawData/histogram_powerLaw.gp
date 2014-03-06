set terminal postscript enhanced eps lw 1 18
set output "histogram_powerLaw.eps"

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
	set label 3 "histogram using\nlinear binning" at graph 0.4,0.9 font "Helvetica,18"
	set logsc
	set format "10^{%L}"
	set xr [1:10000]
	set yr [10**(-6):5]; set ytics (0.01*10**(-8),10**(-8),10**(-6),10**(-4),10**(-2),10**(0))

	set ylabel "{/Times-Italic p}({/Times-Italic x})" font "Helvetica,18"
	set xlabel "{/Times-Italic x}" font "Helvetica,18"

	p "./linBinned.hist" u (0.5*($1+$2)):3 w p pt 7 notitle

## distribution function
	set origin 0.5,0.
	set size 0.5,0.5
	unset label 1
	unset label 3
	set label 2 "(b)" at graph -0.36,1. font "Times-Roman"
	set label 4 "histogram using\nlog binning" at graph 0.4,0.9 font "Helvetica,18"

	set logsc
	set format "10^{%L}"
	set xr [1:10000]
	#set yr [0.01*10**(-11):5*10**(-1)]
	set yr [0.01*10**(-8):5]

	set ylabel "{/Times-Italic p}({/Times-Italic x})" font "Helvetica,18"
	set xlabel "{/Times-Italic x}" font "Helvetica,18"

	p "./logBinned.hist" u (0.5*($1+$2)):3 w p pt 7 notitle

unset multiplot
