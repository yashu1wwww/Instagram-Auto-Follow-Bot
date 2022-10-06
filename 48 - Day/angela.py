from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver_path = "c:/Development/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


driver.get(url="http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Arunesh")

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("kumar")

email = driver.find_element(By.NAME, "email")
email.send_keys("aruneshkumar@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()
