
from selenium import webdriver
import time
import webbrowser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
link = 'https://piter-online.net/'
browser = webdriver.Chrome()
browser.get(link)

serch_street = browser.find_element(By.CSS_SELECTOR,'input[class*=app141 ]')
serch_street.send_keys('Тестовая лини' )
time.sleep(1)
button = browser.find_element(By.CSS_SELECTOR,'div[class*=app151]').click()
time.sleep(2)
home = browser.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/input')
# можно и через хпас но это неверно с точки зрения практичности


home.send_keys("1")
time.sleep(2)

type_of_connection = browser.find_element(By.CSS_SELECTOR,'span[class*=app174 ]').click()




type_of_connection2 = browser.find_element(By.CSS_SELECTOR,'li[class*=app186 ]').click()

show_rates = browser.find_element(By.CSS_SELECTOR,'div[class*=app205]').click()
time.sleep(3)

tel= browser.find_element(By.XPATH,"// div[ @ datatest = 'close_popup1_from_quiz_input_tel']").click()
time.sleep(2)

connect= browser.find_element(By.CSS_SELECTOR,'div[class*=app421 ]').click()
time.sleep(2)

username= browser.find_element(By.XPATH,"//input[@autocomplete='name']" )
username.send_keys('Автотест' )


tel2= browser.find_element(By.XPATH,"//input[@name='tel']" )
tel2.send_keys('1111111111' )
time.sleep(3)
  # ----- > т.к в тестовом не указано что нужно отправить заявку отправлять не буду <-----
# во всяком случае оставлю тут еще и отправку
#send_request=browser.find_element(By.XPATH,"//div[@data-test='order_form_input_connect_button']" ).click()

time.sleep(2)
rates=browser.find_element(By.XPATH,"//a[@datatest='main_exclusive_downbutton']").click()
time.sleep(2)
new_rates=browser.find_element(By.XPATH,"//div[@datatest='providers_form_inspect_connect_tariff_button']").click()
time.sleep(2)
username= browser.find_element(By.XPATH,"//input[@autocomplete='name']" )
username.send_keys('Автотест' )

time.sleep(2)
tel2= browser.find_element(By.XPATH,"//input[@name='tel']" )
tel2.send_keys('1111111111' )
time.sleep(2)
rates=browser.find_element(By.XPATH,"//a[@datatest='main_exclusive_downbutton']").click()

new_rates=browser.find_element(By.XPATH,"//div[@datatest='providers_form_inspect_connect_tariff_button']").click()

username= browser.find_element(By.XPATH,"//input[@autocomplete='name']" )
username.send_keys('Автотест' )


tel2= browser.find_element(By.XPATH,"//input[@name='tel']" )
tel2.send_keys('1111111111' )


