# Phase 2 Project: Technical Presentation of Price Predictor

<img src="images/problem.jpg" alt="drawing" align="left"  width="380"/> 

<br>

*  ## Overview

*  The goal of this project is to develop a predictive model for house pricing in King County.
*  The model will estimate how the features of a house will affect its price. 
*  The price estimation tool may be benefitial for Real Estates Agencies and Developers, as well as individual sellers and buyers.


<br>
<br>

# Objective

*  Determining how multiple features work individually and together
*  Quantifying joined features effect
*  Building a predictive model
*  Building a front end for a customer



# Solution

*  Analyzing 2014-2015 dataset with past sales
*  Identifying individual and joined factors.
*  Prepairing features for the model
*  Calculate all the features coefficients 
*  Testing the results



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
<br>

<br>
#### Only marginal effect from:
* Renovation, number of bedrooms, bathrooms, and floors  
<br>
<br>
more on feature analysis - see "analysis_and_regression/Investigation of Features.ipynb"


# Initial Data Load and Cleaning
***
* Loaded the "kc_house_data.csv" using "initial_data_prep.py"
* Filled or removed rows with missing properties 
* Construction Grade 3-5 (below the acceptable code) were removed
* Out of 22,000 rows 20,880 were used in the model


# Data Modeling
#### An iterative approach to data modeling 
-  Calculating Efficiency for basic features  
-  Prepairing model features
-  Training multiple models
-  Chosing the most efficient model 
-  Testing against different subset of data



Steps:

* Prepared data for modeling using custom "transform_data" function (see functions_v1.4.py)  


* Created/trained model using statsmodels.OLS  


* Made sure r-square is higher than 80%
***


### In addition to automatic -sklearn- methods, custom functions <br> were created to manually get all the coefficients from statsmodels OLS  <br> and calculate the linear slopes formula

* used custom function "calcuate_price" and "get_coeff" to get coefficients from ols model (see functions_v1.4.py)

# Creating UI forms
***
#### Building a Front End Tool:
***
* ipywidgets were used to create custom ui forms ( Build_Forms_v1.4.py )<br>  
<br>
* custom calculate_price function was linked to the input/output of the ui  
<br>
<br>
<br>

<img src="images/predictor.jpg" alt="drawing" align="center"  width="1200"/> 


# Testing
***

We made sure the tool works as expected:
* Multiple comparissons of predicted data against the actual data
* Predicted price is within 90-110% of actual price (houses newer than 1980)
* Predicted price is within 87-113% of actual price (houses older than 1980)
***
More deails about regression testing in  "analysis_and_regression/Regression Tests.ipynb"

# Conclusions
***

#### Considerations and Limitations:


* The tool can be effective to estimate base price for known features
* In the future a model should be re-trained with more up-to-date data
* The presented prototype will be greatly improved by more advanced modeling

