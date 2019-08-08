from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep 

import pickle
import time
import datetime
from random import randint
usr ="[User]"
pwd = "[Password]"
browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
try: 
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
except Exception:
    pass

browser.get('https://auth.nextmag.com.tw/web/v7/apps/5c175dd2fa20ae00181c03dc/redirect/facebook?loginOnly=true')


username_box = browser.find_element_by_id('email') 
username_box.send_keys(usr) 

password_box = browser.find_element_by_id('pass') 
password_box.send_keys(pwd) 
login_box = browser.find_element_by_id('loginbutton') 
login_box.click() 

# Save Login cookies
pickle.dump( browser.get_cookies() , open("cookies.pkl","wb"))

sleep(15)
browser.get('https://feature.nextmag.com.tw/service2019/vote')
sleep(5)
# radio Q1 5=國泰世華
browser.find_element_by_xpath('//input[@value="5"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q2 13=南山人壽
browser.find_element_by_xpath('//input[@value="13"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

#input('Press anything to quit') 

# radio Q3 28=東森房屋
browser.find_element_by_xpath('//input[@value="28"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q4 43=和泰汽車                            
browser.find_element_by_xpath('//input[@value="43"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q5 54=中華航空
browser.find_element_by_xpath('//input[@value="54"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q6 71=AsiaYo
browser.find_element_by_xpath('//input[@value="71"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q7 79=華泰名品城
browser.find_element_by_xpath('//input[@value="79"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q8 97=承億文旅集團                            
browser.find_element_by_xpath('//input[@value="97"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q9 108=康是美藥妝店                            
browser.find_element_by_xpath('//input[@value="108"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q10 112=全家便利商店                            
browser.find_element_by_xpath('//input[@value="112"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q11 121=路易莎咖啡                            
browser.find_element_by_xpath('//input[@value="121"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q12 128=漢堡王                            
browser.find_element_by_xpath('//input[@value="128"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q13 140=H&M
browser.find_element_by_xpath('//input[@value="140"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q14 156=全聯福利中心
browser.find_element_by_xpath('//input[@value="156"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q15 162=亞太電信
browser.find_element_by_xpath('//input[@value="162"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q16 174=ET Mall東森購物網                            
browser.find_element_by_xpath('//input[@value="174"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q17 184=六福村主題遊樂園                            
browser.find_element_by_xpath('//input[@value="184"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

# radio Q18 189=秀泰影城                            
browser.find_element_by_xpath('//input[@value="189"]').send_keys(Keys.SPACE)  # send space
submit_button = browser.find_element_by_class_name("btn-lg")
submit_button.click()

browser.quit() 
