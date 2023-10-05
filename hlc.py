from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import ActionChains
import random

hashtag = 'instagram' #replace with your hashtag

commentsDict = ['good','amazing one','keep going','excellent','next video please','follow your page','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #Add or replace words...

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)
driver.find_element_by_name('username').send_keys('instagram') #replace with your insta username
sleep(1)
driver.find_element_by_name('password').send_keys('insta_123@#$%') #replace with your insta password
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(6)
driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') #hashtag
sleep(8)
post_click=driver.find_element_by_class_name("_aagw").click() #click on first post 
sleep(3)
like=driver.find_element_by_class_name("_aamw").click() #click on like button
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_akhn"]//textarea').click() #click on comment section area
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_akhn"]//textarea').send_keys(random.choice(commentsDict)) #send the text in comment section
sleep(1)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]').click() #click on post button of comment
sleep(3)
next_button=driver.find_element_by_class_name("_abl-").click() #next button
sleep(4)

while True:
    try:
        # Find and click the like button
        driver.find_element_by_class_name("_aamw").click()
        
        sleep(1)

        # Find and click the comment text area
        comment_textarea = driver.find_element(By.XPATH, '//*[@class ="_akhn"]//textarea')
        comment_textarea.click()
        
        sleep(1)
        
        # Type a comment
        comment_text = driver.find_element(By.XPATH, '//*[@class ="_akhn"]//textarea')
        comment_text.send_keys(random.choice(commentsDict))

        sleep(1)
        
        # Post the comment
        post_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]')
        post_button.click()
        
        sleep(1)

        # Click the next post button
        next_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]')
        next_button.click()

        sleep(3)  

    except Exception as e:
        print("An error occurred:", e)
        break  
