
import numpy as np
import math
import pandas as pd
import itertools

import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
########################################################### FUNCTIONS

def enum_category(label):
    num=0
    if label == 'Poor' : num =1
    elif label == 'Fair': num = 2
    elif label == 'Average': num = 3
    elif label == 'Good': num = 4
    elif label == 'Very Good': num = 5
    else: return label
    
    return int(num)





### FUNCTION FOR LOG TRANSFORMATIONS AND/OR NORMALIZATION 

def log_and_normalize (data, log, norm_type):
    if log == 'log':
        data = np.log(data) 
    if norm_type == 1:
        data = (data-np.mean(data))/np.std(data)  # std normalisation
    elif norm_type == 2:
        data = (data-min(data))/(max(data)-min(data))      #  min_max_min
    elif norm_type == 3:
        data = (data-np.mean(data))/(max(data)-min(data))  # mean norm
    
    return data    



### FUNCTION FOR HOT ENCODING

def hot_encode (data, directions):
    if directions == 'yes':
        data = pd.get_dummies(data, prefix=data.name[:3], drop_first=True)
    return data





### TO GET COEFFECIENTS FROM MODEL OBJECT

def get_coeff( year,zipcode,grade, water,view, coef_df):
    intercept=coef_df[coef_df['Column'] == "const"]["Value"].tolist()[0]
    sqft_living_coef=coef_df[coef_df['Column'] == "sqft_living"]["Value"].tolist()[0]

    try:
        sqft_lot_coef=coef_df[coef_df['Column'] == "sqft_lot"]["Value"].tolist()[0]
    except:
        sqft_lot_coef=0


    if water == 'WATERFRONT':
        water_coef=coef_df[coef_df['Column'] == "wat_YES"]["Value"].tolist()[0]
    else:
        water_coef=0

    if len(str(year)) != 4:
        year_coef=0
    else:
        try: year_coef=coef_df[coef_df['Column'].str.endswith(str(year))]["Value"].tolist()[0]
        except: year_coef=0

    if len(str(zipcode)) != 5:
        zipcode_coef=0
    else:
        try: zipcode_coef=coef_df[coef_df['Column'].str.endswith(str(zipcode))]["Value"].tolist()[0]
        except: zipcode_coef=0

    if len(str(grade))!=1 and len(str(grade))!=2:
        grade_coef=0
    else:
        try: grade_coef=coef_df[coef_df['Column'].str.endswith('gra_'+str(grade))]["Value"].tolist()[0]
        except: grade_coef=0

    if view  not in ['NONE','FAIR','GOOD','EXCELLENT']:
        view_coef=0
    else:
        try: view_coef=coef_df[coef_df['Column'].str.endswith(view)]["Value"].tolist()[0]
        except: view_coef=0
#    try:
#        sqft_living15_coef=coef_df[coef_df['Column'] == "sqft_living15"]["Value"].tolist()[0]
#    except:
#        sqft_living15_coef=0
    return intercept, sqft_living_coef, year_coef, zipcode_coef, grade_coef,  water_coef, view_coef, sqft_lot_coef


