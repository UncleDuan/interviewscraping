import  requests
# q=面经&t=&domain=&o=&s=&u=&l=&f=
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
base_url="https://so.csdn.net/so/search/s.do?q=%E9%9D%A2%E7%BB%8F"
driver=webdriver.Chrome()
driver.get(base_url)
urls = []
def store(url):
    pass
def download(url):
    pass


def nextpage():
    try:
        driver.find_element_by_class_name("btn btn-xs btn-default btn-next")
        return True
    except:
        return False

def findUrls(urls):
    tags = driver.find_elements_by_xpath('//dl/dt/div/a')
    for tag in tags:
        str = tag.get_attribute("href")
        if str.startswith("https://blog.csdn.net") and "?" not in str:
            urls.append(str)
        print(tag.get_attribute("href"))
    urls = list(set(urls))
def main():
    WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.ID,"BAIDU_DUP_fp_wrapper")))
    findUrls(urls)
    # body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next
    # body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next
    try:
        driver.find_element_by_xpath("//a[@class='btn btn-xs btn-default btn-next']").click()
        main()
    except:
        driver.close()


if __name__ == '__main__':
    try:
        main()
    finally:
        driver.close()
