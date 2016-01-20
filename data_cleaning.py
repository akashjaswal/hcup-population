
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pylab import *
from scipy import *
from pylab import rcParams
import statsmodels.formula.api as smf
get_ipython().magic(u'matplotlib inline')


# In[99]:

raw_data_99 = pd.read_csv('/Users/Akash/Desktop/Projects/hcup-data/data/raw_data_1990_1999.txt', sep = '\t', header = None)
raw_data_99.head()


# In[ ]:

# Filtering Data to retain only Washington state counties

WA_data_99 = raw_data_99[(raw_data_99[0].str.contains('53001')) |
                         (raw_data_99[0].str.contains('53003')) | 
                         (raw_data_99[0].str.contains('53005')) | 
                         (raw_data_99[0].str.contains('53007')) | 
                         (raw_data_99[0].str.contains('53009')) | 
                         (raw_data_99[0].str.contains('53011')) |
                         (raw_data_99[0].str.contains('53013')) |
                         (raw_data_99[0].str.contains('53015')) |
                         (raw_data_99[0].str.contains('53017')) |
                         (raw_data_99[0].str.contains('53019')) |
                         (raw_data_99[0].str.contains('53021')) |
                         (raw_data_99[0].str.contains('53023')) |
                         (raw_data_99[0].str.contains('53025')) |
                         (raw_data_99[0].str.contains('53027')) |
                         (raw_data_99[0].str.contains('53029')) |
                         (raw_data_99[0].str.contains('53031')) |
                         (raw_data_99[0].str.contains('53033')) |
                         (raw_data_99[0].str.contains('53035')) |
                         (raw_data_99[0].str.contains('53037')) |
                         (raw_data_99[0].str.contains('53039')) |
                         (raw_data_99[0].str.contains('53041')) |
                         (raw_data_99[0].str.contains('53043')) |
                         (raw_data_99[0].str.contains('53045')) |
                         (raw_data_99[0].str.contains('53047')) |
                         (raw_data_99[0].str.contains('53049')) |
                         (raw_data_99[0].str.contains('53051')) |
                         (raw_data_99[0].str.contains('53053')) |
                         (raw_data_99[0].str.contains('53055')) |
                         (raw_data_99[0].str.contains('53057')) |
                         (raw_data_99[0].str.contains('53059')) |
                         (raw_data_99[0].str.contains('53061')) |
                         (raw_data_99[0].str.contains('53063')) |
                         (raw_data_99[0].str.contains('53065')) |
                         (raw_data_99[0].str.contains('53067')) |
                         (raw_data_99[0].str.contains('53069')) |
                         (raw_data_99[0].str.contains('53071')) |
                         (raw_data_99[0].str.contains('53073')) |
                         (raw_data_99[0].str.contains('53075')) |
                         (raw_data_99[0].str.contains('53077'))]


# In[100]:

len(WA_data_99)
WA_data_99.head()


# In[ ]:

WA_data_99_clean = pd.DataFrame(columns = ['year','FIPS_state_code','FIPS_county_code','race_sex','ethnic_origin','pop'])
val = []


# In[ ]:

index_vals = range(len(WA_data_99))
WA_data = list(WA_data_99[0])
WA_data_99_df = pd.DataFrame(WA_data,index=index_vals)


# In[ ]:

def append_df(val,i):
    WA_data_99_clean.set_value(i, 'year', val[1])
    WA_data_99_clean.set_value(i,'FIPS_state_code', val[2])
    WA_data_99_clean.set_value(i,'FIPS_county_code', val[3])
    WA_data_99_clean.set_value(i,'race_sex', val[4])
    WA_data_99_clean.set_value(i,'ethnic_origin', val[5])
    WA_data_99_clean.set_value(i,'pop', val[6])

for i in WA_data_99_df.index.tolist():
    val = list(str(WA_data_99_df.iloc[i]).split())
    append_df(val,i)


WA_data_99_clean.to_csv("WA_data_99_clean.csv", cols =['year','FIPS_state_code','FIPS_county_code','race_sex','ethnic_origin','pop'])


WA_data_99_clean = pd.read_csv("/Users/Akash/Desktop/Projects/hcup-population/WA_data_99_clean.csv")


WA_data_99_clean = WA_data_99_clean.rename(columns={'FIPS_county_code':'age_group'})
WA_data_99_clean = WA_data_99_clean.rename(columns = {'pop': 'population'})
WA_data_99_clean.head()



