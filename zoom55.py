from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import pandas as pd 
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.zomato.com/indore') 
time.sleep(4)
driver.maximize_window()
time.sleep(5) 


f_D_data=[]  

def whole_func(): 
    res_name=driver.find_element(By.CLASS_NAME,'sc-7kepeu-0.sc-eilVRo.eAhpQG').text
    print(res_name)
    try:
        res_addres=driver.find_element(By.CLASS_NAME,'sc-emmjRN.elDjui').text
        print(res_addres)   
    except:
        print("none")
    try:
        res_time=driver.find_element(By.CLASS_NAME,'sc-fhYwyz.fRKkxr').text
        print(res_time)
    except:
        print("none")
    try:
        res_rating=driver.find_element(By.CLASS_NAME,'sc-1q7bklc-1.cILgox').text
        print(res_rating)
    except:
        print("none")
    try:
        res_Delivery_Review=driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
        print(res_Delivery_Review)
    except:
        print("none")

    driver.execute_script('scrollTo(0,1000)')
    time.sleep(5) 

    list1=[] 
    menu_list=driver.find_elements(By.CLASS_NAME,'sc-1s0saks-17.bGrnCu')
    big_list=[]
    for i in menu_list:
        menu=[]
        try:
            dish_name=i.find_element(By.CLASS_NAME,'sc-1s0saks-15.iSmBPS').text
            #print(dish_name)
            menu.append(dish_name)
            print("Dish_name=>",dish_name)
        except:
            menu.append("none")
            #print("none")
        try:
            dish_price=i.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text
            menu.append(dish_price)
            print("dish_price=",dish_price)
        except:
            menu.append("none")
            #print("none")
        try:
            dish_votes=i.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text
            menu.append(dish_votes)
            print("dish_votes=",dish_votes)
        except:
            menu.append("none")
        try:
            dish_discription=i.find_element(By.CLASS_NAME,'sc-1s0saks-12.hcROsL').text
            menu.append(dish_discription)
            print("dish_discription=",dish_discription)
        except:
            menu.append("none")
        big_list.append(menu)
    print(big_list) 

    for i, n in enumerate(big_list):
        if n not in list1:
            list1.append(n)

    f_D_data.append(list1)
    print(len(big_list)) 
    print(len(list1)) 
    print(list1) 

def link_fun():
    for i in range(20):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(10)
            if(i==5 or i==10 or i==15):
                driver.execute_script('scrollTo(0,700)')
                time.sleep(5)
link_fun()

res_links=[]
driver.execute_script('scrollTo(0,700)')
time.sleep(5)
divs = driver.find_elements(By.CLASS_NAME,'sc-fgrSAo.ctkAaV')
for j in divs: 
    link=j.get_attribute("href")
    print(link)

    res_links.append(link)
  
print(res_links)
print(len(res_links))



def click():
    for ind, i in enumerate(res_links):
        # if ind==5:
        driver.get(i)
        time.sleep(3)
        print('index',ind)
        whole_func()  
click() 
