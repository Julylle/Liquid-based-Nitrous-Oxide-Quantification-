# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 13:20:01 2025

@author: Shuting Wang
"""
#%%
from liquidbased_quantification import LiquidQuantifier

# The D_R and AerationFieldSize parameters can be adjusted based on specific site conditions
model = LiquidQuantifier("data/Monitoring_Data_Example.xlsx", D_R = 7.55, AerationFieldSize = 462.0)

results = model.run_pipeline(show_plots=True)
print(results.head())
results.to_excel("liquid_quantification_results.xlsx", index=False)