WA_data_99_clean1 = WA_data_99_clean
WA_data_99_clean1['race_sex_name'] = WA_data_99_clean1['race_sex']
WA_data_99_clean1["county"] = WA_data_99_clean1['FIPS_state_code']
WA_data_99_clean1['age_category'] = WA_data_99_clean1['age_group']

WA_data_99_clean1 = WA_data_99_clean.replace(to_replace={'race_sex_name': {1: "white_male", 2: "white_female", 3: "black_male", 4: "black_female",
                                                 5: "american_indian/alaska_male", 6: "american_indian/alaska_female", 7: "asian/pacific_male", 
                                                  8: "asian/pacific_female"} , 'ethnic_origin': {1: "not_hispanic/latino", 2: "hispanic/latino"}})

WA_data_99_clean1 = WA_data_99_clean1.replace(to_replace = {'county':{53001:'Adams', 53003:'Asotin', 53005: 'Benton', 53007:'Chelan',
                                                                     53009: 'Clallam', 53011:'Clark', 53013:'Columbia', 53015:'Cowlitz', 53017: 'Douglas',
                                                                     53019: 'Ferry', 53021: 'Franklin', 53023:'Garfield', 53025: 'Grant', 53027: 'Grays Harbor', 53029:'Island', 53031: 'Jefferson',
                                                                     53033: 'King', 53035: 'Kitsap', 53037: 'Kittitas', 53039: 'Klickitat', 53041: 'Lewis', 53043: 'Lincoln', 
                                                                     53045: 'Mason', 53047: 'Okanogan', 53049: 'Pacific', 53051: 'Pend Oreille', 53053: 'Pierce', 53055: 'San Juan', 
                                                                     53057: 'Skagit', 53059: 'Skamania', 53061: 'Snohomish', 53063: 'Spokane', 53065: 'Stevens', 53067: 'Thurston', 
                                                                     53069: 'Wahkiakum', 53071: 'Walla Walla', 53073: 'Whatcom', 53075: 'Whitman', 53077: 'Yakima'}})

WA_data_99_clean1 = WA_data_99_clean1.replace(to_replace = {'age_category': {0:'below 1 yr', 1: '1-4 yrs', 2: '5-9 yrs', 3: '10-14 yrs', 4: '15-19 yrs', 
                                                     5: '20-24 yrs', 6: '25-29 yrs', 7: '30-34 yrs', 8: '35-39 yrs', 9: '40-44 yrs', 
                                                     10: '45-49 yrs', 11: '50-54 yrs', 12: '55-59 yrs', 13: '60-64 yrs', 14: '65-69 yrs',
                                                     15: '70-74 yrs', 16: '75-79 yrs', 17:'80-84 yrs', 18: 'over 85 yrs'}})
WA_data_99_clean1.head()


# In[158]:

WA_population = pd.DataFrame(WA_data_99_clean1.groupby(['year','county']).sum()['population'])
WA_population.reset_index(level=0, inplace = True)
WA_population.reset_index(level=0, inplace = True)
WA_population = WA_population.rename(columns = {'population': 'total_population'})
WA_population.head()


# In[159]:

pop_gender = WA_data_99_clean1
pop_gender.head()
pop_gender['gender'] = pop_gender['race_sex']
pop_gender = pop_gender.replace(to_replace = {'gender': {1:'M', 2: 'F', 3:'M', 4:'F', 5:'M', 6:'F', 7:'M', 8:'F'}})
pop_gender = pd.DataFrame(pop_gender.groupby(['year','county','gender']).sum()['population'])
pop_gender.reset_index(level = 0, inplace = True)
pop_gender.reset_index(level = 0, inplace = True)
pop_gender.reset_index(level = 0, inplace = True)


# In[160]:

pop_male = pop_gender[pop_gender['gender'] == 'M']
pop_male = pop_male.rename(columns = {'population':'population_male'})
WA_population = pd.merge(pop_male[['county','year','population_male']], WA_population, on = ['county','year'], how = 'inner')

WA_population.head()


# In[161]:

pop_female = pop_gender[pop_gender['gender'] == 'F']
pop_female = pop_female.rename(columns = {'population':'population_female'})
WA_population = pd.merge(pop_female[['county','year','population_female']], WA_population, on = ['county','year'], how = 'inner')

WA_population.head()




