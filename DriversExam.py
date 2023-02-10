from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import keyboard
import time
import sys
from datetime import datetime


def Captcha():

    while(True):
        try:
            Platse = d.find_element(By.XPATH, "//*[contains(text(), 'Solving')]")
            time.sleep(2)
        except Exception:
            try:
                d.find_element(By.XPATH, "//*[contains(text(), 'Jätkan')]").click(); time.sleep(2)
                break
            except Exception:
                break

C_O = Options()
C_O.add_extension(r"C:\Users\ramma\OneDrive\Dokumendid\.Proge\ARK\anticaptcha-plugin_v0.62.zip")
d = webdriver.Chrome(options = C_O, executable_path = r"C:\Users\ramma\OneDrive\Dokumendid\.Proge\ARK\chromedriver_win32\chromedriver.exe")

d.get("https://eteenindus.mnt.ee/")

d.find_element(By.ID, "header:userLogin").click(); time.sleep(2)
d.find_element(By.LINK_TEXT, "Smart-ID").click()
d.find_element(By.ID, "sid-personal-code").send_keys("50309172750")
d.find_element(By.XPATH, '//*[@id="smartIdForm"]/table/tbody/tr[2]/td[2]/button').click()

time.sleep(60)

while(True):
    Aeg = datetime.now()
    if Aeg.hour > 20 or Aeg.hour < 6:
        time.sleep(200)
    
    try:
        d.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/div/form/a[1]').click(); time.sleep(3)
        Captcha()

        d.find_element(By.LINK_TEXT, "Muuda valikut »").click(); time.sleep(3)
        Captcha()    
        
        d.find_element(By.LINK_TEXT, "Kus saab kõige kiiremini eksamile?").click(); time.sleep(2)

        Dates = d.find_element(By.XPATH, '//*[@id="varaseimadEksamiajadForm"]/ul').text.split()
        
        for i in range(11):
            Date = Dates[i*4].split(".")
            
            Day = int(Date[0])
            Month = int(Date[1])
            Year = int(Date[2])
            City = Dates[(i*4)+2]
            
            if Year == 2022 and Month == 7 and Day > 22 and Day < 30 and (City == "Tartu"):
                d.find_element(By.XPATH, "//*[contains(text(), \'" + Dates[(i*4)+2] + " »\')]").click(); time.sleep(2)
                d.find_element(By.XPATH, "//*[contains(text(), 'Aeg valitud')]").click(); time.sleep(3)
                print(Day)
                sys.exit()
        
        d.get("https://eteenindus.mnt.ee/"); time.sleep(2)
    except Exception:
        time.sleep(2)
        d.get("https://eteenindus.mnt.ee/")
        time.sleep(2)
