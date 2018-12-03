from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dao import dao
import time





def main(urls,driver,pagenum):

    # body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next
    # body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next
    try:
        pagenum = pagenum + 1
        base_url = "https://www.jianshu.com/search?q=面经&page={0}".format(pagenum)
        driver.get(base_url)
        time.sleep(3)
        if pagenum==100:
            pagenum=pagenum/0
        tags = driver.find_elements_by_xpath("//a[@class='title']")
        for tag in tags:
            str = tag.get_attribute("href")
            if "面经" in tag.text:
                urls[0].append(str)
                urls[1].append(tag.text)


        main(urls=urls,driver=driver,pagenum=pagenum)
    except:
        driver.close()


if __name__ == '__main__':
    pagenum=0
    driver = webdriver.Chrome()
    urls = [[], []]
    main(urls=urls,driver=driver,pagenum=pagenum)
    print(urls)
    dao(urls)
