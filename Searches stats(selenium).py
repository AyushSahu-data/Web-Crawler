from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Topics: Locate a button, select element within dropdown and extract data from a table

# define the website to scrape and path where the chromediver is located
website = 'https://www.youtube.com/c/OpeninApp'
path = 'D:\Python Project\chromedriver_win32' # write the path here

# define 'driver' variable
driver = webdriver.Chrome(path)
# open Google Chrome with chromedriver
driver.get(website)

# locate a button
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="OpeninApp"]')
# click on a button
all_matches_button.click()

# using the "box" section as a reference to help us locate an element inside
box = driver.find_element_by_class_name('panel-body')

# implicit wait (useful in JavaScript driven websites when elements need seconds to load and avoid error "ElementNotVisibleException")
time.sleep(5)
# select elements in the table
matches = driver.find_elements_by_css_selector('tr')

# storage in a list
all_matches = [match.text for match in matches]

#quit drive we opened in the beginning
driver.quit()

