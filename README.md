# hivap
repository for hivap and calculations

To compile HIVAP, run in the terminal:
  make clean
  make

Main HIVAP script is hivapn.

The script to automatize HIVAP consists of several subscripts:
 - ifus_mode_0.sh - changes HIVAP mode to IFUS=0
 - ifus_mode_10.sh - changes HIVAP mode to IFUS=10
 - move_hivapein_hivaperg.sh - automatically moves output file (hivaperg.dat) to the adam_MyHivap/hivaperg folder
    and changes its name (and its header - time, date and the reaction) according to the reaction, BARFAC value and IFUS mode used
 - script_hivap.sh - main script which runs all subscripts
 - values.sh - script to change initial values

To run a script which automatizes the HIVAP calculation, update values in values.sh:
 - Z and A of projectile, target and CN are needed as well as the "name" of isotope (to update the name of output file). 
 - r0 parameter can be calculated with a use of r0_calc macro. 
 - q2 deformation parameter (of the target nucleus) is from the Moller_1995_deformations_and_masses.pdf article (beta_2 parameter therein). 
 - sigr param. depends on the deformation, usually ~2.5 for spherical targets and up to 3.5 for deformed ones. 
  
Note: the scripts changing values and modes change those based on the position of affected line, 
therefore adding/removing lines from the hivapein.dat file messes things up.
