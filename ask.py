from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time
import json


def search(beg,end):
    for i in range(beg,end+1):
        string="http://47.92.197.167:5283/submission/"+str(i)
        x=ask(string,str(i))
        if x==1:
            print("搜索到"+str(i)+"条")
            break



def ask(string,uid):
    driver.get(string)
    #time.sleep(0.5)
    try:
        a1 = driver.find_element(By.ID,'status_table').text
    except:
        return 0
    else:
        time.sleep(0.5)
        #print(a1)
        # if("Accepted" in a1):
        #     f1=driver.find_element(By.TAG_NAME,'code').text
        #     print(f1)
        searchstr="light"
        if("Accepted" in a1 and searchstr in a1):
            print(a1)
            print("fvvvvvvvvvvvvvvvvvvvvvv")
            f1=driver.find_element(By.TAG_NAME,'code').text
            with open(uid+"_"+searchstr+'.txt','w') as f:
                f.write(f1)
            time.sleep(3)
        return 0

gecko_driver_path = 'D:\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=gecko_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://47.92.197.167:5283")
with open('cookies.txt','r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)
driver.refresh()

search(245100,250000)
