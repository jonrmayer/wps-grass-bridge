#!/bin/sh

echo "1  Running module r.contour"
python ../../GrassModuleStarter.py -f r.contour_input.txt     -l 1.log  -o 1_stdout.log  -e 1_stderr.log
echo "2  Running module r.neighbors"
python ../../GrassModuleStarter.py -f r.neighbors_input.txt   -l 2.log  -o 2_stdout.log  -e 2_stderr.log
echo "3  Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar2_input.txt     -l 3.log  -o 3_stdout.log  -e 3_stderr.log
echo "4  Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar2_mc_input.txt  -l 4.log  -o 4_stdout.log  -e 4_stderr.log
echo "5  Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar_input.txt      -l 5.log  -o 5_stdout.log  -e 5_stderr.log
echo "6  Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar_mc_input.txt   -l 6.log  -o 6_stdout.log  -e 6_stderr.log
echo "7  Running module r.watershed"
python ../../GrassModuleStarter.py -f r.watershed_input.txt   -l 7.log  -o 7_stdout.log  -e 7_stderr.log
echo "8  Running module v.buffer"
python ../../GrassModuleStarter.py -f v.buffer_input.txt      -l 8.log  -o 8_stdout.log  -e 8_stderr.log
echo "9  Running module v.to.rast"
python ../../GrassModuleStarter.py -f v.to.rast_input.txt     -l 9.log  -o 9_stdout.log  -e 9_stderr.log
echo "10 Running module r.contour"
python ../../GrassModuleStarter.py -f r.contour_res_input.txt -l 10.log -o 10_stdout.log -e 10_stderr.log
echo "11 Running addon module r.add"
python ../../GrassModuleStarter.py -f r.add_input.txt         -l 11.log -o 11_stdout.log -e 11_stderr.log
echo "12 Running addon module r.sub"
python ../../GrassModuleStarter.py -f r.sub_input.txt         -l 12.log -o 12_stdout.log -e 12_stderr.log
echo "13 Running addon module r.mult"
python ../../GrassModuleStarter.py -f r.mult_input.txt        -l 13.log -o 13_stdout.log -e 13_stderr.log
echo "14 Running addon module r.div"
python ../../GrassModuleStarter.py -f r.div_input.txt         -l 14.log -o 14_stdout.log -e 14_stderr.log
echo "15 Running module r.neighbors producing an error"
python ../../GrassModuleStarter.py -f r.neighbors_error_input.txt -l 15.log  -o 15_stdout.log  -e 15_stderr.log
echo "16 Running module v.voronoi"
python ../../GrassModuleStarter.py -f v.voronoi_input.txt         -l 16.log -o 16_stdout.log -e 16_stderr.log
echo "17 Running module r.contour with resolution change"
python ../../GrassModuleStarter.py -f r.contour_res_input.txt     -l 17.log  -o 17_stdout.log  -e 17_stderr.log
echo "18 Running module r.contour with HFA"
python ../../GrassModuleStarter.py -f r.contour_input_HFA.txt     -l 18.log  -o 18_stdout.log  -e 18_stderr.log
echo "19 Running module r.contour with netCDF"
python ../../GrassModuleStarter.py -f r.contour_input_netCDF.txt  -l 19.log  -o 19_stdout.log  -e 19_stderr.log
echo "20 Running module r.math with netCDF output"
python ../../GrassModuleStarter.py -f r.math1_input.txt  -l 20.log  -o 20_stdout.log  -e 20_stderr.log
echo "21 Running module r.math"
python ../../GrassModuleStarter.py -f r.math2_input.txt  -l 21.log  -o 21_stdout.log  -e 21_stderr.log
echo "22 Running module r.math producing an error"
python ../../GrassModuleStarter.py -f r.math3_input.txt  -l 22.log  -o 22_stdout.log  -e 22_stderr.log

