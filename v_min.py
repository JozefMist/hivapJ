from cgi import print_arguments
from inspect import getmembers
import numpy as np 
import sys

magic_numbers = [2, 8, 20, 28, 50, 82, 126]

def getMagicDistance(number, magic): 
    if number  == 1:
        return 1

    for i in range(len(magic)):
        if number == magic[i]:
            return 0
        elif number < magic[i]:
            if abs(number - magic[i]) < abs(number - magic[i-1]):
                return abs(number - magic[i])
            else:
                return abs(number - magic[i-1])

def getMin(number1, number2):
    if number1 == number2:
        return number1
    elif number1 < number2:
        return number1
    else:
        return number2

if len(sys.argv) != 5:
    print('Need four arguments: A_target, Z_target, A_projectile, Z_projectile')
else:
    Nt = int(sys.argv[1]) - int(sys.argv[2])
    Zt = int(sys.argv[2])
    Np = int(sys.argv[3]) - int(sys.argv[4])
    Zp = int(sys.argv[4])

    print(getMin(getMagicDistance(Zp, magic_numbers), getMagicDistance(Np, magic_numbers)))

    v_min = getMin(getMagicDistance(Zt, magic_numbers), getMagicDistance(Nt, magic_numbers)) + getMin(getMagicDistance(Zp, magic_numbers), getMagicDistance(Np, magic_numbers))
    zt_zp = Zt*Zp

    print('Z_t * Z_p = ' + str(zt_zp))
    print('v_min = ' + str(v_min))
    print('Z_t * Z_p + 15 * v_min = ' + str(zt_zp + 15*v_min))
