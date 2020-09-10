from Prefeituras.BH.Form import Inputs, Buttons
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Site:
    def login(browser, iptu_indice):
        browser.find_element_by_id(Inputs.IPTU_INDICE.value).send_keys(iptu_indice)
        browser.find_element_by_id(Buttons.PESQUISAR.value).click()

    
    def open_bill(browser):
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'form')))
        browser.execute_script("mojarra.jsfcljs(document.getElementById('form'),{'form:timoveis:0:j_idt33':'form:timoveis:0:j_idt33'},'_blank');")
        browser.switch_to.window(browser.window_handles[-1])