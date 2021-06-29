#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd

with open('Artists.json') as json_file:
    data = json.load(json_file)


# In[31]:


df = pd.read_json('Artists.json')


# In[32]:


df


# ## Which are top 10 nationalities?

# In[33]:


df_nationality = df.Nationality.value_counts(ascending=False).sort_values(ascending=False).head(10)


# In[34]:


df_nationality


# ## Divide by gender

# In[35]:


df.Gender.value_counts()


# In[36]:


df.Gender = df.Gender.replace(
    {'Male': 'M',
     'Female': 'F',
     'male': 'M',
     'female': 'F',
     'Non-binary': 'Non-Binary'    
    })


# In[98]:


df[['Gender', 'Nationality']].value_counts()


# In[99]:


df.Nationality.value_counts().head(10)


# In[100]:


df.groupby('Gender').Nationality.value_counts()


# In[ ]:





# ## Create separate columns for gender identity

# In[39]:


import numpy as np


# In[41]:


df['Male'] = df.Gender.replace({
    'F': np.nan,
    'Non-binary': np.nan,
    'Non-Binary': np.nan
})


# In[42]:


df['Female'] = df.Gender.replace({
    'M': np.nan,
    'Non-binary': np.nan,
    'Non-Binary': np.nan
})


# In[43]:


df


# In[44]:


df['Non-Binary'] = df.Gender.replace({
    'M': np.nan,
    'F': np.nan,
})


# In[45]:


df


# In[48]:


df.groupby(by='Nationality').Male.value_counts().sort_values(ascending=False).head(10)


# In[58]:


df.groupby(by='Nationality').Female.value_counts().sort_values(ascending=False).head(10)


# In[52]:


df.groupby(by='Nationality')['Non-Binary'].value_counts().sort_values(ascending=False).head(10)


# In[87]:


df_male = df.groupby(by='Nationality').Male.value_counts().sort_values(ascending=False).head(10)


# In[89]:


df_female = df.groupby(by='Nationality').Female.value_counts().sort_values(ascending=False).head(10)


# In[61]:


df_nonbinary = df.groupby(by='Nationality')['Non-Binary'].value_counts().sort_values(ascending=False).head(10)


# ### Use frames variable to concatenate dataframes.

# In[94]:


frames = [df_male, df_female, df_nonbinary]


# In[95]:


pd.concat(frames)


# ## Export

# In[96]:


df_categories = pd.concat(frames)


# In[97]:


df_categories.to_csv("df_categories.csv")


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




