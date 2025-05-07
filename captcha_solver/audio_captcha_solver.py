import time
import requests
import  whisper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import captcha_solver.constants as constants

DEFAULT_SLEEP = 2

model = whisper.load_model("small")

def __speech_to_text():
    result = model.transcribe(constants.CAPTCHA_PATH, fp16=False) #MUST HAVE FFMPEG installed!!!
    return  result["text"].replace(" ","")

def __audio_downloader(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(constants.CAPTCHA_PATH, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print("Download complete:", constants.CAPTCHA_PATH)
    else:
        print("Failed to download MP3 file")

def available_captcha(browser):
    try:
        browser.find(By.ID, constants.CAPTCHA_CONTAINER)
        return True
    except:
        return False

def solve_captcha(browser):
    browser.find(By.ID, constants.CAPTCHA_AUDIO_BTN).click()
    time.sleep(DEFAULT_SLEEP)

    for i in range(1,10):
        audio_link = browser.find(By.TAG_NAME, "audio").get_attribute("src")
        __audio_downloader(audio_link)
        time.sleep(DEFAULT_SLEEP)
        captcha_text = __speech_to_text()
        print(captcha_text)
        browser.find(By.ID, constants.CAPTCHA_INPUT).send_keys(captcha_text)
        time.sleep(DEFAULT_SLEEP)
        browser.find(By.XPATH, constants.CAPTCHA_VERIFY_BTN).click()
        time.sleep(DEFAULT_SLEEP*3)
        if not available_captcha(browser):
            print("captcha_solved!")
            break
