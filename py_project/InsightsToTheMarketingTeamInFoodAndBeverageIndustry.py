#!/usr/bin/env python
# coding: utf-8
import streamlit as st

st.info('''
Title: "BiteSights: F&B Industry Analysis" (DATA ANALYSIS)\n
Enrollment number: 22002170220021\n
Subject : FCSP-2\n
Problem Statement: Provide Insights to the Marketing Team in Food & Beverage Industry\n
          ''')

st.image('./ps1.png')

# ![image-2.png](attachment:image-2.png)

# st.subheader("Importing required libraries")
# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#to ignore all the warnings
warnings.filterwarnings("ignore")


# ### Importing csv files

# In[3]:


survey_df = pd.read_csv('Dataset/fact_survey_responses.csv')


# In[4]:


respondants_df = pd.read_csv('Dataset/dim_repondents.csv')


# In[5]:


city_df = pd.read_csv('Dataset/dim_cities.csv')


# ### Merging csv files based on common columns between tables

# In[6]:


two_tables = pd.merge(left=survey_df,right=respondants_df,how='outer',on='Respondent_ID')


# In[96]:


two_tables.head()


# In[8]:


full_df = pd.merge(left=two_tables,right=city_df,how='outer',on='City_ID')


# In[9]:


full_df.head()


st.subheader("1. Demographic Insights (examples)")

st.markdown("#### a.Who prefers energy drink more? (male/female/non-binary?)")

# In[10]:


# finding out the columns


# In[11]:


# full_df.columns


# In[12]:


# grouping the dataset by consume frequency and gender


# In[13]:


energy_pref = full_df.groupby(['Consume_frequency','Gender']).size().unstack()


# In[14]:


energy_pref


# ### Plotting the data

# In[15]:


# plt.figure(figsize=(12,8))
# energy_pref.plot(kind='bar')
# plt.ylabel("Count of nums")
# plt.title("Energy drink preferences based on gender")
# # plt.legend(loc=(1.1,0.75))
# plt.show()
st.subheader('Energy drink preferences based on gender')
st.bar_chart(energy_pref)

st.markdown('''####  Observations : 
#### - people more likly to have energy drink 2-3 times a week
#### - male are more prone to energy drink than others''')

st.subheader("b. Which age group prefers energy drinks more?")  
# In[16]:


age_df = full_df.groupby(['Consume_frequency','Age']).size().unstack()


# In[17]:


age_df


# ### Plotting the result

# In[18]:


# plt.figure(figsize=(12,8))
# age_df.plot(kind='bar')
# plt.ylabel("Count of nums")
# plt.title("Energy drink preferences based on Age group")
# # plt.legend(loc=(1.1,0.75))
# plt.show()

st.subheader('Energy drink preferences based on Age group')
st.bar_chart(age_df)


st.markdown('''
#### Observations: 
#### - There is a increasing trend in having energy drinks from age 15 to 30
#### - People with age group of 19-30 are the highest consumers of energy drink
#### - after 30 people are less probable to have energy drink''')

st.subheader("c. Which type of marketing reaches the most Youth (15-30)?")

# ### Extracting coustomers within the range of 15-30 then finding the frequency

# In[19]:


youth_df = full_df.loc[(full_df["Age"]=='15-18') | (full_df["Age"]=='19-30'), 'Marketing_channels'].value_counts()


# In[20]:


youth_df


# In[21]:


# plt.figure(figsize=(12,8))
# sns.barplot(x=youth_df.index,y=youth_df.values)
# plt.xticks(rotation = 90)
# plt.xlabel("Marketing Channel")
# plt.ylabel("Count of occurence")
# plt.title("Marketing channel preferences for age group 15-30")
# plt.show()

st.subheader('Marketing channel preferences for age group 15-30')
st.bar_chart(youth_df)


st.markdown('''
#### Observations: 
#### - online ads are reaching to more people''')

# ## 2. Consumer Preferences:

# ### a. What are the preferred ingredients of energy drinks among respondents?

# In[22]:


# Finding the frequency of ingredients 


# In[23]:


ingredients_pref = full_df['Ingredients_expected'].value_counts()


# In[24]:


ingredients_pref


# In[25]:


# plt.figure(figsize=(12,8))
# sns.barplot(x=ingredients_pref.index,y=ingredients_pref.values)
# plt.xticks(rotation = 90)
# plt.xlabel("Ingredients Expected")
# plt.ylabel("Count of occurence")
# plt.title("Ingredients preferences")
# plt.show()

st.subheader('Ingredients preferences')
st.bar_chart(ingredients_pref)


# ### Observations : 
# - People ask for Caffeine more than vitamins

# ### b. What packaging preferences do respondents have for energy drinks?

# In[26]:


pack_df = full_df['Packaging_preference'].value_counts()


# In[27]:


pack_df


# In[28]:


plt.figure(figsize=(12,8))
sns.barplot(x=pack_df.index,y=pack_df.values)
plt.xticks(rotation = 90)
plt.xlabel("Packaging_preference")
plt.ylabel("Count of occurence")
plt.title("Packaging preferences of customers")
plt.show()

st.subheader('Packaging preferences of customers')
st.bar_chart(pack_df)


st.markdown('''
#### Observations:
#### - In packaging people are liking to have Compact and portable cans''')

