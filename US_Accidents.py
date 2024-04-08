#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[3]:


df = pd.read_csv(r'C:\Users\ascom\Desktop\prodigy_info_tech\US_Accidents\US_Accidents_March23.csv')
df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


df.shape


# In[9]:


df.isnull().sum()


# In[11]:


na_Values = df.isna().sum()
na_Values


# In[14]:


missing_values = na_Values.sort_values(ascending=False) * 100. / len(df)
missing_values


# In[17]:


missing_values.plot(kind='bar')


# In[19]:


cities = df.City.unique()
cities


# In[20]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[21]:


cities_by_accident['New York']


# In[25]:


cities_by_accident[:25].plot(kind='barh')


# In[26]:


sns.distplot(cities_by_accident)


# In[27]:


high_cities_by_accident = cities_by_accident[cities_by_accident > 10000] 

low_cities_by_accident = cities_by_accident[cities_by_accident < 10000] 


# In[29]:


#percent of high_cities_by_accident
high_cities_by_accident_percent = len(high_cities_by_accident) / len(cities_by_accident)
high_cities_by_accident_percent


# In[30]:


sns.distplot(high_cities_by_accident)


# In[31]:


sns.distplot(low_cities_by_accident)


# In[33]:


sns.histplot(high_cities_by_accident,log_scale=True)


# In[34]:


sns.histplot(low_cities_by_accident,log_scale=True)


# In[35]:


cities_by_accident[cities_by_accident == 1 ]


# In[36]:


df.Start_Time[0]


# In[45]:


plt.figure(figsize=(15,10))
sns.scatterplot(y=df.Start_Lat, x=df.Start_Lng,hue=df.State)


# In[46]:


plt.figure(figsize=(20,15))
sns.scatterplot(y=df.Start_Lat, x=df.Start_Lng, hue=df.Severity)


# In[47]:


pie, ax = plt.subplots(figsize=[15,15])
labels = df.State.value_counts().keys()
plt.pie(x=df.State.value_counts(), autopct="%.1f%%", explode=[0.1]*len(df.State.value_counts()), labels=labels, pctdistance=0.5)
plt.show();


# In[48]:


weather = df.Weather_Condition.value_counts()


# In[49]:


weather[weather > 1000]


# In[50]:


pie, ax = plt.subplots(figsize=[15,15])
labels = weather[weather > 1000].keys()
plt.pie(x=weather[weather > 1000], autopct="%.1f%%", explode=[0.1]*len(weather[weather > 1000]), labels=labels, pctdistance=0.5)
plt.show();


# In[51]:


df['Temperature(F)']


# In[52]:


temperature = df['Temperature(F)'].value_counts()


# In[53]:


temperature.index


# In[54]:


temperature.values


# In[55]:


plt.figure(figsize=(10,5))
sns.scatterplot(x=temperature.index, y=temperature.values)
plt.show();


# In[ ]:




