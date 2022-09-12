import sys
import os
import os.path
import pathlib

current_path = pathlib.Path().resolve()
if len(sys.argv) != 2:
    print('Incorrect input')
    exit()

file_name = sys.argv[1]

if not sys.argv[1].endswith('.dat'):
    print('You need to provide .dat file')

file = open(sys.argv[1], 'r', encoding='ascii', errors='ignore')
lines_in_file = file.readlines()

line_array = []

for line in lines_in_file:
    line_array.append(line.split())  

for line in line_array:
    if len(line) != 0:
        print(line[0] == 'E*/MeV')

