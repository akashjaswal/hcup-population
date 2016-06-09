
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

pop_data = pd.read_csv('WA_population.csv', parse_dates={'Timestamp': ['Year']},index_col='Timestamp')
pop_data.tail()


# In[37]:


county_list = pop_data['County'].unique()
gender_list = pop_data['Gender'].unique()
Age_Groups = pop_data['AgeGroup'].unique()
final_data = pd.DataFrame(columns = ['Population','County','Gender','AgeGroup'])

for county in county_list:
    print "Working on County: ", county
    for gender in gender_list:
        for age_group in Age_Groups:
            pop_subset = pop_data[(pop_data['County'] == county) & (pop_data['Gender'] == gender) & (pop_data['AgeGroup'] == age_group)]
            pop_interpolated = pd.DataFrame(pop_subset['Population'].resample('M').interpolate(method='linear'))
            length = len(pop_interpolated)
            pop_interpolated['County'] = [county] * length
            pop_interpolated['Gender'] = [gender] * length
            pop_interpolated['AgeGroup'] = [age_group] * length
            pop_interpolated = pop_interpolated.round({"Population":0})
            final_data = pd.concat([final_data,pop_interpolated])
    
            
print final_data.head(), final_data.tail()


# In[38]:

final_data.reset_index(level = 0, inplace=True)
final_data['year'] = pd.DatetimeIndex(final_data['index']).year
final_data['month'] = pd.DatetimeIndex(final_data['index']).month
final_data.to_csv('Interpolated_Population.csv')


# In[49]:

import glob
import os
# h_data = pd.read_csv('/Users/Akash/Desktop/Projects/hcup-data/Extracted_hospcv/')
path = '/Users/Akash/desktop/Projects/hcup-data/Extracted_hospcsv'                 
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent
h_data = pd.concat((pd.read_csv(f) for f in all_files))    # doesn't create a list, nor d


# In[92]:

final_data.head()


# In[198]:

h_data.describe


# In[125]:

h_data = h_data[h_data['ayear'] >= 2004]
h_04 = h_data[(h_data['age'] <=4)]
h_grouped = pd.DataFrame(h_04.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_grouped['AgeGroup'] = [1] * len(h_grouped)
h_grouped.reset_index(level=0, inplace=True)
h_grouped.reset_index(level=0, inplace=True)
h_grouped.reset_index(level=0, inplace=True)
h_grouped.reset_index(level=0, inplace=True)
print len(h_grouped)

h_09 = h_data[(h_data['age'] >= 5) & (h_data['age'] <= 9)]
h_09 = pd.DataFrame(h_09.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_09['AgeGroup'] = [2] * len(h_09)
h_09.reset_index(level=0, inplace=True)
h_09.reset_index(level=0, inplace=True)
h_09.reset_index(level=0, inplace=True)
h_09.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_09])
print len(h_grouped)

h_14 = h_data[(h_data['age'] >= 10) & (h_data['age'] <= 14)]
h_14 = pd.DataFrame(h_14.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_14['AgeGroup'] = [3] * len(h_14)
h_14.reset_index(level=0, inplace=True)
h_14.reset_index(level=0, inplace=True)
h_14.reset_index(level=0, inplace=True)
h_14.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_14])
print len(h_grouped)

h_19 = h_data[(h_data['age'] >= 15) & (h_data['age'] <= 19)]
h_19 = pd.DataFrame(h_19.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_19['AgeGroup'] = [4] * len(h_19)
h_19.reset_index(level=0, inplace=True)
h_19.reset_index(level=0, inplace=True)
h_19.reset_index(level=0, inplace=True)
h_19.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_19])
print len(h_grouped)

h_24 = h_data[(h_data['age'] >= 20) & (h_data['age'] <= 24)]
h_24 = pd.DataFrame(h_24.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_24['AgeGroup'] = [5] * len(h_24)
h_24.reset_index(level=0, inplace=True)
h_24.reset_index(level=0, inplace=True)
h_24.reset_index(level=0, inplace=True)
h_24.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_24])
print len(h_grouped)

h_29 = h_data[(h_data['age'] >= 25) & (h_data['age'] <= 29)]
h_29 = pd.DataFrame(h_29.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_29['AgeGroup'] = [6] * len(h_29)
h_29.reset_index(level=0, inplace=True)
h_29.reset_index(level=0, inplace=True)
h_29.reset_index(level=0, inplace=True)
h_29.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_29])
print len(h_grouped)

h_34 = h_data[(h_data['age'] >= 30) & (h_data['age'] <= 34)]
h_34 = pd.DataFrame(h_34.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_34['AgeGroup'] = [7] * len(h_34)
h_34.reset_index(level=0, inplace=True)
h_34.reset_index(level=0, inplace=True)
h_34.reset_index(level=0, inplace=True)
h_34.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_34])
print len(h_grouped)

