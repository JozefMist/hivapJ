from exp_data import ExpData
from reaction import Reaction

import numpy as np

reactions = [

# RADONS

    Reaction('58Ni', '142Nd', '200Ra', barfac=0.52, sigr=2.0, bf_diff=0.0, channels_to_plot=['197Ra', '196Ra'], unit='nb'),
    
]
