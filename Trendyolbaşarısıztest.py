from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window() #ekranı tam boyut yap
driver.get("https://www.trendyol.com/")

searchBtn = driver.find_element(By.XPATH, "//*[@id='Combined-Shape']") #Pop-up'ı kaldır
searchBtn.click()
sleep(1)
searchBtn = driver.find_element(By.XPATH, "//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
searchBtn.click() #Giriş Yap
email= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/div[1]/input")
email.click()
email.send_keys("berk.kaldar@etiya.com") #e-mail addresi gir
sleep(1)
password = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/div[2]/div/div/input")
password.click()
password.send_keys("123456") #şifre gir
sleep(2)

searchBtn = driver.find_element(By.XPATH, "//*[@id='login-register']/div[3]/div[1]/form/button/span")
searchBtn.click()

sleep(3)
searchBtn = driver.find_element(By.XPATH, "//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
searchBtn = searchBtn.text
if searchBtn == "Hesabım":
    print("Test Başarılı Aferim Size 😍")
else:
    print("Test Başarısız Puh 😢") 

input()