h_39 = h_data[(h_data['age'] >= 35) & (h_data['age'] <= 39)]
h_39 = pd.DataFrame(h_39.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_39['AgeGroup'] = [8] * len(h_39)
h_39.reset_index(level=0, inplace=True)
h_39.reset_index(level=0, inplace=True)
h_39.reset_index(level=0, inplace=True)
h_39.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_39])
print len(h_grouped)

h_44 = h_data[(h_data['age'] >= 40) & (h_data['age'] <= 44)]
h_44 = pd.DataFrame(h_44.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_44['AgeGroup'] = [9] * len(h_44)
h_44.reset_index(level=0, inplace=True)
h_44.reset_index(level=0, inplace=True)
h_44.reset_index(level=0, inplace=True)
h_44.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_44])
print len(h_grouped)

h_49 = h_data[(h_data['age'] >= 45) & (h_data['age'] <= 49)]
h_49 = pd.DataFrame(h_49.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_49['AgeGroup'] = [10] * len(h_49)
h_49.reset_index(level=0, inplace=True)
h_49.reset_index(level=0, inplace=True)
h_49.reset_index(level=0, inplace=True)
h_49.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_49])
print len(h_grouped)

h_54 = h_data[(h_data['age'] >= 50) & (h_data['age'] <= 54)]
h_54 = pd.DataFrame(h_54.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_54['AgeGroup'] = [11] * len(h_54)
h_54.reset_index(level=0, inplace=True)
h_54.reset_index(level=0, inplace=True)
h_54.reset_index(level=0, inplace=True)
h_54.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_54])
print len(h_grouped)

h_59 = h_data[(h_data['age'] >= 55) & (h_data['age'] <= 59)]
h_59 = pd.DataFrame(h_59.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_59['AgeGroup'] = [12] * len(h_59)
h_59.reset_index(level=0, inplace=True)
h_59.reset_index(level=0, inplace=True)
h_59.reset_index(level=0, inplace=True)
h_59.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_59])
print len(h_grouped)

h_64 = h_data[(h_data['age'] >= 60) & (h_data['age'] <= 64)]
h_64 = pd.DataFrame(h_64.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_64['AgeGroup'] = [13] * len(h_64)
h_64.reset_index(level=0, inplace=True)
h_64.reset_index(level=0, inplace=True)
h_64.reset_index(level=0, inplace=True)
h_64.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_64])
print len(h_grouped)

h_69 = h_data[(h_data['age'] >= 65) & (h_data['age'] <= 69)]
h_69 = pd.DataFrame(h_69.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_69['AgeGroup'] = [14] * len(h_69)
h_69.reset_index(level=0, inplace=True)
h_69.reset_index(level=0, inplace=True)
h_69.reset_index(level=0, inplace=True)
h_69.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_69])
print len(h_grouped)

h_74 = h_data[(h_data['age'] >= 70) & (h_data['age'] <= 74)]
h_74 = pd.DataFrame(h_74.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_74['AgeGroup'] = [15] * len(h_74)
h_74.reset_index(level=0, inplace=True)
h_74.reset_index(level=0, inplace=True)
h_74.reset_index(level=0, inplace=True)
h_74.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_74])
print len(h_grouped)

h_79 = h_data[(h_data['age'] >= 75) & (h_data['age'] <= 79)]
h_79 = pd.DataFrame(h_79.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_79['AgeGroup'] = [16] * len(h_79)
h_79.reset_index(level=0, inplace=True)
h_79.reset_index(level=0, inplace=True)
h_79.reset_index(level=0, inplace=True)
h_79.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_79])
print len(h_grouped)

h_84 = h_data[(h_data['age'] >= 80) & (h_data['age'] <= 84)]
h_84 = pd.DataFrame(h_84.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_84['AgeGroup'] = [17] * len(h_84)
h_84.reset_index(level=0, inplace=True)
h_84.reset_index(level=0, inplace=True)
h_84.reset_index(level=0, inplace=True)
h_84.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_84])
print len(h_grouped)

h_85 = h_data[(h_data['age'] >= 85)]
h_85 = pd.DataFrame(h_85.groupby(['female','ayear','amonth','pstco2']).count()['age'])
h_85['AgeGroup'] = [18] * len(h_85)
h_85.reset_index(level=0, inplace=True)
h_85.reset_index(level=0, inplace=True)
h_85.reset_index(level=0, inplace=True)
h_85.reset_index(level=0, inplace=True)
h_grouped = pd.concat([h_grouped,h_85])
print len(h_grouped)

h_grouped.rename(columns={"age":"Patients_Count", "female":"Gender",'pstco2':'FIPS','ayear':"year",'amonth':'month'}, inplace=True)
# h_grouped[h_grouped['Gender'] == 0]['Gender'] = 1 # Male
# h_grouped[h_grouped['Gender'] == 1]['Gender'] = 2 # Female
h_grouped['Gender'].replace(to_replace=[0,1], value=[1,2], inplace=True)
h_grouped.to_csv("Aggregated_Hosp.csv")
print h_grouped.head(), h_grouped.tail()


