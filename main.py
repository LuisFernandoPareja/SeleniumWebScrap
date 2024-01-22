from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import requests

# BeautifulSoup Part (Webscraping the housing site)
URL = 'https://appbrewery.github.io/Zillow-Clone/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0', 'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'}
response = requests.get(URL, headers=headers).text

soup = BeautifulSoup(response, 'html.parser')


link_houses_list = []
price_houses_list = []
address_houses_list = []

for i in soup.select(selector='.property-card-link'):
    link_houses_list.append(i.get('href'))

for i in soup.select(selector='.PropertyCardWrapper__StyledPriceLine'):

    price_houses_list.append(i.text.strip('+/mo'))


for i in soup.select(selector='.Image-c11n-8-84-listing'):

    address_houses_list.append(i.get('alt').strip().replace('|', ''))

print(link_houses_list)
print(price_houses_list)
print(address_houses_list)


# Selenium part, filling forms

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

google_form = 'https://docs.google.com/forms/d/e/1FAIpQLScrLOx6hjIhi5UksyTsDrJgcBP77U_F1mxyaRWiX5mvgdoU-w/viewform?usp=sf_link'

driver.get(google_form)

# Get 3 inputs


for i in range(len(link_houses_list)):
    address_property_form = driver.find_element(By.XPATH,
                                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_property_form = driver.find_element(By.XPATH,
                                             value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_property_form = driver.find_element(By.XPATH,
                                             value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_button_form = driver.find_element(By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    sleep(1)
    address_property_form.send_keys(address_houses_list[i])
    rent_property_form.send_keys(price_houses_list[i])
    link_property_form.send_keys(link_houses_list[i])
    sleep(1)
    send_button_form.click()
    sleep(1)
    send_more_answers = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_more_answers.click()
    sleep(1)






