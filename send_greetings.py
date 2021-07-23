#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from time import sleep
import filter_contacts


wishingContacts = filter_contacts.filter_contacts("google.csv")
driver = webdriver.Firefox('C:\webdrivers')
driver.get('https://web.whatsapp.com')
sleep(30)
contacts = dict()

for key, value in wishingContacts.items():
    pre_msg = "Salam *"
    post_msg = "* Eid mubarak to you and your family. _This message is automatically sent from my Eid-greeting bot program to my contact list. For more info visit my repo: https://github.com/sazk07/Eid-Auto-Wish-Bot_ *"
    input_box = None
    try:
        input_box = driver.find_element_by_css_selector("div[data-tab='3']")
        input_box.click()
        input_box.send_keys(key)
        sleep(0.7)
        userbox = driver.find_element_by_css_selector("span[title='"+key+"']")
        userbox.click()
        inputbox = driver.find_element_by_css_selector("div[data-tab='6']")
        inputbox.click()
        inputbox.send_keys(pre_msg+value+post_msg+'\n')
        #sleep(1)
        #send_button = driver.find_element_by_css_selector("span[data-icon='send']")
        #send_button.click()
        #sleep(1)
        continue
    except Exception:
        input_box.clear()
        continue
    


# ### for groups
# span class = "i0jNr"

# ### in chats
# 
# #### chat 2
# 
# div class = "_3m_Xw"
# 
# div tabindex = "-1"
# 
# div class = "_2nY6U"
# 
# div class = "_3OvU8"
# 
# div class = "_3vPI2"
# 
# div class = "zoWT4"
# 
# span class = "_3q9s6"
# 
# span class = "_ccCW FqYAR.i0jNr" dir = "auto" title = "zeeshan"

# ## for chat 3
# 
# div class = "_3m_Xw"
# 
# div tabindex = "-1"
# 
# div class = "_2nY6U"
# 
# div class = "_3OvU8"
# 
# div class = "_3vPI2"
# 
# div class = "zoWT4"
# 
# span class = "_3q9s6"
# 
# span class = "_ccCW FqYAR i0jNr" dir = "auto" title = "Zeeshan Jessani Ksbl"
# 

# In[ ]:




