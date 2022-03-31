
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



### FUNCTION FOR HOT ENCODING

def hot_encode (data, directions):
    if directions == 'yes':
        data = pd.get_dummies(data, prefix=data.name[:3], drop_first=True)
    return data

## FUNCTION TO TRANSFORM DATA using log_and_normalize AND hot_encode FUNCTIONS :

def transform_data(x0, y0):

#    cont=[ 'sqft_living','sqft_lot', 'lat','sqft_basement' ] 
#    nochange=pred[['grade','condition', 'bedrooms', 'renovated','basement','bathrooms']].copy() 
    nochange=['grade']
    log=["sqft_living", 'sqft_lot']
    hot=[ 'zipcode', 'waterfront']

    ord_cat=pd.DataFrame(x0['view2'].cat.codes)
    ord_cat.columns=['view']

    asis=x0[nochange]

    x1=pd.DataFrame([])

    # One log transformations
    y1=log_and_normalize(y0, 'log', 0)

    for col in log:
        x1[col]=log_and_normalize(x0[col], 'log', 0)


    # One hot encode categoricals
    for col in hot:
        new_cols=hot_encode(x0[col], 'yes')
        x1 = pd.concat([x1, new_cols], axis=1)

    x1 = pd.concat([x1, ord_cat, asis], axis=1)
    return x1,y1


#def transform_data(pred, price): 
#    other=[]
#    log=["sqft_living", 'sqft_lot']
#    hot=[ "grade", 'zipcode', 'yr_built','waterfront','view']
#
#    asis=x0[other]
#    x1=pd.DataFrame([])
#
#
#    cont=["sqft_living", 'sqft_lot' ]
#    hot=[ 'zipcode', 'waterfront','view' ] 
#
#
#    pred_fin=pd.concat([pred[['grade']], view_cat],axis=1)
#
##    pred_fin=pd.DataFrame([])
#
#    price_fin = log_and_normalize(price, 'log', 0)
#
#    for col in cont:
#        pred_fin[col]=log_and_normalize(pred[col], 'log', 0)
#
#    for col in hot:
#        hot_encode_cols = hot_encode(pred[col], 'yes')
#        pred_fin = pd.concat([pred_fin, hot_encode_cols], axis=1)
#
#    return pred_fin, price_fin



def exp_transformed_cols(pred):
    cont=["sqft_living", 'sqft_lot']

    for col in cont:
        pred[col]=np.exp(pred[col])

    return pred



### TO GET COEFFECIENTS FROM MODEL OBJECT

def get_coeff( year,zipcode, grade, water,view, coef_df):
    intercept=coef_df[coef_df['Column'] == "const"]["Value"].tolist()[0]
    sqft_living_coef=coef_df[coef_df['Column'] == "sqft_living"]["Value"].tolist()[0]
 #   grade_coef=coef_df[coef_df['Column'] == "grade"]["Value"].tolist()[0]

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


