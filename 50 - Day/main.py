from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


EMAIL = "0786indianking@gmail.com"
PASSWORD = "9534857622"

# EMAIL = "python.email.8050523394@gmail.com"
# PASSWORD = "ASzx@8002756958"

URL = "https://tinder.com/"
driver_path = "c:/Development/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url=URL)
sleep(3)

print(driver.window_handles)
print(driver.title)

#   log in
log_in = driver.find_element(By.LINK_TEXT, "Log in")
log_in.click()

print("logged in page")
sleep(20)

more_option = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div[1]/div/div/div[3]/span/button')
more_option.click()

print("more option")
sleep(5)

facebook = driver.find_element(By.XPATH, '//*[@id="q-104725266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
facebook.click()

print("facebook window")
sleep(10)

#   window switch
main_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)

sleep(2)


#   login tinder using of facebook
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.NAME, "pass")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
sleep(20)
print("facebook logged in")

#   switch window again
driver.switch_to.window(main_window)
print(driver.title)
sleep(20)

#   location
location = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
location.click()
sleep(5)

#   notification
notification = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
notification.click()
sleep(5)

#   accept
accept = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept.click()
sleep(5)

#   like people
for _ in range(50):
    sleep(5)
    try:
        like = driver.find_element(By.XPATH, '//*[@id="q1623655810"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')
        like.click()
    except NoSuchElementException:
        continue
