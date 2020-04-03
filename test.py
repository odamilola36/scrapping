from bs4 import SoupStrainer, BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import io
from selenium import webdriver
import os
import re
from datetime import datetime


entryPage = "https://javascript.info/hello-world"
page = urllib.request.urlopen(entryPage)
path = "C:\\Users\\odami\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)



def loader():
    entryPage = "https://javascript.info/hello-world"
    driver.get(entryPage)

    def checkPath():
            try:
                driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[2]/a[2]/span[1]")
            except NoSuchElementException:
                return False
            return True
    
    def checkArticle():
        try:
            driver.find_element_by_name("article")
        except NoSuchElementException:
            return True
        return False
    

    #add a condition say while the xpath exists a loop runs
    while(checkPath()):
        if(checkArticle()):
            print('working')
            mySoup = BeautifulSoup(urllib.request.urlopen(driver.current_url), 'html.parser',  parse_only=SoupStrainer("article"))
            pageName = mySoup.meta['content']            
            writer(mySoup, pageName)            
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[2]/a[2]/span[1]").click()                        
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[2]/a[2]/span[1]").click()
            #tryna know what to do next after finding the page element
            
def writer(soup, pageName):
    resultFolder = "C:\\Users\\odami\\developments\\bs4\\outputs"
    name = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in pageName.split("\n")]
    fName = ''.join(name).rstrip() +'.txt'
    with io.open(os.path.join(resultFolder, fName), "w", encoding ="utf-8") as file:
            file.write(str(soup.get_text()))

def load():
    startTime = datetime.now()
    loader()
    endTime = datetime.now

    print(endTime - startTime)


load()