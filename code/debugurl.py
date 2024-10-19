from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time
import json

gecko_driver_path = 'D:\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=gecko_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://47.92.197.167:5283")
with open('cookies.txt','r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)
driver.refresh()
string="http://47.92.197.167:5283/submission/"+str(295100)

driver.get(string)
#time.sleep(0.5)
s1=driver.find_element(By.CLASS_NAME,"content").text
if("提交记录" in s1 and "不正确" in s1):
    print("fvvvvvvvvvvvvvv")
time.sleep(5)
# try:
#     a1 = driver.find_element(By.ID,'status_table').text
# except:
#     return 0
# else:
#     #time.sleep(0.5)
#     #print(uid)
#     #print(a1)
#     # if("Accepted" in a1):
#     #     f1=driver.find_element(By.TAG_NAME,'code').text
#     #     print(f1)
#     if("Accepted" in a1 and (searchstr in a1 or searchstr=='')):
#         print(a1)
#         f1=driver.find_element(By.TAG_NAME,'code').text
#         with open("code/"+searchstr+"_"+uid+'.txt','w') as f:
#             f.write(f1)
#         #time.sleep(5)
#     return 0

#245222
#245281