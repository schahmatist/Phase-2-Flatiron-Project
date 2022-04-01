#!/usr/bin/env python
# coding: utf-8

# In[232]:

from __future__ import print_function
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual, Layout

from IPython.display import display, clear_output

import pandas as pd


# In[394]:

df2=pd.read_csv('data/kc_house_data.csv', index_col=0)

zipcodes=(list(df2['zipcode'].sort_values().unique()))
years=(list(df2['yr_built'].sort_values().unique()))
mean_price=df2['price'].mean()

title=widgets.Text(
    value='Predicting House Sale Prices for Kings County',
    placeholder='',
    description='',
    disabled=True,
    layout=Layout(width='1200px')
)

zipW = widgets.Dropdown(description="", options=zipcodes, value=zipcodes[0], layout=Layout(width='100px'))

viewW = widgets.Dropdown(
    description="", 
    options=['NONE','FAIR','AVERAGE','GOOD','EXCELLENT'], 
    value='NONE',
    layout=Layout(width='120px'))

yearW = widgets.Dropdown(description="Year:", options=years, value=years[-1], layout=Layout(width='200px'))

style = {'description_width': 'initial', 'handle_color' : 'darkgreen' }
button_style = {'button_color':'green', 'description_color':'white'}

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


button = widgets.Button(description="Calculate", style=button_style)


# In[400]:


form_item_layout = widgets.Layout(
    display='flex-grow',
    flex_flow='row',
    justify_content='flex-start',
    align_content='flex-end',
    width='100%', style=style
)


form_items = [
    
    widgets.Box([title], layout=widgets.Layout(justify_content='flex-start')),
    widgets.Box([meanW], layout=widgets.Layout(justify_content='flex-start')),
    widgets.Box([widgets.Label(value='ZipCode:'), zipW, yearW], layout=form_item_layout),
    widgets.Box([widgets.Label(value='Grade:'), gradeW], layout=form_item_layout),
    widgets.Box([widgets.Label(value='House Square Footage:'),  livingW],  layout=form_item_layout),
    widgets.Box([widgets.Label(value='Lot Square Footage:'), lotW], layout=form_item_layout),
    widgets.HBox([widgets.Label(value='View:'), viewW, waterW],  layout=form_item_layout)
#    widgets.Box([button], layout=widgets.Layout(justify_content='center'))
]

form = widgets.Box(form_items, layout=widgets.Layout(
    display='flex',
    flex_flow='column',
    border='solid 3px',
    width='1000px',
    height='300px',
    
))

form.box_style='success'


# In[398]:


