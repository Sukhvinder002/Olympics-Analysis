# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:17:59 2024

@author: My
"""

import pandas as pd 
import numpy as np 


def preprocess(df, region_df):
    
    #filtering for summer olympics 
    df= df[df['Season'] =='Summer']
    
    # merging with region_df 
    df = df.merge(region_df, on='NOC', how ='left') 
    
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    
    #one hot encoding - medals column 
    df= pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df 
