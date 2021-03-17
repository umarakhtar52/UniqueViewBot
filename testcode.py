from selenium import webdriver
import time

counter = 0
while counter < 5:

    driver = webdriver.Chrome('/Users/umarakhtar/Desktop/chromedriver')
    driver.get("https://www.google.com")
    time.sleep(5)

    driver.quit()
    counter = counter + 1
else:
    print("Finished")