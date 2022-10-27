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
#driver.get("https://www.zomato.com/indore/grand-hotel-abids/order")
time.sleep(4)
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="root"]/div/div[10]/div/div[1]/div/div/a[2]/div[1]/h4').click()#send_keys(Keys.CONTROL,Keys.END)
# time.sleep(4)

main_link_list=[]
f_D_data=[]

def new_fun(): 
    hotel_name=driver.find_element(By.CLASS_NAME,'sc-7kepeu-0.sc-eilVRo.eAhpQG').text
    print(hotel_name)
    try:
        hotel_addres=driver.find_element(By.CLASS_NAME,'sc-emmjRN.elDjui').text
        print(hotel_addres)   
    except:
        print("none")
    try:
        hotel_open_time=driver.find_element(By.CLASS_NAME,'sc-fhYwyz.fRKkxr').text
        print(hotel_open_time)
    except:
        print("none")
    try:
        hotel_rating=driver.find_element(By.CLASS_NAME,'sc-1q7bklc-1.cILgox').text
        print(hotel_rating)
    except:
        print("none")
    try:
        hotel_Delivery_Review=driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
        print(hotel_Delivery_Review)
    except:
        print("none")

    driver.execute_script('scrollTo(0,1000)')
    time.sleep(5)
    m=[]
    D_name=[]
    hotel_dish=driver.find_elements(By.CLASS_NAME,'sc-1s0saks-17.bGrnCu')
    dish_list=[]
    for i in hotel_dish:
        dish=[]
        try:
            dish_name=i.find_element(By.CLASS_NAME,'sc-1s0saks-15.iSmBPS').text
            #print(dish_name)
            dish.append(dish_name)
            print("Dish_name=>",dish_name)
        except:
            dish.append("none")
            #print("none")
        try:
            dish_price=i.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text
            dish.append(dish_price)
            print("dish_price=",dish_price)
        except:
            dish.append("none")
            #print("none")
        try:
            dish_votes=i.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text
            dish.append(dish_votes)
            print("dish_votes=",dish_votes)
        except:
            dish.append("none")
        try:
            dish_discription=i.find_element(By.CLASS_NAME,'sc-1s0saks-12.hcROsL').text
            dish.append(dish_discription)
            print("dish_discription=",dish_discription)
        except:
            dish.append("none")
        dish_list.append(dish)
    print(dish_list)

    for i, n in enumerate(dish_list):
        if n not in m:
            m.append(n)

    f_D_data.append(m)
    print(len(dish_list)) 
    print(len(m)) 
    print(m) 

  
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
        new_fun()  
click() 




















# for i in range(20):
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     time.sleep(10)
#     print(i)
#     # if(i==4):
#     #     break
#     if(i==5 or i==10 or i==15):
#         driver.execute_script('scrollTo(0,700)')
#         time.sleep(5)      
# driver.execute_script("window.scrollTo(0,700)")

# new_links=[]
# divs = driver.find_elements(By.CLASS_NAME,'jumbo-tracker a')
# print("divs length ============================ ",len(divs))
# for j in divs:   
#     link=j.get_attribute("href")
#     #print(link)

#     new_links.append(link)

# print(new_links)
# print(len(new_links))


# sub="/hyderabad/kfc-abids/order"
# for l in new_links:
#     if sub not in res_links:
#         main_link_list.append(l)
# print(len(main_link_list))

