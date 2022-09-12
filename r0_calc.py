#!/usr/bin/python3

import sys

if len(sys.argv) != 5:
    print('Four arguments needed: A_projectile, Z_projectile, A_target, Z_target')
    exit()

A_proj = int(sys.argv[1])
Z_proj = int(sys.argv[2])
A_targ = int(sys.argv[3])
Z_targ = int(sys.argv[4])

A_cn = A_proj + A_targ
Z_cn = Z_proj + Z_targ

A_proj_13 = A_proj**(1/3)
A_targ_13 = A_targ**(1/3)
A_cn_13 = A_cn**(1/3)

R_proj = 1.28*A_proj_13 + 0.8 / A_proj_13 - 0.76
R_targ = 1.28*A_targ_13 + 0.8 / A_targ_13 - 0.76

C_proj = R_proj - 1/R_proj
C_targ = R_targ - 1/R_targ

r0 = (C_proj + C_targ) / (A_proj_13 + A_targ_13)

print(round(r0,5))

sys.exit(0)
