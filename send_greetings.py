from selenium import webdriver
from time import sleep
import filter_contacts

wishingContacts = filter_contacts.filter_contacts("./google.csv")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://web.whatsapp.com")
sleep(30)

for key, value in wishingContacts.items():
    pre_msg = "Salam *"
    post_msg = "* Eid mubarak to you and your family. \n _This message is automatically sent from my Eid-greeting bot program to my contact list. If you want to view my source code visit my repo: https://github.com/sazk07/WhatsApp-Eid-Greeting-Bot_ "
    # search for name
    name_box = driver.find_element_by_css_selector("div[data-tab='3'")
    name_box.click()
    name_box.send_keys(key)
    sleep(0.7)
    try:
        # click on user name
        user_box = driver.find_element_by_css_selector("span[title='" + key + "']")
        user_box.click()
        # click on message text box
        message_box = driver.find_element_by_css_selector("div[title='Type a message']")
        message_box.click()
        message_box.send_keys(pre_msg + value + post_msg)
        sleep(1)
        # click send
        button_box = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
        button_box.click()
        sleep(1)
    except Exception():
        # when name is in contacts but not found in WhatsApp
        name_box.clear()
        continue
    
