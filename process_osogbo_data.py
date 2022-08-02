# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:12:02 2022

@author: ogunjosam
"""

import pandas as pd

xx = pd.read_excel('osogbo_data_chaos.csv',index_col='created_at',parse_dates=True)
xy = pd.read_csv('osogbo_data1.csv',index_col='created_at',parse_dates=True)

xx = xx.resample('2min').mean()
xy = xy.resample('2min').mean()

xx['Pressure'] = xy

xx.index = xx.index.tz_localize(None)
xx.to_excel('osogbo_chaos_final.xlsx')