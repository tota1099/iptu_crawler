from browser import chrome_browser
from Prefeituras.BH.Site import Site
from Prefeituras.BH.Boleto import Boleto
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/iptu/<indice_iptu>", methods=['GET'])
def iptu(indice_iptu):
  data = {}
  try:
    browser = chrome_browser.get_browser('chromedriver')
    browser.get('http://iptuonline.siatu.pbh.gov.br/IptuOnline/index.xhtml')
    Site.login(browser, '{}.{} .{} .{}.{}'.format(indice_iptu[0:3], indice_iptu[3:6], indice_iptu[6:9], indice_iptu[9:12], indice_iptu[12]))
    Site.open_bill(browser)

    data['parcelas'] = Boleto.getParcelas(browser)
    data['linha_digitavel'] = Boleto.getLinhaDigitavel(browser)
    data['data_vencimento'] = Boleto.getDataVencimento(browser)
    data['codigo_barras_img'] = '/home/renanporto/git/iptu-crawler/codigoDeBarras/{}.png'.format(indice_iptu)
    Boleto.saveBarras(browser, indice_iptu)
    
  except Exception as e:
    print(f"ERROR: {e}")

  browser.quit()
  resp = jsonify(data)
  return resp

if __name__ == '__main__':
    app.run(port=8080)