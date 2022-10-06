from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = "c:/Development/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


# driver.get("https://www.amazon.com/SanDisk-128GB-MicroSDXC-Memory-Adapter/dp/B08GYKNCCP/ref=lp_16225007011_1_5")
# # price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
# price = driver.find_element(By.CSS_SELECTOR, 'span.a-offscreen')
# print(price.get_attribute("innerHTML"))


driver.get("https://www.python.org/")

# #   name
# form = driver.find_element(By.NAME, "q")
# print(form.tag_name)
# print(form.get_attribute("placeholder"))
#
# #   class name
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# #   css selector
# docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs_link.text)
#
# #   xpath
# bug = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug.text)


#   find elements
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

time_list = [time.text for time in times]
title_list = [title.text for title in titles]

events = {}

for i in range(len(times)):
    events[i] = {time_list[i]: title_list[i]}

print(events)

driver.quit()














