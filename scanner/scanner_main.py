import random
from sympy.printing.tree import print_node
from bs4 import BeautifulSoup
import scanner.constants as constants
import human_mouse

MAX_FILTERS = 100
filters = []
DEFAULT_SLEEP = [2,4,2.3,1.5,4,3.2]

def append_filters(filters):
    if len(filters) == MAX_FILTERS:
        __clear_old_filters(filters)
    with open(constants.FILTERS_DIR, 'a') as file:
        file.writelines(filters)

def __clear_old_filters(filters):
    if len(filters) == MAX_FILTERS:
        filters.pop(50)
    with open(constants.FILTERS_DIR, 'w') as file:
        file.writelines(filters)
        file.truncate()

def __load_filters():
    with open(constants.FILTERS_DIR, 'r') as file:
        return file.readlines()

def save_links_for_download(urls):
    with open("tiktok_manager/for_download.txt", 'a') as file:
        file.writelines(urls)

def __find_not_pined_posts(url, driver):
    url_list = []
    driver.uc_activate_cdp_mode(url)
    driver.sleep(random.choice(DEFAULT_SLEEP))
    source = driver.get_page_source()

    html_parse = BeautifulSoup(source, 'html.parser')
    all_posts = html_parse.find_all(class_="css-1j167yi-DivWrapper e1cg0wnj1") #classes are diffrent on every browser or computer(not sure)
    for post in all_posts:
        if post.find(attrs={"data-e2e": "video-card-badge"}) is None:
            url_list.append(post.find("a").get('href') + '\n')
    return url_list

def scan_page_and_download(url, driver):
    urls = __find_not_pined_posts(url, driver)
    print(driver.get_current_url() + '\n')
    if urls[0].strip() not in filters:
        filters.append(urls[0].strip())
        return urls[0]
    print("FILTERS:")
    print(filters)
    return None

if __name__ == '__main__':
    filters = __load_filters()