#!/bin/bash

#read -p "Which IFUS to use?  " which_ifus

ifus_opt=IFUS=0

test=$(sed '32q;d' hivapein.dat)

IFS=' '
read -a ifus_test <<< "$test"

echo

if [ ${ifus_test[3]} = $ifus_opt ] 
then
	cp hivapein_IFUS0.dat hivapein.dat
	echo File hivapein.dat in $ifus_opt mode updated
else
	cp hivapein_IFUS0.dat hivapein.dat
	echo File hivapein.dat changed from ${ifus_test[3]} to $ifus_opt mode and updated
fi