# In[123]:

c = pop_data['County'].unique()
f = pop_data['FIPS_state_county'].unique()


# In[109]:

c = pop_data['County'].unique().T
f = pop_data['FIPS_state_county'].unique().T
county = pd.DataFrame([c,f]).T
county.rename(columns={0:'County',1:'FIPS'}, inplace=True)


# In[115]:

final_pop = final_data.merge(county, how="inner", on="County")
final_pop = final_pop[['year','month','County','FIPS','Gender','AgeGroup','Population']]
final_pop.to_csv("Final_Population_Interpolated.csv")
pop_04 = final_pop[final_pop['year'] >= 2004]


# In[126]:

hosp_merged = pop_04.merge(h_grouped, how='left',on=['year','month','FIPS','Gender','AgeGroup'])


# In[129]:

hosp_merged = hosp_merged[hosp_merged['year']<2014]
hosp_merged.to_csv('Hosp_Pop_Merged.csv')


# In[132]:

hosp_merged['Patients_ratio'] = np.array(hosp_merged['Patients_Count']) / np.array(hosp_merged['Population']) 
hosp_merged.to_csv('Hosp_Pop_Merged.csv')


# In[160]:

vaccine_data = pd.read_csv('WA_state_vaccine_data.csv')

vaccine_data['year'] = "20" + vaccine_data['MONTH_YR'].str[-2:]
vaccine_data['year'] = vaccine_data['year'].astype(int)
vaccine_data = vaccine_data[(vaccine_data['year'] >= 2004) & (vaccine_data['year'] < 2014)]
vaccine_data['month'] = vaccine_data['MONTH_YR'].str[:3]
vaccine_data.reset_index(inplace=True)
vaccine_data.replace(to_replace=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
       'Oct', 'Nov', 'Dec'], value=[1,2,3,4,5,6,7,8,9,10,11,12], inplace=True)

vaccine_data


# In[159]:

vaccine_data['month'].unique()


# In[171]:

zip_list = h_data[['pstco2','zip']].drop_duplicates('zip')
zip_list.rename(columns={'pstco2':'FIPS','zip':"ADDRESS_ZIP"}, inplace=True)
zip_county = zip_list.merge(county, how='inner', on='FIPS')
vaccine_data = vaccine_data.merge(zip_county, how='inner', on='ADDRESS_ZIP')


# In[177]:

vaccine_g = vaccine_data.groupby(['year','month','FIPS','County']).sum()
vaccine_g.reset_index(inplace=True)
vaccine_g['AgeGroup'] = [1]*len(vaccine_g)
vaccine_g = vaccine_g[['year','month','FIPS','County','AgeGroup','TOTAL POPULATION','4313314 SERIES']]
vaccine_g.to_csv('Vaccine_Cleaned.csv')


# In[178]:

vaccine_g


# In[196]:

# hosp_merged.groupby(['year'])
group1_pop = pop_04[pop_04['AgeGroup']==1]
group1_pop = group1_pop.groupby(['year','month','County','FIPS','AgeGroup']).sum()
group1_pop.reset_index(inplace=True)
group1_pop = group1_pop[['year','month','County','FIPS','AgeGroup','Population']]

h_group1 = h_grouped[h_grouped['AgeGroup']==1]
h_group1 = h_group1.groupby(['year','month','FIPS','AgeGroup']).sum()
h_group1.reset_index(inplace=True)
h_group1 = h_group1[['year','month','FIPS','AgeGroup','Patients_Count']]

gr1_pop_hosp = group1_pop.merge(h_group1, how='inner', on = ['year','month','FIPS','AgeGroup'])
hosp_vaccine1 = gr1_pop_hosp.merge(vaccine_g, how='left', on=['year','month','FIPS','County','AgeGroup'])
hosp_vaccine1.rename(columns={"TOTAL POPULATION":'all_vaccinated','4313314 SERIES':"4313314_SERIES"}, inplace=True)
hosp_vaccine1['Patients_Ratio'] = np.array(hosp_vaccine1['Patients_Count']) / np.array(hosp_vaccine1['Population'])
hosp_vaccine1['All_Vaccinated_Ratio'] = np.array(hosp_vaccine1['all_vaccinated']) / np.array(hosp_vaccine1['Population'])
hosp_vaccine1['All_4313314_Ratio'] = np.array(hosp_vaccine1['4313314_SERIES']) / np.array(hosp_vaccine1['Population'])
hosp_vaccine1['Timeline'] =  np.array(hosp_vaccine1['year'].astype(str)) + "-" +np.array(hosp_vaccine1['month'].astype(str))
hosp_vaccine1.to_csv("Master_Data_Final.csv")
hosp_vaccine1


# In[ ]:




# In[ ]:



