#! /bin/bash -ux

for file in $(ls -1 Toi_star.*)
do
   ftpixcalc corr_${file} "(a-b)/c" a=$file b=master_dark.fits c=mode_norm_mas_flat.fits 
done
