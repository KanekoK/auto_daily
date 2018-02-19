from config import USER, PASSWORD, URL
from templete import daily_text

import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get(URL)




# ======= ログイン画面　======== #
driver.find_element_by_id("txtName").send_keys(USER)
driver.find_element_by_id("txtPass").send_keys(PASSWORD)
driver.find_element_by_xpath('//*[@id="loginBox"]/form/div/p[2]/input').click()




# ======= ダッシュボード　======== #
add = driver.find_element_by_css_selector('#navi .navi_off a[href="/blogs/blog_list.php?"]')
Hover = ActionChains(driver).move_to_element(add)
Hover.perform()
driver.find_element_by_xpath('//*[@id="navi"]/li[6]/ul/li[1]/a').click()


# ======= ブログ ======== #
today = datetime.datetime.today().strftime('%m%d')
driver.find_element_by_xpath('//*[@id="regist_form_content"]/dl/dd[1]/input').send_keys("日報"+today)

driver.find_element_by_id("regist_form_comment").send_keys(daily_text)