st.subheader("3. Competition Analysis:")

st.markdown("#### a. Who are the current market leaders?")

# In[29]:

lead_df = full_df['Current_brands'].value_counts()


# In[30]:


lead_df


# In[31]:


plt.figure(figsize=(12,8))
sns.barplot(x=lead_df.index,y=lead_df.values)
plt.xticks(rotation = 90)
plt.xlabel("Content_brands")
plt.ylabel("Count of occurence")
plt.title("Brand preferences of customers")
plt.show()

st.subheader('Brand preferences of customers')
st.bar_chart(lead_df)


# In[32]:


market_share_df = full_df['Current_brands'].value_counts(normalize=True)*100 


# In[33]:


market_share_df


# In[40]:


# plt.figure(figsize = (12,8))
# fig1 = plt.pie(market_share_df,labels=market_share_df.index, autopct='%.0f%%',explode=[0,0,0,0,0.10,0,0])
# plt.title("Market share of the existing brands")


fig1, ax1 = plt.subplots()
ax1.pie(market_share_df,labels=market_share_df.index, autopct='%.0f%%',explode=[0,0,0,0,0.10,0,0])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


st.subheader('Brand preferences of customers')
st.pyplot(fig1)

st.markdown('''### Observations: 
### - cola-coka is leading the market!
### - cola-coka is occupying 25% of the market closely followed by bepsi by 21%''')

st.markdown("#### b. What are the primary reasons consumers prefer those brands over ours?")

# In[41]:


full_df.columns


# **Segregating customers whose current brand is not codeX**

# In[42]:


cus_of_other_brand = full_df.loc[full_df['Current_brands']!='CodeX',:]


# In[44]:


cus_of_other_brand.head()


# **Finding the issue**

# In[45]:


iss_df = cus_of_other_brand['Reasons_preventing_trying'].value_counts()

plt.figure(figsize=(12,8))
sns.barplot(x=iss_df.index,y=iss_df.values)
plt.xticks(rotation = 90)
plt.xlabel("Reasons_preventing_trying")
plt.ylabel("Count of occurence")
plt.title("Why not us?")
plt.show()

st.subheader("Why not us?")
st.bar_chart(iss_df)

st.markdown('''
#### Observations:
#### - The prime reason is that the brand is not available locally''')

# **Finding out the reason to choose other brands**

# In[47]:


other_brands_df = cus_of_other_brand['Reasons_for_choosing_brands'].value_counts()

plt.figure(figsize=(12,8))
sns.barplot(x=other_brands_df.index,y=other_brands_df.values)
plt.xticks(rotation = 90)
plt.xlabel("Reasons for choosing ")
plt.ylabel("Count of occurence")
plt.title("Why us?")
plt.show()

st.subheader("Why us?")
st.bar_chart(other_brands_df)


st.markdown('''
#### Observations :
#### - Brand reputation is the demanding factor''')

st.subheader("4. Marketing Channels and Brand Awareness:")

st.subheader ("#### a. Which marketing channel can be used to reach more customers?")

# **trying to find what marketing source is bringing customers to other companies?**

# In[49]:


ms_counts = full_df['Marketing_channels'].value_counts()


# In[50]:


cus_of_codex= full_df.loc[full_df['Current_brands']=="CodeX",:]


# In[51]:


cus_of_codex.head()


# In[52]:


codex_counts = cus_of_codex['Marketing_channels'].value_counts()


# In[53]:


codex_counts


# In[63]:


fig2,ax1 = plt.subplots()
plt.title("Analyzing marketing channel performance")
ax2 = ax1.twinx()
ax1.bar(ms_counts.index,ms_counts.values,color='red')
ax2.bar(ms_counts.index,codex_counts.values,color='orange')

ax1.set_xlabel("Marketing channel")
ax1.set_ylabel("Customers of other brands",color='red')
ax2.set_ylabel("Customers of codex",color='orange')
ax1.set_xticklabels(ms_counts.index,rotation='vertical')

st.subheader("Analyzing market channel")
st.pyplot(fig2)

st.markdown('''
#### Observations:
#### - online ads is reaching more people''')

st.markdown("#### b. How effective are different marketing strategies and channels in reaching our customers?")

# ### focusing on the codex customers

# In[77]:


codex_cust = full_df[full_df['Current_brands']=='CodeX']
codex_cust


# In[76]:


full_df.columns


# In[78]:


market_codex = codex_cust.groupby(['Heard_before','Tried_before','Marketing_channels']).size().unstack()


# ### assuring the marketing channels are performing well 

# In[79]:


market_codex


# In[83]:


market_codex.loc[("No")]


# In[82]:


heard_tried = market_codex.loc[("Yes","Yes")]/sum(market_codex.loc[("Yes","Yes")])*100


# In[80]:


heard_but_never_tried = market_codex.loc[("Yes","No")]/sum(market_codex.loc[("Yes","No")])*100


# In[85]:


plt.figure(figsize=(12,8))
plt.pie(heard_but_never_tried,labels=heard_but_never_tried.index,autopct='%.0f%%')
plt.title("Bounced Advertisement rate")

fig3, ax1 = plt.subplots()
ax1.pie(heard_but_never_tried,labels=heard_but_never_tried.index,autopct='%.0f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig3)

# ### Observations:
# - Online ads are performing well in marketing
