from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://rehtsira.github.io')

elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/a[3]")

elem.click()

elem2 = driver.find_element_by_xpath("/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[2]/div/div/div/a/span")

elem2.click()

elem3 = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/signup-prompt/div/div/a")

elem3.click()

elem4 = driver.find_element_by_id("user_login")

elem4.send_keys('your_user')

elem5 = driver.find_element_by_id("user_email")

elem5.send_keys('your_mail.com')


