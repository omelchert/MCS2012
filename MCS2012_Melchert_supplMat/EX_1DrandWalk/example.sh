echo "...generating 1D random walks"
python 1D_randWalk.py > N100_n100000.dat

echo "...generting pmf from data"
python pmf.py N100_n100000.dat 1 > N100_n100000.pmf

echo "...get eps"
gnuplot endpointDistrib.gp
