import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files\SeleniumBasic\chromedriver.exe')  # Optional argument, if not specified will search path.

storage = [];

url = "file:///C:/Users/izui/Downloads/3fmiva.html";
driver.get(url);

table = driver.find_element("//*[@id='fd-table-']/tbody")
links = table.find_element_by_link_text('a');
storage.append(links);

    