import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

counting = 0;

c = webdriver.ChromeOptions()
c.add_argument("--incognito");

#fazer o loop 100 vezes porque sim
while counting != 100:
    counting += 1;
    driver = webdriver.Chrome(executable_path='C:\Program Files\SeleniumBasic\chromedriver.exe', options=c);

    url = 'https://encurta.eu/pitbullreturns' #url do site

    driver.get(url); #abrir url

    time.sleep(3);

    #dar scroll down na página pq essa fdp bloqueia click por find_element
    driver.execute_script("window.scrollTo(0, 1080)");
    loc = driver.find_element(By.XPATH,'//*[@id="invisibleCaptchaShortlink"]')
    action = webdriver.common.action_chains.ActionChains(driver)
    #simulando click de mouse 
    action.move_to_element_with_offset(loc, 120.21875, 31.4375);
    action.click()
    action.perform()

    #dando tempo de sobra pro timer de 10 segundos que demora muito mais que isso
    time.sleep(20);

    #simulando click novamente
    loc = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/div/div/div/div/div[3]/a')
    action.move_to_element_with_offset(loc, 50.5, 14.640625);
    action.click()
    action.perform()
    #tentativa de dar ctrl+w pra fechar a aba, mas não deu então foda-se, fica ai
    #vai ver esses comando repetidos abaixo pq ele pode abrir até 3 propagandas até chegar no link final do mediafire
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").perform()
    time.sleep(5);
    action.move_to_element_with_offset(loc, 50.5, 14.640625);
    action.click()
    action.perform()
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").perform()
    time.sleep(5);
    action.move_to_element_with_offset(loc, 50.5, 14.640625);
    action.click()
    action.perform()
    time.sleep(5);

    driver.quit();

    print(f'Repetição de número: {counting}');