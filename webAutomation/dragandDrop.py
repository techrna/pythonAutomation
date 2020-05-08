from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver =webdriver.Chrome("C:\Program Files (x86)\Google\Chrome Beta\Application\chromedriver")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

src=driver.find_element_by_xpath('//*[@id="box7"]')
dst=driver.find_element_by_xpath('//*[@id="box105"]')
action=ActionChains(driver)

action.drag_and_drop(src,dst).perform()