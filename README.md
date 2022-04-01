# Phase 2 Project: Technical Presentation of Price Predictor

  <img src="images/solution.jpg" alt="drawing" align="right"  width="350"/> 
  
# Solution

*  Analyzing 2014-2015 dataset with past sales
*  Identifying individual and joined factors.
*  Prepairing features for the model
*  Calculate all the features coefficients 
*  Testing the results



<img src="images/problem.jpg" alt="drawing" align="right"  width="380"/> 

# Objectives

*  How multiple features work together?
*  Quantifying joined features effect
*  Building a predictive model
* Building a front end for a customer




# Data
***
#### King County house sales dataset contains:
*  details for 22,000 sold houses
*  final sales prices 

All the data is from 2014-2015 




# Features Identified
#### Main Features: 
* House Sq footage 
* Grade of design and materials quality
* Zipcode
* Waterfront
* View



## Additional Features: 
* Lot size
* Basement
* House Age

#### Only marginal effect from:
* Number of bedrooms, bathrooms, and floors


```python
## importing Libraries
%run code/import_libs.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

## Importing Functions
%run code/functions_v1.4.py



## Loading and Initial preparation of the data (fillnulls, new features, filtering)
%run code/initial_data_prep.py

%matplotlib inline
mean_price_2014_2015=initial_price.mean()[0]

# SPLITTING DATA IN PREDICTORS(X) and price (Y)

initial_pred = df.drop(columns=["price"]).copy()
initial_price = df[["price"]]

#FILTER
df=df[~df["grade"].isin([3,4,5])].copy()
df.shape
```




    (20880, 28)



# Data Modeling
#### An iterative approach to data modeling 
-  Calculating Efficiency for basic features  
-  Prepairing model features
-  Training multiple models
-  Chosing the most efficient model 
-  Testing against different subset of data


* ## Prepared Data for Modeling using custom "transform_data" function (see functions_v1.4.py)  


* ## Created/trained model using statsmodels.OLS  


* ## Made sure r-square is good  



```python
# Create OLS linear model
pred_fin, price_fin = transform_data(initial_pred, initial_price)

pred_int = sm.add_constant(pred_fin)
model = sm.OLS(price_fin,pred_int).fit()

coef_df=model.params.reset_index()
coef_df.columns=["Column","Value"]
```

# custom functions to get coefficients from <br>OLS and calculate the formula of the slopes

* used custom function "calcuate_price" and "get_coeff" to get coefficients from ols model (see functions_v1.4.py


```python


#############################################################################
def calculate_price (sqft_living, decade, basement, zipcode, grade, waterfront, view , sqft_lot,  
                     mean_price, coef_df=coef_df, output='yes'):
 
    if waterfront == 'NO' or not waterfront: 
        waterfront = 0
    else: 
        waterfront = 1
            
    b0,b1,b2,b3,b4,b5,b6,b7,b8 = get_coeff( decade, zipcode, grade, waterfront, view, coef_df)
    y=round( np.exp(b0 + b1*np.log(sqft_living) + b2*np.log(sqft_lot) + b3*basement + b4*waterfront + b5*grade + b6 + b7 + b8) )
    
    if output == 'yes': y=y*(mean_price/mean_price_2014_2015)
    print('{:,.0f}'.format(y))
    return y,b0,b1,b2,b3,b4,b5,b6,b7,b8
####################################################################################

```

# Creating UI forms


```python
## Importing Widgets Forms
%run code/Build_Forms_v1.4.py


inp={ 'view':viewW,'waterfront':waterW,
    'zipcode': zipW, 'decade':decadeW, 'grade':gradeW, 'basement':basementW, "mean_price":meanW,
    'sqft_living':livingW,'sqft_lot':lotW }

output = widgets.interactive_output(calculate_price, inp )



ui = widgets.VBox([form, output])

output.layout={'border': '3px solid green', 'width':'150px'}

```

# Building a Front End Tool:


```python
display(ui)
```


    VBox(children=(Box(box_style='success', children=(Box(children=(Text(value='Predicting House Sale Prices for K…


# Testing
***

We made sure the tool works as expected:
* Multiple comparissons of predicted data against the actual data
* Predicted price is within 90-110% of actual price (houses newer than 1980)
* Predicted price is within 87-113% of actual price (houses older than 1980)
***

# Conclusions
***

#### Considerations and Limitations:


* The tool can be effective to estimate base price for known features
* In the future a model should be re-trained with more up-to-date data
* The presented prototype will be greatly improved by more advanced modeling

