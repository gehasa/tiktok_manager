from seleniumbase import Driver
import atexit
import random

AGENTS = []
with open(r"C:\Users\cecoM\Desktop\code\Python\browser_gen\agents.txt", 'r') as file:
    AGENTS = file.readlines()

PROXIES = []
with open(r"C:\Users\cecoM\Desktop\code\Python\browser_gen\proxies.txt", 'r') as file:
    PROXIES = file.readlines()

def get_uc_sesh():
    proxy = f"{random.choice(PROXIES).strip()}"
    agent = f"{random.choice(AGENTS).strip()}"
    print(proxy)
    print(agent)
    driver = Driver(uc=True, proxy=proxy, incognito=True, agent=agent)
    atexit.register(driver.quit)
    return driver
