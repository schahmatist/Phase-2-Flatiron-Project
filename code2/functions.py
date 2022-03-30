
import numpy as np
import math
import pandas as pd
import itertools

########################################################### FUNCTIONS

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

def hot_encode (data, directions):
    if directions == 'yes':
        data = pd.get_dummies(data, prefix=data.name[:3], drop_first=True)
    return data

def transform_data(x0, y0):

    other=[]
    log=["sqft_living", 'sqft_lot']
    hot=[ "grade", 'zipcode', 'yr_built','waterfront','view']

    asis=x0[other]
    x1=pd.DataFrame([])

    # One log transformations
    y1=log_and_normalize(y0, 'log', 0)

    for col in log:
        x1[col]=log_and_normalize(x0[col], 'log', 0)


    # One hot encode categoricals
    for col in hot:
        new_cols=hot_encode(x0[col], 'yes')
        x1 = pd.concat([x1, new_cols], axis=1)

    x1 = pd.concat([x1, asis], axis=1)
    return x1,y1

