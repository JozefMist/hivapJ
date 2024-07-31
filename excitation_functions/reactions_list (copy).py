from exp_data import ExpData
from reaction import Reaction

import numpy as np

reactions = [

# RADONS

    Reaction('52Cr', '144Sm', '196Rn', barfac=0.47, sigr=2.5, bf_diff=0.02, channels_to_plot=['193Rn', '194Rn'], unit='nb',
exp_data=ExpData([232, 248], 
                 cs_data=
                 {
                 '193Rn': [np.nan, 50E-9],
                 '194Rn': [50e-9, np.nan],
                 },
                 error_data=
                 {
                 '193Rn': [[np.nan, 20e-9]],
                 '194Rn':[[50e-9, np.nan]],
                 })
),
    Reaction('56Fe', '142Nd', '198Rn', barfac=0.57, sigr=2.5, bf_diff=0.02, channels_to_plot=['195Rn', '196Rn'], unit='nb', plot_maxCS_data=True,
exp_data=ExpData([250], 
                 cs_data=
                 {
                 '195Rn': [0.00000204],
                 '196Rn': [0.00000196],
                 })
),
    Reaction('52Cr', '147Sm', '199Rn', barfac=0.58, sigr=3.0, bf_diff=0.02, channels_to_plot=['195Rn', '196Rn', '197Rn'], unit='nb',
exp_data=ExpData([221.8,224.9,232.6,235.8,252.1,260.5], 
                 cs_data=
                 {'197Rn': [5.95E-06,4.07E-06,6.53E-07,1.21E-06,2.15E-07,np.nan],
                 '196Rn': [np.nan,2.28E-07,4.45E-07,1.33E-06,9.21E-08,9.87E-08], 
                 '195Rn': [np.nan,np.nan,np.nan,np.nan,3.80E-07,2.15E-07]},
                 error_data=
                 {'197Rn': [[1.14E-06,1.21E-06,2.15E-07,1.98E-07,7.39E-08,np.nan], [1.14E-06,1.58E-06,3.22E-07,1.98E-07,1.01E-07,np.nan]],
                 '196Rn': [[np.nan,1.88E-07,1.48E-07,1.60E-07,3.76E-08,8.16E-08], [np.nan,5.24E-07,1.48E-07,1.60E-07,3.76E-08,2.27E-07]],
                 '195Rn': [[np.nan,np.nan,np.nan,np.nan,1.18E-07,1.78E-07],[np.nan,np.nan,np.nan,np.nan,1.24E-07,4.94E-07]]})
),
    
    Reaction('52Cr', '147Sm', '199Rn', barfac=0.58, sigr=3.0, bf_diff=0.02, channels_to_plot=['195At', '196At', '198At', '199At'], unit='nb', evap_channel='pxn', 
# exp_data=ExpData([221.8,224.9,232.6,235.8,252.1,260.5], 
#                  cs_data=
#                  {'197Rn': [5.95E-06,4.07E-06,6.53E-07,1.21E-06,2.15E-07,np.nan],
#                  '196Rn': [np.nan,2.28E-07,4.45E-07,1.33E-06,9.21E-08,9.87E-08], 
#                  '195Rn': [np.nan,np.nan,np.nan,np.nan,3.80E-07,2.15E-07]},
#                  error_data=
#                  {'197Rn': [[1.14E-06,1.21E-06,2.15E-07,1.98E-07,7.39E-08,np.nan], [1.14E-06,1.58E-06,3.22E-07,1.98E-07,1.01E-07,np.nan]],
#                  '196Rn': [[np.nan,1.88E-07,1.48E-07,1.60E-07,3.76E-08,8.16E-08], [np.nan,5.24E-07,1.48E-07,1.60E-07,3.76E-08,2.27E-07]],
#                  '195Rn': [[np.nan,np.nan,np.nan,np.nan,1.18E-07,1.78E-07],[np.nan,np.nan,np.nan,np.nan,1.24E-07,4.94E-07]]})
),
    Reaction('82Kr', '118Sn', '200Rn', barfac=0.61, sigr=2.5, bf_diff=0.02, channels_to_plot=['197Rn'], unit='nb',
exp_data=ExpData([362], 
                 cs_data=
                 {
                 '197Rn': [13e-6],
                 },
                 error_data=
                 {
                 '197Rn': [[3e-6]],
                 })
),
    
    Reaction('52Cr', '149Sm', '201Rn', barfac=0.63, sigr=3.0, bf_diff=0.02, channels_to_plot=['196Rn', '197Rn', '198Rn', '199Rn'], unit='nb',
exp_data=ExpData([218.9,222.1,229.4,233.6,236.2,244.5,251.3], 
                 cs_data=
                 {'196Rn': [np.nan,np.nan,np.nan,np.nan,np.nan,8.18E-08,1.70E-07], 
                 '197Rn': [np.nan,np.nan,1.38E-06,7.04E-06,1.55E-05,1.41E-05,6.16E-06],
                 '198Rn': [2.85E-05,4.09E-05,5.52E-05,4.73E-05,8.58E-06,2.12E-06,1.21E-06],
                 '199Rn': [3.64E-05,3.03E-05,1.76E-05,1.17E-05,np.nan,np.nan,np.nan]
                 },
                 error_data=
                 {'196Rn': [[np.nan,np.nan,np.nan,np.nan,np.nan,6.76E-08,1.10E-07], [np.nan,np.nan,np.nan,np.nan,np.nan,1.88E-07,2.24E-07]],
                 '197Rn': [[np.nan,np.nan,8.38E-08,1.25E-06,1.47E-06,1.12E-06,7.54E-07], [np.nan,np.nan,8.38E-08,1.25E-06,1.47E-06,1.12E-06,7.54E-07]],
                 '198Rn': [[1.01E-06,2.32E-06,5.78E-07,3.52E-06,1.19E-06,4.74E-07,3.66E-07], [1.01E-06,2.32E-06,5.78E-07,3.52E-06,1.19E-06,4.74E-07,3.66E-07]],
                 '199Rn':[[2.04E-06,3.37E-06,5.57E-07,2.62E-06,np.nan,np.nan,np.nan], [2.04E-06,3.37E-06,5.57E-07,2.62E-06,np.nan,np.nan,np.nan]]
                 })
),
Reaction('52Cr', '149Sm', '201Rn', barfac=0.63, sigr=3.0, bf_diff=0.02, channels_to_plot=['196At', '197At', '199At', '200At'], unit='nb', evap_channel='pxn', 
# exp_data=ExpData([218.9,222.1,229.4,233.6,236.2,244.5,251.3], 
#                  cs_data=
#                  {'196Rn': [np.nan,np.nan,np.nan,np.nan,np.nan,8.18E-08,1.70E-07], 
#                  '197Rn': [np.nan,np.nan,1.38E-06,7.04E-06,1.55E-05,1.41E-05,6.16E-06],
#                  '198Rn': [2.85E-05,4.09E-05,5.52E-05,4.73E-05,8.58E-06,2.12E-06,1.21E-06],
#                  '199Rn': [3.64E-05,3.03E-05,1.76E-05,1.17E-05,np.nan,np.nan,np.nan]
#                  },
#                  error_data=
#                  {'196Rn': [[np.nan,np.nan,np.nan,np.nan,np.nan,6.76E-08,1.10E-07], [np.nan,np.nan,np.nan,np.nan,np.nan,1.88E-07,2.24E-07]],
#                  '197Rn': [[np.nan,np.nan,8.38E-08,1.25E-06,1.47E-06,1.12E-06,7.54E-07], [np.nan,np.nan,8.38E-08,1.25E-06,1.47E-06,1.12E-06,7.54E-07]],
#                  '198Rn': [[1.01E-06,2.32E-06,5.78E-07,3.52E-06,1.19E-06,4.74E-07,3.66E-07], [1.01E-06,2.32E-06,5.78E-07,3.52E-06,1.19E-06,4.74E-07,3.66E-07]],
#                  '199Rn':[[2.04E-06,3.37E-06,5.57E-07,2.62E-06,np.nan,np.nan,np.nan], [2.04E-06,3.37E-06,5.57E-07,2.62E-06,np.nan,np.nan,np.nan]]
#                  })
),
    
    Reaction('52Cr', '150Sm', '202Rn', barfac=0.66, sigr=3.0, bf_diff=0.02, channels_to_plot=['198Rn', '199Rn', '200Rn'], unit='nb', 
exp_data=ExpData([220.4,228.3,236.1], 
                 cs_data=
                 {
                 '198Rn': [9.77E-07,6.11E-06,9.11E-05],
                 '199Rn': [4.25E-04,6.40E-04,1.74E-04],
                 '200Rn': [1.26E-04,1.15E-04,1.68E-04]
                 },
                 error_data=
                 {
                 '198Rn': [[5.64E-07,3.94E-07,6.29E-06], [8.89E-07,3.94E-07,6.29E-06]],
                 '199Rn':[[2.40E-05,7.98E-06,1.73E-05], [2.40E-05,7.98E-06,1.73E-05]],
                 '200Rn':[[1.62E-05,4.33E-06,2.16E-05], [1.62E-05,4.33E-06,2.16E-05]]
                 })
),
    
    Reaction('52Cr', '150Sm', '202Rn', barfac=0.66, sigr=3.0, bf_diff=0.02, channels_to_plot=['197At', '198At', '199At', '200At'], unit='nb', evap_channel='pxn', 
# exp_data=ExpData([220.4,228.3,236.1], 
#                  cs_data=
#                  {
#                  '198Rn': [9.77E-07,6.11E-06,9.11E-05],
#                  '199Rn': [4.25E-04,6.40E-04,1.74E-04],
#                  '200Rn': [1.26E-04,1.15E-04,1.68E-04]
#                  },
#                  error_data=
#                  {
#                  '198Rn': [[5.64E-07,3.94E-07,6.29E-06], [8.89E-07,3.94E-07,6.29E-06]],
#                  '199Rn':[[2.40E-05,7.98E-06,1.73E-05], [2.40E-05,7.98E-06,1.73E-05]],
#                  '200Rn':[[1.62E-05,4.33E-06,2.16E-05], [1.62E-05,4.33E-06,2.16E-05]]
#                  })
),   
    
    Reaction('36Ar', '166Er', '202Rn', barfac=0.70, sigr=3.2, bf_diff=0.02, channels_to_plot=['198Rn'], unit='nb',
exp_data=ExpData([175], 
                 cs_data=
                 {
                 '198Rn': [180e-6],
                 })
),
    Reaction('35Cl', '169Tm', '204Rn', barfac=0.71, sigr=3.3, bf_diff=0.02, channels_to_plot=['197Rn', '198Rn'], unit='nb',
exp_data=ExpData([196, 208.25], 
                 cs_data=
                 {
                 '197Rn': [np.nan,0.000022],
                 '198Rn': [0.00006,np.nan]
                 })
),
    Reaction('28Si', '176Hf', '204Rn', barfac=0.67, sigr=3.2, bf_diff=0.02, channels_to_plot=['200Rn'], unit='ub',
exp_data=ExpData([142], 
                 cs_data=
                 {
                 '200Rn': [5e-3],
                 })
),
    Reaction('45Sc', '159Tb', '204Rn', barfac=0.67, sigr=3.2, bf_diff=0.02, channels_to_plot=['199Rn', '200Rn'], unit='ub', evap_channel='xn', save_note='Werke',
             exp_data=ExpData(
                 E_lab=[195,195.8,199.4,201.2,203.9,205.8,213.3,217,221.4],
                 cs_data={
                     '199Rn': [np.nan,np.nan,np.nan,np.nan,0.0005,np.nan,np.nan,np.nan,np.nan],
                     '200Rn': [np.nan,np.nan,0.0024,np.nan,0.0008,np.nan,0.002,np.nan,np.nan]
                 },
                 error_data={
                     '199Rn': [[np.nan,np.nan,np.nan,np.nan,0.0003,np.nan,np.nan,np.nan,np.nan], [np.nan,np.nan,np.nan,np.nan,0.0004,np.nan,np.nan,np.nan,np.nan]],
                     '200Rn': [[np.nan,np.nan,0.0014,np.nan,0.0004,np.nan,0.0009,np.nan,np.nan], [np.nan,np.nan,0.0023,np.nan,0.0006,np.nan,0.0013,np.nan,np.nan]]
                 }
             )
    
),
    Reaction('45Sc', '159Tb', '204Rn', barfac=0.67, sigr=3.2, bf_diff=0.02, channels_to_plot=['198At', '199At', '200At', '201At'], unit='ub', evap_channel='pxn', save_note='Werke',
             exp_data=ExpData(
                 E_lab=[195,195.8,199.4,201.2,203.9,205.8,213.3,217,221.4],
                 cs_data={
                     '198At': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.015],
                     '199At': [np.nan,np.nan,0.0031,0.003,0.0095,0.017,np.nan,0.029,0.011],
                     '200At': [np.nan,0.04,0.039,0.026,0.052,0.054,0.031,0.019,np.nan],
                     '201At': [np.nan,np.nan,np.nan,np.nan,0.0098,0.0074,0.0081,np.nan,np.nan]
                 },
                 error_data={
                     '198At': [[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.005],[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.007]],
                     '199At': [[np.nan,np.nan,0.0016,0.0016,0.0014,0.003,np.nan,0.004,0.004],[np.nan,np.nan,0.0025,0.0025,0.0014,0.003,np.nan,0.004,0.006]],
                     '200At': [[np.nan,0.014,0.01,0.01,0.005,0.008,0.006,0.006,np.nan],[np.nan,0.014,0.01,0.01,0.005,0.008,0.006,0.006,np.nan]],
                     '201At': [[np.nan,np.nan,np.nan,np.nan,0.0023,0.0025,0.0026,np.nan,np.nan],[np.nan,np.nan,np.nan,np.nan,0.0023,0.0033,0.0034,np.nan,np.nan]]
                 }
             )
    
),
    Reaction('44Ca', '162Dy', '206Rn', barfac=0.68, sigr=3.2, bf_diff=0.02, channels_to_plot=['201Rn', '202Rn', '203Rn'], unit='ub',
exp_data=ExpData([183.7,188.9,195.4,199.5,207.1], 
                 cs_data=
                 {
                 '203Rn': [0.071,0.059,0.031,np.nan,np.nan],
                 '202Rn': [0.05,0.13,0.076,0.055,0.014],
                 '201Rn': [np.nan,np.nan,0.024,0.02,0.027]
                 },
                 error_data=
                 {
                 '203Rn': [[0.014,0.015,0.009,np.nan,np.nan], [0.017,0.019,0.011,np.nan,np.nan]],
                 '202Rn':[[0.011,0.02,0.014,0.01,0.005], [0.013,0.02,0.014,0.012,0.007]],
                 '201Rn':[[np.nan,np.nan,0.006,0.005,0.006], [np.nan,np.nan,0.007,0.007,0.007]]
                 })
),
    Reaction('48Ca', '162Dy', '210Rn', barfac=0.68, sigr=3.2, bf_diff=0.02, channels_to_plot=['204Rn', '207Rn'], unit='mb',
exp_data=ExpData([181.5,190.2,197.9,204.9,210.4], 
                 cs_data=
                 {
                 '207Rn': [1.6,1.7,1.3,0.5,np.nan],
                 '204Rn': [np.nan,np.nan,np.nan,0.3,1.1],
                 },
                 error_data=
                 {
                 '207Rn': [[0.4,0.9,0.3,0.2,np.nan]],
                 '204Rn':[[np.nan,np.nan,np.nan,0.1,0.2]],
                 })
),
    Reaction('22Ne', '190Os', '212Rn', barfac=0.79, sigr=3.0, bf_diff=0.02, channels_to_plot=['200Rn', '201Rn', '202Rn', '203Rn', '204Rn', '205Rn'], unit='ub', plot_maxCS_data=True, 
exp_data=ExpData([150], 
                 cs_data={
                     '205Rn': [27.7], 
                     '204Rn': [7.7], 
                     '203Rn': [3], 
                     '202Rn': [0.52], 
                     '201Rn': [0.058], 
                     '200Rn': [0.0036]
                 })),
    
    
