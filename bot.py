from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


url = "https://www.youtube.com/watch?v=tWG-h0bqdws"  # url of video
views = 5  # amount of views


for i in range(views):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located

    driver.get(url)

    # play the video
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    sleep(60)
    driver.quit()
