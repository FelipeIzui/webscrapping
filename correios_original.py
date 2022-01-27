import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files\SeleniumBasic\chromedriver.exe')  # Optional argument, if not specified will search path.

rastreio = 'OS677439523BR'
url = 'https://www2.correios.com.br/sistemas/rastreamento/';
driver.get(url);

driver.find_element(By.ID, 'objetos').send_keys(rastreio);
driver.find_element(By.ID, 'btnPesq').click();

status_time = driver.find_element(By.CLASS_NAME, 'sroDtEvent').text;
status_location = driver.find_element(By.CLASS_NAME, 'sroLbEvent').text;

print('\n')
print(f'{status_time} \n');
print(status_location);

driver.quit()
