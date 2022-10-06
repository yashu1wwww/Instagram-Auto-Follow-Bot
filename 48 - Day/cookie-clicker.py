from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


driver_path = "c:/Development/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


driver.get(url="https://orteil.dashnet.org/cookieclicker/")

sleep(30)

cookie = driver.find_element(By.ID, "bigCookie")

for _ in range(100):
    for _ in range(1000):
        cookie.click()
    sleep(5)


total_cookies = driver.find_element(By.ID, "cookies")
print(total_cookies.text)
