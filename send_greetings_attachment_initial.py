from time import sleep
from selenium import webdriver
import filterContacts

file_path = input("enter absolute file path to greeting card: ")
PRE_MSG = "Salam *"
ASTERISK_END = "* "
POST_MSG = input("enter your message: ")
wishing_contacts = filterContacts.filter_contacts("./staging/notes/assets/google.csv")
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
        # click on attach icon
        attach_item = driver.find_element_by_css_selector('span[data-icon="clip"]')
        attach_item.click()
        try:
            attach_image = driver.find_element_by_xpath('//input[@type="file"]')
        except NameError:
            sleep(0.5)
        finally:
            attach_image.send_keys(file_path)
            # find message box that comes with attachment
            message_box = driver.find_element_by_css_selector('div[data-tab="10"]')
            message_box.click()
            message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
            # find send button
            send_button = driver.find_element_by_css_selector('span[data-icon="send"]')
            send_button.click()
