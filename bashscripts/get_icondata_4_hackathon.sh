#!/bin/bash

### Note: 80km and 40km have a different file structure
#for RES in 20 10 5 2; do
for RES in 10; do
for NBR in 0001 0002 0003 0004 0005 0006 0007 0008 0009 0010; do

EXP=nawdexnwp-${RES}km-mis-${NBR}
echo "Working on:" $EXP

cd /scratch/b/b380459/icon_4_hackathon
mkdir ${EXP}
cd ${EXP}

#
pftp <<ENDE
cd /hpss/arch/bm0834/k203095/NAWDEX/ICON_OUTPUT_NWP
prompt
cd $EXP
mget nawdex*
quit
ENDE
#

done
done

cd /work/bb1018 
