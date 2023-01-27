import json

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

PATH = "D:\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
html_page = driver.get("https://hamkorbank.uz/")
time.sleep(5)

def jismoniy():
    d_jismoniy = {1: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[1]/a', 2: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[2]/a',
         3: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[3]/a', 4: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[4]/a',
         5: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[5]/a', 6: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[6]/a',
         7: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[7]/a', 8: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[8]/a',
         9: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[9]/a', 10: '/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[10]/a',
         11:'/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[11]/a',12:'/html/body/div[2]/div[1]/div/ul[5]/li[1]/div/ul/li[12]/a'}

    for i in d_jismoniy:
        action = ActionChains(driver)
        xpath = d_jismoniy[i]
        jismoniy_shaxslarga = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[1]/a')
        action.move_to_element(jismoniy_shaxslarga).perform()
        a = driver.find_element(By.XPATH, xpath)
        a.click()
        time.sleep(1)


def buziness():
    d_biznes = {1: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[1]/a',
                2: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[2]/a',
                3: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[3]/a',
                4: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[4]/a',
                5: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[5]/a',
                6: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[6]/a',
                7: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[7]/a',
                8: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[8]/a',
                9: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[9]/a',
                10: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[10]/a',
                11: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[11]/a',
                12: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[12]/a',
                13: '/html/body/div[2]/div[1]/div/ul[5]/li[2]/div/ul/li[13]/a'}
    for i in d_biznes:
        action = ActionChains(driver)
        xpath = d_biznes[i]
        biznes_uchun = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[2]/a')
        action.move_to_element(biznes_uchun).perform()
        a = driver.find_element(By.XPATH, xpath)
        a.click()
        time.sleep(1)
def aksiyador():
    d_aksiyador = {1: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[1]/a',
                2: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[2]/a',
                3: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[3]/a',
                4: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[4]/a',
                5: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[5]/a',
                6: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[6]/a',
                7: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[7]/a',
                8: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[8]/a',
                9: '/html/body/div[2]/div[1]/div/ul[5]/li[3]/div/ul/li[9]/a' }
    for i in d_aksiyador:
        action = ActionChains(driver)
        xpath = d_aksiyador[i]
        biznes_uchun = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[3]/a')
        action.move_to_element(biznes_uchun).perform()
        a = driver.find_element(By.XPATH, xpath)
        a.click()
        time.sleep(1)

def moliyaviy():
    d_moliyaviy = {1: '/html/body/div[2]/div[1]/div/ul[5]/li[4]/div/ul/li[1]/a',
                2: '/html/body/div[2]/div[1]/div/ul[5]/li[4]/div/ul/li[2]/a',
                3: '/html/body/div[2]/div[1]/div/ul[5]/li[4]/div/ul/li[3]/a',
                4: '/html/body/div[2]/div[1]/div/ul[5]/li[4]/div/ul/li[4]/a'}
    for i in d_moliyaviy:
        action = ActionChains(driver)
        xpath = d_moliyaviy[i]
        biznes_uchun = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[4]/a')
        action.move_to_element(biznes_uchun).perform()
        a = driver.find_element(By.XPATH, xpath)
        a.click()
        time.sleep(1)

def bank():
    d_bank = {1: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[1]/a',
                2: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[2]/a',
                3: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[3]/a',
                4: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[4]/a',
                5: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[5]/a',
                6: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[6]/a',
                7: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[7]/a',
                8: '/html/body/div[2]/div[1]/div/ul[5]/li[5]/div/ul/li[8]/a'}
    for i in d_bank:
        action = ActionChains(driver)
        xpath = d_bank[i]
        biznes_uchun = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[5]/a')
        action.move_to_element(biznes_uchun).perform()
        a = driver.find_element(By.XPATH, xpath)
        a.click()
        time.sleep(1)

def matbuot():
        matbuot = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[6]/a')
        matbuot.click()
        time.sleep(1)


def istemolchi():
    matbuot = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul[5]/li[7]/a')
    matbuot.click()
    time.sleep(1)

def change_lang():
    action = ActionChains(driver)
    change_lang_uz = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div/div[1]/div[1]/ul/li[7]/a')
    action.move_to_element(change_lang_uz).perform()
    a = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div/div[1]/div[1]/ul/li[7]/ul/li[1]/a')
    a.click()
    time.sleep(5)


dict_func = {1: jismoniy(), 2: buziness(), 3: aksiyador(), 4:moliyaviy(), 5:bank(), 6:matbuot(), 7:istemolchi(), 8:change_lang(), 9:jismoniy(),10:buziness(), 11:aksiyador(), 12:moliyaviy(), 13:bank(), 14:matbuot(), 15:istemolchi()}

