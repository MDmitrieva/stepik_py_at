import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    browser.execute_script("window.scrollBy(0, 200);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()