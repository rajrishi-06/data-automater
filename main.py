import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

def fill_form(current):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url="https://forms.gle/CtMT577GnHqUPdf28")
    time.sleep(3)
    for j in range(3):
        input_field = driver.find_element(By.XPATH,f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{j + 1}]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input_field.send_keys(current[j])
    button = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()
    driver.quit()


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8"
}
sites = []
def get_sites():
    response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
    content = response.text
    # print(content)
    soup = BeautifulSoup(content, "html.parser")
    rent_prices_tags = soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
    address_tags = soup.find_all(name="address")
    links_tags = soup.find_all(name='a',class_="property-card-link")
    # print(rent_prices_tags)
    for i in range(len(rent_prices_tags)):
        price = rent_prices_tags[i].getText().replace(',','')[0:5]
        try:
            sites.append({
                0 : ' '.join(address_tags[i].getText().split(' ')).strip(),
                1 : price,
                2 : links_tags[i].get('href')
            })
        except IndexError:
            continue
        fill_form(sites[i])

get_sites()