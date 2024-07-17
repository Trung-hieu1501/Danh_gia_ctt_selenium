from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome()
driver.get("https://ctt-sis.hust.edu.vn/Surveys/dghp.aspx")
time.sleep(2)

user = ''
pass_word = ''
# login
login = driver.find_elements(By.CSS_SELECTOR, '.dxeEditAreaSys')
login[0].send_keys(user)
time.sleep(1)

element = login[2]
actions = ActionChains(driver)
actions.move_to_element(element).click().send_keys(pass_word).perform()
time.sleep(10)


while True:
    wait = WebDriverWait(driver, 10)
    ticks = driver.find_elements(By.CSS_SELECTOR, '.dxflNestedControlCell_Mulberry .dx-wrap')
    if ticks:
        for i in range(2, len(ticks)-1, 5):
            ticks[i].click()
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dxb')))
        next_button.click()
    else:
        break
        time.sleep(30)
        driver.quit()





