from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

element_list = []

# for page in range(1, 3, 1):

#     page_url = "https://en.wikipedia.org/wiki/Taj_Mahal"
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get(page_url)
#     title = driver.find_elements(By.CLASS_NAME, "title")
#     price = driver.find_elements(By.CLASS_NAME, "price")
#     description = driver.find_elements(By.CLASS_NAME, "description")
#     rating = driver.find_elements(By.CLASS_NAME, "ratings")

#     for i in range(len(title)):
#         element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
page_url = "https://en.wikipedia.org/wiki/Taj_Mahal"
driver.get(page_url)
paragraph = driver.find_element(By.XPATH, "//p[contains(text(), 'Construction of the mausoleum')]")
print("printing text",paragraph.text)

driver.close()