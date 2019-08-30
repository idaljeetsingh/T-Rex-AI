"""
    Title: T-Rex AI
    File Name: game_control.py
    Author: Daljeet Singh Chhabra
    Language: Python
    Date Created: 22-05-2019
    Date Modified: 22-05-2019
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

status = 0
driver = None


def control(k):
    global status
    global driver

    if status is 0 and k is 1:
        status = 1
        print("Launching Game!!!")
        driver = webdriver.Chrome()
        driver.get('chrome://dino')
        body = driver.find_element_by_id("t")
        body.send_keys(Keys.SPACE)
    if status is 1:
        if k == 5:
            body = driver.find_element_by_id("t")
            body.send_keys(Keys.SPACE)
            # if input() == 'q':
            #     break
            # continue
