#!/usr/bin/env python
# coding: utf-8

# In[232]:

from __future__ import print_function
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual, Layout

from IPython.display import display, clear_output

import pandas as pd

#FUNCTION TO GET A DECADE

def create_decade (year):
    if year > 2009:
        decade="2010-2019"
    elif year > 1999 and year <= 2009:
        decade="2000-2009"
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
    elif year >= 1900 and year <= 1919:
        decade="1900-1919"
    elif year < 1900:
        decade="Unknown"
    else:
        decade="Unknown"

    return decade

# Loading data to get the range for zipcodes, dates, and median price

df2=pd.read_csv('data/kc_house_data.csv', index_col=0)
df2['decade']=df2['yr_built'].apply(create_decade)

# Setting lists of values for dates and decades

zipcodes=(list(df2['zipcode'].sort_values().unique()))
decades=list(df2['decade'].sort_values().unique())

mean_price=df2['price'].mean()

#############################################################################################

style = {'description_width': 'initial', 'handle_color' : 'darkgreen' }
#button_style = {'button_color':'green', 'description_color':'white'}

### Configuring individual fields (widgets)

title=widgets.Text(
    value='Predicting House Sale Prices for Kings County',
    placeholder='',
    description='',
    disabled=True,
    layout=Layout(width='1200px')
)

zipW = widgets.Dropdown(
        description="", 
        options=zipcodes, 
        value=zipcodes[0], 
        layout=Layout(width='100px')
        )

viewW = widgets.Dropdown(
    description="", 
    options=['NONE','FAIR','AVERAGE','GOOD','EXCELLENT'], 
    value='NONE',
    layout=Layout(width='120px')
    )

decadeW = widgets.Dropdown(
        description="Built in:", 
        options=decades, 
        value=decades[-1], 
        layout=Layout(width='200px')
        )

meanW = widgets.IntText(
    value=mean_price,
    description='Mean House Price to compare with:',
    disabled=False,
    style=style,
    readout_format=','
    )


gradeW = widgets.BoundedIntText(
    value=6,
    min=6,
    max=13,
    step=1,
    description='',
    disabled=False,
    layout=Layout(width='100px')
    )

livingW = widgets.IntSlider(
    value=1500,
    min=100,
    max=15000,
    step=10,
    description='',
    continuous_update=False,
    readout=True,
    readout_format=',',
    layout=Layout(width='500px'),  style=style
)

lotW = widgets.IntSlider(
    value=15000,
    min=1,
    max=100000,
    step=100,
    description='',
    continuous_update=False,
    readout=True,
    readout_format=',',
    layout=Layout(width='500px'),  style=style
)

waterW = widgets.Checkbox(
    value=False,
    description='Waterfront',
    disabled=False,
    indent=False
)

basementW = widgets.Checkbox(
    value=True,
    description='Incl. basement',
    disabled=False,
    indent=False , style=style
)


# Creating layouts for individual form items


form_item_layout = widgets.Layout(
    display='flex-grow',
    flex_flow='row',
    justify_content='flex-start',
    align_content='flex-end',
    width='100%', style=style
)


# Creating a form and adding the widgets above

form_items = [
    widgets.Box([title], layout=widgets.Layout(justify_content='flex-start')),
    widgets.Box([meanW], layout=widgets.Layout(justify_content='flex-start')),
    widgets.Box([widgets.Label(value='ZipCode:'), zipW, decadeW], layout=form_item_layout),
    widgets.Box([widgets.Label(value='Grade:'), gradeW], layout=form_item_layout),
    widgets.Box([widgets.Label(value='House Square Footage:'),  livingW, basementW],  layout=form_item_layout),
    widgets.Box([widgets.Label(value='Lot Square Footage:'), lotW], layout=form_item_layout),
    widgets.HBox([widgets.Label(value='View:'), viewW, waterW],  layout=form_item_layout)
]

form = widgets.Box(form_items, layout=widgets.Layout(
    display='flex',
    flex_flow='column',
    border='solid 3px',
    width='980',
    height='300px',
    
))

form.box_style='success'


# In[398]: # Not necessary:

#title=form_items[0].children[0]
#meanW=form_items[1].children[0]
#zipW=form_items[2].children[1]
#yearW=form_items[2].children[2]
#decadeW=form_items[2].children[2]
#gradeW=form_items[3].children[1]
#livingW=form_items[4].children[1]
#basementW=form_items[4].children[2]
#lotW=form_items[5].children[1]
#viewW=form_items[6].children[1]
#waterW=form_items[6].children[2]
#waterW2=form_items[6].children[2]

