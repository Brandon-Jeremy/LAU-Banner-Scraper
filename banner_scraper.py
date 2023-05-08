import csv
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

username = sys.argv[1]
password = sys.argv[2]

driver = webdriver.Chrome()

# Navigate to the LAU portal login page
driver.get("https://banweb.lau.edu.lb/")

# Enter the username and password in the input fields and submit the form
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys(username)
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

driver.get("https://banweb.lau.edu.lb/prod/bwskfcls.p_sel_crse_search")

dropdown = driver.find_element(By.ID,'term_input_id')
select = Select(dropdown)
select.select_by_visible_text('Fall 2023 (View only)')


driver.close()