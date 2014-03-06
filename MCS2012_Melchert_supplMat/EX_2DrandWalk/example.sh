echo "...generating 2d random walks"
#python 2D_randWalk.py > 2dRW_N100_n100000.dat

echo "...generating pdf from data"
python hist.py 2dRW_N100_n100000.dat 1 100 > 2dRW_N100_n100000.pdf

echo "...get eps"
gnuplot distance.gp
