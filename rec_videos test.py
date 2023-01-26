from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import numpy as np
import pandas as pd
import time
chrome_options = ChromeOptions()
chrome_options.add_extension(r"./Selenium Stuff/Ublock.crx")
#Driver
PATH = './Selenium Stuff/chromedriver.exe'#'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH, options = chrome_options)


driver.get('https://www.youtube.com/watch?v=zVlJrE0mBno')
driver.get('https://www.youtube.com/watch?v=zVlJrE0mBno')
def get_rec_vids():
    comment_section = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="comments"]')))
    driver.execute_script("arguments[0].scrollIntoView();",comment_section)
    time.sleep(5)
    video_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    return video_elements


vid_ELEMENTS = get_rec_vids()
print(vid_ELEMENTS)
vid_titles = []
for video in vid_ELEMENTS:
    title = video.text
    vid_titles.append(title)
print(vid_titles)

test= driver.find_elements_by_xpath('//*[@id="interaction"]')[1]
driver.execute_script("arguments[0].scrollIntoView();",test)
WebDriverWait(test, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="interaction"]'))).click()
# 
# time.sleep(5)
# test.click()
print(len(vid_titles))