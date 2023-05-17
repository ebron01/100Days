from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

number_of_users = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div[3]/a[1]').text
print(number_of_users)

# all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
# print("Element is visible? " + str(search.is_displayed()))
# driver.implicitly_wait(10)
search.send_keys('Python')
search.send_keys(Keys.ENTER)

driver.quit()