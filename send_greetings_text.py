from time import sleep
from selenium import webdriver, common.exceptions
import filterContacts

spec_case = input("enter name: ")
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
    new_chat_button = driver.find_element_by_css_selector("span[data-icon:'chat'")
    new_chat_button.click()
    name_box = driver.find_element_by_css_selector("div[data-tab='3'")
    name_box.click()
    name_box.send_keys(key)
    try:
        # search for user name in aside
        driver.implicitly_wait(10)
        sleep(1)
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
        if key == spec_case:
            message_box.send_keys(PRE_MSG2 + value + ASTERISK_END + POST_MSG2)
        else:
            message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
        # click send
        send_button = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
        send_button.click()
