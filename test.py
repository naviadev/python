from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import configparser
import time


options = Options()
options.use_chromium = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--blink-setting=imagesEnable=false')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

config = configparser.ConfigParser()
config.read('configID.ini')


def macro():
    try:
     driver = webdriver.Chrome(options=options)
     driver.get('https://kream.co.kr/products/268241?fetchRelated=true')
     kream_id = config.get('Kream', 'id')
     kream_pw = config.get('Kream', 'password')
     time.sleep(0.3)
     a_button = driver.find_element(By.CSS_SELECTOR, '.display_button.block[data-v-4950b353]')
     a_button.click()
     time.sleep(0.3)
     inputLogin = driver.find_elements(By.CLASS_NAME, 'input_txt')
     id = inputLogin[0]
     pw = inputLogin[1]
     id.send_keys(kream_id)
     pw.send_keys(kream_pw)
     time.sleep(0.2)
     loginButton = driver.find_element(By.CLASS_NAME, 'login_btn_box')
     loginButton.click()
     time.sleep(3)

     
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        if driver:
            driver.quit()
    return 



macro()
