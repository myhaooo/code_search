from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import json
gecko_driver_path = 'D:\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=gecko_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://47.92.197.167:5283")

time.sleep(15)

with open('cookies.txt','w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
