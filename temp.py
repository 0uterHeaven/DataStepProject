# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import glassscraper as gs
import pandas as pd
path = 'C:/Users/robla/Documents/DataStepProject/chromedriver.exe'

df = gs.get_jobs('data scientist', 15, False, path, 10)