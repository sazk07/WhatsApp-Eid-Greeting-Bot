from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import filterContacts


def main():
    text_or_attachment = input(
        "do you want to send (1) text only or (2) with attachment?: "
    )
    file_path = "./card.jpg"
    PRE_MSG = "Salam *"
    ASTERISK_END = "* "
    POST_MSG = "Eid Mubarak to you and your family\nfrom Shahan"
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
            selector = (By.CSS_SELECTOR, "span[data-icon='chat'")
            condition = expected_conditions.element_to_be_clickable(selector)
            new_chat_button = WebDriverWait(driver, 30).until(condition)
            new_chat_button.click()
            # enter name
            selector = (By.CSS_SELECTOR, "div[data-tab='3'")
            condition = expected_conditions.element_to_be_clickable(selector)
            name_box = WebDriverWait(driver, 30).until(condition)
            name_box.click()
            name_box.send_keys(key)
            try:
                # search for user name in aside
                selector = (By.CSS_SELECTOR, "span[title='" + key + "'")
                condition = expected_conditions.visibility_of_element_located(selector)
                user_box = WebDriverWait(driver, 30).until(condition)
                user_box.click()
                if key in list_keys_for_deletion:
                    del wishing_contacts[key]
            except exceptions.TimeoutException:
                break
            except exceptions.NoSuchElementException as err:
                print(f"unexpected {err=}, {type(err)=}")
                # clear name_box if name not found in aside
                name_box.clear()
                continue
            else:
                match text_or_attachment:
                    case "1":
                        selector = (By.CSS_SELECTOR, "div[title='Type a message']")
                        message_box = driver.find_element(selector)
                        message_box.click()
                        if key == "AM":
                            message_box.send_keys(
                                PRE_MSG2 + value + ASTERISK_END + POST_MSG2
                            )
                        else:
                            message_box.send_keys(
                                PRE_MSG + value + ASTERISK_END + POST_MSG
                            )
                        # click send button
                        selector = (
                            By.XPATH,
                            "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span",
                        )
                        send_button = driver.find_element(selector)
                    case "2":
                        selector = (By.XPATH, '//input[@type="file"]')
                        attach_image = driver.find_element(selector)
                        attach_image.send_keys(file_path)
                        selector = (
                            By.XPATH,
                            "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]",
                        )
                        condition = expected_conditions.element_to_be_clickable(
                            selector
                        )
                        message_box = WebDriverWait(driver, 30).until(condition)
                        message_box.click()
                        # change name here
                        if key == "AM":
                            message_box.send_keys(
                                PRE_MSG2 + value + ASTERISK_END + POST_MSG2
                            )
                        else:
                            message_box.send_keys(
                                PRE_MSG + value + ASTERISK_END + POST_MSG
                            )
                        # click send button
                        selector = (By.CSS_SELECTOR, "span[data-icon='send'")
                        condition = expected_conditions.element_to_be_clickable(
                            selector
                        )
                        send_button = WebDriverWait(driver, 30).until(condition)
                    case _:
                        print("invalid input. Quitting")
                        quit()
                send_button.click()


if __name__ == "__main__":
    main()
