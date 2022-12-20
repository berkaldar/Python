# bir kütüphaneden dosya import etmek
# kalıp => from {kütüphane -ismi} import {nesne-ismi}
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
#sitenin açılmasını bekle!
sleep(1)
input = driver.find_element(By.NAME, "q")
input.send_keys("Çalışıyor mu? Deneme 1-2-3")
sleep(1)
SearchBtn = driver.find_element(By.NAME, "btnK")