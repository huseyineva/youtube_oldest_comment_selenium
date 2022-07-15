from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


url = input("En eski yorumu bulmak istediğiniz videonun url'sini buraya yapıştırınız: ")
driver = webdriver.Edge()
driver.get(url)

driver.maximize_window()
time.sleep(3)

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(3)

siralama = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/span/yt-sort-filter-sub-menu-renderer/yt-dropdown-menu/tp-yt-paper-menu-button/div/tp-yt-paper-button/div")
siralama.click()
time.sleep(3)

en_yeni = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/span/yt-sort-filter-sub-menu-renderer/yt-dropdown-menu/tp-yt-paper-menu-button/tp-yt-iron-dropdown/div/div/tp-yt-paper-listbox/a[2]/tp-yt-paper-item/tp-yt-paper-item-body/div[1]")
en_yeni.click()
time.sleep(3)

while True:
    scroll_height = 2000
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(1.5)
    document_height_after = driver.execute_script("return document.documentElement.scrollHeight")
    if document_height_after == document_height_before:
        break

time.sleep(1.5)

comments = driver.find_elements(By.ID, 'content-text')

allc = []
for comment in comments:
    allc.append(comment.text)

print("ARATTIĞINIZ VİDEONUN EN ESKİ YORUMU")
print("-----------------------------------")
print(allc[-1])
print("-----------------------------------")
driver.close()


