import sys
import os
import os.path
import pathlib

current_path = pathlib.Path().resolve()
if len(sys.argv) < 2:
    print('Incorrect input')
    exit()

for input_file in sys.argv[1:]:
    print('Processing file ' + input_file)
    if not input_file.endswith('.dat'):
        print('You need to provide .dat file')
    
    file = open(input_file, 'r', encoding='ascii', errors='ignore')
    lines_in_file = file.readlines()
    
    line_array = []
    
    for line in lines_in_file:
        line_array.append(line.split())  
    
    output_name = line_array[4][0] + '_' + line_array[4][2] + '_' + line_array[4][4] + '_' + line_array[4][5] + '_' + line_array[4][6] + '.dat'

    temp_xn_name = 'temp_xn.dat'
    temp_pxn_name = 'temp_pxn.dat'
    temp_2pxn_name = 'temp_2pxn.dat'

    temp_xn = open(temp_xn_name, 'w')
    temp_pxn = open(temp_pxn_name, 'w')
    temp_2pxn = open (temp_2pxn_name, 'w')
    
    output = open(output_name, 'a')
    
    i = 0
    while i < (len(line_array)-4):
        if len(line_array[i]) != 0 and line_array[i][0] == 'Querschnitte' and len(line_array[i+1]) == 0 and len(line_array[i+2]) != 0 and line_array[i+2][0] == 'E*/MeV':
            i += 2
            while len(line_array[i]) != 0:
                temp_xn.write(' '.join(line_array[i]) + '\n')
                i += 1
            i += 1
            while len(line_array[i]) != 0:
                temp_pxn.write(' '.join(line_array[i]) + '\n')
                i += 1
            i += 1
            while len(line_array[i]) != 0:
                temp_2pxn.write(' '.join(line_array[i]) + '\n')
                i += 1
            i += 1
            if len(line_array[i]) != 0 and line_array[i][0] == 'Z-Verteilung':
                i += 1
                continue
        i += 1
    
#os.remove(temp_xn_name)
#os.remove(temp_pxn_name)
#os.remove(temp_2pxn_name)
