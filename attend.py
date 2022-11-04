from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from time import sleep
import datetime

#
id = ""
pw = ""
#

















nowhour = datetime.datetime.now().hour   # the current hour
nowmin = datetime.datetime.now().minute # the current minute

if int(nowhour) == 17 and int(nowmin) >= 50:
    driver = webdriver.Chrome()
    driver.get('https://tacademy.skplanet.com')
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[1]/label/input").click()
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[1]/label/input").send_keys(id)
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[2]/label/input").click()
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[2]/label/input").send_keys(pw)
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[3]/a/img").click()
    sleep(0.3)
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[2]/a[1]/img").click()
    sleep(0.5)
    driver.find_element("xpath","/html/body/div/div[2]/div[2]/ul/li[3]/a/p").click() # 퇴실
    
    print("퇴실 예정시각: ",nowhour,":",nowmin)
    input("press enter to exit")
    
elif int(nowhour) == 8 and int(nowmin) >= 50:
    driver = webdriver.Chrome()
    driver.get('https://tacademy.skplanet.com')
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[1]/label/input").click()
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[1]/label/input").send_keys(id)
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[2]/label/input").click()
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[2]/label/input").send_keys(pw)
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[3]/a/img").click()
    sleep(0.3)
    driver.find_element("xpath","/html/body/div/div[2]/form/div[1]/div[2]/div[1]/div/fieldset/p[2]/a[1]/img").click()
    sleep(0.5)
    driver.find_element("xpath","/html/body/div/div[2]/div[2]/ul/li[3]/a[1]/p/img").click()
    
    print("출석 예정시각: ",nowhour,":",nowmin)
    input("press enter to exit")
    
else:
    print("아직 시간이 아닙니다",nowhour,":",nowmin)
    input("press enter to exit")

    