#ASTATINES
    
    Reaction('90Zr', '103Rh', '193At', 0.41, 3.0, bf_diff=0.02, channels_to_plot=['190At'], unit='nb', exp_data=ExpData(
        E_lab=[410],
        cs_data={
        '190At': [0.13*1e-6]
        },
        error_data={
            '190At': [[0.065*1e-6]]
        }
    )),
    Reaction('51V', '144Sm', '195At', 0.60, 2.5, bf_diff=0.02, channels_to_plot=['192At'], unit='ub', save_note='SHIP', exp_data=ExpData(
        E_lab=[230], cs_data={'192At': [0.00004]}, error_data={'192At': [[0.00001]]}
    )),
    Reaction('54Fe', '141Pr', '195At', 0.55, 2.5, bf_diff=0.02, channels_to_plot=['191At'], unit='ub', save_note='RITU', exp_data=ExpData(
        E_lab=[260], cs_data={'191At': [0.0000003]}
    )),
    Reaction('56Fe', '141Pr', '197At', 0.64, 2.5, bf_diff=0.02, channels_to_plot=['193At', '194At', '195At'], unit='ub', save_note='SHIP', 
            exp_data=ExpData(
                E_lab=[229.4,235,243.4,251.8,265.8],
                cs_data={
                    '195At': [0.00013,0.00026,0.00013,0.000038,0.0000027],
                    '194At': [np.nan,0.000019,0.00018,0.0008,0.00018]
                },
                error_data={
                    '195At': [[0.00005,0.00008,0.00003,0.00001,0.0000013]],
                    '194At': [[np.nan,0.000009,0.00005,0.00024,0.00005]]
                }
            )),
    Reaction('56Fe', '141Pr', '197At', 0.64, 2.5, bf_diff=0.02, channels_to_plot=['193At', '194At', '195At'], unit='ub', save_note='RITU',
            exp_data=ExpData(
                E_lab=[230,248,266],
                cs_data={
                    '195At': [0.0009,np.nan,np.nan],
                    '194At': [np.nan,0.0015,np.nan],
                    '193At': [np.nan,np.nan,0.00004]
                }
            )),
    Reaction('56Fe', '141Pr', '197At', 0.64, 2.5, bf_diff=0.02, channels_to_plot=['193At', '194At', '195At'], unit='ub', save_note='both_exp',
            exp_data=ExpData(
                E_lab=[229.4,230,235,243.4,248,251.8,265.8,266],
                cs_data={
                    '195At': [0.00013,0.0009,0.00026,0.00013,np.nan,0.000038,0.0000027,np.nan],
                    '194At': [np.nan,np.nan,0.000019,0.00018,0.0015,0.0008,0.00018,np.nan],
                    '193At': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.00004],
                },
                error_data={
                    '195At': [[0.00005,np.nan,0.00008,0.00003,np.nan,0.00001,0.0000013,np.nan]],
                    '194At': [[np.nan,np.nan,0.000009,0.00005,np.nan,0.00024,0.00005,np.nan]],
                    '193At': [[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]],
                }
            )),
    Reaction('51V', '147Sm', '198At', 0.62, 3.0, bf_diff=0.02, channels_to_plot=['194At', '195At', '196At'], unit='ub',
            exp_data=ExpData(
            E_lab=[224],
                cs_data={
                    '194At': [50e-6],
                    '195At': [1200e-6],
                    '196At': [230e-6]
                }
            )),
    Reaction('40Ca', '159Tb', '199At', 0.72, 3.2, bf_diff=0.02, channels_to_plot=['194Po', '195Po', '196Po'], unit='ub', evap_channel='pxn',
            exp_data=ExpData(
                E_lab=[184,190,194,201,206],
                cs_data={
                    '196Po': [0.023,0.019,0.014,np.nan,0.0025],
                    '195Po': [0.041,0.11,0.102,0.04,0.03],
                    '194Po': [0.0005,0.004,0.015,0.042,0.089]
                }
            )),
    
    Reaction('45Sc', '156Gd', '201At', 0.61, 3.2, bf_diff=0.02, channels_to_plot=['197At', '198At'], unit='ub', save_note='Werke', 
            exp_data=ExpData(
                E_lab=[182.6,191.5,197.9,203.3,208.7],
                cs_data={
                    '198At': [0.0058,0.0031,np.nan,np.nan,np.nan],
                    '197At': [0.0012,0.0034,0.0057,np.nan,np.nan]
                },
                error_data={
                    '198At': [[0.0017,0.0013,np.nan,np.nan,np.nan], [0.0017,0.0019,np.nan,np.nan,np.nan]],
                    '197At': [[0.0006,0.0013,0.0021,np.nan,np.nan], [0.0009,0.0018,0.0021,np.nan,np.nan]]
                }
            )),
    Reaction('45Sc', '156Gd', '201At', 0.61, 3.2, bf_diff=0.02, channels_to_plot=['196Po', '197Po', '198Po'], unit='ub', evap_channel='pxn', save_note='Werke',
            exp_data=ExpData(
                E_lab=[182.6,191.5,197.9,203.3,208.7],
                cs_data={
                    '198Po': [0.0036,np.nan,np.nan,np.nan,np.nan],
                    '197Po': [0.0014,0.026,0.032,0.024,0.011],
                    '196Po': [np.nan,np.nan,np.nan,0.013,0.034]
                },
                error_data={
                    '198Po': [[0.0013,np.nan,np.nan,np.nan,np.nan],[0.0019,np.nan,np.nan,np.nan,np.nan]],
                    '197Po': [[0.0007,0.005,0.005,0.005,0.003],[0.0011,0.005,0.005,0.005,0.003]],
                    '196Po': [[np.nan,np.nan,np.nan,0.003,0.005],[np.nan,np.nan,np.nan,0.003,0.005]]
                }
            )),
    
    Reaction('45Sc', '157Gd', '202At', 0.62, 3.2, bf_diff=0.02, channels_to_plot=['197At', '198At', '199At'], unit='ub', save_note='Werke',
            exp_data=ExpData(
                E_lab=[185.3,190.9,194.2,198.2,200.5,205.9,211.3],
                cs_data={
                    '199At': [0.0098,0.0067,0.014,0.0029,0.0037,np.nan,np.nan],
                    '198At': [np.nan,0.025,0.022,0.02,0.014,0.0033,np.nan],
                    '197At': [np.nan,np.nan,np.nan,np.nan,0.0035,np.nan,np.nan]
                },
                error_data={
                    '199At': [[0.0034,0.0023,0.004,0.0015,0.0016,np.nan,np.nan],[0.0046,0.0031,0.004,0.0024,0.0023,np.nan,np.nan]],
                    '198At': [[np.nan,0.005,0.005,0.005,0.004,0.0018,np.nan],[np.nan,0.005,0.005,0.005,0.004,0.0029,np.nan]],
                    '197At': [[np.nan,np.nan,np.nan,np.nan,0.0015,np.nan,np.nan],[np.nan,np.nan,np.nan,np.nan,0.0021,np.nan,np.nan]]
                }
            )),
    Reaction('45Sc', '157Gd', '202At', 0.62, 3.2, bf_diff=0.02, channels_to_plot=['196Po', '197Po', '198Po', '199Po'], unit='ub', evap_channel='pxn', save_note='Werke',
            exp_data=ExpData(
                E_lab=[185.3,190.9,194.2,198.2,200.5,205.9,211.3],
                cs_data={
                    '199Po': [np.nan,np.nan,0.036,np.nan,0.049,np.nan,np.nan],
                    '198Po': [np.nan,0.018,0.008,0.039,0.042,0.015,0.01],
                    '197Po': [np.nan,0.0059,np.nan,0.018,0.028,0.029,0.042],
                    '196Po': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.0069]
                },
                error_data={
                    '199Po': [[np.nan,np.nan,0.015,np.nan,0.018,np.nan,np.nan],[np.nan,np.nan,0.021,np.nan,0.025,np.nan,np.nan]],
                    '198Po': [[np.nan,0.006,0.0029,0.008,0.008,0.006,0.004],[np.nan,0.006,0.0039,0.008,0.008,0.006,0.006]],
                    '197Po': [[np.nan,0.0023,np.nan,0.005,0.006,0.007,0.009],[np.nan,0.0032,np.nan,0.005,0.006,0.007,0.009]],
                    '196Po': [[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.0028],[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.004]]
                }
            )),
    
    Reaction('45Sc', '158Gd', '203At', 0.60, 3.2, bf_diff=0.02, channels_to_plot=['198At', '199At', '200At'], unit='ub', save_note='Werke',
            exp_data=ExpData(
                E_lab=[180.4,185.9,189.1,195.3,201.3],
                cs_data={
                    '200At': [0.015,0.0087,0.0083,np.nan,np.nan],
                    '199At': [0.0071,0.034,0.039,0.033,0.017],
                    '198At': [np.nan,np.nan,np.nan,0.003,0.011],
                },
                error_data={
                    '200At': [[0.008,0.0042,0.0037,np.nan,np.nan],[0.013,0.0062,0.0052,np.nan,np.nan]],
                    '199At': [[0.0043,0.008,0.007,0.005,0.004],[0.0068,0.008,0.007,0.005,0.004]],
                    '198At': [[np.nan,np.nan,np.nan,0.0013,0.004],[np.nan,np.nan,np.nan,0.0019,0.004]],
                }
            )),
    Reaction('45Sc', '158Gd', '203At', 0.60, 3.2, bf_diff=0.02, channels_to_plot=['198Po', '199Po', '200Po'], unit='ub', evap_channel='pxn', save_note='Werke',
            exp_data=ExpData(
                E_lab=[180.4,185.9,189.1,195.3,201.3],
                cs_data={
                    '200Po': [0.069,np.nan,np.nan,np.nan,np.nan],
                    '199Po': [np.nan,np.nan,0.026,0.017,0.088],
                    '198Po': [np.nan,np.nan,np.nan,0.0035,0.023],
                },
                error_data={
                    '200Po': [[0.038,np.nan,np.nan,np.nan,np.nan],[0.059,np.nan,np.nan,np.nan,np.nan]],
                    '199Po': [[np.nan,np.nan,0.015,0.009,0.033],[np.nan,np.nan,0.024,0.015,0.033]],
                    '198Po': [[np.nan,np.nan,np.nan,0.0017,0.007],[np.nan,np.nan,np.nan,0.0026,0.007]],
                }
            )),
    
    Reaction('44Ca', '159Tb', '203At', 0.64, 3.2, bf_diff=0.02, channels_to_plot=['198At', '199At', '200At'], unit='ub', save_note='Werke',
            exp_data=ExpData(
                E_lab=[184.7,189.8,196.3,200.5,208],
                cs_data={
                    '200At': [0.14,0.09,0.023,np.nan,np.nan],
                    '199At': [0.13,0.23,0.12,0.041,np.nan],
                    '198At': [np.nan,0.018,0.034,0.048,0.033],
                },
                error_data={
                    '200At': [[0.03,0.021,0.008,np.nan,np.nan],[0.04,0.025,0.011,np.nan,np.nan]],
                    '199At': [[0.02,0.02,0.01,0.008,np.nan],[0.02,0.02,0.01,0.01,np.nan]],
                    '198At': [[np.nan,0.006,0.007,0.009,0.007],[np.nan,0.008,0.008,0.011,0.009]],
                }
            )),
    Reaction('44Ca', '159Tb', '203At', 0.64, 3.2, bf_diff=0.02, channels_to_plot=['197Po', '198Po', '199Po'], unit='ub', evap_channel='pxn', save_note='Werke',
            exp_data=ExpData(
                E_lab=[184.7,189.8,196.3,200.5,208],
                cs_data={
                    '199Po': [np.nan,0.17,0.22,0.2,0.16],
                    '198Po': [np.nan,np.nan,0.033,0.051,0.05],
                    '197Po': [np.nan,np.nan,np.nan,np.nan,0.038],
                },
                error_data={
                    '199Po': [[np.nan,0.06,0.05,0.06,0.05],[np.nan,0.07,0.06,0.08,0.07]],
                    '198Po': [[np.nan,np.nan,0.008,0.012,0.011],[np.nan,np.nan,0.01,0.015,0.014]],
                    '197Po': [[np.nan,np.nan,np.nan,np.nan,0.009],[np.nan,np.nan,np.nan,np.nan,0.011]],
                }
            )),
    
    Reaction('45Sc', '160Gd', '205At', 0.63, 3.2, bf_diff=0.02, channels_to_plot=['199At', '200At', '201At', '202At'], unit='ub', save_note='Werke',
             exp_data=ExpData(
                E_lab=[181.2,186.6,189.9,194.3,202],
                cs_data={
                    '202At': [np.nan,0.041,np.nan,0.012,np.nan],
                    '201At': [0.1,0.15,0.12,0.14,0.028],
                    '200At': [np.nan,0.035,0.1,0.14,0.33],
                    '199At': [np.nan,np.nan,np.nan,0.0024,0.041]
                },
                error_data={
                    '202At': [[np.nan,0.014,np.nan,0.004,np.nan],[np.nan,0.014,np.nan,0.006,np.nan]],
                    '201At': [[0.02,0.02,0.02,0.01,0.009],[0.02,0.02,0.02,0.01,0.009]],
                    '200At': [[np.nan,0.01,0.02,0.01,0.03],[np.nan,0.01,0.02,0.01,0.03]],
                    '199At': [[np.nan,np.nan,np.nan,0.001,0.007],[np.nan,np.nan,np.nan,0.0014,0.007]]
                }
            )),
    Reaction('45Sc', '160Gd', '205At', 0.63, 3.2, bf_diff=0.02, channels_to_plot=['199Po', '200Po', '201Po'], unit='ub', save_note='Werke', evap_channel='pxn',
             exp_data=ExpData(
                E_lab=[181.2,186.6,189.9,194.3,202],
                cs_data={
                    '201Po': [np.nan,np.nan,0.15,np.nan,np.nan],
                    '200Po': [np.nan,np.nan,np.nan,0.038,np.nan],
                    '199Po': [np.nan,np.nan,np.nan,np.nan,0.055]
                },
                error_data={
                    '201Po': [[np.nan,np.nan,0.08,np.nan,np.nan],[np.nan,np.nan,0.12,np.nan,np.nan]],
                    '200Po': [[np.nan,np.nan,np.nan,0.011,np.nan],[np.nan,np.nan,np.nan,0.015,np.nan]],
                    '199Po': [[np.nan,np.nan,np.nan,np.nan,0.022],[np.nan,np.nan,np.nan,np.nan,0.03]]
                }
            )),    
    
    Reaction('24Mg', '181Ta', '205At', 0.74, 3.2, bf_diff=0.02, channels_to_plot=['197At', '198At', '199At', '200At'], unit='mb', save_note='Andreyev',
            exp_data=ExpData(
                E_lab=[118.8,128.8,135.8,137.6,141.8,151.8,162.8,167.9,172.8],
                cs_data={
                    '200At': [24.3,29.7,8.1,3.3,1.72,0.15,np.nan,np.nan,np.nan],
                    '199At': [0.027,1.98,4.4,3.8,2.9,0.54,0.035,0.044,0.012],
                    '198At': [np.nan,np.nan,0.06,0.293,0.65,0.85,0.27,0.21,0.077],
                    '197At': [np.nan,np.nan,np.nan,np.nan,np.nan,0.007,0.05,0.054,0.04],                    
                },
            )),
    Reaction('24Mg', '181Ta', '205At', 0.74, 3.2, bf_diff=0.02, channels_to_plot=['196Po', '197Po', '198Po', '199Po'], unit='mb', evap_channel='pxn', save_note='Andreyev',
            exp_data=ExpData(
                E_lab=[118.8,128.8,135.8,137.6,141.8,151.8,162.8,167.9,172.8],
                cs_data={
                    '199Po': [0.022,0.9,2.2,2.9,2.9,1.1,0.16,0.16,0.054],
                    '198Po': [np.nan,np.nan,0.12,0.33,0.74,1.54,1,1.1,0.45],
                    '197Po': [np.nan,np.nan,np.nan,np.nan,np.nan,0.181,1.1,1.2,1.35],
                    '196Po': [np.nan,np.nan,np.nan,np.nan,np.nan,0.025,0.058,0.055,0.25],
                },
            )),
    
    Reaction('40Ar', '165Ho', '205At', 0.75, 3.3, bf_diff=0.02, channels_to_plot=['199At', '200At', '201At', '202At'], unit='mb', save_note='Vermeulen',
            exp_data=ExpData(
                E_lab=[164.9,170.6,178.1,184.3,186.3,192,199.2],
                cs_data={
                    '202At': [4.4,2.3,0.309,np.nan,np.nan,np.nan,np.nan],
                    '201At': [3.1,11.3,7.6,1.7,1.4,0.547,0.104],
                    '200At': [np.nan,0.356,3.6,9.8,9.1,8.2,0.965],
                    '199At': [np.nan,np.nan,7.31E-04,2.39E-01,3.39E-01,1.1,2],                    
                },
                error_data={
                    '202At': [[0.0748,0.069,0.0309,np.nan,np.nan,np.nan,np.nan]],
                    '201At': [[0.0496,0.113,0.1216,0.0867,0.0224,0.08752,0.003432]],
                    '200At': [[np.nan,0.016732,0.054,0.1666,0.0546,0.246,0.012545]],
                    '199At': [[np.nan,np.nan,4.24E-04,1.91E-02,8.81E-03,0.0605,0.012]],                
                }
            )),
    
    Reaction('40Ar', '165Ho', '205At', 0.74, 3.3, bf_diff=0.02, channels_to_plot=['196At', '197At', '198At', '199At', '200At'], unit='mb', save_note='Andreyev',
            exp_data=ExpData(
                E_lab=[175.6,180,182.4,185.5,189.2,194.8,198.5,199.8,202.9,207.2,211,219,224.7,231.5,237.1,241.4,249.5,256.3,263.8,271.2,279.3],
                cs_data={
                    '200At': [2.43,9.3,8.25,11.5,8.8,4.65,2.6,1.7,1.25,0.35,0.21,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
                    '199At': [np.nan,np.nan,0.1,0.46,0.85,1.17,1.93,1.62,1.95,0.8,0.32,0.1,0.02,0.028,np.nan,0.01,np.nan,np.nan,np.nan,np.nan,np.nan],
                    '198At': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.035,0.1,0.3,0.35,0.37,0.16,0.15,0.035,0.056,0.017,0.009,np.nan,np.nan,np.nan],
                    '197At': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.015,0.035,0.028,0.035,0.031,0.016,0.004,0.0015,0.0008,np.nan],
                    '196At': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.001,0.0014,0.003,0.0035,0.0017,0.001,np.nan],
                },
            )),
    Reaction('40Ar', '165Ho', '205At', 0.74, 3.3, bf_diff=0.02, channels_to_plot=['195Po', '196Po', '197Po', '198Po', '199Po'], unit='mb', evap_channel='pxn', save_note='Andreyev',
            exp_data=ExpData(
                E_lab=[175.6,180,182.4,185.5,189.2,194.8,198.5,199.8,202.9,207.2,211,219,224.7,231.5,237.1,241.4,249.5,256.3,263.8,271.2,279.3],
                cs_data={
                    '199Po': [np.nan,np.nan,0.1,0.46,0.32,0.55,0.65,0.71,1.34,0.91,0.6,0.25,0.25,0.07,0.06,0.031,0.015,np.nan,np.nan,np.nan,np.nan],
                    '198Po': [np.nan,np.nan,np.nan,np.nan,np.nan,0.09,0.075,0.105,0.25,0.62,0.75,1.05,0.712,0.475,0.26,0.256,0.081,0.024,np.nan,np.nan,np.nan],
                    '197Po': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.1,0.41,1,0.6,1,0.79,0.56,0.22,0.09,0.036,np.nan],
                    '196Po': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.015,0.03,0.084,0.15,0.18,0.345,0.33,0.23,0.14,0.056],
                    '195Po': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.019,0.054,0.09,0.12,0.072],
                },
            )),

    Reaction('40Ar', '165Ho', '205At', 0.68, 3.3, bf_diff=0.02, channels_to_plot=['199At'], unit='mb', save_note='Jakobsson',
            exp_data=ExpData(
                E_lab=[200],
                cs_data={
                    '199At': [0.7],                    
                },
            )),
    
    Reaction('40Ar', '165Ho', '205At', 0.74, 3.3, bf_diff=0.02, channels_to_plot=['198At', '199At', '200At'], unit='mb', save_note='Folden',
            exp_data=ExpData(
                E_lab=[180.3,188.4,196.5,202.6,208.6,213.3,218.5],
                cs_data={
                    '200At': [9.1,5,1.19,0.13,np.nan,np.nan,np.nan],
                    '199At': [0.2,1.21,2.29,1.54,0.73,0.28,0.1],                    
                    '198At': [np.nan,np.nan,np.nan,0.1,0.21,0.18,0.08],                    
                },
                error_data={
                    '200At': [[3.3,1.8,0.44,0.06,np.nan,np.nan,np.nan]],
                    '199At': [[0.12,0.43,0.8,0.54,0.26,0.1,0.04]],
                    '198At': [[np.nan,np.nan,np.nan,0.05,0.08,0.07,0.03]],
                }
            )),
    Reaction('40Ar', '165Ho', '205At', 0.74, 3.3, bf_diff=0.02, channels_to_plot=['197Po', '198Po', '199Po'], unit='mb', evap_channel='pxn', save_note='Folden',
            exp_data=ExpData(
                E_lab=[180.3,188.4,196.5,202.6,208.6,213.3,218.5],
                cs_data={
                    '199Po': [0.04,0.42,1.03,1.64,1.19,0.72,0.34],
                    '198Po': [np.nan,np.nan,np.nan,0.26,0.78,1.13,0.96],
                    '197Po': [np.nan,np.nan,np.nan,np.nan,0.02,0.06,0.17],                
                },
                error_data={
                    '199Po': [[0.03,0.17,0.38,0.59,0.43,0.26,0.13]],
                    '198Po': [[np.nan,np.nan,np.nan,0.1,0.28,0.4,0.34]],
                    '197Po': [[np.nan,np.nan,np.nan,np.nan,0.01,0.03,0.07]],              
                }
            )),
    
    Reaction('26Mg', '181Ta', '207At', 0.76, 3.2, bf_diff=0.02, channels_to_plot=['200At', '201At', '202At', '203At'], unit='mb', plot_maxCS_data=True, save_note='Yeremin',
            exp_data=ExpData(
            E_lab = [150],
                cs_data={
                    '203At': [14],
                    '202At': [40],
                    '201At': [20],
                    '200At': [8]
                }
            )),
    
    Reaction('48Ca', '159Tb', '207At', 0.78, 3.2, bf_diff=0.02, channels_to_plot=['201At', '202At', '203At', '204At'], unit='mb', save_note='Mayorov',
            exp_data=ExpData(
                E_lab=[185.1,190.8,193,193.5,197.8,198,201.3,203.1,204.1,209.4],
                cs_data={
                    '204At': [5.1,4.2,3.5,2.5,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
                    '203At': [3,6.1,10.9,12.6,12.5,10.7,7,5.8,3.1,2.2],
                    '202At': [np.nan,np.nan,1.5,1.3,1.6,2.7,16.7,17.5,23.3,21.1],
                    '201At': [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.8],                    
                },
                error_data={
                    '204At': [[1.7,3,2,1.6,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]],
                    '203At': [[0.6,1.4,1.8,1.9,2,1.6,1.1,1.9,0.6,2]],
                    '202At': [[np.nan,np.nan,0.5,0.5,0.7,0.6,4.5,7,7.1,7.8]],
                    '201At': [[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,0.2]],
                }
            )),
]