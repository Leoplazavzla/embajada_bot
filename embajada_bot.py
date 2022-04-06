import os
import random
import sys
import time
from urllib.parse import urlparse
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import pandas as pd


# Open Webdriver
driver = webdriver.Firefox(executable_path=r'./driver/geckodriver.exe')
time.sleep(2)
driver.set_window_size(1100,900)

# Booking the appoinment
def bookingAppoinment():
    driver.get('https://pastel.diplomatie.gouv.fr/rdvinternet/html-4.02.00/frameset/frameset.html?lcid=1&sgid=74&suid=1')
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID, "BODY_WIN"))
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="MENU_WIN"]'))
    time.sleep(1)
    book_appoinment = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td')
    book_appoinment.click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.ID, "BODY_WIN"))
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="CONTENU_WIN"]'))
    time.sleep(1)
    check_input = driver.find_element(By.ID, 'ccg')
    check_input.click()
    time.sleep(2)
    driver.find_element(By.ID, 'boutonSuivant_link').click()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.ID, "BODY_WIN"))
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="CONTENU_WIN"]'))
    time.sleep(5)
    checkbox = driver.find_element(By.ID, 'ccg')
    checkbox.click()
    time.sleep(1)
    driver.find_element(By.ID, 'boutonSuivant_link').click()
    time.sleep(5)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except UnexpectedAlertPresentException:
        alert = driver.switch_to.alert
        alert.accept()
        print('no alert')     

# Fill the form with details
def fill_form():
    try:
        driver.switch_to.default_content()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.ID, "BODY_WIN"))
        time.sleep(1)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="CONTENU_WIN"]'))
        print('enterin fill form')
        pencil_table = driver.find_element(By.ID, 'compTableau_tbody')
        pencil_table.find_element(By.TAG_NAME, 'a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'boutonSuivant_link').click()
        time.sleep(1)
        last_name = driver.find_element(By.ID, 'nom').send_keys('ALGASIBIUR')
        family_name = driver.find_element(By.ID, 'nomnaiss').send_keys('ALGASIBIUR')
        first_name = driver.find_element(By.ID, 'prenoms').send_keys('Martin')
        birth_year = driver.find_element(By.ID, 'neen1').send_keys('1990')
        birth_month = driver.find_element(By.ID, 'neen2').send_keys('07')
        birth_day = driver.find_element(By.ID, 'neen3').send_keys('05')
        time.sleep(1)
        country_select = driver.find_element(By.ID, 'natactuelle')
        option = country_select.find_element(By.XPATH, '//option[@value="10"]')
        option.click()
        time.sleep(1)
        sex = driver.find_element(By.XPATH, '//*[@id="sexe"]').click()
        time.sleep(1)
        passport_num = driver.find_element(By.ID, 'num').send_keys('AAG439899')
        telephone_num = driver.find_element(By.ID, 'telephone').send_keys('3407458972')
        email = driver.find_element(By.ID, 'email').send_keys('malgasibiur@gmail.com')
        confirmation_email = driver.find_element(By.ID, 'confirm_email').send_keys('malgasibiur@gmail.com')
    except:
        print('error in fill form')

bookingAppoinment()

def booking_appoinment_2():
    driver.refresh()
    time.sleep(1)
    driver.switch_to.default_content()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID, "BODY_WIN"))
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="CONTENU_WIN"]'))
    time.sleep(1)
    driver.find_element(By.ID, 'boutonSuivant_link').click()
    time.sleep(5)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except UnexpectedAlertPresentException:
        alert = driver.switch_to.alert
        alert.accept()
        print('no alert')

#refreshing the page
def recursion():
    print('enterin recursion')
    booking_appoinment_2()
    time.sleep(5)
    print('Booking appoinment')
    fill_form()
    time.sleep(5)
    recursion()

recursion()

