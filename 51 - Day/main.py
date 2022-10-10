from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 150
PROMISED_UP = 10
# EMAIL = "python.email.8050523394@gmail.com"
EMAIL = "pythonbot12345"
PASSWORD = "8050523394"
chrome_driver_path = "c:/Development/chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.download_speed = 0
        self.upload_speed = 0
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def get_internet_speed(self, url):
        #   open speedtest website on chrome
        self.driver.get(url=url)
        sleep(3)

        #   accept cookies
        accept_all = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[2]/div[1]/div/button')
        accept_all.click()
        sleep(2)

        #   click on speed test
        go = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        go.click()
        sleep(60)

        #   download speed
        download_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.download_speed = download_speed.text
        print(self.download_speed)
        sleep(1)

        #   upload speed
        upload_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.upload_speed = upload_speed.text
        print(self.upload_speed)
        sleep(1)

    def tweet_at_provider(self, url, email, password):
        #   open Twitter website on chrome
        self.driver.get(url=url)
        sleep(5)

        #   login Twitter account
        sign_in = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span')
        sign_in.click()
        sleep(20)

        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        sleep(5)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(15)

        #   if internet speed below, he promised then tweet on Twitter
        if float(self.download_speed) < PROMISED_DOWN or float(self.upload_speed) < PROMISED_UP:
            get_form = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block")
            get_form.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_speed}/{self.upload_speed}, when i pay for promised {PROMISED_DOWN}/{PROMISED_UP}")
            sleep(5)

            button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            button.click()
            sleep(2)


bot = InternetSpeedTwitterBot(driver_path=chrome_driver_path)

#   get internet speed
bot.get_internet_speed(url="https://www.speedtest.net/")

#   tweet to internet provider
bot.tweet_at_provider(url="https://twitter.com/", email=EMAIL, password=PASSWORD)

