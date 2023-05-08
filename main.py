from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

username = input("Please enter your username: ")
password = input("Please enter your password: ")

service = Service(executable_path="../chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
driver = webdriver.Chrome(executable_path="../chromedriver.exe", chrome_options=chrome_options)

driver.get("https://myportal.lau.edu.lb/")

driver.find_element("name", "username").send_keys(username)  
driver.find_element("name", "password").send_keys(password)
driver.find_element("xpath", "//input[@type='submit' and @value='Log In']").send_keys(Keys.ENTER)

driver.find_element("xpath", '//a[@class="static menu-item" and @href="/sites/courses"]').send_keys(Keys.ENTER)
driver.find_element("xpath", '//a[@href="https://banweb.lau.edu.lb/prod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu"]').send_keys(Keys.ENTER)

handles = driver.window_handles
new_window_handle = handles[-1]
driver.switch_to.window(new_window_handle)
driver.find_element("xpath", '//a[contains(text(), "Look-up Classes to Add")]').send_keys(Keys.ENTER)

select_element = driver.find_element("id", "term_input_id")

select = Select(select_element)

select.select_by_value("202410")

driver.find_element("xpath", "//input[@type='submit' and @value='Submit']").send_keys(Keys.ENTER)

driver.find_element("xpath", "//input[@type='submit' and @value='Advanced Search']").send_keys(Keys.ENTER)

subject_element = driver.find_element("id", "subj_id")

subject = Select(subject_element)

subject.select_by_value("CSC")

campus_element = driver.find_element("id", "camp_id")

campus = Select(campus_element)

campus.select_by_value("2")

driver.find_element("xpath", "//input[@type='submit' and @value='Section Search']").send_keys(Keys.ENTER)



