import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Program Files\SeleniumBasic\chromedriver.exe');

rastreio = 'OS13204O12421BR';
url = 'https://www.linkcorreios.com.br/?id=' + str(rastreio);

driver.get(url);

print(f'Rastreando o objeto {rastreio} ...');

status = driver.find_element(By.CLASS_NAME,'linha_status').text;
print('\n');
print(status);
print('\n');

driver.quit()

