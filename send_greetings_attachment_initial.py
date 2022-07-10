from time import sleep
from selenium import webdriver, common.exceptions
import filterContacts

spec_cases = input("enter names for separate messaging, separated by comma: ")
spec_cases = spec_cases.split(",")
# check file_path
file_path = "./card.jpg"
# edit msgs as needed before exec code
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
        # click on attach icon
        try:
            attach_item = driver.find_element_by_css_selector('span[data-icon="clip"]')
            attach_item.click()
        except exceptions.NoSuchElementException as err2:
            print(f"second unexpected {err2=}, {type(err2)=}")
            name_box.clear()
            continue
        else:
            attach_image = driver.find_element_by_xpath('//input[@type="file"]')
            attach_image.send_keys(file_path)
            # find message box that comes with attachment
            sleep(1)
            message_box = driver.find_element_by_css_selector('div[data-tab="10"')
            message_box.click()
            try:
                for element in spec_cases:
                    if key == element:
                        message_box.send_keys(PRE_MSG2 + value + ASTERISK_END + POST_MSG2)
                        driver.implicitly_wait(10)
                        send_button = driver.find_element_by_css_selector('span[data-icon="send"')
                        send_button.click()
            # i expect hell here. suggest improvements pls
            except Exception as err3:
                print(f"third unexpected {err3=}, {type(err3)=}")
                message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
                # find send button
                driver.implicitly_wait(10)
                send_button = driver.find_element_by_css_selector('span[data-icon="send"')
                send_button.click()
