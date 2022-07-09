from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import filter_contacts

wishingContacts = filter_contacts.filter_contacts("./google.csv")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://web.whatsapp.com")
sleep(15)

for key, value in wishingContacts.items():
    PRE_MSG = "Salam *"
    ASTERISK = "*"
    POST_MSG = " Eid Mubarak to you and your family."
    # search for name
    name_box = driver.find_element_by_css_selector("div[data-tab='3']")
    name_box.click()
    name_box.send_keys(key)
    sleep(5)
    try:
        # click on user name
        user_box = driver.find_element_by_css_selector("span[title='" + key + "']")
        sleep(1)
        user_box.click()
        # click on attach icon. should i do this or go straight to attach_image
        attach_item = driver.find_element_by_css_selector('span[data-icon="clip"]')
        attach_item.click()
        attach_image = driver.find_element_by_xpath('//input[@type="file"]')
        attach_image.send_keys("/home/sazk/unodrive/umbrella folders/python umbrella folder/eid wishbot/card.jpg")
        sleep(1)
        # find message box that comes with attachment
        message_box = driver.find_element_by_css_selector('div[data-tab="10"]')
        message_box.click()
        # send message in message box
        message_box.send_keys(PRE_MSG + value + ASTERISK + POST_MSG)
        sleep(1)
        # find send button
        button_box = driver.find_element_by_css_selector('span[data-icon="send"]')
        button_box.click()
        sleep(1)
    except Exception:
        # when name is in contacts but not found in WhatsApp
        name_box.clear()
        continue
