#!/bin/bash

indir='../data/interm'
outdir='../data/interm'
processeddir='../data/processed'

for i in {1..59}
do
    echo "Merging $i"
    cdo setmissval,-999 ${indir}/nee_hemis.${i}.nc ${outdir}/nee_hemis.${i}.na.nc
    if [ $i -eq 1 ]
    then  
        echo "Creating outfile nee_hemis.out.nc"
        cdo mergegrid ${indir}/nee_hemis.0.nc ${outdir}/nee_hemis.${i}.na.nc ${outdir}/nee_hemis.out.${i}.nc
    else
        cdo mergegrid ${outdir}/nee_hemis.out.$[i - 1].nc ${outdir}/nee_hemis.${i}.na.nc ${outdir}/nee_hemis.out.${i}.nc
    fi
    
done

mv ${outdir}/nee_hemis.out.59.nc ${processeddir}/nee_hemis.out.globe.nc