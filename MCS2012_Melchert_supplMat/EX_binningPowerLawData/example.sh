echo "...generate power law data"
#python getPowerLawData.py > alpha2.5_xMin1.0_N100000.dat

echo "...perform linear binning"
python hist.py  alpha2.5_xMin1.0_N100000.dat 0 20000 > linBinned.hist
echo "...perform logarithmic binning"
python hist2.py alpha2.5_xMin1.0_N100000.dat 55  > logBinned.hist

echo "...get eps"
gnuplot histogram_powerLaw.gp
