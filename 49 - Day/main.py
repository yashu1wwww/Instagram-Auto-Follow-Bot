from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


EMAIL = "python.email.8050523394@gmail.com"
PASSWORD = "8050523394"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3305730192&f_AL=true&geoId=102713980&keywords=human%20resources&location=India&refresh=true"
driver_path = "c:/Development/chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

#   open linkedin
driver.get(url=URL)

sleep(5)

#   go to login page
login_button = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis")
login_button.click()

#   login
email_input = driver.find_element(By.NAME, "session_key")
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.NAME, "session_password")
password_input.send_keys(PASSWORD)

login_button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
login_button.click()

sleep(30)


jobs = driver.find_elements(By.CSS_SELECTOR, "ul.scaffold-layout__list-container li")

sleep(5)


for job in jobs:
    job.click()
    sleep(5)

    try:
        #   apply for job
        apply_job_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
        apply_job_button.click()
        sleep(5)
        #   submit application
        submit_application = driver.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
        submit_application.click()
        sleep(5)
    except NoSuchElementException:
        continue




#

#
# #   done
# close_icon = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.mlA.block")
# close_icon.click()
#
# #   save jobs
# save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
# save_button.click()


















