from time import sleep
from selenium import webdriver
import filterContacts

PRE_MSG = "Salam *"
ASTERISK_END = "* "
POST_MSG = input("enter your message: ")
wishing_contacts = filterContacts.filter_contacts("./google.csv")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://web.whatsapp.com")
sleep(15)

for key, value in wishing_contacts.items():
    # search for name
    name_box = driver.find_element_by_css_selector("div[data-tab='3']")
    name_box.click()
    name_box.send_keys(key)
    try:
        # search for user name in aside
        user_box = driver.find_element_by_css_selector("span[title='" + key + "']")
    except NameError:
        try:
            sleep(1)
        except NameError:
            name_box.clear()
            continue
        else:
            pass
    else:
        user_box.click()
        # click on message text box
        message_box = driver.find_element_by_css_selector("div[title='Type a message']")
        message_box.click()
        message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
        try:
            # click send
            send_button = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
        except NameError:
            sleep(1)
        else:
            send_button.click()
