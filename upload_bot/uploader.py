import random
import time
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import upload_bot.constants as constants
from captcha_solver import audio_captcha_solver

DEFAULT_SLEEP = 2

def login(browser, email, password):
    browser.get(constants.LOGIN_PAGE_LINK)
    input = browser.find(By.NAME, constants.USERNAME_INPUT)
    for ch in email:
        time.sleep(random.uniform(0.1, 0.4))
        input.send_keys(ch)
    input = browser.find(By.CSS_SELECTOR, constants.PASSWORD_INPUT)
    for ch in password:
        time.sleep(random.uniform(0.1, 0.4))
        input.send_keys(ch)
    browser.find(By.CSS_SELECTOR, constants.LOGIN_BTN).click()

def is_logged_in(browser):
    try:
        browser.find(By.ID, constants.VERIFY_LOGIN_TEXT)
        return False
    except:
        return True


def upload(browser, video_path):
    browser.get("https://www.tiktok.com/tiktokstudio/upload")
    time.sleep(DEFAULT_SLEEP)

    if not is_logged_in(browser):
        login(constants.EMAIL, constants.PASSWORD)
        if audio_captcha_solver.available_captcha(browser):
             time.sleep(DEFAULT_SLEEP)
             audio_captcha_solver.solve_captcha(browser)
             time.sleep(DEFAULT_SLEEP)

    time.sleep(DEFAULT_SLEEP)

    #inputs video path into browser
    browser.find(By.XPATH, constants.VIDEO_INPUT_PATH).send_keys(video_path)
    time.sleep(DEFAULT_SLEEP)

    description_field = browser.find(By.XPATH, constants.DESCRIPTION_INPUT_FIELD)
    description_field.send_keys(Keys.CONTROL + 'a')
    description_field.send_keys(constants.DESCRIPTION)

    #it finds and clicks the upload button
    browser.find(By.XPATH, constants.POST_BTN).click()
