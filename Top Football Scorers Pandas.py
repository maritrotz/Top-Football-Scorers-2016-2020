#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np
df = pd.read_csv('Data.csv')


# In[191]:


#Find the top scorer for each year: 2016
display(df.loc[df['Year'] == 2016].sort_values('Goals', ascending=False).head(1))
                        


# In[169]:


#Find the top scorer for each year: 2017 
display(df.loc[df['Year'] == 2017].sort_values('Goals', ascending=False).head(1))


# In[170]:


#Find the top scorer for each year: 2018
display(df.loc[df['Year'] == 2018].sort_values('Goals', ascending=False).head(1))


# In[171]:


#Find the top scorer for each year: 2019
display(df.loc[df['Year'] == 2019].sort_values('Goals', ascending=False).head(1))


# In[172]:


#Find the top scorer for each year: 2020
display(df.loc[df['Year'] == 2020].sort_values('Goals', ascending=False).head(1))


# In[174]:


#Find the player with the highest expected goals per match for each year: 2016
display(df.loc[df['Year'] == 2016].sort_values('xG Per Avg Match', ascending=False).head(1))


# In[192]:


#Find the player with the highest expected goals per match for each year: 2017
display(df.loc[df['Year'] == 2017].sort_values('xG Per Avg Match', ascending=False).head(1))


# In[193]:


#Find the player with the highest expected goals per match for each year: 2018
display(df.loc[df['Year'] == 2018].sort_values('xG Per Avg Match', ascending=False).head(1))


# In[194]:


#Find the player with the highest expected goals per match for each year: 2019
display(df.loc[df['Year'] == 2019].sort_values('xG Per Avg Match', ascending=False).head(1))


# In[195]:


#Find the player with the highest expected goals per match for each year: 2020
display(df.loc[df['Year'] == 2020].sort_values('xG Per Avg Match', ascending=False).head(1))


# In[196]:


#Find the player with the most minutes played for each year: 2016

display(df.loc[df['Year'] == 2016].sort_values('Mins', ascending=False).head(1))


# In[197]:


#Find the player with the most minutes played for each year: 2017

display(df.loc[df['Year'] == 2017].sort_values('Mins', ascending=False).head(1))


# In[198]:


#Find the player with the most minutes played for each year: 2018

display(df.loc[df['Year'] == 2018].sort_values('Mins', ascending=False).head(1))


# In[201]:


#Find the player with the most minutes played for each year: 2019

display(df.loc[df['Year'] == 2019].sort_values('Mins', ascending=False).head(1))


# In[200]:


#Find the player with the most minutes played for each year: 2020

display(df.loc[df['Year'] == 2020].sort_values('Mins', ascending=False).head(1))


# In[258]:


#Find the top scorer in La Liga in 2016
top_scorer1 = df.query("League == 'La Liga' & Year == 2016")['Goals'].max()
top_scorer1_row = df.loc[df['Goals'] == top_scorer1]
display(top_scorer1_row)


# In[274]:


#Find the top scorer with the least amount of shots in 2018
display(df.loc[df['Year'] == 2018].sort_values('Shots', ascending=True).head(1))


# In[275]:


##Find the top scorer with the least amount of shots in 2019
display(df.loc[df['Year'] == 2019].sort_values('Shots', ascending=True).head(1))

