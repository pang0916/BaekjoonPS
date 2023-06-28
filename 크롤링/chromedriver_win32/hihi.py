import selenium 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get('https://map.kakao.com/?map_type=TYPE_MAP&q=%EC%84%9C%EC%9A%B8%EB%8C%80+26%EB%8F%99')

html = driver.page_source
bsObject = BeautifulSoup(html,'html.parser')
bsObject = bsObject.find(class_="moreview")

link = bsObject['href']
print(link)

driver.get(link)
html = driver.page_source
bsObject = BeautifulSoup(html,'html.parser')
bsObject = bsObject.find(class_="wrap_mapdetail.lbar_on")
print(bsObject)
