
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
base_url="https://blog.csdn.net/qq_36125072/article/details/82753214"
driver=webdriver.Chrome()
driver.get(base_url)
# 持久层
def dao():
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
    dao()
    driver.close()