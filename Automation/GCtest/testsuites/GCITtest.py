from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
# import requests
from setuptools.extension import Library





with open("../testdata/test_data.json") as jsonFile:    #Loading testdata
    jsonObject = json.load(jsonFile)
    jsonFile.close()



service_object = Service("C:/Users/Vipinraj/PycharmProjectGCtest/Drivers/chromedriver.exe")

driver = webdriver.Chrome(service=service_object)
driver.maximize_window()

driver.get(jsonObject["url"])
driver.maximize_window()
driver.implicitly_wait(10)   #implicit wait


def test_dashboardValues():
    driver.refresh()
    time.sleep(2)  # sleep
    driver.find_element(By.XPATH, "//div[@class='menu']").click()
    Totvals = driver.find_elements(By.XPATH, "//div[@class='menu-list']//ul//li//a[1]")
    list_new = []
    for i in Totvals:
        list_new.append(str(i.get_attribute('text')))
        # list_new.append(str(i.text))
    print(list_new)




# def test_socialWebsites():
#
#     global res
#     global j
#     driver.refresh()
#     time.sleep(2)  # sleep
#     driver.find_element(By.XPATH, "//div[@class='menu']").click()
#     soc = driver.find_elements(By.XPATH, "//div[@class='social so-slide']//ul//li//a[1]")
#     myList = []
#     for i in soc:
#         myList.append(str(i.get_attribute('href')))
#     print(myList)
#     try:
#         for j in myList:
#             driver.get(j)
#             resp = requests.get(j)
#             res = resp
#             print(res.status_code)
#             time.sleep(2)
#             if res.status_code == 200:
#                 print("Script passed")
#             elif res.status_code == 400:
#                 print("Bad Request")
#             elif res.status_code == 999:
#                 print("Secured website")
#             else:
#                 print("Bad request")
#         driver.switch_to.window(j)
#         time.sleep(2)
#     except:
#         pass

