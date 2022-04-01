import warnings
warnings.filterwarnings(action='ignore', category=UserWarning)
warnings.filterwarnings(action='ignore', category=FutureWarning)

import numpy as np
import math
import pandas as pd
import itertools

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
