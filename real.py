from bs4 import SoupStrainer, BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import io
from selenium import webdriver
import os
from datetime import datetime

startTime = datetime.now()
entryPage = "https://javascript.info/hello-world"
page = urllib.request.urlopen(entryPage)
path = "C:\\Users\\odami\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)



def loader():
    entryPage = "https://javascript.info/hello-world"
    driver.get(entryPage)
    #source = driver.page_source
    
    """
    mySoup = soupMaker(source)
    pageName = mySoup.meta['content']
    """

    def checkPath():
            try:
                driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[2]/a[2]/span[1]")
            except NoSuchElementException:
                return False
            return True

    def checkArticle():
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[1]/article")
        except NoSuchElementException:
            return True
        return False

    #add a condition say while the xpath exists a loop runs
    while(checkPath()):
        if( checkArticle()):
            #writer(mySoup, pageName)
            mySoup = BeautifulSoup(urllib.request.urlopen(driver.current_url), 'html.parser',  parse_only=SoupStrainer("article"))
            pageName = mySoup.meta['content']  
            print('found')
            #print(driver.current_url)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[2]/a[2]/span[1]").click()
                        
        else:
            print('not found')
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/main/div[2]/a[2]/span[1]").click()
            #tryna know what to do next after finding the page element
            
        

    
"""def soupMaker(pageSource):
    return BeautifulSoup(pageSource, 'html.parser',  parse_only=SoupStrainer("article"))
def writer(soup, pageName):
    resultFolder = "C:\\Users\\odami\\developments\\bs4\\outputs"
    with io.open(os.path.join(resultFolder, pageName +".txt"), "w", encoding ="utf-8") as file:
            file.write(str(soup.get_text()))
"""
def load():
    loader()
load()
endTime = datetime.now()
print(endTime - startTime)