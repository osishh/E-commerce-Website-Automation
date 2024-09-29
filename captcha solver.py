from selenium import webdriver
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Initialize the WebDriver
driver = webdriver.Edge()

# Open amazon
driver.get("https://www.amazon.com/errors/validateCaptcha")
time.sleep(4)
link=driver.find_element(By.XPATH,"//div[@class = 'a-row a-text-center']//img").get_attribute('src')

print(link)
captcha=AmazonCaptcha.fromlink(link)
captcha_value=AmazonCaptcha.solve(captcha)

print(captcha_value)
input_value=driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)


button=driver.find_element(By.CLASS_NAME,'a-button-text')
button.click()
print("captcha printed")
# Wait for the page to load
time.sleep(2)