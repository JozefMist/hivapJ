#!/bin/bash

#what is produced
proj=54Cr
targ=208Pb
cn=262Sg

#here, input new values
mproj=54	
zproj=24
mtarg=208
ztarg=82
barfac=$1
r0=`python3 r0_calc.py $mproj $zproj $mtarg $ztarg`
q2=0.0
sigr=2.5
v0=40

line1=$(sed '1q;d' hivapein_IFUS10.dat)
line3=$(sed '3q;d' hivapein_IFUS10.dat)
line23=$(sed '23q;d' hivapein_IFUS10.dat)
line32=$(sed '32q;d' hivapein_IFUS10.dat)
line33=$(sed '33q;d' hivapein_IFUS10.dat)
line34=$(sed '34q;d' hivapein_IFUS10.dat)

IFS=' '
read -a word_line1 <<< "$line1"
read -a word_line3 <<< "$line3"
read -a word_line23 <<< "$line23"
read -a word_line32 <<< "$line32"
read -a word_line33 <<< "$line33"
read -a word_line34 <<< "$line34"

mproj_orig=${word_line3[0]}
zproj_orig=${word_line3[1]}
mtarg_orig=${word_line3[2]}
ztarg_orig=${word_line3[3]}
barfac_orig=${word_line23[2]}
v0_orig=${word_line33[0]}
r0_orig=${word_line33[1]}
q2_orig=${word_line33[3]}
sigr_orig=${word_line34[1]}

#For IFUS10 file
sed -i "s/$mproj_orig/MPROJ=$mproj/" hivapein_IFUS10.dat
sed -i "s/$zproj_orig/ZPROJ=$zproj/" hivapein_IFUS10.dat
sed -i "s/$mtarg_orig/MTARG=$mtarg/" hivapein_IFUS10.dat
sed -i "s/$ztarg_orig/ZTARG=$ztarg/" hivapein_IFUS10.dat
sed -i "s/$barfac_orig/BARFAC=$barfac/" hivapein_IFUS10.dat
sed -i "s/$v0_orig/V0=$v0/" hivapein_IFUS10.dat
sed -i "s/$r0_orig/r0=$r0/" hivapein_IFUS10.dat
sed -i "s/$q2_orig/Q2=$q2/" hivapein_IFUS10.dat
sed -i "s/$sigr_orig/sigr=$sigr/" hivapein_IFUS10.dat

#For IFUS0 file
sed -i "s/$mproj_orig/MPROJ=$mproj/" hivapein_IFUS0.dat
sed -i "s/$zproj_orig/ZPROJ=$zproj/" hivapein_IFUS0.dat
sed -i "s/$mtarg_orig/MTARG=$mtarg/" hivapein_IFUS0.dat
sed -i "s/$ztarg_orig/ZTARG=$ztarg/" hivapein_IFUS0.dat
sed -i "s/$barfac_orig/BARFAC=$barfac/" hivapein_IFUS0.dat

echo Values changed to:
echo
echo MPROJ=$mproj
echo ZPROJ=$zproj
echo MTARG=$mtarg
echo ZTARG=$ztarg
echo BARFAC=$barfac
echo V0=$v0
echo r0=$r0
echo Q2=$q2
echo sigr=$sigr

#Header update
today=$(date +"%d/%m/%Y")
now=$(date +"%H:%M")
sed -i "s|${word_line1[6]}|$today|" hivapein_IFUS10.dat
sed -i "s|${word_line1[6]}|$today|" hivapein_IFUS0.dat
sed -i "s|${word_line1[7]}|$now|" hivapein_IFUS10.dat
sed -i "s|${word_line1[7]}|$now|" hivapein_IFUS0.dat
sed -i "s|${word_line1[4]}|barfac$barfac|" hivapein_IFUS10.dat
sed -i "s|${word_line1[4]}|barfac$barfac|" hivapein_IFUS0.dat
sed -i "s|${word_line1[5]}|sigr$sigr|" hivapein_IFUS10.dat
sed -i "s|${word_line1[5]}|sigr$sigr|" hivapein_IFUS0.dat

sed -i "s|${word_line1[0]}|$proj|" hivapein_IFUS10.dat
sed -i "s|${word_line1[0]}|$proj|" hivapein_IFUS0.dat
sed -i "s|${word_line1[1]}|$targ|" hivapein_IFUS10.dat
sed -i "s|${word_line1[1]}|$targ|" hivapein_IFUS0.dat
sed -i "s|${word_line1[2]}|$cn|" hivapein_IFUS10.dat
sed -i "s|${word_line1[2]}|$cn|" hivapein_IFUS0.dat
