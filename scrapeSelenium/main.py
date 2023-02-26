from selenium import webdriver
from selenium.webdriver.common.by import By
# URL="https://www.amazon.com/dp/B0B727YMJT/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
URL="https://www.python.org/"

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
event_details = {}
counter = 0
for i in range(0, len(events.split('\n')), 2):
    value = {
        "time" : events.split('\n')[i],
        "name" : events.split('\n')[i+1]
    }
    event_details[counter] = value
    counter += 1
print(event_details)
# driver.close()
driver.quit()