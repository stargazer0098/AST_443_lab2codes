#! /bin/bash -u



for file in $(ls -1 corr_Toi_star.*.new) 
do
   sex ${file} -c default.se -CATALOG_NAME "${file}.cat"
done
