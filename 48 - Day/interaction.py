from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver_path = "c:/Development/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(articles.text)

# articles.click()

link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Site news")
# link_text.click()


search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)



























# driver.quit()
