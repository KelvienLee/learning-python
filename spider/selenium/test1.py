from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
# 无头模式
option.add_argument('headless')
# 沙盒模式运行
option.add_argument('no-sandbox')
# 大量渲染时候写入/tmp而非/dev/shm
option.add_argument('disable-dev-shm-usage')
# 指定驱动路径
driver = webdriver.Chrome('/usr/bin/chromedriver',options=option)
# 访问百度
driver.get('https://ankiweb.net/account/login')

username = driver.find_element_by_id('email')
password = driver.find_element_by_id('password')

username.send_keys('1154296130@qq.com')
password.send_keys('WGX9.anki')

driver.find_element_by_xpath('//div[@class="form-group"]/input').click()
print(driver.title)

sleep(2)
driver.find_element_by_xpath('//button[@data-full="test"]').click()
print(driver.title)

driver.quit()