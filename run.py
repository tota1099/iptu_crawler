import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from BELO_HORIZONTE.Form import Inputs, Buttons

ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
URL = 'http://iptuonline.siatu.pbh.gov.br/IptuOnline/index.xhtml'

def get_browser(driver, download_dir = None):
  
    driver_bin = driver
    bin_path =  os.path.join(ROOT_DIR, driver_bin)
    os.environ['PATH'] = f"{os.getenv('PATH')}:{bin_path}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path=bin_path, 
                                        options=chrome_options)

    return browser

def get_time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def init():
  print(f"{get_time_now()} Starting... ")

  browser = get_browser('chromedriver')

  try:
    wait = WebDriverWait(browser, 5)
    browser.get(URL)
    browser.find_element_by_id(Inputs.IPTU_INDICE.value).send_keys('492.218 .005 .009.2')
    browser.find_element_by_id(Buttons.PESQUISAR.value).click()

    time.sleep(2)
    browser.execute_script("mojarra.jsfcljs(document.getElementById('form'),{'form:timoveis:0:j_idt33':'form:timoveis:0:j_idt33'},'_blank');")
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[-1])
    browser.save_screenshot('iptu.png')
  except Exception as e:
    print(f"{get_time_now()} Try again! This error has not handled")
    print(f"{get_time_now()} ERROR: {e}")
    browser.quit()
    exit(0)

if __name__ == '__main__':
  init()