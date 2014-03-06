echo "...generating data"
python poorConvergence.py > powerLaw_poorConv_N100000.dat
echo "...get eps"
gnuplot powerLaw_poorConv.gp
