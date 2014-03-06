f(x)=exp(-(x-x0)**2./(2.*s*s))/(s*sqrt(2.*pi))*a
s = 0.175938822972801
x0 = 7.2
a = 1.
fit f(x) 'test.dat' u (0.5*($1+$2)):3:4 via x0,s,a

p 'test.dat' u (0.5*($1+$2)):3:4  w yerrorbars, f(x)
#    EOF
