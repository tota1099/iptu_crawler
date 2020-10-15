import os
from selenium import webdriver

def get_browser(driver):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    bin_path =  os.path.join(dir_path, '../{}'.format(driver))
    os.environ['PATH'] = f"{os.getenv('PATH')}:{bin_path}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=bin_path, 
                                        options=chrome_options)
    return browser