from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DRIVER_PATH = './chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://suf.purs.gov.rs/v/?vl=A1RMVE5QTjlBVExUTlBOOUHrZQIAlGQCAAA+SQAAAAAAAAABhC5ycbgAAAAvmGh+K/QGa9fPmVrcBd1O1eBz7SK7CP2/ABrNczyklPqjt3gBczbUcl7nBO2OhHp4X5eZs534ljddNz1/5sDTZFSKQxCP9On/l81uY6TjBPE3D0EsXIw/T7C3eg8O8Y10E2/rS+NAKan5Xc047kQTT1rZnXP8Elk6t7QxBtAms9lrxeuVx89Q57+QRvgWAoD91DbUf0iPuhyaQtAPvArQsEwrWqRBRxgkYOjJ1vjRhxPcy1gL1M75Oh0wwUma4dMA9ZJe6WRtybhEQWyAMhXiiYlBvHYSVcSTaCK66vQCXi9HjUyxrjLuanuQJMwLuP9CLsBLXuaXYME3lR6wyTrkL/6MCOciGDscXAWUGkxMBAQs09PCW23u0dzNtdESleKPKEpkHeoYuRxqe9xLJ8X2uyQOIPzY4OVXUIkvc09EEQJZsD6r/KsrKMWT5LdjwTTzPZkJ5+TtSTp0cjevuCCKrkYmozh4Sjgv8V8qH1j5a8kvJfPQ0+tP5rxVK+YzqIerRRF0MeDLvaSA/1gfxoWRqBEUOE7fZ2cEC3034yU+ywhPj3ksZJRXptzsYZR0lB8tEpNcdNiEEpWO9qkwKpSk4LZdZCX5eatN1Z0G6vU7QALqOYP4JOuix/YnI0jW250bAeuHafRLb3hGCEKwUrINjKscPHaMB8LY7WK6Dhx3z1DadBUqSS047tNTxP16s5Q=")
#print(driver.page_source)
prodajno_mesto = driver.find_element(By.XPATH, "//*[contains(text(),'Име продајног места')]/../div[@class='col-md-12']") 
iznos = driver.find_element(By.XPATH, "//*[contains(text(),'Укупан износ')]/../div[@class='col-md-12']")
print(iznos.text + ' RSD potroseno u ' + prodajno_mesto.text)
driver.quit()