#!/bin/bash

line_in=$(sed '1q;d' hivapein.dat)
echo $line_in

line_erg=$(sed '5q;d' hivaperg.dat)

read -a header_in <<< "$line_in"
read -a header_erg <<< "$line_erg"

date_in=${header_in[6]}
date_erg=${header_erg[6]}
time_in=${header_in[7]}
time_erg=${header_erg[7]}

IFS=' '
read -a word <<< "$line_in"

whereto_in="MyHivap/hivapein"
whereto_erg="MyHivap/hivaperg"

hivapein_dest="${whereto_in}/hivapein_${word[0]}_${word[2]}_${word[4]}_${word[5]}_${word[6]}.dat"
hivaperg_dest="${whereto_erg}/hivaperg_${word[0]}_${word[2]}_${word[4]}_${word[5]}_${word[6]}.dat"

echo
if [ $date_in = $date_erg ] && [ $time_in = $time_erg ]
then
	cp hivapein.dat "$hivapein_dest"
	cp hivaperg.dat "$hivaperg_dest"

	echo hivapein.dat coppied into $hivapein_dest
	echo hivaperg.dat coppied into $hivaperg_dest
else
	echo hivaperg.dat does not correspond to hivapein.dat
fi

echo 
echo $whereto_in:
ls -lrth $whereto_in | tail -4

echo
echo $whereto_erg:
ls -lrth $whereto_erg | tail -4
