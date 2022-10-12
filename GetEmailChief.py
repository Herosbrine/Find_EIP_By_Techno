#!/usr/bin/python3
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from decouple import config
from boteip import connection

def GetEmailChief(driver):
    AllValidLinks = []
    with open("EIPTECHNO.txt", "r") as f:
        for line in f:
            AllValidLinks.append(line.strip())
    #print("AllValidLinks: ", AllValidLinks)
    for link in AllValidLinks:
        driver.get(link)
        sleep(4)
        try:
            GetHref = driver.find_element(By.XPATH, "//span[@class='subject-view-basic-info-content ng-binding']/a").get_attribute("href")
            #remove the last 3 characters from the string
            GetHref = GetHref.replace("https://eip.epitech.eu/#/users/user/", "")
            with open ("EmailOfChief.txt", "r") as f:
                if GetHref in f.read():
                    continue
                else:
                    with open ("EmailOfChief.txt", "a") as f:
                        f.write(GetHref + "\n")
        except:
            print("No Href")
    exit(84)
    
def main():
    driver = connection()
    GetEmailChief(driver)

if __name__ == '__main__':
    main()