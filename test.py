from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome('modules/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
user_id='s37687344'
driver.get('https://map.naver.com/?query=%EB%B4%89%EC%B2%9C%EB%8F%99%EC%BB%B4%ED%93%A8%ED%84%B0%EC%88%98%EB%A6%AC&type=SITE_1&queryRank=0')
elements  = driver.find_element_by_class_name('lst_site')
elem = elements.find_element_by_css_selector("li[data-id='"+user_id+"']")
images= driver.find_element_by_xpath('//li[@data-id="'+user_id+'"]/div[@class="lsnx"]/div[contains(@class, "pin")]/img')
print ('finding')
images.click()
print('wait')
time.sleep(5)
print('end')
driver.quit()
