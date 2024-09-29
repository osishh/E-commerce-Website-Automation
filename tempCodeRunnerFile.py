final_price=driver.find_element("xpath",'//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)