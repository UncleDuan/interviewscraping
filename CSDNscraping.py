import  requests
# q=面经&t=&domain=&o=&s=&u=&l=&f=
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dao import dao

base_url = "https://so.csdn.net/so/search/s.do?q=" + "面经"
driver = webdriver.Chrome()
driver.get(base_url)
urls = [[], []]
def nextpage():
    try:
        driver.find_element_by_class_name("btn btn-xs btn-default btn-next")
        return True
    except:
        return False

def findUrls(urls):
    tags = driver.find_elements_by_xpath('//dl/dt/div/a')
    newTags=[]
    for tag in tags:
        str = tag.get_attribute("href")
        if str.startswith("https://blog.csdn.net") and "?" not in str:
            urls[0].append(str)
            urls[1].append(tag.text)

def main(urls):
    WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.ID,"BAIDU_DUP_fp_wrapper")))
    findUrls(urls)
    # body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next
    # body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next
    try:
        driver.find_element_by_xpath("//a[@class='btn btn-xs btn-default btn-next']").click()
        main(urls)
    except:
        driver.close()
def scrapingtext():
    WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.ID, "btn-readmore")))
    try:
        # driver.find_element_by_xpath("//a[@id='btn-readmore']").click()
        driver.find_element_by_xpath("//div[@class='hide-article-box text-center']").click()
        WebDriverWait(driver, 5)

    except:
        pass
    #     driver.find_element_by_xpath("//a[@class='btn btn-xs btn-default btn-next']").click()
    # title=driver.find_element_by_xpath("//h1[@class='title-article']").text
    title = driver.find_element_by_xpath("//h1[1]").text
    context=driver.find_element_by_id("content_views").text
    print(title)
    print(context)

if __name__ == '__main__':

    main(urls)
    print(urls)
    dao(urls)
