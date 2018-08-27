# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# setting options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('--headless')
default_width = 600
default_height = 800
user_agent = 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MI 6X Build/OPM1.171019.011) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36'
options.add_argument("user-agent=%s"%user_agent)

chrome_path = r'../chromedriver.exe'
driver = webdriver.Chrome(chrome_path, chrome_options=options)  # setup chrome
# driver.maximize_window()
driver.set_window_size(default_width, default_height)
driver.implicitly_wait(10)
driver.get("https://s4.uczzd.cn/webapp/webview/article/news.html?app=uc-iflow&aid=11348296367183493272&cid=100&zzd_from=uc-iflow&uc_param_str=dndseiwifrvesvntgipf&rd_type=share&pagetype=share&btifl=100&sdkdeep=2&sdksid=7512f270-4bb6-7571-cf5a-ae2480de1f24&sdkoriginal=7512f270-4bb6-7571-cf5a-ae2480de1f24")
try:
    myElem = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'ucCommentContent')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
time.sleep(1)
height = driver.execute_script("return document.body.parentNode.scrollHeight")
print(height)
driver.set_window_size(default_width, height)
height = driver.execute_script("return document.body.parentNode.scrollHeight")
driver.set_window_size(default_width, height)
print(height)
time.sleep(0.3)


# element=driver.find_elements_by_xpath("/html/child::*/child::*")
# eheight=set()
# for e in element:
#     eheight.add(round(e.size["height"]))
# print (eheight)
# total_height = sum(eheight)
# driver.execute_script("document.getElementsByTagName('html')[0].setAttribute('style', 'height:"+str(total_height)+"px')")
# element=driver.find_element_by_tag_name('body')
# element_png = element.screenshot_as_png

driver.get_screenshot_as_file("./result/test.png")
driver.quit()
