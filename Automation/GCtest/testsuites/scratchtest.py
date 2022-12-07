from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
import requests
from setuptools.extension import Library
# from GCITtest import *





with open("../testdata/test_data.json") as jsonFile:    #Loading testdata
    jsonObject = json.load(jsonFile)
    jsonFile.close()



service_object = Service("C:/Users/Johnbabu/PycharmProjects/project_automation/Drivers/chromedriver.exe")

driver = webdriver.Chrome(service=service_object)
driver.maximize_window()

driver.get(jsonObject["url"])
driver.maximize_window()
driver.implicitly_wait(10)   #implicit wait


# def test_dashboardValues():
#     driver.refresh()
#     time.sleep(2)  # sleep
#     driver.find_element(By.XPATH, "//div[@class='menu']").click()
#     Totvals = driver.find_elements(By.XPATH, "//div[@class='menu-list']//ul//li//a[1]")
#     list_new = []
#     for i in Totvals:
#         list_new.append(str(i.get_attribute('text')))
#         # list_new.append(str(i.text))
#     print(list_new)






def test_socialWebsites():

    global res
    global j
    global re
    driver.refresh()
    time.sleep(2)  # sleep
    driver.find_element(By.XPATH, "//div[@class='menu']").click()
    soc = driver.find_elements(By.XPATH, "//div[@class='social so-slide']//ul//li//a[1]")
    myList = []
    for i in soc:
        myList.append(str(i.get_attribute('href')))
    print(myList)
    driver.switch_to.new_window()
    driver.get(myList[2])
    pl = driver.set_page_load_timeout(5)
    print(pl)
    try:
        for j in myList:
            print(j)
            driver.switch_to.new_window()
            driver.get(j)
            pl = driver.set_page_load_timeout(5)
            print(pl)
            if pl != None:
                print("passed")
            else:
                print("fail")
    except:
        pass
    # driver.switch_to.window(j)
    # driver.set_page_load_timeout(3)






























    # try:
    #     for j in myList:
    #         driver.get(j)
    #         pl = driver.set_page_load_timeout(3)
    #         print("kpom")
    #         print(pl)
    #         resp = requests.get(j)
    #         # res = resp
    #         print(res)
    #     driver.switch_to.window(j)
    #     try:
    #         if driver.set_page_load_timeout(3):
    #             print("Script passed")
    #         else:
    #             print("Bad request")
    #     except:
    #         pass
    #
    #     # driver.switch_to.window(j)
    #     time.sleep(2)
    # except:
    #     pass
    # # driver.switch_to.window(j)
    #
