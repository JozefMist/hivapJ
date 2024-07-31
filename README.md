# HIVAP

To compile HIVAP, you need a fortran compiler, for example GNU Fortran (gfortran). To install gfortran, run
~~~
sudo apt install gfortran
~~~

Then, compile HIVAP:
~~~
make clean
make
~~~

The main HIVAP script is hivapn (run it with ./hivapn, after updating hivapein.dat file with correct values).
<br/>

Input file is hivapein.dat - hivapein_IFUS0.dat and hivapein_IFUS10.dat are for easy change of the IFUS mode <br/>

Output file is hivaperg.dat, ALL OUTPUT CS values are in milibarns [mb].<br>

Two fission-barrier approaches can be used, by changing the FISROT value in hivapein.dat (or hivapein_IFUS\*.dat to be used in the automatization script) - the Cohen-Plasil-Swiatecki approach (FISROT=0) [Cohen et al., Ann. Phys. 82, 1974] or the Sierk approach (FISROT=2) [Sierk, PRC 33, 1986]. 

The nuclear masses are in mlz.dat file, in the form of mass excess. 

## HIVAP automatization:

### Script parts
The script to automatize HIVAP consists of several subscripts:
 - ifus_mode_0.sh - changes HIVAP mode to IFUS=0 - mode without sub-barrier fusion
 - ifus_mode_10.sh - changes HIVAP mode to IFUS=10 - sub-barrier fusion enabled
 - move_hivapein_hivaperg.sh - automatically moves output file (hivaperg.dat) to the MyHivap/hivaperg folder
    and changes its name (and its header - time, date and the reaction) according to the reaction, BARFAC value and IFUS mode used
 - script_hivap.sh - main script which runs all subscripts
 - values.sh - script to change initial values
 - extract_data.py - script extract data for each evap channel and saves it into MyHivap/data_hivap in easily usable form - groups together each evap channel and adds beam energy

### Running the script
To run a script which automatizes the HIVAP calculation, update values in values.sh:
 - Z and A of projectile, target and CN are needed as well as the "name" of isotope (to update the name of output file). (I'll add automatic Z and A deduction from the isotope name later)
 - r0 parameter is calculated automatically by r0_calc.py script. 
 - v0 parameter - could be 40 (recommended in manual), 59, also seen other values, who knows what is correct
 - q2 deformation parameter (of the target nucleus) is from the Moller_1995_deformations_and_masses.pdf article (beta_2 parameter therein). 
 - sigr param. depends on the deformation and describes the barrier fluctuations, while influencing CS values below/near the barrier:
    - usually ~2.5 for spherical targets 
    - up to 3.5 for deformed ones
 - BARFAC value is taken as the command line parameter:
	for example, to run HIVAP with BARFAC=0.7, you run script_hivap.sh as follows:
    ~~~
    ./scrip_hivap.sh 0.7
    ~~~
    
     - If you want to run HIVAP for several BARFAC values (in an interval), run
    ~~~
    for i in $(seq <lower_limit> <step> <upper_limit_included>); do ./script_hivap.sh $i; done
    ~~~
    
    This will run HIVAP script for all values between <lowe_limit> and <upper_limit_included> with a step of <step>. 
    <br>
    <em>Example:</em>
    ~~~
    for i in $(seq 0.7 0.01 0.8); do ./script_hivap.sh $i; done
    ~~~
    This command runs HIVAP for BARFAC values from 0.7 to 0.8 (included), with a step of 0.01.
    
    In SK language, the decimal separator is comma (,), you have to change it to dot (.) with:
    ~~~
    export 'LC_NUMERIC="C"' 
    ~~~

<br>

<em>Note:</em> the scripts changing values and modes change those based on the position of affected line, 
therefore adding/removing lines from the hivapein.dat file messes things up.

