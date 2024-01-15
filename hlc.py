from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import random

hashtag = 'funnyvideo' #replace instagram with your hashtag

commentsDict = ['good','amazing one','keep going','excellent','next video please','follow your page','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #Add or replace words...

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)
driver.find_element_by_name('username').send_keys('instaa') #replace with your insta username
sleep(1)
driver.find_element_by_name('password').send_keys('insta@123$%') #replace with your insta password
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(6)
driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') #hashtag
sleep(8)
driver.find_element_by_class_name("_aagw").click() #click on first post 
sleep(3)
element = driver.find_element_by_class_name("_aamw") # click on the like button
element.click()  
sleep(3)
driver.find_element(By.XPATH,'//*[@class ="_akhn"]//textarea').click() #click on comment section area
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_akhn"]//textarea').send_keys(random.choice(commentsDict)) #send the text in comment section
sleep(1)
driver.execute_script('document.querySelector("body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aaoe._ae5y._ae5z._ae62 > div > form > div > div._am-5 > div").click()') #click the cmt post button
sleep(1)
#click on next post button
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_RIGHT)
actions.perform()
sleep(4)

while True:
    try:
        # Find and click the like button
        element = driver.find_element_by_class_name("_aamw")
        element.click()
        
        sleep(1)

        # Find and click the comment text area
        comment_textarea = driver.find_element(By.XPATH, '//*[@class ="_akhn"]//textarea')
        comment_textarea.click()
        
        sleep(1)
        
        # Type a comment
        comment_text = driver.find_element(By.XPATH, '//*[@class ="_akhn"]//textarea')
        comment_text.send_keys(random.choice(commentsDict))

        sleep(1)
        
        # send a comment...
        driver.execute_script('document.querySelector("body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > section._aaoe._ae5y._ae5z._ae62 > div > form > div > div._am-5 > div").click()') #click the cmt post button
        sleep(1)
        # click on next post button
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform() 

    except Exception as e:
        print("An error occurred:", e)
        break  

        
