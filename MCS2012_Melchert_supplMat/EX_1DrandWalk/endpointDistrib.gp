set terminal postscript enhanced eps lw 1 18
set output "endpointDistrib.eps"

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
	set yr [:0.11]; set ytics (0.,0.02,0.04,0.06,0.08,0.1)
	set xr [-50:50]
	set xlabel "x_N" font "Times-Italic"
	set ylabel "p_X(X=x_N)" font "Times-Italic"
	set label 1 "(a)" at graph -0.42,1. font "Times-Roman"

	## expected probability
	f(x)=2*exp(-(x)**2/(2*s*s))/(s*sqrt(2*pi))
	mu=0; s=10.

	p "N100_n100000.pmf" u 1:($2) w impulses t "observed"\
	, f(x) t "expected"

## distribution function
	set origin 0.5,0.
	set size 0.5,0.5
	set yr [0:1]; set ytics (0.,0.25,0.5,0.75,1.)
	set xr [-50:50]
	set ylabel "F_X(x_N)" font "Times-Italic"
	unset label 1
	set label 2 "(b)" at graph -0.42,1. font "Times-Roman"

	p "N100_n100000.pmf" u 1:($3) w steps notitle

unset multiplot
