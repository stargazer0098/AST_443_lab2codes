#! /bin/bash -ux

for file in $(ls -1 corr_Toi_star.*)
do
    solve-field --ra 44.2917 --dec 33.3128 --radius 0.5 ${file} -m /astrolab/Fall_21/sshanto/
done
