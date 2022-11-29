from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


EMAIL = "dlopoelevolllll.8ennis22225"
PASSWORD = "Yashu123@#"
MENTOR_USERNAME = "mahi7781"
INSTAGRAM_URL = "https://www.instagram.com/"
chrome_driver_path = r"C:\Users\Hp\Desktop\Bots\INSTAGRAM bot/chromedriver.exe"


class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(service=Service(executable_path=driver))

    def login(self, url, email, password):
        #   open instagram
        self.driver.get(url=url)
        sleep(5)

        #   login
        email_input = self.driver.find_element(By.NAME, "username")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        sleep(2)
        password_input.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self, url, account):
        #   get profile
        sleep(5)
        self.driver.get(url=f"{url}{account}")
        sleep(8)

        #   click on followers
        followers = self.driver.find_element(By.CSS_SELECTOR, 'ul.xieb3on li.x2pgyrj a._a6hd')
        followers.click()
        sleep(7)

        modal = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')

        # while True:
        for _ in range(2):
            sleep(5)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

        sleep(5)

        print("Find followers end")

    def follow(self):
        print("Follow start")
        sleep(5)
        # buttons = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Follow")

        buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div button")

        print(buttons)

        for button in buttons:
            button.click()
            print(button.text)
            sleep(2)

        print("Follow end")


bot = InstaFollower(driver=chrome_driver_path)

bot.login(url=INSTAGRAM_URL, email=EMAIL, password=PASSWORD)

bot.find_followers(url=INSTAGRAM_URL, account=MENTOR_USERNAME)

bot.follow()