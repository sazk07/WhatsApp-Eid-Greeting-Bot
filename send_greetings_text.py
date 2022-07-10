from time import sleep
from selenium import webdriver, common.exceptions
import filterContacts

spec_cases = input("enter names for separate messaging, separated by comma: ")
spec_cases = spec_cases.split(",")
PRE_MSG = "Salam *"
ASTERISK_END = "* "
POST_MSG = "Eid Mubarak to you and your family \nfrom Shahan"
PRE_MSG2 = "Bonjour *"
POST_MSG2 = "Selamat Hari Raya\nfrom Shahan"
wishing_contacts = filterContacts.filter_contacts("./google.csv")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(30)
driver.get("https://web.whatsapp.com")

for key, value in wishing_contacts.items():
    # search for name
    sleep(1)
    new_chat_button = driver.find_element_by_css_selector("span[data-icon='chat'")
    new_chat_button.click()
    name_box = driver.find_element_by_css_selector("div[data-tab='3'")
    name_box.click()
    name_box.send_keys(key)
    try:
        # search for user name in aside
        sleep(1)
        driver.implicitly_wait(10)
        user_box = driver.find_element_by_css_selector("span[title='" + key + "'")
        user_box.click()
    except exceptions.NoSuchElementException as err:
        print(f"unexpected {err=}, {type(err)=}")
        name_box.clear()
        continue
    else:
        # click on message text box
        message_box = driver.find_element_by_css_selector("div[title='Type a message']")
        message_box.click()
        for element in spec_cases:
            if key == element:
                message_box.send_keys(PRE_MSG2 + value + ASTERISK_END + POST_MSG2)
                # find send button
                driver.implicitly_wait(10)
                send_button = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
                send_button.click()
            else:
                break
        message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
        # find send button
        driver.implicitly_wait(10)
        send_button = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
        send_button.click()
