import csv
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def write_csv(filename):
    with open(f"{filename}", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Select","CRN","Subj","Crse","Sec","Cmp","Cred","Title","Days","Time","Cap","Act","Rem","WL","Cap","WL","Act","WL","Rem","XL","Cap","XL","Act","XL","Rem","Instructor","Date (MM/DD)","Location","Attribute"])

        table = driver.find_element(By.XPATH, "//table[@class='datadisplaytable']")
        rows = table.find_elements(By.XPATH, "//tr")[2:] 
        """
            Inside datadisplaytable in html source code there is another part called
            captiontext and within that there exists rows.
            Row 0 is Major name
            Row 1 is Source ...
            Row 2 is actual information
        """ 
        count = 5
        for row in rows:
            if count == 0:
                cols = row.find_elements(By.XPATH, "./td")
                row_data = []
                for col in cols:
                    row_data.append(col.text.strip()+"\t")
                if len(row_data) > 0:
                    writer.writerow(row_data)
            else:
                count-=1

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

btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']")
btn.click()

btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Advanced Search']")
btn.click()

subject = Select(driver.find_element(By.ID,'subj_id'))
subject.select_by_visible_text('Computer Science')

campus = Select(driver.find_element(By.ID,'camp_id'))
campus.select_by_visible_text('Byblos')

btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Section Search']")
btn.click()

filename = input("Enter file to store data ending with .csv:\n")
write_csv(filename)

driver.close()