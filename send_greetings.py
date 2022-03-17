from time import sleep
from selenium import webdriver
import filter_contacts

wishingContacts = filter_contacts.filter_contacts("google.csv")
driver = webdriver.Firefox("./webdrivers")
driver.get("https://web.whatsapp.com")
sleep(30)

for key, value in wishingContacts.items():
    PRE_MSG = "Salam *"
    POST_MSG = "* Eid mubarak to you and your family. _This message is automatically sent from my Eid-greeting bot program to my contact list. For more info visit my repo: https://github.com/sazk07/Eid-Auto-Wish-Bot_ *"
    input_box = None
    try:
        input_box = driver.find_element_by_css_selector("div[data-tab='3']")
        input_box.click()
        input_box.send_keys(key)
        sleep(0.7)
        userbox = driver.find_element_by_css_selector("span[title='" + key + "']")
        userbox.click()
        inputbox = driver.find_element_by_css_selector("div[data-tab='6']")
        inputbox.click()
        inputbox.send_keys(PRE_MSG + value + POST_MSG + "\n")
        continue
    except Exception:
        print(f"Error! at {key}")
        continue
