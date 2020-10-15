from selenium.webdriver.common.by import By

class Boleto():
  def getLinhaDigitavel(browser):
    return browser.find_element_by_xpath('//*[@id="j_idt10"]/table/tbody/tr[8]/td/div/table/tbody/tr/td[2]').text.strip()

  def getDataVencimento(browser):
    return browser.find_element_by_xpath('//*[@id="j_idt10"]/table/tbody/tr[5]/td/table/tbody/tr/td[7]/table/tbody/tr[2]/td').text.strip()

  def saveBarras(browser, fileName):
    browser.find_element_by_xpath('//*[@id="j_idt10"]/table/tbody/tr[8]/td/div/div/table/tbody/tr/td[2]').screenshot('./codigoDeBarras/{}.png'.format(fileName))

  def getParcelas(browser):
    tabela_parcelas = browser.find_element_by_xpath('//*[@id="j_idt10"]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[3]/table[1]/tbody');
    rows = tabela_parcelas.find_elements(By.TAG_NAME, "tr")

    parcelas = {}
    for row in rows:
      col = row.find_elements(By.TAG_NAME, "td")
      if col and len(col) == 2:
        parcelas[col[0].text] = col[1].text
    return parcelas