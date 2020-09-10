from browser import chrome_browser
from Prefeituras.BH.Site import Site
from Prefeituras.BH.Boleto import Boleto

browser = chrome_browser.get_browser('chromedriver')

try:
  indice_iptu = '4922180050092'
  browser.get('http://iptuonline.siatu.pbh.gov.br/IptuOnline/index.xhtml')
  Site.login(browser, '{}.{} .{} .{}.{}'.format(indice_iptu[0:3], indice_iptu[3:6], indice_iptu[6:9], indice_iptu[9:12], indice_iptu[12]))
  Site.open_bill(browser)

  [print('{}: {}'.format(key, parcela)) for key, parcela in Boleto.getParcelas(browser)]
  print('Linha Digitável: ' + Boleto.getLinhaDigitavel(browser))
  print('Data Vencimento: ' + Boleto.getDataVencimento(browser))
  Boleto.saveBarras(browser, indice_iptu);
  
except Exception as e:
  print(f"ERROR: {e}")

browser.quit()