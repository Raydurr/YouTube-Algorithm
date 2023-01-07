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

#Date(DONT USE '/')
date = '01-04-2023'
version = 'v1'
#Create Ublock Extension
chrome_options = ChromeOptions() 
chrome_options.add_extension(r"C:\Users\Raymond\OneDrive\Documents\Selenium Stuff\Ublock.crx")
#Driver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH, options = chrome_options)
driver.get('https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&ifkv=AeAAQh6XAOr5EDoVDF9Iks6MhwzwlCJlhYM2qvC2ppQ4tTq_muU3qD2wBVfNZVRJhGF74PlTynFtAw&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.get('https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&ifkv=AeAAQh6XAOr5EDoVDF9Iks6MhwzwlCJlhYM2qvC2ppQ4tTq_muU3qD2wBVfNZVRJhGF74PlTynFtAw&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#Elements
username_box = '//*[@id="identifierId"]'
password_box = '//*[@id="password"]/div[1]/div/div[1]/input'
Show_more = '//*[@id="expand"]'
#Time Tracking Variables
run_for = 60*60 #How long program should run for(in seconds)
ran_for = 0 #How long the program has run(in seconds)
max_dur = 15*60 #sets max duration of video(in seconds)
wait = WebDriverWait(driver, 10)
#Create dataframe
Scraped_Data = pd.DataFrame([], columns= ['Title', 'Channel', 'Views', 'Likes', 'Duration', "Number of Comments", "Liked?"])
#Create skip action chain
skip_action = ActionChains(driver)
skip_action.send_keys(Keys.SHIFT)
skip_action.send_keys('N')
#Create pause/unpause action chain(to show duration)
action = ActionChains(driver)
action.send_keys(Keys.SPACE)
action.send_keys(Keys.SPACE)


#signs in 
def sign_in(input):
    if input == "C":
        driver.find_element_by_xpath(username_box).send_keys("nickneut22@gmail.com")
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        password = WebDriverWait(driver, 600).until(EC.element_to_be_clickable((By.XPATH, password_box)))
        password.send_keys('Npg53qKl2t')
        driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

    elif input == "R":
        driver.find_element_by_xpath(username_box).send_keys("catconserve@gmail.com")
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        password = WebDriverWait(driver, 600).until(EC.element_to_be_clickable((By.XPATH, password_box)))
        password.send_keys('cT47&^3#RtpQ')
        driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

    elif input == "L":
        driver.find_element_by_xpath(username_box).send_keys("leftwardlila67@gmail.com")
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        password = WebDriverWait(driver, 600).until(EC.element_to_be_clickable((By.XPATH, password_box)))
        password.send_keys('56tdjeo@$%g')
        driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()



def subscribed():
    if driver.find_element_by_xpath('//*[@id="notification-preference-button"]/ytd-subscription-notification-toggle-button-renderer-next/yt-button-shape/button/div[2]/span').text  == 'Subscribed':
        return True
    else:
        return False


def like_video_com(subscribed, likes, comments, views):
    driver.execute_script("arguments[0].scrollIntoView();",top_title)
    if subscribed and ((likes + comments + (2 * views / 5)) / views) >= .35:
        Like = driver.find_element_by_xpath('//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button')
        Like.click()
    elif ((likes + comments + (2 * views / 5)) / views) >= .50:
        Like = driver.find_element_by_xpath('//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button')
        Like.click()
    else:
        return False
    return True
    
def like_video_nocom(subscribed, likes, views):  
    driver.execute_script("arguments[0].scrollIntoView();",top_title)
    if subscribed and ((likes + (2 * views / 5)) / views) >= .30:
        Like = driver.find_element_by_xpath('//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button')
        Like.click()
    elif ((likes + (2 * views / 5)) / views) >= .4:
        Like = driver.find_element_by_xpath('//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button')
        Like.click()
    else:
        return False
    return True

#convert youtube duration into seconds
def duration_convert(duration): 
    #splits duration at : to get how many variables
    splited = duration.split(":")
    list_len = len(splited)
    if list_len == 1: #video is less than a minute
       sec = splited[0] 
    elif list_len == 2: # video is less than an hour over a minute
        sec = (int(splited[0])*60) + int(splited[1])
    elif list_len == 3: #video is more than an hour
        sec = (int(splited[0])*3600) + (int(splited[1])*60) + (int(splited[2]))
    else:
        sec = 0
    return sec

#convert likes into int
def likes_convert(likes):
    if "K" in likes:
        splitted = likes.split("K")
        likes_real = float(splitted[0]) * 1000
    elif "M" in likes:
        splitted = likes.split("M")
        likes_real = float(splitted[0]) *1000000
    else:
        likes_real = float(likes)
    return likes_real

#gets data
def scrape_data():
    global ran_for
    global Scraped_Data
    time.sleep(3)
    #get title
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/h1/yt-formatted-string'))
        ).text
    print("Title of Video: " + title)
    # get duration
    action.perform()
    duration = wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, 'ytp-time-duration'))
             ).text
    print('Duration: ' + duration)
    if duration == '': #Skip Live
        skip_action.perform()
        return
    #Get Views
    wait.until(EC.element_to_be_clickable((By.XPATH, Show_more))).click() #clicks show more
    try:
        Views = driver.find_element_by_xpath('//*[@id="info"]/span[1]').text
    except: #skip movies 
        skip_action.perform()
        return
    Views = Views.split(' ')
    if ',' in Views[0]:
        Views = int(Views[0].replace(',', ''))
    else:
        Views[0] = int(Views[0])
    print('Views: ' + str(Views))
    #Get Channel 
    channel = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="text"]/a'))
        ).text
    print("Channel: " + channel)
    #Get Likes
    try:
        Likes = driver.find_element_by_xpath('//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/div[2]/span').text
        if Likes == '':
            skip_action.perform()
    except: #skip undesirables 
        skip_action.perform()
        return
    Likes = likes_convert(Likes)
    print('Likes: ' + str(Likes))
    #Subscribed?
    sub = subscribed()
    #Get Number of Comments
    driver.execute_script("arguments[0].scrollIntoView();",comment_section)
    try:
        Comments = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]'))
    ).text
        if ',' in Comments:
            Comments = int(Comments.replace(',', ''))
        else:
            Comments = int(Comments)
    except: 
        Comments = 'No comments'
    print('Comments: ' + str(Comments))
    #convert duration to seconds
    sec_dur = duration_convert(duration)
    #modify max video watch time 
    if Comments != 'No comments' and Comments != '':
        mod_dur = max_dur * ( (Likes + Comments + (2 * Views) / 5) / Views)
        Liked = like_video_com(sub, Likes, Comments, Views) 
    else: 
        mod_dur = max_dur * ((Likes +(2 * Views) / 5) / Views)
        Liked = like_video_nocom(sub, Likes, Views) 
    #check if video is too long/short enough
    if sec_dur <= mod_dur:
        time.sleep(sec_dur)
        ran_for = ran_for + sec_dur #modifies how long its ran for
        skip_action.perform()
    else: 
        time.sleep(mod_dur)
        ran_for = ran_for + mod_dur #modifies how long its ran for
        skip_action.perform()
    #Edit DataFrame
    Scraped_Data.loc[len(Scraped_Data)]= [title, channel, Views, Likes, duration, Comments, Liked]

def first_vid_select():
    input1 = input("Ready? Press Enter ")
    home_videos = driver.find_elements_by_id('video-title-link')
    X = np.random.randint(0, len(home_videos) - 1)
    return home_videos[X].get_attribute('href')

input1 = input("Press C for centrist, R for Rightwing, and L for Leftwing: ")
sign_in(input1)

url = first_vid_select()
driver.get(url)
#get elements for future use
comment_section = wait.until(EC.presence_of_element_located((
    By.XPATH,'//*[@id="comments"]'))
)
top_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/h1/yt-formatted-string')))

while run_for > ran_for:
   scrape_data()
   Scraped_Data.to_csv(r'C:\Users\Raymond\OneDrive\Desktop\YouTube Stuff\YouTube R Stuff\Scraped Data-' + date + input1 + version  + '.csv' )
print("Program Ended")
driver.quit()