# Crawler Prefeituras
Extração de dados com Selenium + BeautifulSoup para consultar IPTUs.

## Install

Download & Install Browser

### Google Chrome Stable:

**Linux**

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
```

**Windows**

Download page: https://www.google.pt/intl/pt-PT/chrome/

### Google Chrome Driver:

Download Google Chrome Driver from here: https://chromedriver.chromium.org/downloads

## Create virtual env

``` bash
virtualenv -p python3.6 env
env/bin/activate
```

## Install Dependencies

``` bash
pip install -r requirements.txt
```