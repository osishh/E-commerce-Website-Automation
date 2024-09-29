from selenium import webdriver
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Edge()

# Open amazon
driver.get("https://www.amazon.com/")
time.sleep(4)


# Maximize the browser window
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Locate and click on the Login button
login_button = driver.find_element(By.ID,'nav-link-accountList-nav-line-1')
login_button.click()

# Wait for the login modal to appear
time.sleep(2)

#enter the phone no.
phone_no = driver.find_element(by=By.NAME,value="email")
number="9902581195"
phone_no.send_keys(number)
time.sleep(2)
#continue click

cont=driver.find_element(By.ID,'continue')
cont.click()
time.sleep(2)



#password
pas=driver.find_element(By.ID,'ap_password')
pas.click()
pa="osishbanthaamazon%%"
pas.send_keys(pa)

sig=driver.find_element(By.ID,'signInSubmit')
sig.click()
time.sleep(2)


#search
search=driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys("xiaomi redmi note 13 pro")
time.sleep(3)
se=driver.find_element(By.ID,'nav-search-submit-button')
se.click()
time.sleep(2)

#select item to add to cart
select=driver.find_element(By.ID,'a-autoid-1-announce')
select.click()
time.sleep(2)

#view cart
view=driver.find_element(By.ID,'nav-cart-count-container')
view.click()
time.sleep(2)
print(" \n")
print(" \n")
print(" \n")
print(" \n")

print('you have been successfully signout from amazon.com!!!!')




#account
account=driver.find_element("xpath",'nav-link-accountList')
account.click()
time.sleep(2)
#logout
logout=driver.find_element(By.ID,'nav-item-signout')
logout.click()

time.sleep(2)



# Close the browser
driver.close()

