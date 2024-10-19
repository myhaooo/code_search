from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time
import json

searchstr="jump"
Headless=False

def search(beg,end):
    for i in range(beg,end+1):
        string="http://47.92.197.167:5283/submission/"+str(i)
        x=ask(string,str(i))
        if x==1:
            print("搜索到"+str(i)+"条")
            break


def ask(string,uid):
    driver.get(string)
    try:
        a1 = driver.find_element(By.ID,'status_table').text
        s1=driver.find_element(By.CLASS_NAME,"content").text
        if("提交记录" in s1 and "不正确" in s1):#在搜索至最后一个时末尾自动停止
            return 1
        time.sleep(0.1)
    except:
        return 0
    else:
        #time.sleep(0.5)
        #print(uid)
        #print(a1)
        # if("Accepted" in a1):
        #     f1=driver.find_element(By.TAG_NAME,'code').text
        #     print(f1)
        if("Accepted" in a1 and (searchstr in a1 or searchstr=='')):#搜索所有AC的代码，若有searchstr则追加搜索
            print(a1)
            f1=driver.find_element(By.TAG_NAME,'code').text
            with open("code/"+searchstr+"_"+uid+'.txt','w') as f:#存放在./code 文件夹下
                f.write(f1)
            time.sleep(3)
        return 0

gecko_driver_path = '..\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=gecko_driver_path)
if(Headless==True):
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=service,options=opt)
else:
    driver = webdriver.Chrome(service=service)
driver.get("http://47.92.197.167:5283")
with open('./cookies.txt','r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)
driver.refresh()


search(246082,255105)
