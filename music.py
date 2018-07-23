from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#url
url = 'https://music.163.com/#/discover/toplist'
#选择浏览器,设置无头模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
#访问网易云音乐
browser.get(url)
#找到子页面
iframe = browser.find_element_by_id('g_iframe')
#进入子页面
browser.switch_to.frame(iframe)

#设置显示等待 直到按钮可以被点击,
wait = WebDriverWait(browser, 10)
def bofang():
    #设置显示等待 直到按钮可以被点击,
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btns a')))
    #获得播放按钮
    button_bofang = browser.find_element_by_css_selector('.btns a')
    button_bofang.click()

temp = input('是否播放音乐：(y/n)')
if temp == 'y':
    bofang()
else:
    browser.close()
