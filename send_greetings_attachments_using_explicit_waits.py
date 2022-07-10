from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import filterContacts

spec_cases = input("enter names for separate messaging, separated by comma: ")
spec_cases = spec_cases.split(",")
file_path = "./card.jpg"
PRE_MSG = "Salam *"
ASTERISK_END = "* "
POST_MSG = "Eid Mubarak to you and your family \nfrom Shahan"
PRE_MSG2 = "Bonjour *"
POST_MSG2 = "Selamat Hari Raya\nfrom Shahan"
list_keys = []
wishing_contacts = filterContacts.filter_contacts(
    "./google.csv"
)
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(30)
driver.get("https://web.whatsapp.com")

while True:
    for key, value in wishing_contacts.items():
        list_keys.append(key)
        # click chat button
        new_chat_button = WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, "span[data-icon='chat'")
            )
        )
        new_chat_button.click()
        # enter name
        name_box = WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[data-tab='3'")
            )
        )
        name_box.click()
        name_box.send_keys(key)
        try:
            # search for user name in aside
            user_box = WebDriverWait(driver, 30).until(
                expected_conditions.visibility_of_element_located(
                    (By.CSS_SELECTOR, "span[title='" + key + "'")
                )
            )
            user_box.click()
            if key in list_keys:
                del wishing_contacts[key]
        except exceptions.TimeoutException:
            break
        except exceptions.NoSuchElementException as err:
            print(f"unexpected {err=}, {type(err)=}")
            # clear name_box if name not found in aside
            name_box.clear()
            continue
        else:
            try:
                # click on attach icon
                attach_item = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="clip"]')
                attach_item.click()
            except exceptions.NoSuchElementException as err2:
                print(f"second unexpected {err2=}, {type(err2)=}")
                # if contact blocked, cannot find attach_item element
                name_box.clear()
                continue
            else:
                attach_image = driver.find_element(By.XPATH, '//input[@type="file"]')
                attach_image.send_keys(file_path)
                # find message box that comes with attachment
                message_box = WebDriverWait(driver, 30).until(
                    expected_conditions.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]")
                    )
                )
                message_box.click()
                for element in spec_cases:
                if key == element:
                    message_box.send_keys(PRE_MSG2 + value + ASTERISK_END + POST_MSG2)
                    # find send button
                    driver.implicitly_wait(10)
                    send_button = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "span[data-icon='send'")))
                    send_button.click()
                else:
                    break
            message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
                # find send button
                send_button = WebDriverWait(driver, 30).until(
                    expected_conditions.element_to_be_clickable(
                        (By.CSS_SELECTOR, "span[data-icon='send'")
                    )
                )
                send_button.click()
