from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import filterContacts

spec_cases = input("enter names for separate messaging, separated by comma: ")
spec_cases = spec_cases.split(",")
PRE_MSG = "Salam *"
ASTERISK_END = "* "
POST_MSG = "Eid Mubarak to you and your family \nfrom Shahan"
PRE_MSG2 = "Bonjour *"
POST_MSG2 = "Selamat Hari Raya\nfrom Shahan"
list_keys_for_deletion = []
wishing_contacts = filterContacts.filter_contacts("./google.csv")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(30)
driver.get("https://web.whatsapp.com")

while True:
    for key, value in wishing_contacts.items():
        list_keys_for_deletion.append(key)
        # click chat button
        new_chat_button = WebDriverWait(driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, "span[data-icon='chat'")
            )
        )
        new_chat_button.click()
        # enter name
        name_box = WebDriverWait(driver, 30).until(
            expected_conditions.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]",
                )
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
            if key in list_keys_for_deletion:
                del wishing_contacts[key]
        except exceptions.TimeoutException:
            break
        except exceptions.NoSuchElementException as err:
            print(f"unexpected {err=}, {type(err)=}")
            name_box.clear()
            continue
        else:
            # click on message text box
            message_box = driver.find_element(
                By.CSS_SELECTOR, "div[title='Type a message']"
            )
            message_box.click()
            for name in spec_cases:
                if key == name:
                    message_box.send_keys(PRE_MSG2 + value + ASTERISK_END + POST_MSG2)
                    # click send button
                    send_button = driver.find_element(
                        By.XPATH,
                        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span",
                    )
                    send_button.click()
                else:
                    break
            message_box.send_keys(PRE_MSG + value + ASTERISK_END + POST_MSG)
            # click send button
            send_button = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span",
            )
            send_button.click()
