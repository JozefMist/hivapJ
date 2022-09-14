#!/bin/bash

echo Updating input values
echo
./values.sh
echo
echo Changing mode to IFUS=0
echo
./ifus_mode_0.sh
echo
echo Running HIVAP for IFUS=0
echo
./hivapn
echo
echo Saving input and output for IFUS=0
echo
./move_hivapein_hivaperg.sh
echo
python3 extract_data.py hivaperg.dat
echo
echo Changing mode to IFUS=10
echo
./ifus_mode_10.sh
echo
echo Running HIVAP for IFUS=10
echo
./hivapn
echo
echo Saving input and output for IFUS=10
echo 
./move_hivapein_hivaperg.sh
echo
python3 extract_data.py hivaperg.dat
echo
echo Done

