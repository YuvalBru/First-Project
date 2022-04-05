#!/usr/bin/env python
# coding: utf-8

# # Identify:
# 
# Please fill-in your ID in the following cell, **only id numbers, no names!**
# 

# In[3]:


import pandas as pd 
import numpy as np
id1 = "214445595"


# In[4]:


df = pd.DataFrame([id1])


# Uncomment in case two students are doing the assignment together:

# In[5]:


#df = pd.DataFrame([id1,id2])


# In[6]:


df.to_clipboard(index=False,header=False)


# In[7]:


# Please fill your names here: Yuval Brunshtein 


# 

# ---

# ----

# # Write your answers here
# 
# add as much lines of code and markdown as you need for each answer

# # Q1 

# In[165]:


#Countries chosen:
#1. Yemen -  Yuval 
#2. Belgium  - Brunshtein 
import pandas as pd 
import numpy as py 
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
vaccination_dataframe = pd.read_csv(url)
print("The number of records for the country Yemen"
      , len(vaccination_dataframe.loc[vaccination_dataframe["location"] == "Yemen"].values.tolist()))
print("The number of records for the country Belgium" , len(vaccination_dataframe.loc[vaccination_dataframe["location"] == "Belgium"].values.tolist()))      

belguim_records = vaccination_dataframe.loc[vaccination_dataframe["location"] == "Belgium"]
yemen_rec = vaccination_dataframe.loc[vaccination_dataframe["location"] == "Yemen"]


#  # Q2

# In[166]:


print("The last three records of Belgium are ")
belguim_records.iloc[-4:-1] 


# # Q3

# In[198]:



bmax_vacc = belguim_records["daily_vaccinations_per_million"].max()
ymax_vacc = yemen_records["daily_vaccinations_per_million"].max()

#I will put this and one will print none in this case ymax_row and the other will print all the records of belgium 
#bigger than the max record of yemen (bmax_row)
ymax_row = yemen_records.loc[yemen_records["daily_vaccinations_per_million"] >= bmax_vacc]
#ymax_row
bmax_row = belguim_records.loc[belguim_records["daily_vaccinations_per_million"] >= ymax_vacc]
#bmax_row
record_numb = bmax_row.loc[bmax_row["daily_vaccinations_per_million"] == bmax_vacc]
record_numy = ymax_row.loc[ymax_row["daily_vaccinations_per_million"] == ymax_vacc]
df = pd.DataFrame({"date" : record_num["date"] , "location" : record_num["location"] ,  "daily_vaccinations_per_million" : 
                   record_numb["daily_vaccinations_per_million"]
                      })
df


# # Q4

# In[211]:


bf_vacc_people_p100_avg = belguim_records.people_fully_vaccinated_per_hundred.mean() 
yf_vacc_people_p100_avg = yemen_records.people_fully_vaccinated_per_hundred.mean() 

bf_vacc_people_p100_avg
yf_vacc_people_p100_avg

bhalf_per100p = belguim_records.people_fully_vaccinated_per_hundred.median()
yhalf_per100p = yemen_records.people_fully_vaccinated_per_hundred.median()

print(yhalf_per100p)
print(bhalf_per100p)
print(yf_vacc_people_p100_avg)
print(bf_vacc_people_p100_avg)
#In both countries the median is bigger than the average the reason for this is because 
# in all the data combined there are a lot of zeros therefore the average goes down by a lot 
#while we take the median which isn't dependent on the average or the other zeros which are in the data frame
# therefore the median in this specific situation is bigger than the average 


# # Q5

# In[212]:


total_100people_average =  (yf_vacc_people_p100_avg +  bf_vacc_people_p100_avg ) / 2 
total_100people_average


# In[ ]:





# ---
# # GOOD LUCK !!!!
# ---

# In[ ]:


# do not type below this line

