from exceptiongroup import catch
from scanner import scanner_main
from browser_gen import browser_gen
import constants
from scanner import scanner_main

URLS = []
with open(r"C:\Users\cecoM\Desktop\to_scan_tiktok.txt", 'r') as file:
    URLS = file.readlines()


urls_for_download = []

driver = browser_gen.get_uc_sesh()
for url in URLS:
    try:
        url = scanner_main.scan_page_and_download(url,driver)
        if url is not None:
            urls_for_download.append(url)
    except Exception as e:
        for index in range(3):
            try:
                print("Detected on url:" + url + "generating new session and retrying.")
                driver.quit()
                driver = browser_gen.get_uc_sesh()
                url = scanner_main.scan_page_and_download(url, driver)
                if url is not None:
                    urls_for_download.append(url)
                break
            except Exception as ex:
                print(f"Detected again, retrying, attempt:{index}")
    finally:
        driver.quit()
print(urls_for_download)
scanner_main.append_filters(scanner_main.filters)
if urls_for_download is not []:
    scanner_main.save_links_for_download(urls_for_download)
