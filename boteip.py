#!/usr/bin/python3
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from decouple import config

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

print(USERNAME, PASSWORD)
def connection():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    number = 1
    url = "https://eip.epitech.eu/#/subjects?promotion=2024&page=" + str(number) + "&query=&memberCountSort=ASC"
    driver.get("https://eip.epitech.eu/#/login")
    sleep(3)
    driver.set_page_load_timeout(30)
    username = driver.find_element(By.NAME, "login")
    username.send_keys(USERNAME)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary whole-width ng-scope']").click()
    sleep(2)
    driver.get(url)
    return (driver)

def GetAllLink(driver):
    sleep(2)
    #find all href in td
    hrefs = driver.find_elements(By.XPATH, "//tr[@class='ng-scope']/td/a")
    allProjetLink = []
    for number in range(1, 13):
        url = "https://eip.epitech.eu/#/subjects?promotion=2024&page=" + str(number) + "&query=&memberCountSort=ASC"
        driver.get(url)
        sleep(5)
        hrefs = driver.find_elements(By.XPATH, "//tr[@class='ng-scope']/td/a")
        for href in hrefs:
            allProjetLink.append(href.get_attribute("href"))
    print(allProjetLink)
    return (allProjetLink, driver)

def CheckProjetLink(Techno, driver):
    temp = 0
    allProjetLink = ['https://eip.epitech.eu/#/subjects/subject/6189aab2c18bd07bf0821720', 'https://eip.epitech.eu/#/subjects/subject/61895296c18bd06d70fcc49d', 'https://eip.epitech.eu/#/subjects/subject/61767344c18bd068159d632a', 'https://eip.epitech.eu/#/subjects/subject/6182e0e3c18bd0582e1b281c', 'https://eip.epitech.eu/#/subjects/subject/6176ce29c18bd016f497988b', 'https://eip.epitech.eu/#/subjects/subject/618e3409c18bd01dbc6e7939', 'https://eip.epitech.eu/#/subjects/subject/6190e837c18bd037e641a010', 'https://eip.epitech.eu/#/subjects/subject/6177dc43c18bd0115b5c705a', 'https://eip.epitech.eu/#/subjects/subject/62aaf011c18bd049f8ffed79', 'https://eip.epitech.eu/#/subjects/subject/61912428c18bd037e65a4666', 'https://eip.epitech.eu/#/subjects/subject/619d0ae2c18bd0305e16ff85', 'https://eip.epitech.eu/#/subjects/subject/618ff81ac18bd029120580b5', 'https://eip.epitech.eu/#/subjects/subject/61965d98c18bd07a71482594', 'https://eip.epitech.eu/#/subjects/subject/61939db7c18bd04b61adbbdc', 'https://eip.epitech.eu/#/subjects/subject/6188e1c8c18bd029050a1468', 'https://eip.epitech.eu/#/subjects/subject/61880a75c18bd02905fc2044', 'https://eip.epitech.eu/#/subjects/subject/618be702c18bd00b9820439c', 'https://eip.epitech.eu/#/subjects/subject/619144bdc18bd037e661b6b7', 'https://eip.epitech.eu/#/subjects/subject/618a67f1c18bd07813edf957', 'https://eip.epitech.eu/#/subjects/subject/618aa04cc18bd003a6e4b7e5', 'https://eip.epitech.eu/#/subjects/subject/618e96d5c18bd0219789b5b1', 'https://eip.epitech.eu/#/subjects/subject/618a98eac18bd07f36e9a1e6', 'https://eip.epitech.eu/#/subjects/subject/618bb11dc18bd0040a98c4d4', 'https://eip.epitech.eu/#/subjects/subject/61829cd7c18bd04ee854c62e', 'https://eip.epitech.eu/#/subjects/subject/6197aa6ec18bd007e9cb54cd', 'https://eip.epitech.eu/#/subjects/subject/61967ce7c18bd0081c98a355', 'https://eip.epitech.eu/#/subjects/subject/618bafadc18bd0040a968873', 'https://eip.epitech.eu/#/subjects/subject/617a7b6ac18bd02449a5308e', 'https://eip.epitech.eu/#/subjects/subject/618bec01c18bd00b982b7bf6', 'https://eip.epitech.eu/#/subjects/subject/617a685fc18bd02449a0b438', 'https://eip.epitech.eu/#/subjects/subject/61939b83c18bd04b61ab7c86', 'https://eip.epitech.eu/#/subjects/subject/6189352cc18bd06d70dbf9e0', 'https://eip.epitech.eu/#/subjects/subject/618a502bc18bd071ad56d7fa', 'https://eip.epitech.eu/#/subjects/subject/618a946dc18bd07f36ca3329', 'https://eip.epitech.eu/#/subjects/subject/618d3eb5c18bd012566cf29f', 'https://eip.epitech.eu/#/subjects/subject/618bebffc18bd00b982b7bf4', 'https://eip.epitech.eu/#/subjects/subject/616e9aebc18bd01ff743d821', 'https://eip.epitech.eu/#/subjects/subject/618d8d6dc18bd01dbc5e2b4b', 'https://eip.epitech.eu/#/subjects/subject/61944aa6c18bd05d52df1bac', 'https://eip.epitech.eu/#/subjects/subject/618bc468c18bd00876d239b7', 'https://eip.epitech.eu/#/subjects/subject/61866d5ec18bd05bf0299dd3', 'https://eip.epitech.eu/#/subjects/subject/6189344dc18bd06d70d77f29', 'https://eip.epitech.eu/#/subjects/subject/617809cec18bd0115b68ffeb', 'https://eip.epitech.eu/#/subjects/subject/6171aa4fc18bd0681530e320', 'https://eip.epitech.eu/#/subjects/subject/618bdef2c18bd00b981ec633', 'https://eip.epitech.eu/#/subjects/subject/61702b94c18bd04832c0f8f5', 'https://eip.epitech.eu/#/subjects/subject/618a7ed0c18bd07bb52a5ab4', 'https://eip.epitech.eu/#/subjects/subject/618d17aac18bd012565e02f1', 'https://eip.epitech.eu/#/subjects/subject/61912ef8c18bd037e65a467b', 'https://eip.epitech.eu/#/subjects/subject/61897d13c18bd07bf07c1a7d', 'https://eip.epitech.eu/#/subjects/subject/618a84a1c18bd07bb53fdf5d', 'https://eip.epitech.eu/#/subjects/subject/61914f11c18bd037e672e658', 'https://eip.epitech.eu/#/subjects/subject/6195079fc18bd06d46b760e8', 'https://eip.epitech.eu/#/subjects/subject/618011a5c18bd04a53c7db15', 'https://eip.epitech.eu/#/subjects/subject/619631f0c18bd07a711840dc', 'https://eip.epitech.eu/#/subjects/subject/618eb318c18bd0219794e467', 'https://eip.epitech.eu/#/subjects/subject/618e868dc18bd0219780c88d', 'https://eip.epitech.eu/#/subjects/subject/618a7132c18bd07813f9e66f', 'https://eip.epitech.eu/#/subjects/subject/618bcd0bc18bd00876ea2bdb', 'https://eip.epitech.eu/#/subjects/subject/61810e25c18bd04a53f18727', 'https://eip.epitech.eu/#/subjects/subject/617fe5dbc18bd04a53bfb422', 'https://eip.epitech.eu/#/subjects/subject/6179b2bdc18bd02c9c8892f3', 'https://eip.epitech.eu/#/subjects/subject/618a987bc18bd07f36e9a1e1', 'https://eip.epitech.eu/#/subjects/subject/618a5226c18bd0754c151aa8', 'https://eip.epitech.eu/#/subjects/subject/61b21a3cc18bd0637f9eb863', 'https://eip.epitech.eu/#/subjects/subject/618ab510c18bd003a60c447a', 'https://eip.epitech.eu/#/subjects/subject/618152f5c18bd06641ff2b6c', 'https://eip.epitech.eu/#/subjects/subject/6182b8a9c18bd04ee86bb0d0', 'https://eip.epitech.eu/#/subjects/subject/6177b6e9c18bd0115b508029', 'https://eip.epitech.eu/#/subjects/subject/618016c5c18bd04a53da7f32', 'https://eip.epitech.eu/#/subjects/subject/618d402ec18bd012566cf2aa', 'https://eip.epitech.eu/#/subjects/subject/618f8f4fc18bd02197a99a2d', 'https://eip.epitech.eu/#/subjects/subject/619e3b70c18bd03944821bea', 'https://eip.epitech.eu/#/subjects/subject/618baf06c18bd0040a8f10eb', 'https://eip.epitech.eu/#/subjects/subject/6193ca52c18bd04b61d1854b', 'https://eip.epitech.eu/#/subjects/subject/618ba344c18bd00242f4c74e', 'https://eip.epitech.eu/#/subjects/subject/61895550c18bd06d70fcc4b4', 'https://eip.epitech.eu/#/subjects/subject/617a9ad0c18bd02449abc367', 'https://eip.epitech.eu/#/subjects/subject/618adb32c18bd003a60ffa44', 'https://eip.epitech.eu/#/subjects/subject/61754fafc18bd06815687c73', 'https://eip.epitech.eu/#/subjects/subject/6176b333c18bd0157947c15a', 'https://eip.epitech.eu/#/subjects/subject/6179d868c18bd02c9c8a0e5c', 'https://eip.epitech.eu/#/subjects/subject/618c210ac18bd0138f1d993c', 'https://eip.epitech.eu/#/subjects/subject/61896781c18bd07bf0793049', 'https://eip.epitech.eu/#/subjects/subject/618fe235c18bd02912f4996a', 'https://eip.epitech.eu/#/subjects/subject/617ab30bc18bd0319cda1a6b', 'https://eip.epitech.eu/#/subjects/subject/6194f363c18bd06d46ab7662', 'https://eip.epitech.eu/#/subjects/subject/61963418c18bd07a711d7f5d', 'https://eip.epitech.eu/#/subjects/subject/618919f9c18bd06d70ba7d1a', 'https://eip.epitech.eu/#/subjects/subject/61893bfac18bd06d70ed2b7a', 'https://eip.epitech.eu/#/subjects/subject/61794d32c18bd0258a07e8d1', 'https://eip.epitech.eu/#/subjects/subject/61963d0fc18bd07a71267b8e', 'https://eip.epitech.eu/#/subjects/subject/6176ce0cc18bd016f4979889', 'https://eip.epitech.eu/#/subjects/subject/619540e9c18bd07a437ca14f', 'https://eip.epitech.eu/#/subjects/subject/61767fd0c18bd00ba5e31fbf', 'https://eip.epitech.eu/#/subjects/subject/61964e89c18bd07a714529ac', 'https://eip.epitech.eu/#/subjects/subject/6189b3bfc18bd07bf08bbe88', 'https://eip.epitech.eu/#/subjects/subject/618bd3a3c18bd009f6cb25d2', 'https://eip.epitech.eu/#/subjects/subject/618a53dfc18bd0754c210ac2', 'https://eip.epitech.eu/#/subjects/subject/618a4098c18bd071ad3f17f0', 'https://eip.epitech.eu/#/subjects/subject/617005eac18bd03a20be5754', 'https://eip.epitech.eu/#/subjects/subject/618b9d67c18bd07edf7e32f0', 'https://eip.epitech.eu/#/subjects/subject/618f9ca0c18bd0211cda4f12', 'https://eip.epitech.eu/#/subjects/subject/61893947c18bd06d70e8b242', 'https://eip.epitech.eu/#/subjects/subject/618e70acc18bd0175654a218', 'https://eip.epitech.eu/#/subjects/subject/6176af28c18bd0137d99f1f6', 'https://eip.epitech.eu/#/subjects/subject/61755f33c18bd06815687c80', 'https://eip.epitech.eu/#/subjects/subject/619104a8c18bd037e654516d', 'https://eip.epitech.eu/#/subjects/subject/618902edc18bd06be849f4fa', 'https://eip.epitech.eu/#/subjects/subject/6170263dc18bd03a20c73d2d', 'https://eip.epitech.eu/#/subjects/subject/618d2a9ec18bd012566639ca', 'https://eip.epitech.eu/#/subjects/subject/6176bb19c18bd016f4837784', 'https://eip.epitech.eu/#/subjects/subject/618e3ce2c18bd017563fbef3', 'https://eip.epitech.eu/#/subjects/subject/6193df22c18bd05d52d0fbea', 'https://eip.epitech.eu/#/subjects/subject/618e27f0c18bd01dbc6c3d93', 'https://eip.epitech.eu/#/subjects/subject/618bc50ac18bd00876d6b816', 'https://eip.epitech.eu/#/subjects/subject/617a387fc18bd02c9c8b8d30', 'https://eip.epitech.eu/#/subjects/subject/61892790c18bd06d70cd0c18']
    for link in allProjetLink:
        try:
            driver.get(link)
        except:
            continue
        sleep(4)
        RefuseEIP = driver.find_elements(By.XPATH, "//span[@class='subject-view-status-bar-info ng-binding']")
        for element in RefuseEIP:
            if "EIP refusé" in element.text:
                temp = 1
                break
        if temp == 1:
            temp = 0
            continue
        try:
            CheckText = driver.find_elements(By.XPATH, "//div[@class='subject-view-info-title ng-binding']")
            for i, text in enumerate(CheckText):
                try:
                    if (text.text == "Resources"):
                        FullText = driver.find_elements(By.XPATH, "//p[@class='subject-view-info-content ng-binding ng-scope']")
                        if (Techno.lower() in FullText[i].text.lower()):
                            with open("EIPTECHNO.txt", "a") as f:
                                f.write(link + "\n")
                            #print(FullText[i].text)
                except:
                    pass
        except:
            pass

def main():
    Techno = input("Enter Techno you want: ")
    driver = connection()
    #allProjetLink, driver = GetAllLink(driver)
    CheckProjetLink(Techno, driver)
    print("Done")

if __name__ == "__main__":
    main()