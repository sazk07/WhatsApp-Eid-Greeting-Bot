from selenium import webdriver
from time import sleep
import filter_contacts

wishingContacts = filter_contacts.filter_contacts("./staging/test_contacts.csv")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get('https://web.whatsapp.com')
sleep(30)

for key, value in wishingContacts.items():
    pre_msg = "Salam *"
    post_msg = "* Eid mubarak to you and your family. _This message is automatically sent from my Eid-greeting bot program to my contact list. For more info visit my repo: https://github.com/sazk07/WhatsApp-Eid-Greeting-Bot_ *"
    name_box = driver.find_element_by_css_selector("div[data-tab='3'")
    name_box.click()
    name_box.send_keys(key)
    sleep(0.7)
    user_box = driver.find_element_by_css_selector("span[title='"+key+"']")
    user_box.click()
    message_box = driver.find_element_by_css_selector("div[title='Type a message']")
    message_box.click()
    message_box.send_keys(pre_msg+value+post_msg)
    sleep(1)
    button_box = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
    button_box.click()
    sleep(1)