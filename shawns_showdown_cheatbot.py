from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

#opens webpage
driver = webdriver.Chrome(service=ChromeService())
url = 'https://shootem-up-showdown-e624ee86eac8.herokuapp.com/'
driver.get(url)
driver.maximize_window()

#clicks login button
login = driver.find_element("xpath","//a[@href]")
login.click()

#login info
username = driver.find_element(By.NAME,"username")
username.send_keys("GetBotThor")
password = driver.find_element(By.NAME,"password")
password.send_keys("GetBotThor123")
submit = driver.find_element(By.XPATH,"//button[@type]")
submit.click()

#clicks play game
time.sleep(2)
play_game = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/a[1]")
play_game.click()

#game
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[2]/button').click() #mute button
level = 0
while level < 5:

    level += 1
    grid = driver.find_element(By.CLASS_NAME,"grid")
    enemy = grid.find_elements(By.CLASS_NAME,"enemy")   
    reload = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[2]/button')
    
    for spot in enemy:
       
        reload.send_keys("r")
        spot.click()

#score
score = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/main/div/h5[2]/span')
print("\nScore is " + score.text)

time.sleep(120)