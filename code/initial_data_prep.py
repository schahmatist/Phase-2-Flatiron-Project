import pandas as pd
import numpy as np


df=pd.read_csv('data/kc_house_data.csv', index_col=0)

def enum_category(label):
    num=0
    if label == 'Poor' : num =1
    elif label == 'Fair': num = 2
    elif label == 'Average': num = 3
    elif label == 'Good': num = 4
    elif label == 'Very Good': num = 5
    else: return label

    return int(num)

#FUNCTION TO GET A DECADE

def get_decade (year):
    if year > 2009:
        decade="2010_2019"
    elif year > 1999 and year <= 2009:
        decade="2000_2009"
    elif year >1989 and year <= 1999:
        decade="1990-1999"
    elif year >1979 and year <= 1989:
        decade="1980-1989"
    elif year >1969 and year <= 1979:
        decade="1970-1979"
    elif year >1959 and year <= 1969:
        decade="1960-1969"
    elif year > 1949 and year <= 1959:
        decade="1950-1959"
    elif year > 1939 and year <= 1949:
        decade="1940-1949"
    elif year > 1919 and year <= 1939:
        decade="1920-1939"
    elif year > 1899 and year <= 1919:
        decade="1900-1919"
    else:
        decade="Unknown"

    return decade


# initial cleaning operations (splitting , fillig na, etc)

df["grade"]=df["grade"].map(lambda x: x.split()[0]).astype(int)
df['condition'] = df['condition'].apply(enum_category)

df['waterfront'].fillna(value='NO',inplace=True)

df['renovated']=np.where((df['yr_renovated'].isna() |  df['yr_renovated'] == 0), 0, 1)
df['yr_renovated'].fillna(value=df['yr_built'],inplace=True)
df['yr_renovated'] = np.where(df['yr_renovated'] == 0, df['yr_built'], df['yr_renovated'])


df=df[df['sqft_basement'] != '?']
df['sqft_basement']=df['sqft_basement'].astype(float).astype(int)

df['basement']= np.where(df['sqft_basement'] < 90, 0, 1)

# NEW FEATURES
df['price_per_sqft']=round(df['price']/df['sqft_living'],2)
df['decade']=df['yr_built'].apply(get_decade)

#df['decade']=pd.cut(df['yr_built'], 12)
#df["age"]=2016-df['yr_built']
#df["years_after_renovation"]=2016-df['yr_renovated']
#df['month_of_sale']=df['date'].apply(lambda x: str.split(x,'/')[0]).astype(int)
#df['same_living_sqft']=(df['sqft_living']-df['sqft_living15'])/df['sqft_living'] 
#df['same_lot_sqft']=(df['sqft_lot']-df['sqft_lot15'])/df['sqft_lot'] 

df['lat_range']=pd.cut(df['lat'], 30)
df['long_range']=pd.cut(df['long'], 30)
df['coord_range']=np.array(zip(df['lat_range'],df['long_range']))

df['view'] = np.where (df['waterfront'] == 'YES', 'GOOD', df['view'])
df['view'].fillna(value='AVERAGE',inplace=True)
df['view2']=df['view'].astype('category')
df['view2']=df['view2'].cat.reorder_categories(['NONE', 'AVERAGE', 'FAIR', 'GOOD', 'EXCELLENT']) 

