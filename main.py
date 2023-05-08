from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

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
