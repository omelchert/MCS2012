set terminal postscript enhanced eps lw 1 18
set output "scipy_LSE_MLE.eps"

set lmargin 10
set rmargin -1
set bmargin 4
set tmargin -1

set origin 0.,0.
set size 1.,1.0
set multiplot

## distribution function
	set origin 0.,0.5
	set size 0.5,0.5
	set yr [0:0.1]; set ytics (0.,0.02,0.04,0.06,0.08,0.1)
	set xr [0:30]; set xtics (0,10,20,30,40)
	set ylabel "p(R_N)" font "Times-Italic"
	set xlabel "R_N" font "Times-Italic"
	set label 1 "(a)" at graph -0.42,1. font "Times-Roman"
        set label 11 "LSE" at graph 0.7,0.9 font "Helvetica"

	f(x)= x*exp( -(x-mu)**2/(2*s*s)  )/(s*s)
	mu = 0.
	s  = 7.1314

	p "scipy_LSE_nBins30.dat" u 1:2 w p pt 6 notitle\
	, f(x) w l lt 1 notitle
        unset label 1
        unset label 11

## distribution function
	set origin 0.,0.
	set size 0.5,0.5
	set yr [-3.2:-2.88]; set ytics (-3.3,-3.2,-3.1,-3.0,-2.9,-2.8)
	set xr [5:11]; set xtics (5,7,9,11)
	set ylabel "{/Helvetica ln}(L({/Symbol s}))/n" font "Times-Italic"
	set xlabel "{/Symbol s}" font "Times-Italic"
	set label 2 "(c)" at graph -0.42,1. font "Times-Roman"
        set label 21 "MLE" at graph 0.7,0.9 font "Helvetica"

        set format y "%02.1f"

	p "scipy_MLE.dat" u 1:2 w l notitle
        unset label 2
        unset label 21

## resampling MLE
	set origin 0.5,0.
	set size 0.5,0.5
        set xr [7.05:7.13]
        set yr [0:40]
        set xtics (7.05,7.09,7.13)
        set ytics (0,10,20,30,40)
        set format y "%g"
	set label 3 "(d)" at graph -0.42,1. font "Times-Roman"
        set label 31 "MLE" at graph 0.7,0.9 font "Helvetica"
	set ylabel "p({/Symbol s}_{/Helvetica MLE})" font "Times-Italic"
	set xlabel "{/Symbol s}_{/Helvetica MLE}" font "Times-Italic"
        p "res_sigma_MLE_nBoot1000.hist" u (0.5*($1+$2)):3:4 w yerrorlines pt 6 lt 1 notitle\
        , "scipy_MLE_sigmaEstim.dat" u 1:(5):2 w xerrorbars pt 4 lt 1 notitle
        unset label 3
        unset label 31


## resampling LSE
	set origin 0.5,0.5
	set size 0.5,0.5
        set xr [7.08:7.18]
        set yr [0:30]
        set xtics (7.08,7.13,7.18)
        set ytics (0,10,20,30,40)
        set format y "%g"
	set label 4 "(b)" at graph -0.42,1. font "Times-Roman"
        set label 41 "LSE" at graph 0.7,0.9 font "Helvetica"
	set ylabel "p({/Symbol s}_{/Helvetica LSE})" font "Times-Italic"
	set xlabel "{/Symbol s}_{/Helvetica LSE}" font "Times-Italic"
        p "res_sigma_LSE_nBoot2000.hist" u (0.5*($1+$2)):3:4 w yerrorlines pt 6 lt 1 notitle\
        , "scipy_LSE_sigmaEstim.dat" u 1:(5):2 w xerrorbars pt 4 lt 1 notitle
        unset label 4
        unset label 41

unset multiplot
