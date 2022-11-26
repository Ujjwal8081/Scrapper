import requests
import MySQLdb
from bs4 import BeautifulSoup
from selenium import webdriver
HOST = "localhost"
USERNAME = "root"
PASSWORD=""
DATABASE = "scrapping_airtel"
url_to_scrap = "https://www.airtel.in/myplan-infinity/"
browser = webdriver.Chrome()
browser.get(url_to_scrap)
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
plain_html_txt = requests.get(url_to_scrap)
html = browser.page_source
soup = BeautifulSoup(html,features="html.parser")
# print(soup.prettify())
price = soup.findAll('span', class_='price')
priceInfo = soup.findAll('span', class_='priceInfo')

print(price[0].text.strip()+' '+priceInfo[0].text.strip())
print(price[1].text.strip() + ' '+ priceInfo[1].text.strip())
print(price[2].text.strip() + ' '+ priceInfo[2].text.strip())
print(price[3].text.strip() + ' '+ priceInfo[3].text.strip())
# print(soup)
# CREATE TABLE `price_table`(
#     `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#     `price` varchar(255),
#     `priceInfo` varchar(255)
# )
db = MySQLdb.connect(HOST,USERNAME,PASSWORD,DATABASE)
cursor = db.cursor()
sql  = "INSERT INTO price_table(price,priceInfo) values (%s,%s)"
val = (price[0].text.strip(),priceInfo[0].text.strip())
try:
    cursor.execute(sql,val)
    db.commit()
except:
    db.rollback()
    db.close()