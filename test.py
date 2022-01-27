import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files\SeleniumBasic\chromedriver.exe');

driver.get('https://www.google.com');

driver.execute_script("window.open('');")
time.sleep(3);

driver.switch_to_window(driver.window_handles[1]);
driver.get("https://facebook.com");
time.sleep(3);

driver.close()
time.sleep(3);

driver.switch_to_window(driver.window_handles[0]);
driver.get("https://yahoo.com");
