from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")
driver.maximize_window()


# loginBtn = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[3]/a")
# loginBtnText = loginBtn.text
# if loginBtnText =="Giriş Yap":
#     print("Test Başarılı 😍")
# else:
#     print("Test Başarısız 😒")

# input()

# ekran görüntüsü alma
# kaydetme
# element bazlı, ya da driver bazlı alınabilir.
# loginBtn.screenshot("element.png") # => elementin screenshotunu alır.
# driver.save_screenshot("screen.png") # => tüm ekranın ss'ini alır.

# scroll_to fonksiyonu => locate edilmiş bir element'e scroll yapar.
# element.scroll_to
# selenium son sürümlerinde kaldırıldı!
# javascript kullanılarak scroll edilecek...
terms_conditions = driver.find_element(By.XPATH, '/html/body/div[1]/footer/div/div/div[2]/ul/li[1]/a')
sleep(3)
driver.execute_script("window.scroll(0,900)")
driver.execute_script("arguments[0].scrollIntoView()", terms_conditions)

# ActionChains => Yapılacak aksiyonları sırala,ve perform dediğimde bu işlemler
# sırasıyla gerçekleştirilsin
# Testçinin en çok tercih etmesi gereken yöntem!

# elemana scroll ol => screenshot al => butona tıkla
# perform
actions = ActionChains(driver)
actions.move_to_element(terms_conditions)
actions.click(terms_conditions)
actions.perform() # => zincirlenen aksiyonları işleme koyar... En son koy!


# PG_DWN
# özel karakterler nasıl kullanılır => Caps,Shift, Ctrl,Alt,PG_DWN,PG_UP,Insert

actions.send_keys(Keys.PAGE_DOWN)
actions.click(terms_conditions)
actions.perform() 

# 2 adet test case verilecek
# bu test caseler otomatize edilecek.
# sonuçlar test başarılı/test başarısız şeklinde console'a yazdırılacak
# ekran görüntüsü günün tarihi ile kaydedilecek.
# date.today()



