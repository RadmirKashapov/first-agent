from selenium import webdriver
import time
from lxml.html import fromstring

def get_driver():
    agent = webdriver.Chrome(executable_path="./chromedriver")
    return agent

def get_source_code(agent, link):
    agent.get(link)
    return fromstring(agent.page_source)


def table_pages(source):
    pages = source.xpath("//ul/li/a/@href")
    return list(set(pages))

if __name__ == "__main__":
    driver = get_driver()
    urls = [
        "http://kaf65.mephi.ru/tutorial/datasource_first/",
        "http://kaf65.mephi.ru/tutorial/datasource_second/",
        "http://kaf65.mephi.ru/tutorial/datasource_third/"
    ]

    for url in urls:
        source_code = get_source_code(driver, url)
        print(table_pages(source_code))

    driver.close()