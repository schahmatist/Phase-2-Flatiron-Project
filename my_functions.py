import pandas as pd
import numpy as np
def get_decade(year):
    df=pd.read_csv('data/kc_house_data.csv', index_col=0)

    for decade in df['decade'].unique():
        interval=decade.split('-')

        if year >= int(interval[0]) and year <= int(interval[1]):
            decade_col='dec_'+decade
            return decade_col
            break

