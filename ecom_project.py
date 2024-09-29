import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

#initialize webdriver
driver=webdriver.Edge()

#Open URL and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

#phones button
phones=driver.find_element("xpath",'//a[text()="Phones & PDAs"]')
phones.click()


#iphone
iphone=driver.find_element("xpath",'//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

#first picture
first_pic=driver.find_element("xpath",'//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

#next picture
next_click=driver.find_element("xpath",'//button[@title="Next (Right arrow key)"]')

for i in range(0,5):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

#close
x_button=driver.find_element("xpath",'//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)

#quantity
quantity=driver.find_element(By.ID, "input-quantity")
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

#add to cart
add_to_button=driver.find_element(By.ID, 'button-cart')
add_to_button.click()
time.sleep(2)



#Checkout
go_to_cart=driver.find_element(By.ID,'cart-total')
go_to_cart.click()
time.sleep(1)

checkout=driver.find_element("xpath",'//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

#click on guest account
guest=driver.find_element("xpath",'//input[@value="guest"]')
guest.click()

#click continue 1
continue_1=driver.find_element(By.ID, 'button-account')
continue_1.click()
time.sleep(1)

#scrolling
step_2=driver.find_element("xpath",'//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#first name
first_name=driver.find_element(By.ID, 'input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_first_name')
time.sleep(1)

#last_name
last_name=driver.find_element(By.ID, 'input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test_last_name')
time.sleep(1)

#email
email=driver.find_element(By.ID, 'input-payment-email')
email.click()
time.sleep(1)
email.send_keys('test@test.com')
time.sleep(1)

#telephone
telephone=driver.find_element(By.ID, 'input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)

#address
address=driver.find_element(By.ID, 'input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)

#city
city=driver.find_element(By.ID, 'input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Frankfurt')
time.sleep(1)

#postcode
postcode=driver.find_element(By.ID, 'input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


#country
country=driver.find_element(By.ID, 'input-payment-country')
dropdown_1=Select(country)
time.sleep(1)
dropdown_1.select_by_index(87)
time.sleep(1)

#region
region=driver.find_element(By.ID, 'input-payment-zone')
dropdown_2=Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Hessen')
time.sleep(1)

#click continue 2
continue_2=driver.find_element("xpath",'//input[@id="button-guest"]')
continue_2.click()
time.sleep(1)

#click continue 3
continue_3=driver.find_element("xpath",'//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(1)

#accept terms & conditions
t_e=driver.find_element("xpath",'//input[@name="agree"]')
t_e.click()
time.sleep(1)

#click continue 4
continue_4=driver.find_element("xpath",'//input[@id="button-payment-method"]')
continue_4.click()
time.sleep(3)

#final price
final_price=driver.find_element("xpath",'//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)
time.sleep(2)

#click on the confirmation button
confirmation_button=driver.find_element(By.ID, 'button-confirm')
confirmation_button.click()
time.sleep(2)


#success text
success_text=driver.find_element("xpath",'//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

driver.close()















