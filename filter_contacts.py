#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


def filter_contacts(filename):
    all_contacts = pd.read_csv(filename)
    all_contacts = all_contacts[["Name", "Given Name"]]
    wishing_contacts = dict()
    for index, row in all_contacts.iterrows():
        print(str(row['Name'])+"  -  "+str(row['Given Name']))
        wishing_contacts[str(row['Name'])] = str(row['Given Name'])
    return wishing_contacts


# In[ ]:




