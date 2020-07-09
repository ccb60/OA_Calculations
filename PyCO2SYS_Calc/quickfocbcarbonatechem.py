# -*- coding: utf-8 -*-
"""
Calculation of CO2SYS estimates of major carbonate parameters from Casco Bay
coastal acidification data.

The primary carbonate calculator in R, seacarb, is based on CO2SYS, but has
slightly fewer options. We ran this code to confirm whether to confirm calculation steps, and to explore ways to deal with
onconsistencies in how


Created on Wed Jul  8 12:36:51 2020

@author: curtis.bohlen
"""

import os
import csv

import PyCO2SYS as pyco2
import pandas as pd

parent = os.path.dirname(os.getcwd())
fn = 'CMS1DataFALL2016.xlsx'
fpath = os.path.join(parent,fn)


focb_data = pd.io.excel.read_excel(fpath, header = 0)


#CO2dict = CO2SYS(PAR1, PAR2, PAR1TYPE, PAR2TYPE,
#                 SAL, TEMPIN,
#                 TEMPOUT,
#                 PRESIN, PRESOUT, SI, PO4,
#                 pHSCALEIN, K1K2CONSTANTS, KSO4CONSTANTS,
#                 NH3=0.0, H2S=0.0
#                 KFCONSTANT=1, buffers_mode="auto",
#                 totals=None, equilibria_in=None,
#                 equilibria_out=None, WhichR=1)


# Matlab call that Chris Hunt used
# [CO2SYS_DATA,HEADERS,NICEHEADERS]=CO2SYS(lvl3(i,27),lvl3(i,37),4,3,
                                         # lvl3(i,17),lvl3(i,7),
                                         # lvl3(i,7),
                                         # 0,0,0,0,
                                         # 1,9,1);

CO2dict = pyco2.CO2SYS(focb_data['pco2'], focb_data['ph'], 4, 3,
                       focb_data['sal'], focb_data['temp'],
                       focb_data['temp'],
                 0,0,0,0,
                 4,9,1)

## NOTE:  this code is identical to what I used for CBEP data, except I have specified a different 
# ph scale, here the NBS scale is indicated by that value '4'.


# According to the on-line documentation for PyCO2SYS
# pHSCALEIN    = 1  -> Total
# K1K2CONSTANTS = 9 -> CW98
# KSO4CONSTANTS = 1 -> D90a for bisulfate dissociation and U74 for borate:salinity

# Note that this program allows pHSCALEIN = 4 -> NBS


# this produces a dictionary of one dimensional ndarrays, I want to turn that into an
# array of dictionaries to feed to a DictWriter

# first select columns we care about
# Chris sent me code that selected them by location, but these appear correct

keys_to_extract = ["OmegaARin", "OmegaCAin", 'TAlk', 'TCO2', "pHinTOTAL"]
replace_keys =['omega_a', 'omega_c', 'ta', 'dic', 'ph_tot']

co2dict = {key: CO2dict[key] for key in keys_to_extract}
for new,old in zip(replace_keys,keys_to_extract):
    co2dict[new] = co2dict.pop(old)

with open('focbco2sys_out.csv', 'w') as f:
    riter = csv.writer(f, lineterminator= '\n')
    riter.writerow(replace_keys)
    riter.writerows(zip(*[co2dict[key] for key in replace_keys]))


