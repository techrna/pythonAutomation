from selenium import webdriver
driver =webdriver.Chrome("C:\Program Files (x86)\Google\Chrome Beta\Application\chromedriver")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
msgf=driver.find_element_by_xpath('//*[@id="user-message"]')
msgf.send_keys("Hello Rushab")
simButton=driver.find_element_by_xpath('//*[@id="get-input"]/button')
simButton.click()


val1=driver.find_element_by_xpath('//*[@id="sum1"]')
val1.send_keys("3")
val2=driver.find_element_by_xpath('//*[@id="sum2"]')
val2.send_keys("3")
simButton=driver.find_element_by_xpath('//*[@id="gettotal"]/button')
simButton.click()
